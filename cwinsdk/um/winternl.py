from ctypes import POINTER
from ctypes.wintypes import HANDLE, LARGE_INTEGER, ULONG

from .. import status_success, windll
from ..km.wdm import IO_STATUS_BLOCK
from ..shared.ntdef import NTSTATUS, OBJECT_ATTRIBUTES, PVOID
from ..um.winnt import ACCESS_MASK

NtClose = windll.ntdll.NtClose
NtClose.argtypes = [HANDLE]
NtClose.restype = NTSTATUS
NtClose.errcheck = status_success

RtlNtStatusToDosError = windll.ntdll.RtlNtStatusToDosError
RtlNtStatusToDosError.argtypes = [NTSTATUS]
RtlNtStatusToDosError.restype = ULONG

NtCreateFile = windll.ntdll.NtCreateFile
NtCreateFile.argtypes = [
    POINTER(HANDLE),
    ACCESS_MASK,
    POINTER(OBJECT_ATTRIBUTES),
    POINTER(IO_STATUS_BLOCK),
    POINTER(LARGE_INTEGER),
    ULONG,
    ULONG,
    ULONG,
    ULONG,
    PVOID,
    ULONG,
]
NtCreateFile.restype = NTSTATUS
NtCreateFile.errcheck = status_success
