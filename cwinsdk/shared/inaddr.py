from ctypes import POINTER, Structure, Union

from .ntdef import UCHAR, ULONG, USHORT


class IN_ADDR_S_UN_B(Structure):
    _fields_ = [("s_b1", UCHAR), ("s_b2", UCHAR), ("s_b3", UCHAR), ("s_b4", UCHAR)]


class IN_ADDR_S_UN_W(Structure):
    _fields_ = [("s_w1", USHORT), ("s_w2", USHORT)]


class IN_ADDR_S_UN(Union):
    _fields_ = [("S_un_b", IN_ADDR_S_UN_B), ("S_un_w", IN_ADDR_S_UN_W), ("S_addr", ULONG)]


class IN_ADDR(Structure):
    _anonymous_ = ("S_un",)
    _fields_ = [("S_un", IN_ADDR_S_UN)]


PIN_ADDR = POINTER(IN_ADDR)
LPIN_ADDR = PIN_ADDR
