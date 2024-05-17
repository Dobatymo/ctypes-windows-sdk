import platform
from ctypes import LibraryLoader, Structure, Union, WinDLL, WinError, c_int
from ctypes.wintypes import HANDLE
from typing import Any, Callable, Iterable, Iterator, Tuple

windll = LibraryLoader(WinDLL)

INVALID_HANDLE_VALUE = HANDLE(-1).value  # copied from cwinsdk.um.handleapi to prevent cyclic imports
S_OK = 0  # copied from cwinsdk.shared.winerror
MIDL_PASS = False
STATUS_SUCCESS = 0  # copied from cwinsdk.shared.ntstatus


class CEnum(c_int):
    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, CEnum):
            return self.value == other.value
        return NotImplemented


class WinApiError(OSError):
    pass


def _value_with_length(values: Iterable) -> Iterator:
    for value in values:
        if hasattr(value, "_fields_"):
            value = dict(_struct2pairs(value))
        elif hasattr(value, "_length_"):
            raise RuntimeError("Unhandled case: _length_")
        elif hasattr(value, "value"):
            value = value.value

        yield value


def _struct2pairs(struct: Structure) -> Iterator[Tuple[str, Any]]:
    for fieldinfo in struct._fields_:
        if len(fieldinfo) == 2:
            name, _ = fieldinfo
        elif len(fieldinfo) == 3:
            name, _, _ = fieldinfo
        else:
            raise ValueError("too many values to unpack (expected 2 or 3)")

        value = getattr(struct, name)

        if hasattr(value, "_fields_"):
            if name in struct._anonymous_:
                yield from _struct2pairs(value)
                continue
            value = dict(_struct2pairs(value))
        elif hasattr(value, "_length_"):
            value = list(_value_with_length(value))
        elif hasattr(value, "value"):
            value = value.value

        yield name, value


def struct2dict(struct: Structure) -> dict:
    return dict(_struct2pairs(struct))


def nonzero(result, func, arguments):
    if result == 0:
        raise WinError()

    return result


def validhandle(result, func, arguments):
    if result == INVALID_HANDLE_VALUE:
        raise WinError()

    return result


def s_ok(result, func, arguments):
    if result != S_OK:
        raise WinError(result)  # no error code set in windows

    return result


def status_success(result, func, arguments):
    if result != STATUS_SUCCESS:
        raise WinError(result)

    return result


def _not_available(funcname: str) -> Callable:
    def inner(*args, **kwargs):
        raise OSError(f"{funcname}() is not available on {platform.platform()}")

    return inner


def make_struct(fields):
    anonymous = []
    for name, *_ in fields:
        if name in ["u", "DUMMYSTRUCTNAME"]:
            anonymous.append(name)

    class _Structure(Structure):
        _anonymous_ = anonymous
        _fields_ = fields

    return _Structure


def make_union(fields):
    anonymous = []
    for name, *_ in fields:
        if name in ["u", "DUMMYSTRUCTNAME"]:
            anonymous.append(name)

    class _Union(Union):
        _anonymous_ = anonymous
        _fields_ = fields

    return _Union
