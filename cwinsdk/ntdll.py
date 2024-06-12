from ctypes import POINTER
from ctypes.wintypes import HANDLE, ULONG

from . import status_success, windll
from .km.wdm import IO_STATUS_BLOCK
from .shared.ntdef import NTSTATUS, PVOID
from .wintypes import BOOLEAN

NtQueryEaFile = windll.ntdll.NtQueryEaFile
NtQueryEaFile.argtypes = [
    HANDLE,
    POINTER(IO_STATUS_BLOCK),
    PVOID,
    ULONG,
    BOOLEAN,
    PVOID,
    ULONG,
    POINTER(ULONG),
    BOOLEAN,
]
NtQueryEaFile.restype = NTSTATUS
NtQueryEaFile.errcheck = status_success
