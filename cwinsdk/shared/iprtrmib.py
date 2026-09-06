from ctypes import POINTER, Structure, Union
from ctypes.wintypes import BOOL, BYTE, DWORD, WCHAR

from .. import CEnum
from .ipmib import MIB_IPFORWARDROW
from .ntdef import ANYSIZE_ARRAY, PWCHAR, ULONGLONG


class TCP_TABLE_CLASS(CEnum):
    TCP_TABLE_BASIC_LISTENER = 0
    TCP_TABLE_BASIC_CONNECTIONS = 1
    TCP_TABLE_BASIC_ALL = 2
    TCP_TABLE_OWNER_PID_LISTENER = 3
    TCP_TABLE_OWNER_PID_CONNECTIONS = 4
    TCP_TABLE_OWNER_PID_ALL = 5
    TCP_TABLE_OWNER_MODULE_LISTENER = 6
    TCP_TABLE_OWNER_MODULE_CONNECTIONS = 7
    TCP_TABLE_OWNER_MODULE_ALL = 8


PTCP_TABLE_CLASS = POINTER(TCP_TABLE_CLASS)


class UDP_TABLE_CLASS(CEnum):
    UDP_TABLE_BASIC = 0
    UDP_TABLE_OWNER_PID = 1
    UDP_TABLE_OWNER_MODULE = 2


PUDP_TABLE_CLASS = POINTER(UDP_TABLE_CLASS)


class TCPIP_OWNER_MODULE_INFO_CLASS(CEnum):
    TCPIP_OWNER_MODULE_INFO_BASIC = 0


PTCPIP_OWNER_MODULE_INFO_CLASS = POINTER(TCPIP_OWNER_MODULE_INFO_CLASS)


class TCPIP_OWNER_MODULE_BASIC_INFO(Structure):
    _fields_ = [("pModuleName", PWCHAR), ("pModulePath", PWCHAR)]


PTCPIP_OWNER_MODULE_BASIC_INFO = POINTER(TCPIP_OWNER_MODULE_BASIC_INFO)


class MIB_OPAQUE_QUERY(Structure):
    _fields_ = [("dwVarId", DWORD), ("rgdwVarIndex", DWORD * ANYSIZE_ARRAY)]


PMIB_OPAQUE_QUERY = POINTER(MIB_OPAQUE_QUERY)


class MIB_IPMCAST_BOUNDARY(Structure):
    _fields_ = [
        ("dwIfIndex", DWORD),
        ("dwGroupAddress", DWORD),
        ("dwGroupMask", DWORD),
        ("dwStatus", DWORD),
    ]


PMIB_IPMCAST_BOUNDARY = POINTER(MIB_IPMCAST_BOUNDARY)


class MIB_IPMCAST_BOUNDARY_TABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IPMCAST_BOUNDARY * ANYSIZE_ARRAY)]


PMIB_IPMCAST_BOUNDARY_TABLE = POINTER(MIB_IPMCAST_BOUNDARY_TABLE)


class MIB_BOUNDARYROW(Structure):
    _fields_ = [("dwGroupAddress", DWORD), ("dwGroupMask", DWORD)]


PMIB_BOUNDARYROW = POINTER(MIB_BOUNDARYROW)


class MIB_MCAST_LIMIT_ROW(Structure):
    _fields_ = [("dwTtl", DWORD), ("dwRateLimit", DWORD)]


PMIB_MCAST_LIMIT_ROW = POINTER(MIB_MCAST_LIMIT_ROW)
MAX_SCOPE_NAME_LEN = 255
SN_CHAR = WCHAR
SCOPE_NAME_BUFFER = WCHAR * (MAX_SCOPE_NAME_LEN + 1)
SCOPE_NAME = SCOPE_NAME_BUFFER


class MIB_IPMCAST_SCOPE(Structure):
    _fields_ = [
        ("dwGroupAddress", DWORD),
        ("dwGroupMask", DWORD),
        ("snNameBuffer", SCOPE_NAME_BUFFER),
        ("dwStatus", DWORD),
    ]


PMIB_IPMCAST_SCOPE = POINTER(MIB_IPMCAST_SCOPE)


class MIB_IPDESTROW(Structure):
    _fields_ = [
        ("ForwardRow", MIB_IPFORWARDROW),
        ("dwForwardPreference", DWORD),
        ("dwForwardViewSet", DWORD),
    ]


PMIB_IPDESTROW = POINTER(MIB_IPDESTROW)


class MIB_IPDESTTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IPDESTROW * ANYSIZE_ARRAY)]


PMIB_IPDESTTABLE = POINTER(MIB_IPDESTTABLE)


class MIB_BEST_IF(Structure):
    _fields_ = [("dwDestAddr", DWORD), ("dwIfIndex", DWORD)]


PMIB_BEST_IF = POINTER(MIB_BEST_IF)


class MIB_PROXYARP(Structure):
    _fields_ = [("dwAddress", DWORD), ("dwMask", DWORD), ("dwIfIndex", DWORD)]


PMIB_PROXYARP = POINTER(MIB_PROXYARP)


class MIB_IFSTATUS(Structure):
    _fields_ = [
        ("dwIfIndex", DWORD),
        ("dwAdminStatus", DWORD),
        ("dwOperationalStatus", DWORD),
        ("bMHbeatActive", BOOL),
        ("bMHbeatAlive", BOOL),
    ]


PMIB_IFSTATUS = POINTER(MIB_IFSTATUS)


class MIB_ROUTESTATE(Structure):
    _fields_ = [("bRoutesSetToStack", BOOL)]


PMIB_ROUTESTATE = POINTER(MIB_ROUTESTATE)


class MIB_OPAQUE_INFO_UNION(Union):
    _fields_ = [("ullAlign", ULONGLONG), ("rgbyData", BYTE * ANYSIZE_ARRAY)]


class MIB_OPAQUE_INFO(Structure):
    _anonymous_ = ("_data",)
    _fields_ = [("dwId", DWORD), ("_data", MIB_OPAQUE_INFO_UNION)]


PMIB_OPAQUE_INFO = POINTER(MIB_OPAQUE_INFO)
MAX_MIB_OFFSET = 8
