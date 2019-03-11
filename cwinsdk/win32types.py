from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import POINTER
from ctypes import c_ubyte, c_uint64, c_ulong, c_longlong, c_ulonglong, c_void_p
from ctypes.wintypes import WORD

BYTE = c_ubyte # wintypes.BYTE is c_byte
ATOM = WORD
