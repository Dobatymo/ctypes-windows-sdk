import re
from pathlib import Path

patterns = [
    (
        "replace normal defines",
        r"#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_]+)[ ]*(\/\/.*)?\n",
        r"\1 = \2 \3\n",
        0,
    ),
    (
        "replace normal defines string",
        r'#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+("[^"\n]*")[ ]*(\/\/.*)?\n',
        r"\1 = \2 \3\n",
        0,
    ),
    (
        "replace function defines",
        r"#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z0-9_\(\), \|]+)\n",
        r"\1 = \2\n",
        0,
    ),
    (
        "remove empty comments",
        r"^[ ]*\/\/\n",
        r"",
        re.MULTILINE,
    ),
    (
        "typedef _named struct with var, pointer",
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(CEnum):\n\2\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer, LP",
        r"\btypedef\s+enum\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*,\s*\*\s*LP\1\s*;",
        r"class \1(CEnum):\n\2\nP\1 = POINTER(\1)\nLP\1 = POINTER(\1)",
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
        "remove field SAL",
        r"\b(_Field_size_\([^()]*\))\s*(.*)",
        r"\2 # \1",
        0,
    ),
    (
        "replace fields: UCHAR Reserved1;",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", \2),',
        re.MULTILINE,
    ),
    (
        "replace fields: UCHAR Reserved1[12];",
        r"^([ ]+)([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\[([a-zA-Z0-9_]+)\]\s*;",
        r'\1("\3", \2 * \4),',
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
        "replace simple typedef var",
        r"^typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = \1",
        re.MULTILINE,
    ),
    (
        "replace simple typedef double var",  # typedef ULONG DEVICE_DATA_MANAGEMENT_SET_ACTION, DEVICE_DSM_ACTION;
        r"^typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = \1\n\3 = \1",
        re.MULTILINE,
    ),
    (
        "replace simple pointer typedef",
        r"^typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+\*([a-zA-Z_][a-zA-Z0-9_]*);",
        r"\2 = POINTER(\1)",
        re.MULTILINE,
    ),
    (
        "replace simple struct typedef",
        r"^typedef\s+(?:struct\s+)?_?([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2;",
        r"\2 = \1\nP\2 = POINTER(\1)",
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
        "replace cplusplus",
        r"#if defined __cplusplus.*?#endif[^\n]*",
        r"",
        re.DOTALL,
    ),
    (
        "replace long literals",
        r"\b((?:0x[0-9a-fA-F]{8})|(?:\d+))L",
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
    # (
    #    "comment out functions",
    #    r"((?:[a-zA-Z_][a-zA-Z0-9_]*\s+)+\s*\((?:[^()]*|\((?:[^()]*|\([^()]*\))*\))*\)\s*\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\})",
    #    r'"""\1"""',
    #    0,
    # ),
]


patternsloop = [
    (
        "typedef _named struct with var, pointer",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Structure):\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer, var, pointer",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\3\s*;",
        r"class \1(Structure):\n    _fields_ = [\2]\nP\1 = POINTER(\1)\n\3 = \1\nP\3 = POINTER(\1)",
        0,
    ),
    (
        "typedef named struct with var, pointer",
        r"typedef\s+struct\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Structure):\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef _named struct with var, pointer, LP",
        r"typedef\s+struct\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{([^{}]+)}\s*\1\s*,\s*\*\s*P\1\s*,\s*\*LP\1\s*;",
        r"class \1(Structure):\n    _fields_ = [\2]\nP\1 = POINTER(\1)\nLP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef unnamed struct with var, pointer",
        r"typedef\s+struct\s*{([^{}]+)}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2\s*;",
        r"class \2(Structure):\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef _named union with var, pointer",
        r"typedef\s+union\s+_([a-zA-Z_][a-zA-Z0-9_]*)\s*{((?:[^{}\n]*(?:#[^\n]*)?\n)*)}\s*\1\s*,\s*\*\s*P\1\s*;",
        r"class \1(Union):\n    _fields_ = [\2]\nP\1 = POINTER(\1)",
        0,
    ),
    (
        "typedef unnamed union with var",
        r"typedef\s+union\s*{([^{}]+)}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \2(Union):\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef unnamed union with var, pointer",
        r"typedef\s+union\s*{([^{}]+)}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*\*\s*P\2\s*;",
        r"class \2(Union):\n    _fields_ = [\1]",
        0,
    ),
    (
        "typedef unnamed union with var, invalid pointer name",
        r"typedef\s+union\s*{([^{}]+)}\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*(\*\s*P[a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r"class \2(Union):  # fixme: \3\n    _fields_ = [\1]",
        0,
    ),
    (
        "unnamed union with var",
        r"(?<!typedef)(\s+)union\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", make_union([\2])),',
        0,
    ),
    (
        "unnamed struct with var",
        r"(?<!typedef)(\s+)struct\s*{([^{}]+)}\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;",
        r'\1("\3", make_struct([\2])),',
        0,
    ),
    (
        "unnamed union",
        r"(?<!typedef)(\s+)union\s*{([^{}]+)}\s*;",
        r'\1("_unnamed_union", make_union([\2])),',
        0,
    ),
    (
        "unnamed struct",
        r"(?<!typedef)(\s+)struct\s*{([^{}]+)}\s*;",
        r'\1("_unnamed_struct", make_struct([\2])),',
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

required_imports = {
    "shared/ntdddisk.h": [
        [
            ".devioctl",
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
        [".ntdef", ["LPWCH", "PWSTR", "ULONGLONG", "UCHAR", "PVOID", "ANYSIZE_ARRAY"]],
        [".basetsd", ["ULONG64"]],
        [".guiddef", ["GUID"]],
    ],
    "shared/nvme.h": [
        [".ntdef", ["LPWCH", "PWSTR", "ULONGLONG", "UCHAR", "PVOID", "ANYSIZE_ARRAY"]],
        [".guiddef", ["GUID"]],
    ],
}


def write_file(outpath, header, data):
    with open(outpath, "w", encoding="ascii") as fw:
        fw.write(header)
        fw.write(data)


def convert_header(relpath: str, pause: bool) -> Path:
    inbasepath = Path("C:/Program Files (x86)/Windows Kits/10/Include/10.0.22621.0/")
    outbasepath = Path("D:/OneDrive/Repositories/public-libs/ctypes-windows-sdk-auto/cwinsdk/")

    inpath = inbasepath / relpath
    assert inpath.suffix == ".h"
    outpath = (outbasepath / relpath).with_suffix(".py")
    outpath.parent.mkdir(parents=True, exist_ok=True)

    imports = "\n".join(
        f"from {module} import {', '.join(names)}" for module, names in required_imports.get(relpath, [])
    )

    header = f"""
from ctypes import Structure, Union, sizeof, POINTER
from ctypes.wintypes import {", ".join(wintypes)}
from .. import CEnum, make_struct, make_union
{imports}
"""

    with open(inpath, encoding="ascii") as fr:
        data = fr.read()

    for name, pattern, repl, flags in patterns:
        print(name)
        data, num = re.subn(pattern, repl, data, flags=flags)
        print(num)
        if pause:
            write_file(outpath, header, data)
            input("continue")

    while True:
        total = 0
        for name, pattern, repl, flags in patternsloop:
            print(name)
            data, num = re.subn(pattern, repl, data, flags=flags)
            total += num
            if pause:
                write_file(outpath, header, data)
                input("continue")

        if total == 0:
            break

    write_file(outpath, header, data)

    if pause:
        input("processing done")

    return outpath


def main(args):
    header_files = ["shared/ntdddisk.h", "shared/nvme.h"]
    header_files = ["shared/ntddstor.h"]

    for relpath in header_files:
        print(relpath)
        outpath = os.fspath(convert_header(relpath, pause=args.pause_after_each_pattern))
        try:
            subprocess.run(["py", "-m", "ruff", "format", outpath], capture_output=True, check=True, encoding="utf-8")
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            print(f"{e.cmd} failed")
            return

    for relpath in header_files:
        print(relpath)
        try:
            subprocess.run(
                ["py", "-m", "ruff", "check", outpath, "--fix"], capture_output=True, check=True, encoding="utf-8"
            )
        except subprocess.CalledProcessError as e:
            print(e.stdout)
            print(e.stderr)
            print(f"{e.cmd} failed")
            return


if __name__ == "__main__":
    import os
    import subprocess
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--pause-after-each-pattern", action="store_true")
    args = parser.parse_args()

    main(args)
