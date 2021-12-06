from ctypes.wintypes import BOOL, DWORD, HANDLE

from .. import nonzero, windll
from ..shared.minwindef import LPHANDLE

INVALID_HANDLE_VALUE = HANDLE(-1).value

# functions

CloseHandle = windll.kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL
CloseHandle.errcheck = nonzero

DuplicateHandle = windll.kernel32.DuplicateHandle
DuplicateHandle.argtypes = [HANDLE, HANDLE, HANDLE, LPHANDLE, DWORD, BOOL, DWORD]
DuplicateHandle.restype = BOOL
DuplicateHandle.errcheck = nonzero
