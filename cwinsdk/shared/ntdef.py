from ctypes import (
    POINTER,
    Structure,
    c_char,
    c_double,
    c_int64,
    c_long,
    c_short,
    c_ubyte,
    c_uint64,
    c_ulong,
    c_ushort,
    c_void_p,
)
from ctypes.wintypes import HANDLE, WCHAR

PWCHAR = POINTER(WCHAR)
LPWCH = POINTER(WCHAR)
PWCH = POINTER(WCHAR)

LPCWCH = POINTER(WCHAR)  # const
PCWCH = POINTER(WCHAR)  # const

NWPSTR = POINTER(WCHAR)
LPWSTR = POINTER(WCHAR)
PWSTR = POINTER(WCHAR)


PVOID = c_void_p
POINTER_64 = c_void_p
PVOID64 = c_void_p

CHAR = c_char
SHORT = c_short
LONG = c_long
DOUBLE = c_double

UCHAR = c_ubyte
USHORT = c_ushort
ULONG = c_ulong

LONGLONG = c_int64
ULONGLONG = c_uint64

LOGICAL = ULONG

HRESULT = LONG
NTSTATUS = LONG

PCSTR = POINTER(CHAR)  # const
PSTR = POINTER(CHAR)


class STRING(Structure):
    _fields_ = [
        ("Length", USHORT),
        ("MaximumLength", USHORT),
        ("Buffer", POINTER(CHAR)),
    ]


ANSI_STRING = STRING
OEM_STRING = STRING


class CSTRING(Structure):
    _fields_ = [
        ("Length", USHORT),
        ("MaximumLength", USHORT),
        ("Buffer", POINTER(c_char)),
    ]


CANSI_STRING = STRING


class UNICODE_STRING(Structure):
    _fields_ = [
        ("Length", USHORT),
        ("MaximumLength", USHORT),
        ("Buffer", PWCH),
    ]


class OBJECT_ATTRIBUTES(Structure):
    _fields_ = [
        ("Length", ULONG),
        ("RootDirectory", HANDLE),
        ("ObjectName", POINTER(UNICODE_STRING)),
        ("Attributes", ULONG),
        ("SecurityDescriptor", PVOID),  # Points to type SECURITY_DESCRIPTOR
        ("SecurityQualityOfService", PVOID),  # Points to type SECURITY_QUALITY_OF_SERVICE
    ]
