from ctypes import POINTER, Structure, Union, c_char, c_longlong, c_ubyte
from ctypes.wintypes import BOOL, BYTE, DWORD, UINT, ULONG, WCHAR

from ..shared.basetsd import ULONG64
from ..shared.guiddef import GUID
from ..shared.ifdef import (
    IF_INDEX,
    IF_LUID,
    NET_IF_COMPARTMENT_ID,
    NET_IF_CONNECTION_TYPE,
    NET_IF_NETWORK_GUID,
    TUNNEL_TYPE,
)
from ..shared.ipifcons import IF_OPER_STATUS, IFTYPE
from ..shared.nldef import NL_DAD_STATE, NL_PREFIX_ORIGIN, NL_SUFFIX_ORIGIN
from ..shared.ntdef import PWCHAR
from ..shared.ws2def import SOCKET_ADDRESS

MAX_ADAPTER_DESCRIPTION_LENGTH = 128
MAX_ADAPTER_NAME_LENGTH = 256
MAX_ADAPTER_ADDRESS_LENGTH = 8
DEFAULT_MINIMUM_ENTITIES = 32
MAX_HOSTNAME_LEN = 128
MAX_DOMAIN_NAME_LEN = 128
MAX_SCOPE_ID_LEN = 256
MAX_DHCPV6_DUID_LENGTH = 130
MAX_DNS_SUFFIX_STRING_LENGTH = 256

BROADCAST_NODETYPE = 1
PEER_TO_PEER_NODETYPE = 2
MIXED_NODETYPE = 4
HYBRID_NODETYPE = 8


class IP_ADDRESS_STRING(Structure):
    _fields_ = [("String", c_char * (4 * 4))]


PIP_ADDRESS_STRING = POINTER(IP_ADDRESS_STRING)
IP_MASK_STRING = IP_ADDRESS_STRING
PIP_MASK_STRING = PIP_ADDRESS_STRING


class IP_ADDR_STRING(Structure):
    pass


PIP_ADDR_STRING = POINTER(IP_ADDR_STRING)
IP_ADDR_STRING._fields_ = [
    ("Next", PIP_ADDR_STRING),
    ("IpAddress", IP_ADDRESS_STRING),
    ("IpMask", IP_MASK_STRING),
    ("Context", DWORD),
]


class IP_ADAPTER_INFO(Structure):
    pass


PIP_ADAPTER_INFO = POINTER(IP_ADAPTER_INFO)
IP_ADAPTER_INFO._fields_ = [
    ("Next", PIP_ADAPTER_INFO),
    ("ComboIndex", DWORD),
    ("AdapterName", c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
    ("Description", c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
    ("AddressLength", UINT),
    ("Address", BYTE * MAX_ADAPTER_ADDRESS_LENGTH),
    ("Index", DWORD),
    ("Type", UINT),
    ("DhcpEnabled", UINT),
    ("CurrentIpAddress", PIP_ADDR_STRING),
    ("IpAddressList", IP_ADDR_STRING),
    ("GatewayList", IP_ADDR_STRING),
    ("DhcpServer", IP_ADDR_STRING),
    ("HaveWins", BOOL),
    ("PrimaryWinsServer", IP_ADDR_STRING),
    ("SecondaryWinsServer", IP_ADDR_STRING),
    ("LeaseObtained", c_longlong),
    ("LeaseExpires", c_longlong),
]


IP_PREFIX_ORIGIN = NL_PREFIX_ORIGIN
PIP_PREFIX_ORIGIN = POINTER(IP_PREFIX_ORIGIN)
IP_SUFFIX_ORIGIN = NL_SUFFIX_ORIGIN
PIP_SUFFIX_ORIGIN = POINTER(IP_SUFFIX_ORIGIN)
IP_DAD_STATE = NL_DAD_STATE
PIP_DAD_STATE = POINTER(IP_DAD_STATE)


class IP_ADAPTER_ADDRESS_ALIGNMENT(Union):
    class _FIELDS(Structure):
        _fields_ = [("Length", ULONG), ("Flags", DWORD)]

    _anonymous_ = ("_fields",)
    _fields_ = [("Alignment", ULONG64), ("_fields", _FIELDS)]


class IP_ADAPTER_ADDRESS_ALIGNMENT_RESERVED(Union):
    class _FIELDS(Structure):
        _fields_ = [("Length", ULONG), ("Reserved", DWORD)]

    _anonymous_ = ("_fields",)
    _fields_ = [("Alignment", ULONG64), ("_fields", _FIELDS)]


class IP_ADAPTER_ADDRESSES_ALIGNMENT(Union):
    class _FIELDS(Structure):
        _fields_ = [("Length", ULONG), ("IfIndex", IF_INDEX)]

    _anonymous_ = ("_fields",)
    _fields_ = [("Alignment", ULONG64), ("_fields", _FIELDS)]


class IP_ADAPTER_UNICAST_ADDRESS_LH(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_UNICAST_ADDRESS_LH = POINTER(IP_ADAPTER_UNICAST_ADDRESS_LH)
IP_ADAPTER_UNICAST_ADDRESS_LH._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT),
    ("Next", PIP_ADAPTER_UNICAST_ADDRESS_LH),
    ("Address", SOCKET_ADDRESS),
    ("PrefixOrigin", IP_PREFIX_ORIGIN),
    ("SuffixOrigin", IP_SUFFIX_ORIGIN),
    ("DadState", IP_DAD_STATE),
    ("ValidLifetime", ULONG),
    ("PreferredLifetime", ULONG),
    ("LeaseLifetime", ULONG),
    ("OnLinkPrefixLength", c_ubyte),
]


class IP_ADAPTER_UNICAST_ADDRESS_XP(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_UNICAST_ADDRESS_XP = POINTER(IP_ADAPTER_UNICAST_ADDRESS_XP)
IP_ADAPTER_UNICAST_ADDRESS_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT),
    ("Next", PIP_ADAPTER_UNICAST_ADDRESS_XP),
    ("Address", SOCKET_ADDRESS),
    ("PrefixOrigin", IP_PREFIX_ORIGIN),
    ("SuffixOrigin", IP_SUFFIX_ORIGIN),
    ("DadState", IP_DAD_STATE),
    ("ValidLifetime", ULONG),
    ("PreferredLifetime", ULONG),
    ("LeaseLifetime", ULONG),
]


IP_ADAPTER_UNICAST_ADDRESS = IP_ADAPTER_UNICAST_ADDRESS_LH
PIP_ADAPTER_UNICAST_ADDRESS = PIP_ADAPTER_UNICAST_ADDRESS_LH


class IP_ADAPTER_ANYCAST_ADDRESS_XP(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_ANYCAST_ADDRESS_XP = POINTER(IP_ADAPTER_ANYCAST_ADDRESS_XP)
IP_ADAPTER_ANYCAST_ADDRESS_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT),
    ("Next", PIP_ADAPTER_ANYCAST_ADDRESS_XP),
    ("Address", SOCKET_ADDRESS),
]
IP_ADAPTER_ANYCAST_ADDRESS = IP_ADAPTER_ANYCAST_ADDRESS_XP
PIP_ADAPTER_ANYCAST_ADDRESS = PIP_ADAPTER_ANYCAST_ADDRESS_XP


class IP_ADAPTER_MULTICAST_ADDRESS_XP(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_MULTICAST_ADDRESS_XP = POINTER(IP_ADAPTER_MULTICAST_ADDRESS_XP)
IP_ADAPTER_MULTICAST_ADDRESS_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT),
    ("Next", PIP_ADAPTER_MULTICAST_ADDRESS_XP),
    ("Address", SOCKET_ADDRESS),
]
IP_ADAPTER_MULTICAST_ADDRESS = IP_ADAPTER_MULTICAST_ADDRESS_XP
PIP_ADAPTER_MULTICAST_ADDRESS = PIP_ADAPTER_MULTICAST_ADDRESS_XP


class IP_ADAPTER_DNS_SERVER_ADDRESS_XP(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_DNS_SERVER_ADDRESS_XP = POINTER(IP_ADAPTER_DNS_SERVER_ADDRESS_XP)
IP_ADAPTER_DNS_SERVER_ADDRESS_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT_RESERVED),
    ("Next", PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
    ("Address", SOCKET_ADDRESS),
]
IP_ADAPTER_DNS_SERVER_ADDRESS = IP_ADAPTER_DNS_SERVER_ADDRESS_XP
PIP_ADAPTER_DNS_SERVER_ADDRESS = PIP_ADAPTER_DNS_SERVER_ADDRESS_XP


class IP_ADAPTER_WINS_SERVER_ADDRESS_LH(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_WINS_SERVER_ADDRESS_LH = POINTER(IP_ADAPTER_WINS_SERVER_ADDRESS_LH)
IP_ADAPTER_WINS_SERVER_ADDRESS_LH._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT_RESERVED),
    ("Next", PIP_ADAPTER_WINS_SERVER_ADDRESS_LH),
    ("Address", SOCKET_ADDRESS),
]
IP_ADAPTER_WINS_SERVER_ADDRESS = IP_ADAPTER_WINS_SERVER_ADDRESS_LH
PIP_ADAPTER_WINS_SERVER_ADDRESS = PIP_ADAPTER_WINS_SERVER_ADDRESS_LH


class IP_ADAPTER_GATEWAY_ADDRESS_LH(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_GATEWAY_ADDRESS_LH = POINTER(IP_ADAPTER_GATEWAY_ADDRESS_LH)
IP_ADAPTER_GATEWAY_ADDRESS_LH._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT_RESERVED),
    ("Next", PIP_ADAPTER_GATEWAY_ADDRESS_LH),
    ("Address", SOCKET_ADDRESS),
]
IP_ADAPTER_GATEWAY_ADDRESS = IP_ADAPTER_GATEWAY_ADDRESS_LH
PIP_ADAPTER_GATEWAY_ADDRESS = PIP_ADAPTER_GATEWAY_ADDRESS_LH


class IP_ADAPTER_PREFIX_XP(Structure):
    _anonymous_ = ("_alignment",)


PIP_ADAPTER_PREFIX_XP = POINTER(IP_ADAPTER_PREFIX_XP)
IP_ADAPTER_PREFIX_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESS_ALIGNMENT),
    ("Next", PIP_ADAPTER_PREFIX_XP),
    ("Address", SOCKET_ADDRESS),
    ("PrefixLength", ULONG),
]
IP_ADAPTER_PREFIX = IP_ADAPTER_PREFIX_XP
PIP_ADAPTER_PREFIX = PIP_ADAPTER_PREFIX_XP


class IP_ADAPTER_DNS_SUFFIX(Structure):
    pass


PIP_ADAPTER_DNS_SUFFIX = POINTER(IP_ADAPTER_DNS_SUFFIX)
IP_ADAPTER_DNS_SUFFIX._fields_ = [("Next", PIP_ADAPTER_DNS_SUFFIX), ("String", WCHAR * MAX_DNS_SUFFIX_STRING_LENGTH)]


class IP_ADAPTER_ADDRESSES_FLAGS(Union):
    class _BITS(Structure):
        _fields_ = [
            (name, ULONG, 1)
            for name in (
                "DdnsEnabled",
                "RegisterAdapterSuffix",
                "Dhcpv4Enabled",
                "ReceiveOnly",
                "NoMulticast",
                "Ipv6OtherStatefulConfig",
                "NetbiosOverTcpipEnabled",
                "Ipv4Enabled",
                "Ipv6Enabled",
                "Ipv6ManagedAddressConfigurationSupported",
            )
        ]

    _anonymous_ = ("_bits",)
    _fields_ = [("Flags", ULONG), ("_bits", _BITS)]


class IP_ADAPTER_ADDRESSES_LH(Structure):
    _anonymous_ = ("_alignment", "_flags")


PIP_ADAPTER_ADDRESSES_LH = POINTER(IP_ADAPTER_ADDRESSES_LH)
IP_ADAPTER_ADDRESSES_LH._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESSES_ALIGNMENT),
    ("Next", PIP_ADAPTER_ADDRESSES_LH),
    ("AdapterName", POINTER(c_char)),
    ("FirstUnicastAddress", PIP_ADAPTER_UNICAST_ADDRESS_LH),
    ("FirstAnycastAddress", PIP_ADAPTER_ANYCAST_ADDRESS_XP),
    ("FirstMulticastAddress", PIP_ADAPTER_MULTICAST_ADDRESS_XP),
    ("FirstDnsServerAddress", PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
    ("DnsSuffix", PWCHAR),
    ("Description", PWCHAR),
    ("FriendlyName", PWCHAR),
    ("PhysicalAddress", BYTE * MAX_ADAPTER_ADDRESS_LENGTH),
    ("PhysicalAddressLength", ULONG),
    ("_flags", IP_ADAPTER_ADDRESSES_FLAGS),
    ("Mtu", ULONG),
    ("IfType", IFTYPE),
    ("OperStatus", IF_OPER_STATUS),
    ("Ipv6IfIndex", IF_INDEX),
    ("ZoneIndices", ULONG * 16),
    ("FirstPrefix", PIP_ADAPTER_PREFIX_XP),
    ("TransmitLinkSpeed", ULONG64),
    ("ReceiveLinkSpeed", ULONG64),
    ("FirstWinsServerAddress", PIP_ADAPTER_WINS_SERVER_ADDRESS_LH),
    ("FirstGatewayAddress", PIP_ADAPTER_GATEWAY_ADDRESS_LH),
    ("Ipv4Metric", ULONG),
    ("Ipv6Metric", ULONG),
    ("Luid", IF_LUID),
    ("Dhcpv4Server", SOCKET_ADDRESS),
    ("CompartmentId", NET_IF_COMPARTMENT_ID),
    ("NetworkGuid", NET_IF_NETWORK_GUID),
    ("ConnectionType", NET_IF_CONNECTION_TYPE),
    ("TunnelType", TUNNEL_TYPE),
    ("Dhcpv6Server", SOCKET_ADDRESS),
    ("Dhcpv6ClientDuid", BYTE * MAX_DHCPV6_DUID_LENGTH),
    ("Dhcpv6ClientDuidLength", ULONG),
    ("Dhcpv6Iaid", ULONG),
    ("FirstDnsSuffix", PIP_ADAPTER_DNS_SUFFIX),
]


IP_ADAPTER_ADDRESSES = IP_ADAPTER_ADDRESSES_LH
PIP_ADAPTER_ADDRESSES = PIP_ADAPTER_ADDRESSES_LH


class IP_ADAPTER_ADDRESSES_XP(Structure):
    pass


PIP_ADAPTER_ADDRESSES_XP = POINTER(IP_ADAPTER_ADDRESSES_XP)
IP_ADAPTER_ADDRESSES_XP._fields_ = [
    ("_alignment", IP_ADAPTER_ADDRESSES_ALIGNMENT),
    ("Next", PIP_ADAPTER_ADDRESSES_XP),
    ("AdapterName", POINTER(c_char)),
    ("FirstUnicastAddress", PIP_ADAPTER_UNICAST_ADDRESS_XP),
    ("FirstAnycastAddress", PIP_ADAPTER_ANYCAST_ADDRESS_XP),
    ("FirstMulticastAddress", PIP_ADAPTER_MULTICAST_ADDRESS_XP),
    ("FirstDnsServerAddress", PIP_ADAPTER_DNS_SERVER_ADDRESS_XP),
    ("DnsSuffix", PWCHAR),
    ("Description", PWCHAR),
    ("FriendlyName", PWCHAR),
    ("PhysicalAddress", BYTE * MAX_ADAPTER_ADDRESS_LENGTH),
    ("PhysicalAddressLength", DWORD),
    ("Flags", DWORD),
    ("Mtu", DWORD),
    ("IfType", DWORD),
    ("OperStatus", IF_OPER_STATUS),
    ("Ipv6IfIndex", DWORD),
    ("ZoneIndices", DWORD * 16),
    ("FirstPrefix", PIP_ADAPTER_PREFIX_XP),
]


IP_ADAPTER_ADDRESS_DNS_ELIGIBLE = 0x01
IP_ADAPTER_ADDRESS_TRANSIENT = 0x02
IP_ADAPTER_DDNS_ENABLED = 0x00000001
IP_ADAPTER_REGISTER_ADAPTER_SUFFIX = 0x00000002
IP_ADAPTER_DHCP_ENABLED = 0x00000004
IP_ADAPTER_RECEIVE_ONLY = 0x00000008
IP_ADAPTER_NO_MULTICAST = 0x00000010
IP_ADAPTER_IPV6_OTHER_STATEFUL_CONFIG = 0x00000020
IP_ADAPTER_NETBIOS_OVER_TCPIP_ENABLED = 0x00000040
IP_ADAPTER_IPV4_ENABLED = 0x00000080
IP_ADAPTER_IPV6_ENABLED = 0x00000100
IP_ADAPTER_IPV6_MANAGE_ADDRESS_CONFIG = 0x00000200


class IP_PER_ADAPTER_INFO_W2KSP1(Structure):
    _fields_ = [
        ("AutoconfigEnabled", UINT),
        ("AutoconfigActive", UINT),
        ("CurrentDnsServer", PIP_ADDR_STRING),
        ("DnsServerList", IP_ADDR_STRING),
    ]


PIP_PER_ADAPTER_INFO_W2KSP1 = POINTER(IP_PER_ADAPTER_INFO_W2KSP1)
IP_PER_ADAPTER_INFO = IP_PER_ADAPTER_INFO_W2KSP1
PIP_PER_ADAPTER_INFO = PIP_PER_ADAPTER_INFO_W2KSP1


class FIXED_INFO_W2KSP1(Structure):
    _fields_ = [
        ("HostName", c_char * (MAX_HOSTNAME_LEN + 4)),
        ("DomainName", c_char * (MAX_DOMAIN_NAME_LEN + 4)),
        ("CurrentDnsServer", PIP_ADDR_STRING),
        ("DnsServerList", IP_ADDR_STRING),
        ("NodeType", UINT),
        ("ScopeId", c_char * (MAX_SCOPE_ID_LEN + 4)),
        ("EnableRouting", UINT),
        ("EnableProxy", UINT),
        ("EnableDns", UINT),
    ]


PFIXED_INFO_W2KSP1 = POINTER(FIXED_INFO_W2KSP1)
FIXED_INFO = FIXED_INFO_W2KSP1
PFIXED_INFO = PFIXED_INFO_W2KSP1


class IP_INTERFACE_NAME_INFO_W2KSP1(Structure):
    _fields_ = [
        ("Index", ULONG),
        ("MediaType", ULONG),
        ("ConnectionType", c_ubyte),
        ("AccessType", c_ubyte),
        ("DeviceGuid", GUID),
        ("InterfaceGuid", GUID),
    ]


PIP_INTERFACE_NAME_INFO_W2KSP1 = POINTER(IP_INTERFACE_NAME_INFO_W2KSP1)
IP_INTERFACE_NAME_INFO = IP_INTERFACE_NAME_INFO_W2KSP1
PIP_INTERFACE_NAME_INFO = PIP_INTERFACE_NAME_INFO_W2KSP1
