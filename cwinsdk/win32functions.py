from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import windll, wintypes, POINTER
from ctypes.wintypes import DWORD, HANDLE, UINT, BOOL, LPVOID, ULARGE_INTEGER, LONG
from ctypes.wintypes import LPSTR, LPWSTR, LPCSTR, LPCWSTR
from ctypes import c_int as ENUM_TYPE

from .um.minwinbase import OVERLAPPED
from .shared.minwindef import HMODULE
from .um.WinBase import TOKEN_PRIVILEGES
from .um.winnt import LUID

FARPROC = LPVOID # todo: fix!!!

# advapi32

## securitybaseapi.h, see um/securitybaseapi.py
## WinBase.h, see um/WinBase.py
## processthreadsapi.h, see um/processthreadsapi.py

# kernel32

## libloaderapi.h, see um/libloaderapi.py
## handleapi.h, see um/handleapi.py
## fileapi.h, see um/fileapi.py
## WinBase.h, see um/WinBase.py
## consoleapi2.h, see um/consoleapi2.py

DeviceIoControl = windll.kernel32.DeviceIoControl
DeviceIoControl.argtypes = [HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, POINTER(DWORD), POINTER(OVERLAPPED)]
DeviceIoControl.restype = BOOL 

GetCurrentProcess = windll.kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = HANDLE

GetProcAddress = windll.kernel32.GetProcAddress
GetProcAddress.argtypes = [HMODULE, LPCSTR]
GetProcAddress.restype = FARPROC

GetStdHandle = windll.kernel32.GetStdHandle
GetStdHandle.argtypes = [DWORD]
GetStdHandle.restype = BOOL

# user32

ExitWindowsEx = windll.user32.ExitWindowsEx
ExitWindowsEx.argtypes = [UINT, DWORD]
ExitWindowsEx.restype = BOOL
