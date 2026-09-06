from ctypes import POINTER

from .. import CEnum


class NL_PREFIX_ORIGIN(CEnum):
    IpPrefixOriginOther = 0
    IpPrefixOriginManual = 1
    IpPrefixOriginWellKnown = 2
    IpPrefixOriginDhcp = 3
    IpPrefixOriginRouterAdvertisement = 4
    IpPrefixOriginUnchanged = 16


PNL_PREFIX_ORIGIN = POINTER(NL_PREFIX_ORIGIN)


class NL_SUFFIX_ORIGIN(CEnum):
    NlsoOther = 0
    NlsoManual = 1
    NlsoWellKnown = 2
    NlsoDhcp = 3
    NlsoLinkLayerAddress = 4
    NlsoRandom = 5
    IpSuffixOriginOther = 0
    IpSuffixOriginManual = 1
    IpSuffixOriginWellKnown = 2
    IpSuffixOriginDhcp = 3
    IpSuffixOriginLinkLayerAddress = 4
    IpSuffixOriginRandom = 5
    IpSuffixOriginUnchanged = 16


PNL_SUFFIX_ORIGIN = POINTER(NL_SUFFIX_ORIGIN)


class NL_DAD_STATE(CEnum):
    NldsInvalid = 0
    NldsTentative = 1
    NldsDuplicate = 2
    NldsDeprecated = 3
    NldsPreferred = 4
    IpDadStateInvalid = 0
    IpDadStateTentative = 1
    IpDadStateDuplicate = 2
    IpDadStateDeprecated = 3
    IpDadStatePreferred = 4


PNL_DAD_STATE = POINTER(NL_DAD_STATE)


class NL_ROUTE_PROTOCOL(CEnum):
    RouteProtocolOther = 1
    RouteProtocolLocal = 2
    RouteProtocolNetMgmt = 3
    RouteProtocolIcmp = 4
    RouteProtocolEgp = 5
    RouteProtocolGgp = 6
    RouteProtocolHello = 7
    RouteProtocolRip = 8
    RouteProtocolIsIs = 9
    RouteProtocolEsIs = 10
    RouteProtocolCisco = 11
    RouteProtocolBbn = 12
    RouteProtocolOspf = 13
    RouteProtocolBgp = 14
    RouteProtocolIdpr = 15
    RouteProtocolEigrp = 16
    RouteProtocolDvmrp = 17
    RouteProtocolRpl = 18
    RouteProtocolDhcp = 19
    MIB_IPPROTO_OTHER = 1
    MIB_IPPROTO_LOCAL = 2
    MIB_IPPROTO_NETMGMT = 3
    MIB_IPPROTO_ICMP = 4
    MIB_IPPROTO_EGP = 5
    MIB_IPPROTO_GGP = 6
    MIB_IPPROTO_HELLO = 7
    MIB_IPPROTO_RIP = 8
    MIB_IPPROTO_IS_IS = 9
    MIB_IPPROTO_ES_IS = 10
    MIB_IPPROTO_CISCO = 11
    MIB_IPPROTO_BBN = 12
    MIB_IPPROTO_OSPF = 13
    MIB_IPPROTO_BGP = 14
    MIB_IPPROTO_IDPR = 15
    MIB_IPPROTO_EIGRP = 16
    MIB_IPPROTO_DVMRP = 17
    MIB_IPPROTO_RPL = 18
    MIB_IPPROTO_DHCP = 19
    MIB_IPPROTO_NT_AUTOSTATIC = 10002
    MIB_IPPROTO_NT_STATIC = 10006
    MIB_IPPROTO_NT_STATIC_NON_DOD = 10007


PNL_ROUTE_PROTOCOL = POINTER(NL_ROUTE_PROTOCOL)
