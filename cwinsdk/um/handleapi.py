from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import windll
from ctypes.wintypes import HANDLE, BOOL

INVALID_HANDLE_VALUE = HANDLE(-1).value

# functions

CloseHandle = windll.kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL 
