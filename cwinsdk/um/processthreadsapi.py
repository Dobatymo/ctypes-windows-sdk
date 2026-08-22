from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, HANDLE

from .. import nonzero, windll

OpenProcessToken = windll.advapi32.OpenProcessToken
OpenProcessToken.argtypes = [HANDLE, DWORD, POINTER(HANDLE)]
OpenProcessToken.restype = BOOL
OpenProcessToken.errcheck = nonzero

GetCurrentProcess = windll.kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = HANDLE

GetCurrentThread = windll.kernel32.GetCurrentThread
GetCurrentThread.argtypes = []
GetCurrentThread.restype = HANDLE

OpenThreadToken = windll.advapi32.OpenThreadToken
OpenThreadToken.argtypes = [HANDLE, DWORD, BOOL, POINTER(HANDLE)]
OpenThreadToken.restype = BOOL
OpenThreadToken.errcheck = nonzero

TerminateThread = windll.kernel32.TerminateThread
TerminateThread.argtypes = [HANDLE, DWORD]
TerminateThread.restype = BOOL
TerminateThread.errcheck = nonzero
