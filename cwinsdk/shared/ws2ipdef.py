from ctypes import POINTER, Structure, Union

from .in6addr import IN6_ADDR
from .ntdef import ULONG, USHORT
from .ws2def import ADDRESS_FAMILY, SCOPE_ID


class SOCKADDR_IN6_SCOPE_UNION(Union):
    _fields_ = [("sin6_scope_id", ULONG), ("sin6_scope_struct", SCOPE_ID)]


class SOCKADDR_IN6_LH(Structure):
    _fields_ = [
        ("sin6_family", ADDRESS_FAMILY),
        ("sin6_port", USHORT),
        ("sin6_flowinfo", ULONG),
        ("sin6_addr", IN6_ADDR),
        ("u", SOCKADDR_IN6_SCOPE_UNION),
    ]
    _anonymous_ = ("u",)


PSOCKADDR_IN6_LH = POINTER(SOCKADDR_IN6_LH)
LPSOCKADDR_IN6_LH = PSOCKADDR_IN6_LH
SOCKADDR_IN6 = SOCKADDR_IN6_LH
PSOCKADDR_IN6 = PSOCKADDR_IN6_LH
LPSOCKADDR_IN6 = LPSOCKADDR_IN6_LH
