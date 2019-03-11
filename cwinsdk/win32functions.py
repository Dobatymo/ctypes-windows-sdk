from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import windll, wintypes, POINTER
from ctypes.wintypes import DWORD, HANDLE, UINT, PHANDLE, LPCWSTR, BOOL, LPVOID, LPCSTR, ULARGE_INTEGER, LPWSTR, LPSTR
from ctypes import c_int as ENUM_TYPE

from .um.minwinbase import SECURITY_ATTRIBUTES, OVERLAPPED
from .um.WinBase import FILE_ID_DESCRIPTOR, TOKEN_PRIVILEGES
from .win32structs import CONSOLE_SCREEN_BUFFER_INFO
from .um.winnt import LUID

AdjustTokenPrivileges = windll.advapi32.AdjustTokenPrivileges
AdjustTokenPrivileges.argtypes = [HANDLE, BOOL, POINTER(TOKEN_PRIVILEGES), DWORD, POINTER(TOKEN_PRIVILEGES), POINTER(DWORD)]
AdjustTokenPrivileges.restype = BOOL

LookupPrivilegeNameA = windll.advapi32.LookupPrivilegeNameA
LookupPrivilegeNameA.argtypes = [LPCSTR, POINTER(LUID), LPSTR, POINTER(DWORD)]
LookupPrivilegeNameA.restype = BOOL

LookupPrivilegeNameW = windll.advapi32.LookupPrivilegeNameW
LookupPrivilegeNameW.argtypes = [LPCWSTR, POINTER(LUID), LPWSTR, POINTER(DWORD)]
LookupPrivilegeNameW.restype = BOOL

LookupPrivilegeValueA = windll.advapi32.LookupPrivilegeValueA
LookupPrivilegeValueA.argtypes = [LPCSTR, LPCSTR, POINTER(LUID)]
LookupPrivilegeValueA.restype = BOOL

LookupPrivilegeValueW = windll.advapi32.LookupPrivilegeValueW
LookupPrivilegeValueW.argtypes = [LPCWSTR, LPCWSTR, POINTER(LUID)]
LookupPrivilegeValueW.restype = BOOL

OpenProcessToken = windll.advapi32.OpenProcessToken
OpenProcessToken.argtypes = [HANDLE, DWORD, PHANDLE]
OpenProcessToken.restype = BOOL

CloseHandle = windll.kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL 

CreateFileW = windll.kernel32.CreateFileW
CreateFileW.argtypes = [LPCWSTR, DWORD, DWORD, POINTER(SECURITY_ATTRIBUTES), DWORD, DWORD, HANDLE]
CreateFileW.restype = HANDLE

GetCurrentProcess = windll.kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = HANDLE

GetFileAttributesW = windll.kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [LPCWSTR]
GetFileAttributesW.restype = DWORD

DeviceIoControl = windll.kernel32.DeviceIoControl
DeviceIoControl.argtypes = [HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, POINTER(DWORD), POINTER(OVERLAPPED)]
DeviceIoControl.restype = BOOL 

MoveFileExA = windll.kernel32.MoveFileExA
MoveFileExA.argtypes = [LPCSTR, LPCSTR, DWORD]
MoveFileExA.restype = BOOL

MoveFileExW = windll.kernel32.MoveFileExW
MoveFileExW.argtypes = [LPCWSTR, LPCWSTR, DWORD]
MoveFileExW.restype = BOOL

GetFileInformationByHandleEx = windll.kernel32.GetFileInformationByHandleEx
GetFileInformationByHandleEx.argtypes = [HANDLE, ENUM_TYPE, LPVOID, DWORD] # FILE_INFO_BY_HANDLE_CLASS
GetFileInformationByHandleEx.restype = BOOL

OpenFileById = windll.kernel32.OpenFileById
OpenFileById.argtypes = [HANDLE, POINTER(FILE_ID_DESCRIPTOR), DWORD, DWORD, POINTER(SECURITY_ATTRIBUTES), DWORD]
OpenFileById.restype = HANDLE

GetDiskFreeSpaceExW = windll.kernel32.GetDiskFreeSpaceExW
GetDiskFreeSpaceExW.argtypes = [LPCWSTR, POINTER(ULARGE_INTEGER), POINTER(ULARGE_INTEGER), POINTER(ULARGE_INTEGER)]
GetDiskFreeSpaceExW.restype = BOOL

GetStdHandle = windll.kernel32.GetStdHandle
GetStdHandle.argtypes = [DWORD]
GetStdHandle.restype = BOOL

GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
GetConsoleScreenBufferInfo.argtypes = [HANDLE, POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
GetConsoleScreenBufferInfo.restype = BOOL

GetVolumeInformationW = windll.kernel32.GetVolumeInformationW
GetVolumeInformationW.argtypes = [LPCWSTR, LPWSTR, DWORD, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD), LPWSTR, DWORD]
GetVolumeInformationW.restype = BOOL

ExitWindowsEx = windll.user32.ExitWindowsEx
ExitWindowsEx.argtypes = [UINT, DWORD]
ExitWindowsEx.restype = BOOL
