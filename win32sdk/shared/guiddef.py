from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure, Union
from ctypes import c_ulong, c_ushort, c_ubyte

class GUID(Structure):
	_fields_ = [
		("Data1", c_ulong),
		("Data2", c_ushort),
		("Data3", c_ushort),
		("Data4", c_ubyte*8),
	]
