from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import POINTER, Structure, c_float, c_int, c_long, c_ubyte, c_uint, c_ulong, c_ushort, c_void_p
from ctypes.wintypes import HANDLE

from .basetsd import LONG_PTR, UINT_PTR

CPOINTER = POINTER

ULONG = c_ulong
PULONG = POINTER(ULONG)
USHORT = c_ushort
PUSHORT = POINTER(USHORT)
UCHAR = c_ubyte
PUCHAR = POINTER(UCHAR)

MAX_PATH = 260

DWORD = c_ulong
BOOL = c_int 
BYTE = c_ubyte
WORD = c_ushort 
FLOAT = c_float 
PFLOAT = POINTER(FLOAT)
PBOOL = POINTER(BOOL)
LPBOOL = POINTER(BOOL)
PBYTE = POINTER(BYTE)
LPBYTE = POINTER(BYTE)
PINT = POINTER(c_int)
LPINT = POINTER(c_int)
PWORD = POINTER(WORD)
LPWORD = POINTER(WORD)
LPLONG = POINTER(c_long)

PDWORD = POINTER(DWORD)
LPDWORD = POINTER(DWORD)
LPVOID = c_void_p
LPCVOID = CPOINTER(c_long)

INT = c_int
UINT = c_uint
PUINT = POINTER(UINT)

WPARAM = UINT_PTR 
LPARAM = LONG_PTR 
LRESULT = LONG_PTR 

SPHANDLE = POINTER(HANDLE)
LPHANDLE = POINTER(HANDLE)
HGLOBAL = HANDLE
HLOCAL = HANDLE
GLOBALHANDLE = HANDLE
LOCALHANDLE = HANDLE

ATOM = WORD # BUGBUG - might want to remove this from minwin

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
PFILETIME = LPFILETIME = POINTER(FILETIME)
