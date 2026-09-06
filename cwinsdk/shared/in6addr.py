from ctypes import POINTER, Structure, Union

from .ntdef import UCHAR, USHORT


class IN6_ADDR_U(Union):
    _fields_ = [("Byte", UCHAR * 16), ("Word", USHORT * 8)]


class IN6_ADDR(Structure):
    _fields_ = [("u", IN6_ADDR_U)]


PIN6_ADDR = POINTER(IN6_ADDR)
LPIN6_ADDR = PIN6_ADDR
