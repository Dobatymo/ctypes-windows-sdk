from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure, Union, POINTER
from ctypes import c_ulong, c_ushort, c_ubyte

class GUID(Structure):
	_fields_ = [
		("Data1", c_ulong),
		("Data2", c_ushort),
		("Data3", c_ushort),
		("Data4", c_ubyte*8),
	]

IID = GUID
LPIID = POINTER(IID)
CLSID = GUID
LPCLSID = POINTER(CLSID)
FMTID = GUID
LPFMTID = POINTER(FMTID)
REFCLSID = POINTER(IID) # const POINTER
REFIID = POINTER(IID) # const POINTER
