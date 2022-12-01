from ctypes import POINTER, Structure, Union, c_double
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCSTR, LPCWSTR, LPSTR, LPVOID, LPWSTR, UINT, ULONG, USHORT, WORD

from .. import CEnum, windll
from ..shared.basetsd import DWORD_PTR
from ..shared.minwindef import LPDWORD, PBOOL, PDWORD, UCHAR
from ..shared.ntdef import HRESULT, PVOID, ULONGLONG
from .minwinbase import LPFILETIME, LPSYSTEMTIME, SYSTEMTIME
from .winnt import (
    DWORDLONG,
    LOGICAL_PROCESSOR_RELATIONSHIP,
    LPOSVERSIONINFOA,
    LPOSVERSIONINFOW,
    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION,
    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX,
    PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION,
    PULONGLONG,
)


class SYSTEM_INFO_DUMMYSTRUCTNAME(Structure):
    _fields_ = [
        ("wProcessorArchitecture", WORD),
        ("wReserved", WORD),
    ]


class SYSTEM_INFO_DUMMYUNIONNAME(Union):
    _anonymous_ = ["dummy"]
    _fields_ = [
        ("dwOemId", DWORD),
        ("dummy", SYSTEM_INFO_DUMMYSTRUCTNAME),
    ]


class SYSTEM_INFO(Structure):
    _anonymous_ = ["dummy"]
    _fields_ = [
        ("dummy", SYSTEM_INFO_DUMMYUNIONNAME),
        ("dwPageSize", DWORD),
        ("lpMinimumApplicationAddress", LPVOID),
        ("lpMaximumApplicationAddress", LPVOID),
        ("dwActiveProcessorMask", DWORD_PTR),
        ("dwNumberOfProcessors", DWORD),
        ("dwProcessorType", DWORD),
        ("dwAllocationGranularity", DWORD),
        ("wProcessorLevel", WORD),
        ("wProcessorRevision", WORD),
    ]


LPSYSTEM_INFO = POINTER(SYSTEM_INFO)


class MEMORYSTATUSEX(Structure):
    _fields_ = [
        ("dwLength", DWORD),
        ("dwMemoryLoad", DWORD),
        ("ullTotalPhys", DWORDLONG),
        ("ullAvailPhys", DWORDLONG),
        ("ullTotalPageFile", DWORDLONG),
        ("ullAvailPageFile", DWORDLONG),
        ("ullTotalVirtual", DWORDLONG),
        ("ullAvailVirtual", DWORDLONG),
        ("ullAvailExtendedVirtual", DWORDLONG),
    ]


LPMEMORYSTATUSEX = POINTER(MEMORYSTATUSEX)

GlobalMemoryStatusEx = windll.kernel32.GlobalMemoryStatusEx
GlobalMemoryStatusEx.argtypes = [LPMEMORYSTATUSEX]
GlobalMemoryStatusEx.restype = BOOL

GetSystemInfo = windll.kernel32.GetSystemInfo
GetSystemInfo.argtypes = [LPSYSTEM_INFO]
GetSystemInfo.restype = None

GetSystemTime = windll.kernel32.GetSystemTime
GetSystemTime.argtypes = [LPSYSTEMTIME]
GetSystemTime.restype = None

GetSystemTimeAsFileTime = windll.kernel32.GetSystemTimeAsFileTime
GetSystemTimeAsFileTime.argtypes = [LPFILETIME]
GetSystemTimeAsFileTime.restype = None

GetLocalTime = windll.kernel32.GetLocalTime
GetLocalTime.argtypes = [LPSYSTEMTIME]
GetLocalTime.restype = None

GetVersion = windll.kernel32.GetVersion
GetVersion.argtypes = []
GetVersion.restype = DWORD

SetLocalTime = windll.kernel32.SetLocalTime
SetLocalTime.argtypes = [POINTER(SYSTEMTIME)]  # CONST
SetLocalTime.restype = BOOL

GetTickCount = windll.kernel32.GetTickCount
GetTickCount.argtypes = []
GetTickCount.restype = DWORD

GetTickCount64 = windll.kernel32.GetTickCount64
GetTickCount64.argtypes = []
GetTickCount64.restype = ULONGLONG

GetSystemTimeAdjustment = windll.kernel32.GetSystemTimeAdjustment
GetSystemTimeAdjustment.argtypes = [PDWORD, PDWORD, PBOOL]
GetSystemTimeAdjustment.restype = BOOL

# GetSystemTimeAdjustmentPrecise = windll.mincore.GetSystemTimeAdjustmentPrecise
# GetSystemTimeAdjustmentPrecise.argtypes = [PDWORD64, PDWORD64, PBOOL]
# GetSystemTimeAdjustmentPrecise.restype = BOOL

GetSystemDirectoryA = windll.kernel32.GetSystemDirectoryA
GetSystemDirectoryA.argtypes = [LPSTR, UINT]
GetSystemDirectoryA.restype = UINT

GetSystemDirectoryW = windll.kernel32.GetSystemDirectoryW
GetSystemDirectoryW.argtypes = [LPWSTR, UINT]
GetSystemDirectoryW.restype = UINT

GetWindowsDirectoryA = windll.kernel32.GetWindowsDirectoryA
GetWindowsDirectoryA.argtypes = [LPSTR, UINT]
GetWindowsDirectoryA.restype = UINT

GetWindowsDirectoryW = windll.kernel32.GetWindowsDirectoryW
GetWindowsDirectoryW.argtypes = [LPWSTR, UINT]
GetWindowsDirectoryW.restype = UINT

GetSystemWindowsDirectoryA = windll.kernel32.GetSystemWindowsDirectoryA
GetSystemWindowsDirectoryA.argtypes = [LPSTR, UINT]
GetSystemWindowsDirectoryA.restype = UINT

GetSystemWindowsDirectoryW = windll.kernel32.GetSystemWindowsDirectoryW
GetSystemWindowsDirectoryW.argtypes = [LPWSTR, UINT]
GetSystemWindowsDirectoryW.restype = UINT


class COMPUTER_NAME_FORMAT(CEnum):
    ComputerNameNetBIOS = 0
    ComputerNameDnsHostname = 1
    ComputerNameDnsDomain = 2
    ComputerNameDnsFullyQualified = 3
    ComputerNamePhysicalNetBIOS = 4
    ComputerNamePhysicalDnsHostname = 5
    ComputerNamePhysicalDnsDomain = 6
    ComputerNamePhysicalDnsFullyQualified = 7
    ComputerNameMax = 8


GetComputerNameExA = windll.kernel32.GetComputerNameExA
GetComputerNameExA.argtypes = [COMPUTER_NAME_FORMAT, LPSTR, LPDWORD]
GetComputerNameExA.restype = BOOL

GetComputerNameExW = windll.kernel32.GetComputerNameExW
GetComputerNameExW.argtypes = [COMPUTER_NAME_FORMAT, LPWSTR, LPDWORD]
GetComputerNameExW.restype = BOOL

SetComputerNameExW = windll.kernel32.SetComputerNameExW
SetComputerNameExW.argtypes = [COMPUTER_NAME_FORMAT, LPCWSTR]
SetComputerNameExW.restype = BOOL

SetSystemTime = windll.kernel32.SetSystemTime
SetSystemTime.argtypes = [POINTER(SYSTEMTIME)]  # CONST
SetSystemTime.restype = BOOL

GetVersionExA = windll.kernel32.GetVersionExA
GetVersionExA.argtypes = [LPOSVERSIONINFOA]
GetVersionExA.restype = BOOL

GetVersionExW = windll.kernel32.GetVersionExW
GetVersionExW.argtypes = [
    LPOSVERSIONINFOW,
]
GetVersionExW.restype = BOOL

GetLogicalProcessorInformation = windll.kernel32.GetLogicalProcessorInformation
GetLogicalProcessorInformation.argtypes = [PSYSTEM_LOGICAL_PROCESSOR_INFORMATION, PDWORD]
GetLogicalProcessorInformation.restype = BOOL

GetLogicalProcessorInformationEx = windll.kernel32.GetLogicalProcessorInformationEx
GetLogicalProcessorInformationEx.argtypes = [
    LOGICAL_PROCESSOR_RELATIONSHIP,
    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX,
    PDWORD,
]
GetLogicalProcessorInformationEx.restype = BOOL

GetNativeSystemInfo = windll.kernel32.GetNativeSystemInfo
GetNativeSystemInfo.argtypes = [LPSYSTEM_INFO]
GetNativeSystemInfo.restype = None

try:
    GetSystemTimePreciseAsFileTime = windll.kernel32.GetSystemTimePreciseAsFileTime
    GetSystemTimePreciseAsFileTime.argtypes = [LPFILETIME]
    GetSystemTimePreciseAsFileTime.restype = None
except AttributeError:
    pass

GetProductInfo = windll.kernel32.GetProductInfo
GetProductInfo.argtypes = [DWORD, DWORD, DWORD, DWORD, PDWORD]
GetProductInfo.restype = BOOL

VerSetConditionMask = windll.kernel32.VerSetConditionMask
VerSetConditionMask.argtypes = [ULONGLONG, ULONG, UCHAR]
VerSetConditionMask.restype = ULONGLONG

# GetOsSafeBootMode = windll.mincore.GetOsSafeBootMode
# GetOsSafeBootMode.argtypes = [PDWORD]
# GetOsSafeBootMode.restype = BOOL

EnumSystemFirmwareTables = windll.kernel32.EnumSystemFirmwareTables
EnumSystemFirmwareTables.argtypes = [DWORD, PVOID, DWORD]
EnumSystemFirmwareTables.restype = UINT

GetSystemFirmwareTable = windll.kernel32.GetSystemFirmwareTable
GetSystemFirmwareTable.argtypes = [DWORD, DWORD, PVOID, DWORD]
GetSystemFirmwareTable.restype = UINT

try:
    DnsHostnameToComputerNameExW = windll.kernel32.DnsHostnameToComputerNameExW
    DnsHostnameToComputerNameExW.argtypes = [LPCWSTR, LPWSTR, LPDWORD]
    DnsHostnameToComputerNameExW.restype = BOOL
except AttributeError:
    pass

GetPhysicallyInstalledSystemMemory = windll.kernel32.GetPhysicallyInstalledSystemMemory
GetPhysicallyInstalledSystemMemory.argtypes = [PULONGLONG]
GetPhysicallyInstalledSystemMemory.restype = BOOL

SCEX2_ALT_NETBIOS_NAME = 0x00000001

try:
    SetComputerNameEx2W = windll.kernel32.SetComputerNameEx2W
    SetComputerNameEx2W.argtypes = [COMPUTER_NAME_FORMAT, DWORD, LPCWSTR]
    SetComputerNameEx2W.restype = BOOL
except AttributeError:
    pass

SetSystemTimeAdjustment = windll.kernel32.SetSystemTimeAdjustment
SetSystemTimeAdjustment.argtypes = [DWORD, BOOL]
SetSystemTimeAdjustment.restype = BOOL

# SetSystemTimeAdjustmentPrecise = windll.mincore.SetSystemTimeAdjustmentPrecise
# SetSystemTimeAdjustmentPrecise.argtypes = [DWORD64, BOOL]
# SetSystemTimeAdjustmentPrecise.restype = BOOL

try:
    InstallELAMCertificateInfo = windll.kernel32.InstallELAMCertificateInfo
    InstallELAMCertificateInfo.argtypes = [HANDLE]
    InstallELAMCertificateInfo.restype = BOOL
except AttributeError:
    pass

GetProcessorSystemCycleTime = windll.kernel32.GetProcessorSystemCycleTime
GetProcessorSystemCycleTime.argtypes = [USHORT, PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION, PDWORD]
GetProcessorSystemCycleTime.restype = BOOL

try:
    GetIntegratedDisplaySize = windll.onecore.GetIntegratedDisplaySize
    GetIntegratedDisplaySize.argtypes = [POINTER(c_double)]
    GetIntegratedDisplaySize.restype = HRESULT
except (AttributeError, OSError):
    pass

SetComputerNameA = windll.kernel32.SetComputerNameA
SetComputerNameA.argtypes = [LPCSTR]
SetComputerNameA.restype = BOOL

SetComputerNameW = windll.kernel32.SetComputerNameW
SetComputerNameW.argtypes = [LPCWSTR]
SetComputerNameW.restype = BOOL

SetComputerNameExA = windll.kernel32.SetComputerNameExA
SetComputerNameExA.argtypes = [COMPUTER_NAME_FORMAT, LPCSTR]
SetComputerNameExA.restype = BOOL
