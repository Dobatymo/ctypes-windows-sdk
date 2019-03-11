from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import c_void_p, c_char, c_short, c_long, c_double, c_ubyte, c_ushort, c_ulong, c_int64, c_uint64

PVOID = c_void_p
POINTER_64 = c_void_p
PVOID64 = c_void_p

CHAR = c_char
SHORT = c_short
LONG = c_long
DOUBLE = c_double

UCHAR = c_ubyte
USHORT = c_ushort
ULONG = c_ulong

LONGLONG = c_int64
ULONGLONG = c_uint64

LOGICAL = ULONG
