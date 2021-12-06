from ctypes import POINTER, c_int, c_int64, c_long, c_uint, c_uint64, c_ulong
from platform import machine

X64 = machine().endswith("64")

if X64:
    INT_PTR = c_int64
    UINT_PTR = c_uint64
    LONG_PTR = c_int64
    ULONG_PTR = c_uint64
    PULONG_PTR = POINTER(c_uint64)
else:
    INT_PTR = c_int
    UINT_PTR = c_uint
    LONG_PTR = c_long
    ULONG_PTR = c_ulong
    PULONG_PTR = POINTER(c_ulong)

SIZE_T = ULONG_PTR
SSIZE_T = LONG_PTR

DWORD_PTR = ULONG_PTR
LONG64 = c_int64
ULONG64 = c_uint64
DWORD64 = c_uint64
PDWORD64 = POINTER(DWORD64)
KAFFINITY = ULONG_PTR
