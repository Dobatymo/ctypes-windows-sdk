from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, HANDLE

from .. import windll

OpenProcessToken = windll.advapi32.OpenProcessToken
OpenProcessToken.argtypes = [HANDLE, DWORD, POINTER(HANDLE)]
OpenProcessToken.restype = BOOL

GetCurrentProcess = windll.kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = HANDLE
