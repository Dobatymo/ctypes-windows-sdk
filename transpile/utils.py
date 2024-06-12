import logging
import re
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Set

import libcst as cst


class FixEnumsCST(cst.CSTTransformer):
    def __init__(self):
        self.fields: List[cst.SimpleStatementLine] = []

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        assert isinstance(node.bases[0].value, cst.Name)
        assert not self.fields
        if node.bases[0].value.value == "CEnum":
            assert isinstance(node.body, cst.IndentedBlock)
            i = 0
            for _field in node.body.body:
                assert isinstance(_field, cst.SimpleStatementLine)
                assert len(_field.body) == 1
                field = _field.body[0]
                if isinstance(field, cst.Assign):
                    assert len(field.targets) == 1
                    assert isinstance(field.targets[0].target, cst.Name)
                    assert isinstance(field.value, cst.Integer), field.value

                    i = field.value.evaluated_value + 1
                    self.fields.append(_field)
                elif isinstance(field, cst.Expr):
                    assert isinstance(field.value, cst.Name)
                    newfield = cst.Assign(targets=[cst.AssignTarget(target=field.value)], value=cst.Integer(str(i)))
                    i += 1
                    self.fields.append(_field.with_changes(body=[newfield]))
                else:
                    raise RuntimeError(f"Unexpected node: {field.body[0]}")
            return False
        else:
            return True

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.CSTNode:
        if self.fields:
            body = updated_node.body.with_changes(body=self.fields)
            self.fields = []
            return updated_node.with_changes(body=body)
        else:
            return updated_node


class FixAnonymousCST(cst.CSTTransformer):
    def __init__(self):
        self.anonymous: List[str] = []

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        assert isinstance(node.bases[0].value, cst.Name)
        assert not self.anonymous
        if node.bases[0].value.value in ("Structure", "Union"):
            assert isinstance(node.body, cst.IndentedBlock)
            for _field in node.body.body:
                assert isinstance(_field, cst.SimpleStatementLine)
                assert len(_field.body) == 1
                field = _field.body[0]
                if isinstance(field, cst.Assign):
                    for target in field.targets:
                        assert isinstance(target.target, cst.Name)
                        if target.target.value == "_fields_":
                            assert isinstance(field.value, cst.List)
                            for element in field.value.elements:
                                if isinstance(element.value, cst.Tuple):
                                    assert isinstance(element.value.elements[0].value, cst.SimpleString)
                                    fieldname = element.value.elements[0].value.evaluated_value
                                    if fieldname in ("DUMMYSTRUCTNAME", "DUMMYUNIONNAME"):
                                        self.anonymous.append(fieldname)
                                elif isinstance(element.value, (cst.Call, cst.SimpleString)):
                                    pass  # these are errors and should be fixed elsewhere
                                else:
                                    raise TypeError(element.value)
            return False
        else:
            return True

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.CSTNode:
        if self.anonymous:
            sls = cst.SimpleStatementLine(
                body=[
                    cst.Assign(
                        targets=[cst.AssignTarget(target=cst.Name(value="_anonymous_"))],
                        value=cst.Tuple(
                            elements=[cst.Element(value=cst.SimpleString(value=repr(s))) for s in self.anonymous]
                        ),
                    )
                ]
            )
            body = updated_node.body.with_changes(body=[sls, *updated_node.body.body])
            self.anonymous = []
            return updated_node.with_changes(body=body)
        else:
            return updated_node


class FixEnumAccessCST(cst.CSTTransformer):
    def __init__(self, strict: bool = False):
        self.enums: Dict[str, List[str]] = {}
        self.assigns: Set[str] = set()
        self.strict = strict

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        assert isinstance(node.bases[0].value, cst.Name)
        name = node.name.value
        self.assigns.add(name)

        if node.bases[0].value.value == "CEnum":
            assert name not in self.enums
            self.enums[name] = []
            assert isinstance(node.body, cst.IndentedBlock)
            for _field in node.body.body:
                assert isinstance(_field, cst.SimpleStatementLine)
                assert len(_field.body) == 1
                field = _field.body[0]
                if isinstance(field, cst.Assign):
                    assert len(field.targets) == 1
                    assert isinstance(field.targets[0].target, cst.Name)
                    self.enums[name].append(field.targets[0].target.value)
            return False
        return True

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.CSTNode:
        return updated_node

    def visit_ImportFrom(self, node: cst.ImportFrom) -> Optional[bool]:
        for name in node.names:
            if name.asname is not None:
                assert isinstance(name.asname.name, cst.Name), name.asname.name
                self.assigns.add(name.asname.name.value)
            else:
                assert isinstance(name.name, cst.Name), name.name
                self.assigns.add(name.name.value)

        return True

    def leave_ImportFrom(self, original_node: cst.ImportFrom, updated_node: cst.ImportFrom) -> cst.CSTNode:
        return updated_node

    def visit_Assign(self, node: cst.Assign) -> Optional[bool]:
        for target in node.targets:
            assert isinstance(target.target, cst.Name), target.target
            self.assigns.add(target.target.value)
        return True

    def leave_Assign(self, original_node: cst.Assign, updated_node: cst.Assign) -> cst.CSTNode:
        if isinstance(updated_node.value, cst.Name):
            var = updated_node.value.value
            if var not in self.assigns:
                for name, fields in self.enums.items():
                    if var in fields:
                        attr = cst.Attribute(value=cst.Name(value=name), attr=cst.Name(value=var))
                        return updated_node.with_changes(value=attr)

                if self.strict:
                    msg = f"Variable not found: {var}"
                    raise RuntimeError(msg)
                else:
                    logging.error("Variable not found: %s", var)
                    return cst.RemoveFromParent()
                    # return cst.Comment(value=f"#Variable not found: {var}")
        return updated_node


def fix_header_cst(inpath: Path, outpath: Path, encoding="ascii") -> None:
    data = inpath.read_text(encoding=encoding)
    module = cst.parse_module(data)

    transformer = FixEnumsCST()
    module = module.visit(transformer)

    transformer = FixAnonymousCST()
    module = module.visit(transformer)

    transformer = FixEnumAccessCST()
    module = module.visit(transformer)

    outpath.write_text(module.code, encoding=encoding)


typemap = {
    "_Bool": "c_bool",
    "char": "c_char",
    "wchar_t": "c_wchar",
    "unsigned char": "c_ubyte",
    "short": "c_short",
    "unsigned short": "c_ushort",
    "int": "c_int",
    "unsigned int": "c_uint",
    "long": "c_long",
    "unsigned long": "c_ulong",
    "long long": "c_longlong",
    "__int64": "c_longlong",
    "unsigned long long": "c_ulonglong",
    "unsigned __int64": "c_ulonglong",
    "size_t": "c_size_t",
    "ssize_t": "c_ssize_t",
    "time_t": "c_time_t",
    "float": "c_float",
    "double": "c_double",
    "long double": "c_longdouble",
    "char*": "c_char_p",
    "wchar_t*": "c_wchar_p",
    "void*": "c_void_p",
}

bad_identifies = ["_W64"]


def typedef_sub(m: re.Match) -> str:
    t = m.group(1).strip()

    if " " in t:
        t = " ".join(i for i in t.split(" ") if i not in bad_identifies)

    ctype = typemap.get(t, t)
    if " " in ctype:
        raise ValueError(f"Unknown identifier: {ctype}")
    return f"{m.group(2)} = {ctype}"


patterns = [
    (
        "replace normal defines",
        r"^[ ]*#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_]+)[ ]*(\/\/.*)?\n",
        r"\1 = \2 \3\n",
        re.MULTILINE,
    ),
    (
        "replace normal defines string",
        r'^[ ]*#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+("[^"\n]*")[ ]*(\/\/.*)?\n',
        r"\1 = \2 \3\n",
        re.MULTILINE,
    ),
    (
        "replace function defines",
        r"^[ ]*#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_\(\), \|]+)\n",
        r"\1 = \2\n",
        re.MULTILINE,
    ),
    (
        "remove empty comments",
        r"^[ ]*\/\/\n",
        r"",
        re.MULTILINE,
    ),
    (
        "typedef _named enum with var, pointer",
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(CEnum):\n\2\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named enum with var, pointer, LP",
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*,\s*\*\s*LP\1\s*;",
        r"class \1(CEnum):\n\2\nP\1 = POINTER(\1)\nLP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named enum with alt var, alt pointer",  # ignore underscore name
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \3(CEnum):\n\2\nP\4 = POINTER(\3)",
        0,
    ),
    (
        "replace typedef enum with name",
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s+\1\s*;",
        r"class \1(CEnum):\n\2",
        0,
    ),
    (
        "replace typedef enum without name",
        r"\btypedef\s+enum\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \2(CEnum):\n\1",
        0,
    ),
    (
        "replace typedef enum without name, with pointer",
        r"\btypedef\s+enum\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2\s*;",
        r"class \2(CEnum):\n\1\nP\2 = POINTER(\2)",
        0,
    ),
    (
        "replace all comments",
        r"[\/]{2,}",
        r"#",
        0,
    ),
    (
        "remove field SAL _Field_size_",
        r"\b(_Field_size_\([^()]*\))\s*(.*)",
        r"\2 # \1",
        0,
    ),
    (
        "remove field SAL _Field_size_bytes_",
        r"(\s+)_Field_size_bytes_\([^()]*\)",
        r"\1",
        0,
    ),
    (
        "remove field SAL _Field_range_",
        r"_Field_range_\([a-zA-Z_][a-zA-Z0-9_]*\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\)",
        r"",
        0,
    ),
    (
        "remove field SAL _Field_size_bytes_full_, _Field_size_bytes_full_opt_",
        r"(_Field_size_bytes_full_|_Field_size_bytes_full_opt_)\([^()]*\)",
        r"",
        0,
    ),
    (
        "replace fields: UCHAR Reserved1;",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", \2),',
        re.MULTILINE,
    ),
    (
        "replace fields: VOID* Reserved1;",
        r"^([ ]+)(void|VOID)\s+\*\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", LPVOID),',
        re.MULTILINE,
    ),
    (
        "replace fields: UCHAR Reserved1[12];",  #     OPC_TABLE_ENTRY OPCTable[ 1 ]; # can be many of these here....
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\[\s*([a-zA-Z0-9_]+)\s*\]\s*;",
        r'\1("\3", \2 * \4),',
        re.MULTILINE,
    ),
    (
        "replace fields: UCHAR ReservationKeyList[0][8];",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\[\s*([a-zA-Z0-9_]+)\s*\]\s*\[\s*([a-zA-Z0-9_]+)\s*\]\s*;",
        r'\1("\3", (\2 * \4) * \5),',
        re.MULTILINE,
    ),
    (
        "replace fields with bits: ULONGLONG MQES      : 16;",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(\d+)\s*;",
        r'\1("\3", \2, \4),',
        re.MULTILINE,
    ),
    (
        "replace fields: struct pointer",
        r"^([ ]+)struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_][a-zA-Z0-9_]*);",
        r'\1("\3", POINTER(\2)),  # fixme: might be recursive',
        re.MULTILINE,
    ),
    (
        "replace enum fields without assignment",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s*,[ ]*(#[^\n]*)?$",
        r"\1\2  \3",
        re.MULTILINE,
    ),
    (
        "replace enum fields with assignment",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([a-zA-Z0-9_]+)\s*,[ ]*(#[^\n]*)?$",
        r"\1\2 =\3 \4",
        re.MULTILINE,
    ),
    (
        "replace simple struct typedef",  # do struct replaces before others so struct will match as keyword
        r"^[ ]*typedef\s+(?:struct\s+)?_?([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2;",
        r"\2 = \1\nP\2 = POINTER(\1)",
        re.MULTILINE,
    ),
    (
        "replace simple typedef var",  # typedef unsigned int UINT;
        r"^[ ]*typedef\s+((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+)([a-zA-Z_][a-zA-Z0-9_]*);",
        typedef_sub,
        re.MULTILINE,
    ),
    (
        "replace simple typedef double var",  # typedef ULONG DEVICE_DATA_MANAGEMENT_SET_ACTION, DEVICE_DSM_ACTION;
        r"^[ ]*typedef\s+((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+)([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = \1\n\3 = \1",
        re.MULTILINE,
    ),
    (
        "replace simple typedef var, pointer",  # typedef signed char INT8, *PINT8;
        r"^[ ]*typedef\s+((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+)([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = \1\n\3 = POINTER(\1)",
        re.MULTILINE,
    ),
    (
        "replace simple pointer typedef",
        r"^[ ]*typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+\*([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = POINTER(\1)",
        re.MULTILINE,
    ),
    (
        "remove line continuations",
        r"\\\n",
        r"",
        0,
    ),
    (
        "replace multiline comments",
        r"\/\*(.*?)\*\/",
        r"'''\1'''",
        re.DOTALL,
    ),
    (
        "replace cplusplus 1",
        r"#if defined __cplusplus.*?#endif[^\n]*",
        r"",
        re.DOTALL,
    ),
    (
        "replace cplusplus 2",
        r"#ifdef __cplusplus.*?#endif[^\n]*",
        r"",
        re.DOTALL,
    ),
    (
        "replace long literals",
        r"\b((?:0[xX][0-9a-fA-F]{8})|(?:\d+))L",
        r"c_long(\1)",
        0,
    ),
    (
        "replace ulong literals",
        r"\b((?:0x[0-9a-fA-F]{8})|(?:\d+))u",
        r"c_ulong(\1)",
        0,
    ),
    (
        "remove struct SAL",
        r"\b(_Struct_size_bytes_\([^()]*\))\s*(struct.*)",
        r"\2 # \1",
        0,
    ),
    (
        "replace C_ASSERT",
        r"C_ASSERT\s*(\([^)(]*(?:\([^)(]*(?:\([^)(]*(?:\([^)(]*\)[^)(]*)*\)[^)(]*)*\)[^)(]*)*\))",
        r"assert \1",
        0,
    ),
    (
        "replace DEFINE_GUID",
        r"DEFINE_GUID\(\s*([a-zA-Z_][a-zA-Z0-9_]*), (0x[a-zA-Z0-9]{8}, 0x[a-zA-Z0-9]{4}, 0x[a-zA-Z0-9]{4}), (0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2}, 0x[a-zA-Z0-9]{2})\s*\)",
        r"\1 = GUID(\2, (\3))",
        0,
    ),
    (
        "replace pack push",
        r"^[ ]*#[ ]*pragma[ ]+pack[ ]*\([ ]*push[ ]*,[ ]*1[ ]*\)[ ]*$",
        r"_pack_ += 1",
        re.MULTILINE,
    ),
    (
        "replace pack pop",
        r"^[ ]*#[ ]*pragma[ ]+pack[ ]*\([ ]*pop[ ]*\)[ ]*$",
        r"_pack_ -= 1",
        re.MULTILINE,
    ),
    (
        "replace pack push name",
        r"^[ ]*#[ ]*pragma[ ]+pack[ ]*\([ ]*push[ ]*,[ ]*[a-zA-Z_][a-zA-Z0-9_]*[ ]*,[ ]*1[ ]*\)[ ]*$",
        r"_pack_ += 1",
        re.MULTILINE,
    ),
    (
        "replace pack pop name",
        r"^[ ]*#[ ]*pragma[ ]+pack[ ]*\([ ]*pop[ ]*,[ ]*[a-zA-Z_][a-zA-Z0-9_]*[ ]*\)[ ]*$",
        r"_pack_ -= 1",
        re.MULTILINE,
    ),
    (
        "comment out functions with comments",
        r"((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)(]*(?:\([^)(]*(?:\([^)(]*(?:\([^)(]*\)[^)(]*)*\)[^)(]*)*\)[^)(]*)*\)\s*{[^}{]*(?:{[^}{]*(?:{[^}{]*(?:{[^}{]*}[^}{]*)*}[^}{]*)*}[^}{]*)*})",
        r"'''\1'''",
        0,
    ),
    (
        "comment out functions",
        r"((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)(]*(?:\([^)(]*(?:\([^)(]*(?:\([^)(]*\)[^)(]*)*\)[^)(]*)*\)[^)(]*)*\)\s*'''.*'''\s*{[^}{]*(?:{[^}{]*(?:{[^}{]*(?:{[^}{]*}[^}{]*)*}[^}{]*)*}[^}{]*)*})",
        r'"""\1"""',
        re.DOTALL,
    ),
    (
        "comment out annotations",
        r"\n(_Success_\(return != FALSE\))",
        r"\n# \1",
        re.DOTALL,
    ),
]

patternsloop = [
    (
        "typedef _named struct with var, pointer",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}#\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Structure):\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer",
        r"typedef\s+struct\s+STOR_ADDRESS_ALIGN\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}#\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Structure):\n    _pack_ = 8\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer, var, pointer",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}#\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\3\s*;",
        r"class \1(Structure):\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\1 = POINTER(\1)\n\3 = \1\nP\3 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with alt var, alt pointer",
        r"typedef\s+struct\s+_([a-zA-Z0-9_]*)\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\3\s*;",
        r"class \3(Structure):  # \1\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\3 = POINTER(\3)",
        0,
    ),
    (
        "typedef named struct with var, pointer",
        r"typedef\s+struct\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}#\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Structure):\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer, LP",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*,\s*\*LP\1\s*;",
        r"class \1(Structure):\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\1 = POINTER(\1)\nLP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef unnamed struct with var, pointer",
        r"typedef\s+struct\s*{([^{}]+)}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2\s*;",
        r"class \2(Structure):\n    _pack_ = _pack_\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef _named union with var, pointer",
        r"typedef\s+union\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}#\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Union):\n    _pack_ = _pack_\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef unnamed union with var",
        r"typedef\s+union\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \2(Union):\n    _pack_ = _pack_\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef unnamed union with var, pointer",
        r"typedef\s+union\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2\s*;",
        r"class \2(Union):\n    _pack_ = _pack_\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef unnamed union with var, invalid pointer name",
        r"typedef\s+union\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*(\*\s*P[a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \2(Union):  # fixme: \3\n    _pack_ = _pack_\n    _fields_ = [\1]",
        0,
    ),
    (
        "unnamed union with var",
        r"(?<!typedef)(\s+)union\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", make_union([\2], _pack_)),',
        0,
    ),
    (
        "unnamed struct with var",
        r"(?<!typedef)(\s+)struct\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", make_struct([\2], _pack_)),',
        0,
    ),
    (
        "unnamed union",
        r"(?<!typedef)(\s+)union\s*{([^{}]+)}\s*;",
        r'\1("_unnamed_union", make_union([\2], _pack_)),',
        0,
    ),
    (
        "unnamed struct",
        r"(?<!typedef)(\s+)struct\s*{([^{}]+)}\s*;",
        r'\1("_unnamed_struct", make_struct([\2], _pack_)),',
        0,
    ),
    (
        "named struct with var",
        r"struct\s+_([a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*;",
        r'("\1", make_struct([\2], _pack_)),',
        0,
    ),
    (
        "named struct with var, alt var",
        r"struct\s+_([a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'("\1", make_struct([\2], _pack_)), # \3',
        0,
    ),
    (
        "named union, different name",
        r"union\s+_([a-zA-Z0-9_]*)\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'("\3", make_struct([\2], _pack_)), # \1',
        0,
    ),
]

wintypes = [
    "BOOL",
    "BOOLEAN",
    "BYTE",
    "CHAR",
    "DWORD",
    "HANDLE",
    "INT",
    "LONG",
    "LPBOOL",
    "LPBYTE",
    "LPCSTR",
    "LPCVOID",
    "LPCWSTR",
    "LPDWORD",
    "LPLONG",
    "LPSTR",
    "LPVOID",
    "LPWORD",
    "LPWSTR",
    "PBOOL",
    "PBOOLEAN",
    "PCHAR",
    "PULONG",
    "PUSHORT",
    "PWCHAR",
    "PWORD",
    "SHORT",
    "UINT",
    "ULONG",
    "USHORT",
    "WCHAR",
    "WORD",
    "LARGE_INTEGER",
]

c_types = [
    "c_bool",
    "c_buffer",
    "c_byte",
    "c_char",
    "c_char_p",
    "c_double",
    "c_float",
    "c_int",
    "c_int16",
    "c_int32",
    "c_int64",
    "c_int8",
    "c_long",
    "c_longdouble",
    "c_longlong",
    "c_short",
    "c_size_t",
    "c_ssize_t",
    "c_ubyte",
    "c_uint",
    "c_uint16",
    "c_uint32",
    "c_uint64",
    "c_uint8",
    "c_ulong",
    "c_ulonglong",
    "c_ushort",
    "c_void_p",
    "c_voidp",
    "c_wchar",
    "c_wchar_p",
]

required_imports = {
    Path("shared/ntdddisk.h"): [
        [
            "cwinsdk.shared.devioctl",
            [
                "METHOD_NEITHER",
                "CTL_CODE",
                "FILE_DEVICE_DISK",
                "FILE_READ_ACCESS",
                "FILE_WRITE_ACCESS",
                "METHOD_BUFFERED",
                "FILE_ANY_ACCESS",
            ],
        ],
        ["cwinsdk.shared.ntdef", ["LPWCH", "PWSTR", "ULONGLONG", "UCHAR", "PVOID", "ANYSIZE_ARRAY"]],
        ["cwinsdk.shared.basetsd", ["ULONG64"]],
        ["cwinsdk.shared.guiddef", ["GUID"]],
    ],
    Path("shared/ntddscsi.h"): [],
    Path("shared/nvme.h"): [
        ["cwinsdk.shared.ntdef", ["ANYSIZE_ARRAY", "LPWCH", "PWSTR", "ULONGLONG", "UCHAR", "PVOID"]],
        ["cwinsdk.shared.guiddef", ["GUID"]],
    ],
    Path("shared/scsi.h"): [
        ["cwinsdk", ["DECLSPEC_ALIGN"]],
        ["cwinsdk.shared.ntdef", ["ANYSIZE_ARRAY", "UCHAR", "ULONGLONG"]],
    ],
    Path("shared/ntddscsi.h"): [],
    Path("shared/winioctl.h"): [],
    Path("km/ata.h"): [["cwinsdk.shared.ntdef", ["UCHAR", "ULONGLONG", "ANYSIZE_ARRAY"]]],
}


def write_file(outpath: Path, header: str, data: str) -> None:
    with outpath.open("w", encoding="ascii") as fw:
        fw.write(header)
        fw.write(data)


def get_header(relpath: str) -> str:
    imports = "\n".join(
        f"from {module} import {', '.join(names)}" for module, names in required_imports.get(relpath, [])
    )

    header = f"""
from ctypes import Structure, Union, sizeof, POINTER
from ctypes import {", ".join(c_types)}
from ctypes.wintypes import {", ".join(wintypes)}
from cwinsdk import CEnum, make_struct, make_union
{imports}
_pack_ = 0
"""

    return header


def transpile_header(data: str, yield_steps: bool, verbose: bool = False) -> Iterator[str]:
    for name, pattern, repl, flags in patterns:
        try:
            data, num = re.subn(pattern, repl, data, flags=flags)
            if verbose:
                print(f"Name: {name}, replacements: {num}")
            if yield_steps:
                yield data
        except KeyboardInterrupt:
            logging.error("Interrupted at %r", name)
            write_file(Path("_interrupted.py"), "\n", data)
            raise

    nesting = 1000
    for _i in range(nesting):
        total = 0
        for name, pattern, repl, flags in patternsloop:
            try:
                data, num = re.subn(pattern, repl, data, flags=flags)
                if verbose:
                    print(f"Name: {name}, replacements: {num}")
                total += num
                if yield_steps:
                    yield data
            except KeyboardInterrupt:
                write_file(Path("_interrupted.py"), "\n", data)
                raise

        if total == 0:
            break
    else:
        msg = f"There are probably not {nesting} levels of nesting. Check for replacement loops."
        raise RuntimeError(msg)

    yield data


def transpile_header_file(inpath: Path, outpath: Path, relpath: str, interactive: bool) -> None:
    assert inpath.suffix == ".h"

    data = inpath.read_text(encoding="ascii")

    header = get_header(relpath)
    outdata = None
    for outdata in transpile_header(data, yield_steps=interactive):
        write_file(outpath, header, outdata)
        if interactive:
            input("continue")
