"""ctypes bindings for Windows IP Helper APIs."""

import ctypes
from ctypes import POINTER, WINFUNCTYPE, Structure, Union
from ctypes.wintypes import BYTE, DWORD, HANDLE, LPCWSTR, LPWSTR, UINT, ULONG, USHORT, WCHAR

from .. import (
    CEnum,
    error_io_pending,
    error_success,
    no_error,
    no_error_or_no_data,
    no_error_or_pending,
    nonzero,
    windll,
)
from ..shared.basetsd import PULONG64, ULONG64
from ..shared.ifdef import PIF_LUID
from ..shared.ifmib import PMIB_IFROW, PMIB_IFTABLE
from ..shared.ipmib import (
    PMIB_ICMP,
    PMIB_ICMP_EX,
    PMIB_IPADDRTABLE,
    PMIB_IPFORWARDROW,
    PMIB_IPFORWARDTABLE,
    PMIB_IPNETROW,
    PMIB_IPNETTABLE,
    PMIB_IPSTATS,
)
from ..shared.iprtrmib import TCP_TABLE_CLASS, TCPIP_OWNER_MODULE_INFO_CLASS, UDP_TABLE_CLASS
from ..shared.minwindef import DECLARE_HANDLE, LPDWORD, PUCHAR, PULONG
from ..shared.ntdef import PVOID
from ..shared.tcpestats import TCP_ESTATS_TYPE
from ..shared.tcpmib import (
    PMIB_TCP6ROW,
    PMIB_TCP6ROW_OWNER_MODULE,
    PMIB_TCP6TABLE,
    PMIB_TCP6TABLE2,
    PMIB_TCPROW,
    PMIB_TCPROW_OWNER_MODULE,
    PMIB_TCPSTATS,
    PMIB_TCPSTATS2,
    PMIB_TCPTABLE,
    PMIB_TCPTABLE2,
)
from ..shared.udpmib import (
    PMIB_UDP6ROW_OWNER_MODULE,
    PMIB_UDP6TABLE,
    PMIB_UDPROW_OWNER_MODULE,
    PMIB_UDPSTATS,
    PMIB_UDPSTATS2,
    PMIB_UDPTABLE,
)
from ..shared.ws2def import LPSOCKADDR, SOCKADDR, SOCKADDR_IN
from ..shared.ws2ipdef import SOCKADDR_IN6
from ..wintypes import BOOL, BOOLEAN
from .ipexport import (
    PIP_ADAPTER_INDEX_MAP,
    PIP_ADAPTER_ORDER_MAP,
    PIP_INTERFACE_INFO,
    PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS,
)
from .iptypes import (
    PFIXED_INFO,
    PIP_ADAPTER_ADDRESSES,
    PIP_ADAPTER_INFO,
    PIP_INTERFACE_NAME_INFO,
    PIP_PER_ADAPTER_INFO,
)
from .minwinbase import LPOVERLAPPED
from .winnt import PHANDLE


class INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES(Structure):
    _fields_ = [
        ("PtpV2OverUdpIPv4EventMessageReceive", BOOLEAN),
        ("PtpV2OverUdpIPv4AllMessageReceive", BOOLEAN),
        ("PtpV2OverUdpIPv4EventMessageTransmit", BOOLEAN),
        ("PtpV2OverUdpIPv4AllMessageTransmit", BOOLEAN),
        ("PtpV2OverUdpIPv6EventMessageReceive", BOOLEAN),
        ("PtpV2OverUdpIPv6AllMessageReceive", BOOLEAN),
        ("PtpV2OverUdpIPv6EventMessageTransmit", BOOLEAN),
        ("PtpV2OverUdpIPv6AllMessageTransmit", BOOLEAN),
        ("AllReceive", BOOLEAN),
        ("AllTransmit", BOOLEAN),
        ("TaggedTransmit", BOOLEAN),
    ]


PINTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES = POINTER(INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES)


class INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES(Structure):
    _fields_ = [("AllReceive", BOOLEAN), ("AllTransmit", BOOLEAN), ("TaggedTransmit", BOOLEAN)]


PINTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES = POINTER(INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES)


class INTERFACE_TIMESTAMP_CAPABILITIES(Structure):
    _fields_ = [
        ("HardwareClockFrequencyHz", ULONG64),
        ("SupportsCrossTimestamp", BOOLEAN),
        ("HardwareCapabilities", INTERFACE_HARDWARE_TIMESTAMP_CAPABILITIES),
        ("SoftwareCapabilities", INTERFACE_SOFTWARE_TIMESTAMP_CAPABILITIES),
    ]


PINTERFACE_TIMESTAMP_CAPABILITIES = POINTER(INTERFACE_TIMESTAMP_CAPABILITIES)


class INTERFACE_HARDWARE_CROSSTIMESTAMP(Structure):
    _fields_ = [
        ("SystemTimestamp1", ULONG64),
        ("HardwareClockTimestamp", ULONG64),
        ("SystemTimestamp2", ULONG64),
    ]


PINTERFACE_HARDWARE_CROSSTIMESTAMP = POINTER(INTERFACE_HARDWARE_CROSSTIMESTAMP)
HIFTIMESTAMPCHANGE = DECLARE_HANDLE()

INTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK = WINFUNCTYPE(None, PVOID)
PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK = INTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK


GetNumberOfInterfaces = windll.iphlpapi.GetNumberOfInterfaces
GetNumberOfInterfaces.argtypes = [LPDWORD]
GetNumberOfInterfaces.restype = DWORD
GetNumberOfInterfaces.errcheck = no_error

GetIfEntry = windll.iphlpapi.GetIfEntry
GetIfEntry.argtypes = [PMIB_IFROW]
GetIfEntry.restype = DWORD
GetIfEntry.errcheck = no_error

GetIfTable = windll.iphlpapi.GetIfTable
GetIfTable.argtypes = [PMIB_IFTABLE, PULONG, BOOL]
GetIfTable.restype = DWORD
GetIfTable.errcheck = no_error

GetIpAddrTable = windll.iphlpapi.GetIpAddrTable
GetIpAddrTable.argtypes = [PMIB_IPADDRTABLE, PULONG, BOOL]
GetIpAddrTable.restype = DWORD
GetIpAddrTable.errcheck = no_error

GetIpNetTable = windll.iphlpapi.GetIpNetTable
GetIpNetTable.argtypes = [PMIB_IPNETTABLE, PULONG, BOOL]
GetIpNetTable.restype = ULONG
GetIpNetTable.errcheck = no_error_or_no_data

GetIpForwardTable = windll.iphlpapi.GetIpForwardTable
GetIpForwardTable.argtypes = [PMIB_IPFORWARDTABLE, PULONG, BOOL]
GetIpForwardTable.restype = DWORD
GetIpForwardTable.errcheck = no_error

GetTcpTable = windll.iphlpapi.GetTcpTable
GetTcpTable.argtypes = [PMIB_TCPTABLE, PULONG, BOOL]
GetTcpTable.restype = ULONG
GetTcpTable.errcheck = no_error

GetExtendedTcpTable = windll.iphlpapi.GetExtendedTcpTable
GetExtendedTcpTable.argtypes = [PVOID, LPDWORD, BOOL, ULONG, TCP_TABLE_CLASS, ULONG]
GetExtendedTcpTable.restype = DWORD
GetExtendedTcpTable.errcheck = no_error

GetOwnerModuleFromTcpEntry = windll.iphlpapi.GetOwnerModuleFromTcpEntry
GetOwnerModuleFromTcpEntry.argtypes = [PMIB_TCPROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, LPDWORD]
GetOwnerModuleFromTcpEntry.restype = DWORD
GetOwnerModuleFromTcpEntry.errcheck = no_error

GetUdpTable = windll.iphlpapi.GetUdpTable
GetUdpTable.argtypes = [PMIB_UDPTABLE, PULONG, BOOL]
GetUdpTable.restype = ULONG
GetUdpTable.errcheck = no_error

GetExtendedUdpTable = windll.iphlpapi.GetExtendedUdpTable
GetExtendedUdpTable.argtypes = [PVOID, LPDWORD, BOOL, ULONG, UDP_TABLE_CLASS, ULONG]
GetExtendedUdpTable.restype = DWORD
GetExtendedUdpTable.errcheck = no_error

GetOwnerModuleFromUdpEntry = windll.iphlpapi.GetOwnerModuleFromUdpEntry
GetOwnerModuleFromUdpEntry.argtypes = [PMIB_UDPROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, LPDWORD]
GetOwnerModuleFromUdpEntry.restype = DWORD
GetOwnerModuleFromUdpEntry.errcheck = no_error

GetTcpTable2 = windll.iphlpapi.GetTcpTable2
GetTcpTable2.argtypes = [PMIB_TCPTABLE2, PULONG, BOOL]
GetTcpTable2.restype = ULONG
GetTcpTable2.errcheck = no_error

GetTcp6Table = windll.iphlpapi.GetTcp6Table
GetTcp6Table.argtypes = [PMIB_TCP6TABLE, PULONG, BOOL]
GetTcp6Table.restype = ULONG
GetTcp6Table.errcheck = no_error

GetTcp6Table2 = windll.iphlpapi.GetTcp6Table2
GetTcp6Table2.argtypes = [PMIB_TCP6TABLE2, PULONG, BOOL]
GetTcp6Table2.restype = ULONG
GetTcp6Table2.errcheck = no_error

GetPerTcpConnectionEStats = windll.iphlpapi.GetPerTcpConnectionEStats
GetPerTcpConnectionEStats.argtypes = [
    PMIB_TCPROW,
    TCP_ESTATS_TYPE,
    PUCHAR,
    ULONG,
    ULONG,
    PUCHAR,
    ULONG,
    ULONG,
    PUCHAR,
    ULONG,
    ULONG,
]
GetPerTcpConnectionEStats.restype = ULONG
GetPerTcpConnectionEStats.errcheck = no_error

SetPerTcpConnectionEStats = windll.iphlpapi.SetPerTcpConnectionEStats
SetPerTcpConnectionEStats.argtypes = [PMIB_TCPROW, TCP_ESTATS_TYPE, PUCHAR, ULONG, ULONG, ULONG]
SetPerTcpConnectionEStats.restype = ULONG
SetPerTcpConnectionEStats.errcheck = no_error

GetPerTcp6ConnectionEStats = windll.iphlpapi.GetPerTcp6ConnectionEStats
GetPerTcp6ConnectionEStats.argtypes = [
    PMIB_TCP6ROW,
    TCP_ESTATS_TYPE,
    PUCHAR,
    ULONG,
    ULONG,
    PUCHAR,
    ULONG,
    ULONG,
    PUCHAR,
    ULONG,
    ULONG,
]
GetPerTcp6ConnectionEStats.restype = ULONG
GetPerTcp6ConnectionEStats.errcheck = no_error

SetPerTcp6ConnectionEStats = windll.iphlpapi.SetPerTcp6ConnectionEStats
SetPerTcp6ConnectionEStats.argtypes = [PMIB_TCP6ROW, TCP_ESTATS_TYPE, PUCHAR, ULONG, ULONG, ULONG]
SetPerTcp6ConnectionEStats.restype = ULONG
SetPerTcp6ConnectionEStats.errcheck = no_error

GetOwnerModuleFromTcp6Entry = windll.iphlpapi.GetOwnerModuleFromTcp6Entry
GetOwnerModuleFromTcp6Entry.argtypes = [PMIB_TCP6ROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, LPDWORD]
GetOwnerModuleFromTcp6Entry.restype = DWORD
GetOwnerModuleFromTcp6Entry.errcheck = no_error

GetUdp6Table = windll.iphlpapi.GetUdp6Table
GetUdp6Table.argtypes = [PMIB_UDP6TABLE, PULONG, BOOL]
GetUdp6Table.restype = ULONG
GetUdp6Table.errcheck = no_error

GetOwnerModuleFromUdp6Entry = windll.iphlpapi.GetOwnerModuleFromUdp6Entry
GetOwnerModuleFromUdp6Entry.argtypes = [PMIB_UDP6ROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, LPDWORD]
GetOwnerModuleFromUdp6Entry.restype = DWORD
GetOwnerModuleFromUdp6Entry.errcheck = no_error

_iphlpapi_cdecl = ctypes.CDLL("Iphlpapi", use_last_error=True)
GetOwnerModuleFromPidAndInfo = _iphlpapi_cdecl.GetOwnerModuleFromPidAndInfo
GetOwnerModuleFromPidAndInfo.argtypes = [ULONG, PULONG64, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, LPDWORD]
GetOwnerModuleFromPidAndInfo.restype = DWORD
GetOwnerModuleFromPidAndInfo.errcheck = no_error

GetIpStatistics = windll.iphlpapi.GetIpStatistics
GetIpStatistics.argtypes = [PMIB_IPSTATS]
GetIpStatistics.restype = ULONG
GetIpStatistics.errcheck = no_error

GetIcmpStatistics = windll.iphlpapi.GetIcmpStatistics
GetIcmpStatistics.argtypes = [PMIB_ICMP]
GetIcmpStatistics.restype = ULONG
GetIcmpStatistics.errcheck = no_error

GetTcpStatistics = windll.iphlpapi.GetTcpStatistics
GetTcpStatistics.argtypes = [PMIB_TCPSTATS]
GetTcpStatistics.restype = ULONG
GetTcpStatistics.errcheck = no_error

GetUdpStatistics = windll.iphlpapi.GetUdpStatistics
GetUdpStatistics.argtypes = [PMIB_UDPSTATS]
GetUdpStatistics.restype = ULONG
GetUdpStatistics.errcheck = no_error

SetIpStatisticsEx = windll.iphlpapi.SetIpStatisticsEx
SetIpStatisticsEx.argtypes = [PMIB_IPSTATS, ULONG]
SetIpStatisticsEx.restype = ULONG
SetIpStatisticsEx.errcheck = no_error

GetIpStatisticsEx = windll.iphlpapi.GetIpStatisticsEx
GetIpStatisticsEx.argtypes = [PMIB_IPSTATS, ULONG]
GetIpStatisticsEx.restype = ULONG
GetIpStatisticsEx.errcheck = no_error

GetIcmpStatisticsEx = windll.iphlpapi.GetIcmpStatisticsEx
GetIcmpStatisticsEx.argtypes = [PMIB_ICMP_EX, ULONG]
GetIcmpStatisticsEx.restype = ULONG
GetIcmpStatisticsEx.errcheck = no_error

GetTcpStatisticsEx = windll.iphlpapi.GetTcpStatisticsEx
GetTcpStatisticsEx.argtypes = [PMIB_TCPSTATS, ULONG]
GetTcpStatisticsEx.restype = ULONG
GetTcpStatisticsEx.errcheck = no_error

GetUdpStatisticsEx = windll.iphlpapi.GetUdpStatisticsEx
GetUdpStatisticsEx.argtypes = [PMIB_UDPSTATS, ULONG]
GetUdpStatisticsEx.restype = ULONG
GetUdpStatisticsEx.errcheck = no_error

GetTcpStatisticsEx2 = windll.iphlpapi.GetTcpStatisticsEx2
GetTcpStatisticsEx2.argtypes = [PMIB_TCPSTATS2, ULONG]
GetTcpStatisticsEx2.restype = ULONG
GetTcpStatisticsEx2.errcheck = no_error

GetUdpStatisticsEx2 = windll.iphlpapi.GetUdpStatisticsEx2
GetUdpStatisticsEx2.argtypes = [PMIB_UDPSTATS2, ULONG]
GetUdpStatisticsEx2.restype = ULONG
GetUdpStatisticsEx2.errcheck = no_error

SetIfEntry = windll.iphlpapi.SetIfEntry
SetIfEntry.argtypes = [PMIB_IFROW]
SetIfEntry.restype = DWORD
SetIfEntry.errcheck = no_error

CreateIpForwardEntry = windll.iphlpapi.CreateIpForwardEntry
CreateIpForwardEntry.argtypes = [PMIB_IPFORWARDROW]
CreateIpForwardEntry.restype = DWORD
CreateIpForwardEntry.errcheck = no_error

SetIpForwardEntry = windll.iphlpapi.SetIpForwardEntry
SetIpForwardEntry.argtypes = [PMIB_IPFORWARDROW]
SetIpForwardEntry.restype = DWORD
SetIpForwardEntry.errcheck = no_error

DeleteIpForwardEntry = windll.iphlpapi.DeleteIpForwardEntry
DeleteIpForwardEntry.argtypes = [PMIB_IPFORWARDROW]
DeleteIpForwardEntry.restype = DWORD
DeleteIpForwardEntry.errcheck = no_error

SetIpStatistics = windll.iphlpapi.SetIpStatistics
SetIpStatistics.argtypes = [PMIB_IPSTATS]
SetIpStatistics.restype = DWORD
SetIpStatistics.errcheck = no_error

SetIpTTL = windll.iphlpapi.SetIpTTL
SetIpTTL.argtypes = [UINT]
SetIpTTL.restype = DWORD
SetIpTTL.errcheck = no_error

CreateIpNetEntry = windll.iphlpapi.CreateIpNetEntry
CreateIpNetEntry.argtypes = [PMIB_IPNETROW]
CreateIpNetEntry.restype = DWORD
CreateIpNetEntry.errcheck = no_error

SetIpNetEntry = windll.iphlpapi.SetIpNetEntry
SetIpNetEntry.argtypes = [PMIB_IPNETROW]
SetIpNetEntry.restype = DWORD
SetIpNetEntry.errcheck = no_error

DeleteIpNetEntry = windll.iphlpapi.DeleteIpNetEntry
DeleteIpNetEntry.argtypes = [PMIB_IPNETROW]
DeleteIpNetEntry.restype = DWORD
DeleteIpNetEntry.errcheck = no_error

FlushIpNetTable = windll.iphlpapi.FlushIpNetTable
FlushIpNetTable.argtypes = [DWORD]
FlushIpNetTable.restype = DWORD
FlushIpNetTable.errcheck = no_error

CreateProxyArpEntry = windll.iphlpapi.CreateProxyArpEntry
CreateProxyArpEntry.argtypes = [DWORD, DWORD, DWORD]
CreateProxyArpEntry.restype = DWORD
CreateProxyArpEntry.errcheck = no_error

DeleteProxyArpEntry = windll.iphlpapi.DeleteProxyArpEntry
DeleteProxyArpEntry.argtypes = [DWORD, DWORD, DWORD]
DeleteProxyArpEntry.restype = DWORD
DeleteProxyArpEntry.errcheck = no_error

SetTcpEntry = windll.iphlpapi.SetTcpEntry
SetTcpEntry.argtypes = [PMIB_TCPROW]
SetTcpEntry.restype = DWORD
SetTcpEntry.errcheck = no_error

GetInterfaceInfo = windll.iphlpapi.GetInterfaceInfo
GetInterfaceInfo.argtypes = [PIP_INTERFACE_INFO, PULONG]
GetInterfaceInfo.restype = DWORD
GetInterfaceInfo.errcheck = no_error

GetUniDirectionalAdapterInfo = windll.iphlpapi.GetUniDirectionalAdapterInfo
GetUniDirectionalAdapterInfo.argtypes = [PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS, PULONG]
GetUniDirectionalAdapterInfo.restype = DWORD
GetUniDirectionalAdapterInfo.errcheck = no_error

NhpAllocateAndGetInterfaceInfoFromStack = windll.iphlpapi.NhpAllocateAndGetInterfaceInfoFromStack
NhpAllocateAndGetInterfaceInfoFromStack.argtypes = [POINTER(PIP_INTERFACE_NAME_INFO), LPDWORD, BOOL, HANDLE, DWORD]
NhpAllocateAndGetInterfaceInfoFromStack.restype = DWORD
NhpAllocateAndGetInterfaceInfoFromStack.errcheck = error_success

GetBestInterface = windll.iphlpapi.GetBestInterface
GetBestInterface.argtypes = [DWORD, LPDWORD]
GetBestInterface.restype = DWORD
GetBestInterface.errcheck = no_error

GetBestInterfaceEx = windll.iphlpapi.GetBestInterfaceEx
GetBestInterfaceEx.argtypes = [LPSOCKADDR, LPDWORD]
GetBestInterfaceEx.restype = DWORD
GetBestInterfaceEx.errcheck = no_error

GetBestRoute = windll.iphlpapi.GetBestRoute
GetBestRoute.argtypes = [DWORD, DWORD, PMIB_IPFORWARDROW]
GetBestRoute.restype = DWORD
GetBestRoute.errcheck = no_error

NotifyAddrChange = windll.iphlpapi.NotifyAddrChange
NotifyAddrChange.argtypes = [PHANDLE, LPOVERLAPPED]
NotifyAddrChange.restype = DWORD
NotifyAddrChange.errcheck = no_error_or_pending

NotifyRouteChange = windll.iphlpapi.NotifyRouteChange
NotifyRouteChange.argtypes = [PHANDLE, LPOVERLAPPED]
NotifyRouteChange.restype = DWORD
NotifyRouteChange.errcheck = no_error_or_pending

CancelIPChangeNotify = windll.iphlpapi.CancelIPChangeNotify
CancelIPChangeNotify.argtypes = [LPOVERLAPPED]
CancelIPChangeNotify.restype = BOOL

GetAdapterIndex = windll.iphlpapi.GetAdapterIndex
GetAdapterIndex.argtypes = [LPWSTR, PULONG]
GetAdapterIndex.restype = DWORD
GetAdapterIndex.errcheck = no_error

AddIPAddress = windll.iphlpapi.AddIPAddress
AddIPAddress.argtypes = [DWORD, DWORD, DWORD, PULONG, PULONG]
AddIPAddress.restype = DWORD
AddIPAddress.errcheck = no_error

DeleteIPAddress = windll.iphlpapi.DeleteIPAddress
DeleteIPAddress.argtypes = [ULONG]
DeleteIPAddress.restype = DWORD
DeleteIPAddress.errcheck = no_error

GetNetworkParams = windll.iphlpapi.GetNetworkParams
GetNetworkParams.argtypes = [PFIXED_INFO, PULONG]
GetNetworkParams.restype = DWORD
GetNetworkParams.errcheck = no_error

GetAdaptersInfo = windll.iphlpapi.GetAdaptersInfo
GetAdaptersInfo.argtypes = [PIP_ADAPTER_INFO, PULONG]
GetAdaptersInfo.restype = ULONG
GetAdaptersInfo.errcheck = error_success

GetAdapterOrderMap = windll.iphlpapi.GetAdapterOrderMap
GetAdapterOrderMap.argtypes = []
GetAdapterOrderMap.restype = PIP_ADAPTER_ORDER_MAP

GetAdaptersAddresses = windll.iphlpapi.GetAdaptersAddresses
GetAdaptersAddresses.argtypes = [ULONG, ULONG, PVOID, PIP_ADAPTER_ADDRESSES, PULONG]
GetAdaptersAddresses.restype = ULONG
GetAdaptersAddresses.errcheck = error_success

GetPerAdapterInfo = windll.iphlpapi.GetPerAdapterInfo
GetPerAdapterInfo.argtypes = [ULONG, PIP_PER_ADAPTER_INFO, PULONG]
GetPerAdapterInfo.restype = DWORD
GetPerAdapterInfo.errcheck = no_error

GetInterfaceActiveTimestampCapabilities = windll.iphlpapi.GetInterfaceActiveTimestampCapabilities
GetInterfaceActiveTimestampCapabilities.argtypes = [PIF_LUID, PINTERFACE_TIMESTAMP_CAPABILITIES]
GetInterfaceActiveTimestampCapabilities.restype = DWORD
GetInterfaceActiveTimestampCapabilities.errcheck = no_error

GetInterfaceSupportedTimestampCapabilities = windll.iphlpapi.GetInterfaceSupportedTimestampCapabilities
GetInterfaceSupportedTimestampCapabilities.argtypes = [PIF_LUID, PINTERFACE_TIMESTAMP_CAPABILITIES]
GetInterfaceSupportedTimestampCapabilities.restype = DWORD
GetInterfaceSupportedTimestampCapabilities.errcheck = no_error

CaptureInterfaceHardwareCrossTimestamp = windll.iphlpapi.CaptureInterfaceHardwareCrossTimestamp
CaptureInterfaceHardwareCrossTimestamp.argtypes = [PIF_LUID, PINTERFACE_HARDWARE_CROSSTIMESTAMP]
CaptureInterfaceHardwareCrossTimestamp.restype = DWORD

RegisterInterfaceTimestampConfigChange = windll.iphlpapi.RegisterInterfaceTimestampConfigChange
RegisterInterfaceTimestampConfigChange.argtypes = [
    PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK,
    PVOID,
    POINTER(HIFTIMESTAMPCHANGE),
]
RegisterInterfaceTimestampConfigChange.restype = DWORD

UnregisterInterfaceTimestampConfigChange = windll.iphlpapi.UnregisterInterfaceTimestampConfigChange
UnregisterInterfaceTimestampConfigChange.argtypes = [HIFTIMESTAMPCHANGE]
UnregisterInterfaceTimestampConfigChange.restype = None

GetInterfaceCurrentTimestampCapabilities = windll.iphlpapi.GetInterfaceCurrentTimestampCapabilities
GetInterfaceCurrentTimestampCapabilities.argtypes = [PIF_LUID, PINTERFACE_TIMESTAMP_CAPABILITIES]
GetInterfaceCurrentTimestampCapabilities.restype = DWORD

GetInterfaceHardwareTimestampCapabilities = windll.iphlpapi.GetInterfaceHardwareTimestampCapabilities
GetInterfaceHardwareTimestampCapabilities.argtypes = [PIF_LUID, PINTERFACE_TIMESTAMP_CAPABILITIES]
GetInterfaceHardwareTimestampCapabilities.restype = DWORD

NotifyIfTimestampConfigChange = windll.iphlpapi.NotifyIfTimestampConfigChange
NotifyIfTimestampConfigChange.argtypes = [
    PVOID,
    PINTERFACE_TIMESTAMP_CONFIG_CHANGE_CALLBACK,
    POINTER(HIFTIMESTAMPCHANGE),
]
NotifyIfTimestampConfigChange.restype = DWORD

CancelIfTimestampConfigChange = windll.iphlpapi.CancelIfTimestampConfigChange
CancelIfTimestampConfigChange.argtypes = [HIFTIMESTAMPCHANGE]
CancelIfTimestampConfigChange.restype = None

IpReleaseAddress = windll.iphlpapi.IpReleaseAddress
IpReleaseAddress.argtypes = [PIP_ADAPTER_INDEX_MAP]
IpReleaseAddress.restype = DWORD
IpReleaseAddress.errcheck = no_error

IpRenewAddress = windll.iphlpapi.IpRenewAddress
IpRenewAddress.argtypes = [PIP_ADAPTER_INDEX_MAP]
IpRenewAddress.restype = DWORD
IpRenewAddress.errcheck = no_error

SendARP = windll.iphlpapi.SendARP
SendARP.argtypes = [DWORD, DWORD, PVOID, PULONG]
SendARP.restype = DWORD
SendARP.errcheck = no_error

GetRTTAndHopCount = windll.iphlpapi.GetRTTAndHopCount
GetRTTAndHopCount.argtypes = [DWORD, PULONG, ULONG, PULONG]
GetRTTAndHopCount.restype = BOOL
GetRTTAndHopCount.errcheck = nonzero

GetFriendlyIfIndex = windll.iphlpapi.GetFriendlyIfIndex
GetFriendlyIfIndex.argtypes = [DWORD]
GetFriendlyIfIndex.restype = DWORD

EnableRouter = windll.iphlpapi.EnableRouter
EnableRouter.argtypes = [PHANDLE, LPOVERLAPPED]
EnableRouter.restype = DWORD
EnableRouter.errcheck = error_io_pending

UnenableRouter = windll.iphlpapi.UnenableRouter
UnenableRouter.argtypes = [LPOVERLAPPED, LPDWORD]
UnenableRouter.restype = DWORD
UnenableRouter.errcheck = no_error

DisableMediaSense = windll.iphlpapi.DisableMediaSense
DisableMediaSense.argtypes = [PHANDLE, LPOVERLAPPED]
DisableMediaSense.restype = DWORD
DisableMediaSense.errcheck = no_error_or_pending

RestoreMediaSense = windll.iphlpapi.RestoreMediaSense
RestoreMediaSense.argtypes = [LPOVERLAPPED, LPDWORD]
RestoreMediaSense.restype = DWORD
RestoreMediaSense.errcheck = no_error_or_pending

GetIpErrorString = windll.iphlpapi.GetIpErrorString
GetIpErrorString.argtypes = [DWORD, LPWSTR, LPDWORD]
GetIpErrorString.restype = DWORD
GetIpErrorString.errcheck = no_error

ResolveNeighbor = windll.iphlpapi.ResolveNeighbor
ResolveNeighbor.argtypes = [LPSOCKADDR, PVOID, PULONG]
ResolveNeighbor.restype = ULONG

CreatePersistentTcpPortReservation = windll.iphlpapi.CreatePersistentTcpPortReservation
CreatePersistentTcpPortReservation.argtypes = [USHORT, USHORT, PULONG64]
CreatePersistentTcpPortReservation.restype = ULONG
CreatePersistentTcpPortReservation.errcheck = no_error

CreatePersistentUdpPortReservation = windll.iphlpapi.CreatePersistentUdpPortReservation
CreatePersistentUdpPortReservation.argtypes = [USHORT, USHORT, PULONG64]
CreatePersistentUdpPortReservation.restype = ULONG
CreatePersistentUdpPortReservation.errcheck = no_error

DeletePersistentTcpPortReservation = windll.iphlpapi.DeletePersistentTcpPortReservation
DeletePersistentTcpPortReservation.argtypes = [USHORT, USHORT]
DeletePersistentTcpPortReservation.restype = ULONG
DeletePersistentTcpPortReservation.errcheck = no_error

DeletePersistentUdpPortReservation = windll.iphlpapi.DeletePersistentUdpPortReservation
DeletePersistentUdpPortReservation.argtypes = [USHORT, USHORT]
DeletePersistentUdpPortReservation.restype = ULONG
DeletePersistentUdpPortReservation.errcheck = no_error

LookupPersistentTcpPortReservation = windll.iphlpapi.LookupPersistentTcpPortReservation
LookupPersistentTcpPortReservation.argtypes = [USHORT, USHORT, PULONG64]
LookupPersistentTcpPortReservation.restype = ULONG
LookupPersistentTcpPortReservation.errcheck = no_error

LookupPersistentUdpPortReservation = windll.iphlpapi.LookupPersistentUdpPortReservation
LookupPersistentUdpPortReservation.argtypes = [USHORT, USHORT, PULONG64]
LookupPersistentUdpPortReservation.restype = ULONG
LookupPersistentUdpPortReservation.errcheck = no_error

NET_STRING_IPV4_ADDRESS = 0x00000001
NET_STRING_IPV4_SERVICE = 0x00000002
NET_STRING_IPV4_NETWORK = 0x00000004
NET_STRING_IPV6_ADDRESS = 0x00000008
NET_STRING_IPV6_ADDRESS_NO_SCOPE = 0x00000010
NET_STRING_IPV6_SERVICE = 0x00000020
NET_STRING_IPV6_SERVICE_NO_SCOPE = 0x00000040
NET_STRING_IPV6_NETWORK = 0x00000080
NET_STRING_NAMED_ADDRESS = 0x00000100
NET_STRING_NAMED_SERVICE = 0x00000200
NET_STRING_IP_ADDRESS = NET_STRING_IPV4_ADDRESS | NET_STRING_IPV6_ADDRESS
NET_STRING_IP_ADDRESS_NO_SCOPE = NET_STRING_IPV4_ADDRESS | NET_STRING_IPV6_ADDRESS_NO_SCOPE
NET_STRING_IP_SERVICE = NET_STRING_IPV4_SERVICE | NET_STRING_IPV6_SERVICE
NET_STRING_IP_SERVICE_NO_SCOPE = NET_STRING_IPV4_SERVICE | NET_STRING_IPV6_SERVICE_NO_SCOPE
NET_STRING_IP_NETWORK = NET_STRING_IPV4_NETWORK | NET_STRING_IPV6_NETWORK
NET_STRING_ANY_ADDRESS = NET_STRING_NAMED_ADDRESS | NET_STRING_IP_ADDRESS
NET_STRING_ANY_ADDRESS_NO_SCOPE = NET_STRING_NAMED_ADDRESS | NET_STRING_IP_ADDRESS_NO_SCOPE
NET_STRING_ANY_SERVICE = NET_STRING_NAMED_SERVICE | NET_STRING_IP_SERVICE
NET_STRING_ANY_SERVICE_NO_SCOPE = NET_STRING_NAMED_SERVICE | NET_STRING_IP_SERVICE_NO_SCOPE


class NET_ADDRESS_FORMAT(CEnum):
    NET_ADDRESS_FORMAT_UNSPECIFIED = 0
    NET_ADDRESS_DNS_NAME = 1
    NET_ADDRESS_IPV4 = 2
    NET_ADDRESS_IPV6 = 3


class NET_ADDRESS_INFO_NAMED_ADDRESS(Structure):
    _fields_ = [("Address", WCHAR * 256), ("Port", WCHAR * 6)]


class NET_ADDRESS_INFO_UNION(Union):
    _fields_ = [
        ("NamedAddress", NET_ADDRESS_INFO_NAMED_ADDRESS),
        ("Ipv4Address", SOCKADDR_IN),
        ("Ipv6Address", SOCKADDR_IN6),
        ("IpAddress", SOCKADDR),
    ]


class NET_ADDRESS_INFO(Structure):
    _anonymous_ = ("u",)
    _fields_ = [("Format", NET_ADDRESS_FORMAT), ("u", NET_ADDRESS_INFO_UNION)]


PNET_ADDRESS_INFO = POINTER(NET_ADDRESS_INFO)


ParseNetworkString = windll.iphlpapi.ParseNetworkString
ParseNetworkString.argtypes = [LPCWSTR, DWORD, PNET_ADDRESS_INFO, POINTER(USHORT), POINTER(BYTE)]
ParseNetworkString.restype = DWORD
ParseNetworkString.errcheck = error_success
