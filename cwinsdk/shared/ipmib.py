from ctypes import POINTER, Structure, Union, c_ubyte
from ctypes.wintypes import DWORD, USHORT

from .. import CEnum
from .ifdef import IF_INDEX
from .ipifcons import MAXLEN_PHYSADDR
from .nldef import NL_ROUTE_PROTOCOL
from .ntdef import ANYSIZE_ARRAY

MIB_IPADDR_PRIMARY = 0x0001
MIB_IPADDR_DYNAMIC = 0x0004
MIB_IPADDR_DISCONNECTED = 0x0008
MIB_IPADDR_DELETED = 0x0040
MIB_IPADDR_TRANSIENT = 0x0080
MIB_IPADDR_DNS_ELIGIBLE = 0x0100


class MIB_IPADDRROW_XP(Structure):
    _fields_ = [
        ("dwAddr", DWORD),
        ("dwIndex", IF_INDEX),
        ("dwMask", DWORD),
        ("dwBCastAddr", DWORD),
        ("dwReasmSize", DWORD),
        ("unused1", USHORT),
        ("wType", USHORT),
    ]


PMIB_IPADDRROW_XP = POINTER(MIB_IPADDRROW_XP)
MIB_IPADDRROW = MIB_IPADDRROW_XP
PMIB_IPADDRROW = PMIB_IPADDRROW_XP


class MIB_IPADDRROW_W2K(Structure):
    _fields_ = [
        ("dwAddr", DWORD),
        ("dwIndex", DWORD),
        ("dwMask", DWORD),
        ("dwBCastAddr", DWORD),
        ("dwReasmSize", DWORD),
        ("unused1", USHORT),
        ("unused2", USHORT),
    ]


PMIB_IPADDRROW_W2K = POINTER(MIB_IPADDRROW_W2K)


class MIB_IPADDRTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IPADDRROW * ANYSIZE_ARRAY)]


PMIB_IPADDRTABLE = POINTER(MIB_IPADDRTABLE)


class MIB_IPFORWARDNUMBER(Structure):
    _fields_ = [("dwValue", DWORD)]


PMIB_IPFORWARDNUMBER = POINTER(MIB_IPFORWARDNUMBER)
MIB_IPFORWARD_PROTO = NL_ROUTE_PROTOCOL


class MIB_IPFORWARD_TYPE(CEnum):
    MIB_IPROUTE_TYPE_OTHER = 1
    MIB_IPROUTE_TYPE_INVALID = 2
    MIB_IPROUTE_TYPE_DIRECT = 3
    MIB_IPROUTE_TYPE_INDIRECT = 4


PMIB_IPFORWARD_TYPE = POINTER(MIB_IPFORWARD_TYPE)


class MIB_IPFORWARDROW_UNION(Union):
    _fields_ = [("dwForwardType", DWORD), ("ForwardType", MIB_IPFORWARD_TYPE)]


class MIB_IPFORWARDPROTO_UNION(Union):
    _fields_ = [("dwForwardProto", DWORD), ("ForwardProto", MIB_IPFORWARD_PROTO)]


class MIB_IPFORWARDROW(Structure):
    _anonymous_ = ("_type", "_proto")
    _fields_ = [
        ("dwForwardDest", DWORD),
        ("dwForwardMask", DWORD),
        ("dwForwardPolicy", DWORD),
        ("dwForwardNextHop", DWORD),
        ("dwForwardIfIndex", IF_INDEX),
        ("_type", MIB_IPFORWARDROW_UNION),
        ("_proto", MIB_IPFORWARDPROTO_UNION),
        ("dwForwardAge", DWORD),
        ("dwForwardNextHopAS", DWORD),
        ("dwForwardMetric1", DWORD),
        ("dwForwardMetric2", DWORD),
        ("dwForwardMetric3", DWORD),
        ("dwForwardMetric4", DWORD),
        ("dwForwardMetric5", DWORD),
    ]


PMIB_IPFORWARDROW = POINTER(MIB_IPFORWARDROW)


class MIB_IPFORWARDTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IPFORWARDROW * ANYSIZE_ARRAY)]


PMIB_IPFORWARDTABLE = POINTER(MIB_IPFORWARDTABLE)


class MIB_IPNET_TYPE(CEnum):
    MIB_IPNET_TYPE_OTHER = 1
    MIB_IPNET_TYPE_INVALID = 2
    MIB_IPNET_TYPE_DYNAMIC = 3
    MIB_IPNET_TYPE_STATIC = 4


PMIB_IPNET_TYPE = POINTER(MIB_IPNET_TYPE)


class MIB_IPNETROW_UNION(Union):
    _fields_ = [("dwType", DWORD), ("Type", MIB_IPNET_TYPE)]


class MIB_IPNETROW_LH(Structure):
    _anonymous_ = ("_type",)
    _fields_ = [
        ("dwIndex", IF_INDEX),
        ("dwPhysAddrLen", DWORD),
        ("bPhysAddr", c_ubyte * MAXLEN_PHYSADDR),
        ("dwAddr", DWORD),
        ("_type", MIB_IPNETROW_UNION),
    ]


PMIB_IPNETROW_LH = POINTER(MIB_IPNETROW_LH)
MIB_IPNETROW = MIB_IPNETROW_LH
PMIB_IPNETROW = PMIB_IPNETROW_LH


class MIB_IPNETROW_W2K(Structure):
    _fields_ = [
        ("dwIndex", IF_INDEX),
        ("dwPhysAddrLen", DWORD),
        ("bPhysAddr", c_ubyte * MAXLEN_PHYSADDR),
        ("dwAddr", DWORD),
        ("dwType", DWORD),
    ]


PMIB_IPNETROW_W2K = POINTER(MIB_IPNETROW_W2K)


class MIB_IPNETTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IPNETROW * ANYSIZE_ARRAY)]


PMIB_IPNETTABLE = POINTER(MIB_IPNETTABLE)


class MIB_IPSTATS_FORWARDING(CEnum):
    MIB_IP_FORWARDING = 1
    MIB_IP_NOT_FORWARDING = 2


PMIB_IPSTATS_FORWARDING = POINTER(MIB_IPSTATS_FORWARDING)


class MIB_IPSTATS_FORWARDING_UNION(Union):
    _fields_ = [("dwForwarding", DWORD), ("Forwarding", MIB_IPSTATS_FORWARDING)]


class MIB_IPSTATS_LH(Structure):
    _anonymous_ = ("_forwarding",)
    _fields_ = [
        ("_forwarding", MIB_IPSTATS_FORWARDING_UNION),
        ("dwDefaultTTL", DWORD),
        ("dwInReceives", DWORD),
        ("dwInHdrErrors", DWORD),
        ("dwInAddrErrors", DWORD),
        ("dwForwDatagrams", DWORD),
        ("dwInUnknownProtos", DWORD),
        ("dwInDiscards", DWORD),
        ("dwInDelivers", DWORD),
        ("dwOutRequests", DWORD),
        ("dwRoutingDiscards", DWORD),
        ("dwOutDiscards", DWORD),
        ("dwOutNoRoutes", DWORD),
        ("dwReasmTimeout", DWORD),
        ("dwReasmReqds", DWORD),
        ("dwReasmOks", DWORD),
        ("dwReasmFails", DWORD),
        ("dwFragOks", DWORD),
        ("dwFragFails", DWORD),
        ("dwFragCreates", DWORD),
        ("dwNumIf", DWORD),
        ("dwNumAddr", DWORD),
        ("dwNumRoutes", DWORD),
    ]


PMIB_IPSTATS_LH = POINTER(MIB_IPSTATS_LH)
MIB_IPSTATS = MIB_IPSTATS_LH
PMIB_IPSTATS = PMIB_IPSTATS_LH


class MIB_IPSTATS_W2K(Structure):
    _fields_ = [(name, field_type) for name, field_type in MIB_IPSTATS_LH._fields_[1:]]
    _fields_.insert(0, ("dwForwarding", DWORD))


PMIB_IPSTATS_W2K = POINTER(MIB_IPSTATS_W2K)


class MIBICMPSTATS(Structure):
    _fields_ = [
        ("dwMsgs", DWORD),
        ("dwErrors", DWORD),
        ("dwDestUnreachs", DWORD),
        ("dwTimeExcds", DWORD),
        ("dwParmProbs", DWORD),
        ("dwSrcQuenchs", DWORD),
        ("dwRedirects", DWORD),
        ("dwEchos", DWORD),
        ("dwEchoReps", DWORD),
        ("dwTimestamps", DWORD),
        ("dwTimestampReps", DWORD),
        ("dwAddrMasks", DWORD),
        ("dwAddrMaskReps", DWORD),
    ]


PMIBICMPSTATS = POINTER(MIBICMPSTATS)


class MIBICMPINFO(Structure):
    _fields_ = [("icmpInStats", MIBICMPSTATS), ("icmpOutStats", MIBICMPSTATS)]


class MIB_ICMP(Structure):
    _fields_ = [("stats", MIBICMPINFO)]


PMIB_ICMP = POINTER(MIB_ICMP)


class MIBICMPSTATS_EX_XPSP1(Structure):
    _fields_ = [("dwMsgs", DWORD), ("dwErrors", DWORD), ("rgdwTypeCount", DWORD * 256)]


PMIBICMPSTATS_EX_XPSP1 = POINTER(MIBICMPSTATS_EX_XPSP1)
MIBICMPSTATS_EX = MIBICMPSTATS_EX_XPSP1
PMIBICMPSTATS_EX = PMIBICMPSTATS_EX_XPSP1


class MIB_ICMP_EX_XPSP1(Structure):
    _fields_ = [("icmpInStats", MIBICMPSTATS_EX), ("icmpOutStats", MIBICMPSTATS_EX)]


PMIB_ICMP_EX_XPSP1 = POINTER(MIB_ICMP_EX_XPSP1)
MIB_ICMP_EX = MIB_ICMP_EX_XPSP1
PMIB_ICMP_EX = PMIB_ICMP_EX_XPSP1


MIB_USE_CURRENT_TTL = 0xFFFFFFFF
MIB_USE_CURRENT_FORWARDING = 0xFFFFFFFF
