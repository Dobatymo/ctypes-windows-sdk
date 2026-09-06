from ctypes import POINTER, Structure, Union, c_int, c_ubyte
from ctypes.wintypes import DWORD, LARGE_INTEGER

from .basetsd import DWORD64
from .in6addr import IN6_ADDR
from .ntdef import ANYSIZE_ARRAY, ULONGLONG

TCPIP_OWNING_MODULE_SIZE = 16


class MIB_UDPROW(Structure):
    _fields_ = [("dwLocalAddr", DWORD), ("dwLocalPort", DWORD)]


PMIB_UDPROW = POINTER(MIB_UDPROW)


class MIB_UDPTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDPROW * ANYSIZE_ARRAY)]


PMIB_UDPTABLE = POINTER(MIB_UDPTABLE)


class MIB_UDPROW_OWNER_PID(Structure):
    _fields_ = [("dwLocalAddr", DWORD), ("dwLocalPort", DWORD), ("dwOwningPid", DWORD)]


PMIB_UDPROW_OWNER_PID = POINTER(MIB_UDPROW_OWNER_PID)


class MIB_UDPTABLE_OWNER_PID(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDPROW_OWNER_PID * ANYSIZE_ARRAY)]


PMIB_UDPTABLE_OWNER_PID = POINTER(MIB_UDPTABLE_OWNER_PID)


class MIB_UDPROW_OWNER_MODULE_FLAGS(Structure):
    _fields_ = [("SpecificPortBind", c_int, 1)]


class MIB_UDPROW_OWNER_MODULE_UNION(Union):
    _anonymous_ = ("_bits",)
    _fields_ = [("_bits", MIB_UDPROW_OWNER_MODULE_FLAGS), ("dwFlags", c_int)]


class MIB_UDPROW_OWNER_MODULE(Structure):
    _anonymous_ = ("_flags",)
    _fields_ = [
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("_flags", MIB_UDPROW_OWNER_MODULE_UNION),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
    ]


PMIB_UDPROW_OWNER_MODULE = POINTER(MIB_UDPROW_OWNER_MODULE)


class MIB_UDPTABLE_OWNER_MODULE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDPROW_OWNER_MODULE * ANYSIZE_ARRAY)]


PMIB_UDPTABLE_OWNER_MODULE = POINTER(MIB_UDPTABLE_OWNER_MODULE)


class MIB_UDPROW2(Structure):
    _anonymous_ = ("_flags",)
    _fields_ = [
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("_flags", MIB_UDPROW_OWNER_MODULE_UNION),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
        ("dwRemoteAddr", DWORD),
        ("dwRemotePort", DWORD),
    ]


PMIB_UDPROW2 = POINTER(MIB_UDPROW2)


class MIB_UDPTABLE2(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDPROW2 * ANYSIZE_ARRAY)]


PMIB_UDPTABLE2 = POINTER(MIB_UDPTABLE2)


class MIB_UDP6ROW(Structure):
    _fields_ = [("dwLocalAddr", IN6_ADDR), ("dwLocalScopeId", DWORD), ("dwLocalPort", DWORD)]


PMIB_UDP6ROW = POINTER(MIB_UDP6ROW)


class MIB_UDP6TABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDP6ROW * ANYSIZE_ARRAY)]


PMIB_UDP6TABLE = POINTER(MIB_UDP6TABLE)


class MIB_UDP6ROW_OWNER_PID(Structure):
    _fields_ = [
        ("ucLocalAddr", c_ubyte * 16),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("dwOwningPid", DWORD),
    ]


PMIB_UDP6ROW_OWNER_PID = POINTER(MIB_UDP6ROW_OWNER_PID)


class MIB_UDP6TABLE_OWNER_PID(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDP6ROW_OWNER_PID * ANYSIZE_ARRAY)]


PMIB_UDP6TABLE_OWNER_PID = POINTER(MIB_UDP6TABLE_OWNER_PID)


class MIB_UDP6ROW_OWNER_MODULE(Structure):
    _anonymous_ = ("_flags",)
    _fields_ = [
        ("ucLocalAddr", c_ubyte * 16),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("_flags", MIB_UDPROW_OWNER_MODULE_UNION),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
    ]


PMIB_UDP6ROW_OWNER_MODULE = POINTER(MIB_UDP6ROW_OWNER_MODULE)


class MIB_UDP6TABLE_OWNER_MODULE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDP6ROW_OWNER_MODULE * ANYSIZE_ARRAY)]


PMIB_UDP6TABLE_OWNER_MODULE = POINTER(MIB_UDP6TABLE_OWNER_MODULE)


class MIB_UDP6ROW2(Structure):
    _anonymous_ = ("_flags",)
    _fields_ = [
        ("ucLocalAddr", c_ubyte * 16),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("_flags", MIB_UDPROW_OWNER_MODULE_UNION),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
        ("ucRemoteAddr", c_ubyte * 16),
        ("dwRemoteScopeId", DWORD),
        ("dwRemotePort", DWORD),
    ]


PMIB_UDP6ROW2 = POINTER(MIB_UDP6ROW2)


class MIB_UDP6TABLE2(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_UDP6ROW2 * ANYSIZE_ARRAY)]


PMIB_UDP6TABLE2 = POINTER(MIB_UDP6TABLE2)


class MIB_UDPSTATS(Structure):
    _fields_ = [
        ("dwInDatagrams", DWORD),
        ("dwNoPorts", DWORD),
        ("dwInErrors", DWORD),
        ("dwOutDatagrams", DWORD),
        ("dwNumAddrs", DWORD),
    ]


PMIB_UDPSTATS = POINTER(MIB_UDPSTATS)


class MIB_UDPSTATS2(Structure):
    _fields_ = [
        ("dw64InDatagrams", DWORD64),
        ("dwNoPorts", DWORD),
        ("dwInErrors", DWORD),
        ("dw64OutDatagrams", DWORD64),
        ("dwNumAddrs", DWORD),
    ]


PMIB_UDPSTATS2 = POINTER(MIB_UDPSTATS2)
