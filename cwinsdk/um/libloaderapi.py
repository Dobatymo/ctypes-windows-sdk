from ctypes import CFUNCTYPE
from ctypes.wintypes import BOOL, DWORD, LPCSTR, LPCWSTR, LPSTR, LPVOID, LPWSTR, WORD

from .. import windll
from ..shared.basetsd import LONG_PTR
from ..shared.minwindef import HGLOBAL, HMODULE, HRSRC
from .winnt import LANGID

FARPROC = LPVOID  # todo: where does this come from?

ENUMRESTYPEPROCW = CFUNCTYPE(BOOL, HMODULE, LPWSTR, LONG_PTR)
ENUMRESTYPEPROCA = CFUNCTYPE(BOOL, HMODULE, LPSTR, LONG_PTR)
ENUMRESNAMEPROCW = CFUNCTYPE(BOOL, HMODULE, LPCWSTR, LPWSTR, LONG_PTR)
ENUMRESNAMEPROCA = CFUNCTYPE(BOOL, HMODULE, LPCSTR, LPSTR, LONG_PTR)
ENUMRESLANGPROCA = CFUNCTYPE(BOOL, HMODULE, LPCSTR, LPCSTR, WORD, LONG_PTR)
ENUMRESLANGPROCW = CFUNCTYPE(BOOL, HMODULE, LPCWSTR, LPCWSTR, WORD, LONG_PTR)

SizeofResource = windll.kernel32.SizeofResource
SizeofResource.argtypes = [HMODULE, HRSRC]
SizeofResource.restype = DWORD

LockResource = windll.kernel32.LockResource
LockResource.argtypes = [HGLOBAL]
LockResource.restype = LPVOID

LoadResource = windll.kernel32.LoadResource
LoadResource.argtypes = [HMODULE, HRSRC]
LoadResource.restype = HGLOBAL

EnumResourceTypesExW = windll.kernel32.EnumResourceTypesExW
EnumResourceTypesExW.argtypes = [HMODULE, ENUMRESTYPEPROCW, LONG_PTR, DWORD, LANGID]
EnumResourceTypesExW.restype = BOOL

EnumResourceTypesExA = windll.kernel32.EnumResourceTypesExA
EnumResourceTypesExA.argtypes = [HMODULE, ENUMRESTYPEPROCA, LONG_PTR, DWORD, LANGID]
EnumResourceTypesExA.restype = BOOL

EnumResourceNamesExW = windll.kernel32.EnumResourceNamesExW
EnumResourceNamesExW.argtypes = [HMODULE, LPCWSTR, ENUMRESNAMEPROCW, LONG_PTR, DWORD, LANGID]
EnumResourceNamesExW.restype = BOOL

EnumResourceNamesExA = windll.kernel32.EnumResourceNamesExA
EnumResourceNamesExA.argtypes = [HMODULE, LPCSTR, ENUMRESNAMEPROCA, LONG_PTR, DWORD, LANGID]
EnumResourceNamesExA.restype = BOOL

EnumResourceLanguagesExW = windll.kernel32.EnumResourceLanguagesExW
EnumResourceLanguagesExW.argtypes = [HMODULE, LPCWSTR, LPCWSTR, ENUMRESLANGPROCW, LONG_PTR, DWORD, LANGID]
EnumResourceLanguagesExW.restype = BOOL

EnumResourceLanguagesExA = windll.kernel32.EnumResourceLanguagesExA
EnumResourceLanguagesExA.argtypes = [HMODULE, LPCSTR, LPCSTR, ENUMRESLANGPROCA, LONG_PTR, DWORD, LANGID]
EnumResourceLanguagesExA.restype = BOOL

GetProcAddress = windll.kernel32.GetProcAddress
GetProcAddress.argtypes = [HMODULE, LPCSTR]
GetProcAddress.restype = FARPROC
