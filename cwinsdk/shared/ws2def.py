from ctypes import POINTER, Structure, Union, c_int
from ctypes.wintypes import CHAR

from .inaddr import IN_ADDR
from .ntdef import ULONG, USHORT

ADDRESS_FAMILY = USHORT


class _SCOPE_ID_BITS(Structure):
    _fields_ = [("Zone", ULONG, 28), ("Level", ULONG, 4)]


class SCOPE_ID_UNION(Union):
    _fields_ = [("DUMMYSTRUCTNAME", _SCOPE_ID_BITS), ("Value", ULONG)]


class SCOPE_ID(Structure):
    _anonymous_ = ("u",)
    _fields_ = [("u", SCOPE_ID_UNION)]


PSCOPE_ID = POINTER(SCOPE_ID)


class SOCKADDR(Structure):
    _fields_ = [("sa_family", ADDRESS_FAMILY), ("sa_data", CHAR * 14)]


PSOCKADDR = POINTER(SOCKADDR)
LPSOCKADDR = PSOCKADDR


class SOCKET_ADDRESS(Structure):
    _fields_ = [("lpSockaddr", LPSOCKADDR), ("iSockaddrLength", c_int)]


PSOCKET_ADDRESS = POINTER(SOCKET_ADDRESS)
LPSOCKET_ADDRESS = PSOCKET_ADDRESS


class SOCKADDR_IN(Structure):
    _fields_ = [
        ("sin_family", ADDRESS_FAMILY),
        ("sin_port", USHORT),
        ("sin_addr", IN_ADDR),
        ("sin_zero", CHAR * 8),
    ]


PSOCKADDR_IN = POINTER(SOCKADDR_IN)
