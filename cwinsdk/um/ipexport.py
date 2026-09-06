from ctypes import POINTER, Structure, c_int, c_ubyte
from ctypes.wintypes import ULONG, USHORT, WCHAR

from ..shared.basetsd import ULONG64
from ..shared.in6addr import IN6_ADDR
from ..shared.minwindef import PUCHAR
from ..shared.ntdef import PVOID

IPAddr = ULONG
IPMask = ULONG
IP_STATUS = ULONG
IPv6Addr = IN6_ADDR


class IP_OPTION_INFORMATION(Structure):
    _fields_ = [
        ("Ttl", c_ubyte),
        ("Tos", c_ubyte),
        ("Flags", c_ubyte),
        ("OptionsSize", c_ubyte),
        ("OptionsData", PUCHAR),
    ]


PIP_OPTION_INFORMATION = POINTER(IP_OPTION_INFORMATION)


class ICMP_ECHO_REPLY(Structure):
    _fields_ = [
        ("Address", IPAddr),
        ("Status", ULONG),
        ("RoundTripTime", ULONG),
        ("DataSize", USHORT),
        ("Reserved", USHORT),
        ("Data", PVOID),
        ("Options", IP_OPTION_INFORMATION),
    ]


PICMP_ECHO_REPLY = POINTER(ICMP_ECHO_REPLY)


class IPV6_ADDRESS_EX(Structure):
    _pack_ = 1
    _fields_ = [
        ("sin6_port", USHORT),
        ("sin6_flowinfo", ULONG),
        ("sin6_addr", USHORT * 8),
        ("sin6_scope_id", ULONG),
    ]


PIPV6_ADDRESS_EX = POINTER(IPV6_ADDRESS_EX)


class ICMPV6_ECHO_REPLY_LH(Structure):
    _fields_ = [("Address", IPV6_ADDRESS_EX), ("Status", ULONG), ("RoundTripTime", ULONG)]


PICMPV6_ECHO_REPLY_LH = POINTER(ICMPV6_ECHO_REPLY_LH)
ICMPV6_ECHO_REPLY = ICMPV6_ECHO_REPLY_LH
PICMPV6_ECHO_REPLY = PICMPV6_ECHO_REPLY_LH


class ARP_SEND_REPLY(Structure):
    _fields_ = [("DestAddress", IPAddr), ("SrcAddress", IPAddr)]


PARP_SEND_REPLY = POINTER(ARP_SEND_REPLY)


class TCP_RESERVE_PORT_RANGE(Structure):
    _fields_ = [("UpperRange", USHORT), ("LowerRange", USHORT)]


PTCP_RESERVE_PORT_RANGE = POINTER(TCP_RESERVE_PORT_RANGE)
MAX_ADAPTER_NAME = 128


class IP_ADAPTER_INDEX_MAP(Structure):
    _fields_ = [("Index", ULONG), ("Name", WCHAR * MAX_ADAPTER_NAME)]


PIP_ADAPTER_INDEX_MAP = POINTER(IP_ADAPTER_INDEX_MAP)


class IP_INTERFACE_INFO(Structure):
    _fields_ = [("NumAdapters", c_int), ("Adapter", IP_ADAPTER_INDEX_MAP * 1)]


PIP_INTERFACE_INFO = POINTER(IP_INTERFACE_INFO)


class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(Structure):
    _fields_ = [("NumAdapters", ULONG), ("Address", IPAddr * 1)]


PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS = POINTER(IP_UNIDIRECTIONAL_ADAPTER_ADDRESS)


class IP_ADAPTER_ORDER_MAP(Structure):
    _fields_ = [("NumAdapters", ULONG), ("AdapterOrder", ULONG * 1)]


PIP_ADAPTER_ORDER_MAP = POINTER(IP_ADAPTER_ORDER_MAP)


class IP_MCAST_COUNTER_INFO(Structure):
    _fields_ = [
        ("InMcastOctets", ULONG64),
        ("OutMcastOctets", ULONG64),
        ("InMcastPkts", ULONG64),
        ("OutMcastPkts", ULONG64),
    ]


PIP_MCAST_COUNTER_INFO = POINTER(IP_MCAST_COUNTER_INFO)
