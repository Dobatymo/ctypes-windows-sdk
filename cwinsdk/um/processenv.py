from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCSTR, LPCWSTR, LPSTR, LPWSTR

from .. import nonzero, validhandle, windll
from .winnt import LPCH, LPWCH, PHANDLE

SetEnvironmentStringsW = windll.kernel32.SetEnvironmentStringsW
SetEnvironmentStringsW.argtypes = [LPWCH]
SetEnvironmentStringsW.restype = BOOL

GetStdHandle = windll.kernel32.GetStdHandle
GetStdHandle.argtypes = [DWORD]
GetStdHandle.restype = HANDLE
GetStdHandle.errcheck = validhandle

SetStdHandle = windll.kernel32.SetStdHandle
SetStdHandle.argtypes = [DWORD, HANDLE]
SetStdHandle.restype = BOOL
SetStdHandle.errcheck = nonzero

SetStdHandleEx = windll.kernel32.SetStdHandleEx
SetStdHandleEx.argtypes = [DWORD, HANDLE, PHANDLE]
SetStdHandleEx.restype = BOOL

GetCommandLineA = windll.kernel32.GetCommandLineA
GetCommandLineA.argtypes = []
GetCommandLineA.restype = LPSTR

GetCommandLineW = windll.kernel32.GetCommandLineW
GetCommandLineW.argtypes = []
GetCommandLineW.restype = LPWSTR

GetEnvironmentStrings = windll.kernel32.GetEnvironmentStrings
GetEnvironmentStrings.argtypes = []
GetEnvironmentStrings.restype = LPCH

GetEnvironmentStringsW = windll.kernel32.GetEnvironmentStringsW
GetEnvironmentStringsW.argtypes = []
GetEnvironmentStringsW.restype = LPWCH

FreeEnvironmentStringsA = windll.kernel32.FreeEnvironmentStringsA
FreeEnvironmentStringsA.argtypes = [LPCH]
FreeEnvironmentStringsA.restype = BOOL

FreeEnvironmentStringsW = windll.kernel32.FreeEnvironmentStringsW
FreeEnvironmentStringsW.argtypes = [LPWCH]
FreeEnvironmentStringsW.restype = BOOL

GetEnvironmentVariableA = windll.kernel32.GetEnvironmentVariableA
GetEnvironmentVariableA.argtypes = [LPCSTR, LPSTR, DWORD]
GetEnvironmentVariableA.restype = DWORD

GetEnvironmentVariableW = windll.kernel32.GetEnvironmentVariableW
GetEnvironmentVariableW.argtypes = [LPCWSTR, LPWSTR, DWORD]
GetEnvironmentVariableW.restype = DWORD

SetEnvironmentVariableA = windll.kernel32.SetEnvironmentVariableA
SetEnvironmentVariableA.argtypes = [LPCSTR, LPCSTR]
SetEnvironmentVariableA.restype = BOOL

SetEnvironmentVariableW = windll.kernel32.SetEnvironmentVariableW
SetEnvironmentVariableW.argtypes = [LPCWSTR, LPCWSTR]
SetEnvironmentVariableW.restype = BOOL

ExpandEnvironmentStringsA = windll.kernel32.ExpandEnvironmentStringsA
ExpandEnvironmentStringsA.argtypes = [LPCSTR, LPSTR, DWORD]
ExpandEnvironmentStringsA.restype = DWORD

ExpandEnvironmentStringsW = windll.kernel32.ExpandEnvironmentStringsW
ExpandEnvironmentStringsW.argtypes = [LPCWSTR, LPWSTR, DWORD]
ExpandEnvironmentStringsW.restype = DWORD

SetCurrentDirectoryA = windll.kernel32.SetCurrentDirectoryA
SetCurrentDirectoryA.argtypes = [LPCSTR]
SetCurrentDirectoryA.restype = BOOL

SetCurrentDirectoryW = windll.kernel32.SetCurrentDirectoryW
SetCurrentDirectoryW.argtypes = [LPCWSTR]
SetCurrentDirectoryW.restype = BOOL

GetCurrentDirectoryA = windll.kernel32.GetCurrentDirectoryA
GetCurrentDirectoryA.argtypes = [DWORD, LPSTR]
GetCurrentDirectoryA.restype = DWORD

GetCurrentDirectoryW = windll.kernel32.GetCurrentDirectoryW
GetCurrentDirectoryW.argtypes = [DWORD, LPWSTR]
GetCurrentDirectoryW.restype = DWORD

SearchPathA = windll.kernel32.SearchPathA
SearchPathA.argtypes = [LPCSTR, LPCSTR, LPCSTR, DWORD, LPSTR, POINTER(LPSTR)]
SearchPathA.restype = DWORD

SearchPathW = windll.kernel32.SearchPathW
SearchPathW.argtypes = [LPCWSTR, LPCWSTR, LPCWSTR, DWORD, LPWSTR, POINTER(LPWSTR)]
SearchPathW.restype = DWORD

NeedCurrentDirectoryForExePathA = windll.kernel32.NeedCurrentDirectoryForExePathA
NeedCurrentDirectoryForExePathA.argtypes = [LPCSTR]
NeedCurrentDirectoryForExePathA.restype = BOOL

NeedCurrentDirectoryForExePathW = windll.kernel32.NeedCurrentDirectoryForExePathW
NeedCurrentDirectoryForExePathW.argtypes = [LPCWSTR]
NeedCurrentDirectoryForExePathW.restype = BOOL
