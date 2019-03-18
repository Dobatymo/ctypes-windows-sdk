from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure, c_int, POINTER
from ctypes.wintypes import DWORD, HANDLE

from .basetsd import UINT_PTR, LONG_PTR

MAX_PATH = 260

WPARAM = UINT_PTR
LPARAM = LONG_PTR
LRESULT = LONG_PTR

HGLOBAL = HANDLE
HLOCAL = HANDLE
GLOBALHANDLE = HANDLE
LOCALHANDLE = HANDLE

def DECLARE_HANDLE():
	class HANDLE__(Structure):
		_fields_ = [
			("unused", c_int),
		]

	return POINTER(HANDLE__)

HKEY = DECLARE_HANDLE()
HMETAFILE = DECLARE_HANDLE()
HINSTANCE = DECLARE_HANDLE()
HMODULE = HINSTANCE
HRGN = DECLARE_HANDLE()
HRSRC = DECLARE_HANDLE()
HSPRITE = DECLARE_HANDLE()
HLSURF = DECLARE_HANDLE()
HSTR = DECLARE_HANDLE()
HTASK = DECLARE_HANDLE()
HWINSTA = DECLARE_HANDLE()
HKL = DECLARE_HANDLE()

class FILETIME(Structure):
	_fields_ = [
		("dwLowDateTime", DWORD),
		("dwHighDateTime", DWORD),
	]
