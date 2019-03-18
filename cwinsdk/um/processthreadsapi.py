from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import windll, POINTER
from ctypes.wintypes import BOOL, HANDLE, DWORD

OpenProcessToken = windll.advapi32.OpenProcessToken
OpenProcessToken.argtypes = [HANDLE, DWORD, POINTER(HANDLE)]
OpenProcessToken.restype = BOOL
