from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes.wintypes import HANDLE, BOOL, DWORD

from .. import windll, nonzero
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
