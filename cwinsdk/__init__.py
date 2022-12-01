import platform
from ctypes import LibraryLoader, Structure, WinDLL, WinError, c_int
from ctypes.wintypes import HANDLE
from typing import Any, Callable, Iterable, Iterator, Tuple

windll = LibraryLoader(WinDLL)

INVALID_HANDLE_VALUE = HANDLE(-1).value  # copied from cwinsdk.um.handleapi to prevent cyclic imports
S_OK = 0  # copied from cwinsdk.shared.winerror


class CEnum(c_int):
    pass


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

    for name, _ in struct._fields_:
        value = getattr(struct, name)

        if hasattr(value, "_fields_"):
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


def _not_available(funcname: str) -> Callable:
    def inner(*args, **kwargs):
        raise OSError(f"{funcname}() is not available on {platform.platform()}")

    return inner
