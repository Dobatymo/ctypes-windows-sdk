"""ctypes bindings for process and system performance inspection APIs."""

from ctypes import POINTER, WINFUNCTYPE, Structure, Union, sizeof
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCSTR, LPCWSTR, LPSTR, LPVOID, LPWSTR

from .. import nonzero, windll
from ..shared.basetsd import SIZE_T, ULONG64, ULONG_PTR
from ..shared.minwindef import HMODULE, LPDWORD
from ..shared.ntdef import PVOID

LIST_MODULES_DEFAULT = 0x0
LIST_MODULES_32BIT = 0x01
LIST_MODULES_64BIT = 0x02
LIST_MODULES_ALL = LIST_MODULES_32BIT | LIST_MODULES_64BIT


class MODULEINFO(Structure):
    _fields_ = [
        ("lpBaseOfDll", LPVOID),
        ("SizeOfImage", DWORD),
        ("EntryPoint", LPVOID),
    ]


LPMODULEINFO = POINTER(MODULEINFO)


class PSAPI_WS_WATCH_INFORMATION(Structure):
    _fields_ = [("FaultingPc", LPVOID), ("FaultingVa", LPVOID)]


PPSAPI_WS_WATCH_INFORMATION = POINTER(PSAPI_WS_WATCH_INFORMATION)


class PSAPI_WS_WATCH_INFORMATION_EX(Structure):
    _fields_ = [
        ("BasicInfo", PSAPI_WS_WATCH_INFORMATION),
        ("FaultingThreadId", ULONG_PTR),
        ("Flags", ULONG_PTR),
    ]


PPSAPI_WS_WATCH_INFORMATION_EX = POINTER(PSAPI_WS_WATCH_INFORMATION_EX)


class _PSAPI_WORKING_SET_BLOCK_BITS(Structure):
    _fields_ = [
        ("Protection", ULONG_PTR, 5),
        ("ShareCount", ULONG_PTR, 3),
        ("Shared", ULONG_PTR, 1),
        ("Reserved", ULONG_PTR, 3),
        ("VirtualPage", ULONG_PTR, 52 if sizeof(ULONG_PTR) == 8 else 20),
    ]


class PSAPI_WORKING_SET_BLOCK(Union):
    _anonymous_ = ("Bits",)
    _fields_ = [("Flags", ULONG_PTR), ("Bits", _PSAPI_WORKING_SET_BLOCK_BITS)]


PPSAPI_WORKING_SET_BLOCK = POINTER(PSAPI_WORKING_SET_BLOCK)


class PSAPI_WORKING_SET_INFORMATION(Structure):
    _fields_ = [("NumberOfEntries", ULONG_PTR), ("WorkingSetInfo", PSAPI_WORKING_SET_BLOCK * 1)]


PPSAPI_WORKING_SET_INFORMATION = POINTER(PSAPI_WORKING_SET_INFORMATION)


class _PSAPI_WORKING_SET_EX_BLOCK_VALID(Structure):
    _fields_ = [
        ("Valid", ULONG_PTR, 1),
        ("ShareCount", ULONG_PTR, 3),
        ("Win32Protection", ULONG_PTR, 11),
        ("Shared", ULONG_PTR, 1),
        ("Node", ULONG_PTR, 6),
        ("Locked", ULONG_PTR, 1),
        ("LargePage", ULONG_PTR, 1),
        ("Reserved", ULONG_PTR, 7),
        ("Bad", ULONG_PTR, 1),
    ]

    if sizeof(ULONG_PTR) == 8:
        _fields_.append(("ReservedUlong", ULONG_PTR, 32))


class _PSAPI_WORKING_SET_EX_BLOCK_INVALID(Structure):
    _fields_ = [
        ("Valid", ULONG_PTR, 1),
        ("Reserved0", ULONG_PTR, 14),
        ("Shared", ULONG_PTR, 1),
        ("Reserved1", ULONG_PTR, 15),
        ("Bad", ULONG_PTR, 1),
    ]

    if sizeof(ULONG_PTR) == 8:
        _fields_.append(("ReservedUlong", ULONG_PTR, 32))


class _PSAPI_WORKING_SET_EX_BLOCK_BITS(Union):
    _anonymous_ = ("ValidBits",)
    _fields_ = [
        ("ValidBits", _PSAPI_WORKING_SET_EX_BLOCK_VALID),
        ("Invalid", _PSAPI_WORKING_SET_EX_BLOCK_INVALID),
    ]


class PSAPI_WORKING_SET_EX_BLOCK(Union):
    _anonymous_ = ("Bits",)
    _fields_ = [("Flags", ULONG_PTR), ("Bits", _PSAPI_WORKING_SET_EX_BLOCK_BITS)]


PPSAPI_WORKING_SET_EX_BLOCK = POINTER(PSAPI_WORKING_SET_EX_BLOCK)


class PSAPI_WORKING_SET_EX_INFORMATION(Structure):
    _fields_ = [("VirtualAddress", PVOID), ("VirtualAttributes", PSAPI_WORKING_SET_EX_BLOCK)]


PPSAPI_WORKING_SET_EX_INFORMATION = POINTER(PSAPI_WORKING_SET_EX_INFORMATION)


class PROCESS_MEMORY_COUNTERS(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("PageFaultCount", DWORD),
        ("PeakWorkingSetSize", SIZE_T),
        ("WorkingSetSize", SIZE_T),
        ("QuotaPeakPagedPoolUsage", SIZE_T),
        ("QuotaPagedPoolUsage", SIZE_T),
        ("QuotaPeakNonPagedPoolUsage", SIZE_T),
        ("QuotaNonPagedPoolUsage", SIZE_T),
        ("PagefileUsage", SIZE_T),
        ("PeakPagefileUsage", SIZE_T),
    ]


PPROCESS_MEMORY_COUNTERS = POINTER(PROCESS_MEMORY_COUNTERS)


class PROCESS_MEMORY_COUNTERS_EX(PROCESS_MEMORY_COUNTERS):
    _fields_ = [("PrivateUsage", SIZE_T)]


PPROCESS_MEMORY_COUNTERS_EX = POINTER(PROCESS_MEMORY_COUNTERS_EX)


class PROCESS_MEMORY_COUNTERS_EX2(PROCESS_MEMORY_COUNTERS_EX):
    _fields_ = [("PrivateWorkingSetSize", SIZE_T), ("SharedCommitUsage", ULONG64)]


PPROCESS_MEMORY_COUNTERS_EX2 = POINTER(PROCESS_MEMORY_COUNTERS_EX2)


class PERFORMANCE_INFORMATION(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("CommitTotal", SIZE_T),
        ("CommitLimit", SIZE_T),
        ("CommitPeak", SIZE_T),
        ("PhysicalTotal", SIZE_T),
        ("PhysicalAvailable", SIZE_T),
        ("SystemCache", SIZE_T),
        ("KernelTotal", SIZE_T),
        ("KernelPaged", SIZE_T),
        ("KernelNonpaged", SIZE_T),
        ("PageSize", SIZE_T),
        ("HandleCount", DWORD),
        ("ProcessCount", DWORD),
        ("ThreadCount", DWORD),
    ]


PPERFORMANCE_INFORMATION = POINTER(PERFORMANCE_INFORMATION)
PERFORMACE_INFORMATION = PERFORMANCE_INFORMATION
PPERFORMACE_INFORMATION = PPERFORMANCE_INFORMATION


class ENUM_PAGE_FILE_INFORMATION(Structure):
    _fields_ = [
        ("cb", DWORD),
        ("Reserved", DWORD),
        ("TotalSize", SIZE_T),
        ("TotalInUse", SIZE_T),
        ("PeakUsage", SIZE_T),
    ]


PENUM_PAGE_FILE_INFORMATION = POINTER(ENUM_PAGE_FILE_INFORMATION)
PENUM_PAGE_FILE_CALLBACKW = WINFUNCTYPE(BOOL, LPVOID, PENUM_PAGE_FILE_INFORMATION, LPCWSTR)
PENUM_PAGE_FILE_CALLBACKA = WINFUNCTYPE(BOOL, LPVOID, PENUM_PAGE_FILE_INFORMATION, LPCSTR)


EnumProcesses = windll.kernel32.K32EnumProcesses
EnumProcesses.argtypes = [POINTER(DWORD), DWORD, LPDWORD]
EnumProcesses.restype = BOOL
EnumProcesses.errcheck = nonzero

EnumProcessModules = windll.kernel32.K32EnumProcessModules
EnumProcessModules.argtypes = [HANDLE, POINTER(HMODULE), DWORD, LPDWORD]
EnumProcessModules.restype = BOOL
EnumProcessModules.errcheck = nonzero

EnumProcessModulesEx = windll.kernel32.K32EnumProcessModulesEx
EnumProcessModulesEx.argtypes = [HANDLE, POINTER(HMODULE), DWORD, LPDWORD, DWORD]
EnumProcessModulesEx.restype = BOOL
EnumProcessModulesEx.errcheck = nonzero

GetModuleBaseNameA = windll.kernel32.K32GetModuleBaseNameA
GetModuleBaseNameA.argtypes = [HANDLE, HMODULE, LPSTR, DWORD]
GetModuleBaseNameA.restype = DWORD
GetModuleBaseNameA.errcheck = nonzero

GetModuleBaseNameW = windll.kernel32.K32GetModuleBaseNameW
GetModuleBaseNameW.argtypes = [HANDLE, HMODULE, LPWSTR, DWORD]
GetModuleBaseNameW.restype = DWORD
GetModuleBaseNameW.errcheck = nonzero

GetModuleFileNameExA = windll.kernel32.K32GetModuleFileNameExA
GetModuleFileNameExA.argtypes = [HANDLE, HMODULE, LPSTR, DWORD]
GetModuleFileNameExA.restype = DWORD
GetModuleFileNameExA.errcheck = nonzero

GetModuleFileNameExW = windll.kernel32.K32GetModuleFileNameExW
GetModuleFileNameExW.argtypes = [HANDLE, HMODULE, LPWSTR, DWORD]
GetModuleFileNameExW.restype = DWORD
GetModuleFileNameExW.errcheck = nonzero

GetModuleInformation = windll.kernel32.K32GetModuleInformation
GetModuleInformation.argtypes = [HANDLE, HMODULE, LPMODULEINFO, DWORD]
GetModuleInformation.restype = BOOL
GetModuleInformation.errcheck = nonzero

EmptyWorkingSet = windll.kernel32.K32EmptyWorkingSet
EmptyWorkingSet.argtypes = [HANDLE]
EmptyWorkingSet.restype = BOOL
EmptyWorkingSet.errcheck = nonzero

InitializeProcessForWsWatch = windll.kernel32.K32InitializeProcessForWsWatch
InitializeProcessForWsWatch.argtypes = [HANDLE]
InitializeProcessForWsWatch.restype = BOOL
InitializeProcessForWsWatch.errcheck = nonzero

GetWsChanges = windll.kernel32.K32GetWsChanges
GetWsChanges.argtypes = [HANDLE, PPSAPI_WS_WATCH_INFORMATION, DWORD]
GetWsChanges.restype = BOOL
GetWsChanges.errcheck = nonzero

GetWsChangesEx = windll.kernel32.K32GetWsChangesEx
GetWsChangesEx.argtypes = [HANDLE, PPSAPI_WS_WATCH_INFORMATION_EX, LPDWORD]
GetWsChangesEx.restype = BOOL
GetWsChangesEx.errcheck = nonzero

GetMappedFileNameW = windll.kernel32.K32GetMappedFileNameW
GetMappedFileNameW.argtypes = [HANDLE, LPVOID, LPWSTR, DWORD]
GetMappedFileNameW.restype = DWORD
GetMappedFileNameW.errcheck = nonzero

GetMappedFileNameA = windll.kernel32.K32GetMappedFileNameA
GetMappedFileNameA.argtypes = [HANDLE, LPVOID, LPSTR, DWORD]
GetMappedFileNameA.restype = DWORD
GetMappedFileNameA.errcheck = nonzero

EnumDeviceDrivers = windll.kernel32.K32EnumDeviceDrivers
EnumDeviceDrivers.argtypes = [POINTER(LPVOID), DWORD, LPDWORD]
EnumDeviceDrivers.restype = BOOL
EnumDeviceDrivers.errcheck = nonzero

GetDeviceDriverBaseNameA = windll.kernel32.K32GetDeviceDriverBaseNameA
GetDeviceDriverBaseNameA.argtypes = [LPVOID, LPSTR, DWORD]
GetDeviceDriverBaseNameA.restype = DWORD
GetDeviceDriverBaseNameA.errcheck = nonzero

GetDeviceDriverBaseNameW = windll.kernel32.K32GetDeviceDriverBaseNameW
GetDeviceDriverBaseNameW.argtypes = [LPVOID, LPWSTR, DWORD]
GetDeviceDriverBaseNameW.restype = DWORD
GetDeviceDriverBaseNameW.errcheck = nonzero

GetDeviceDriverFileNameA = windll.kernel32.K32GetDeviceDriverFileNameA
GetDeviceDriverFileNameA.argtypes = [LPVOID, LPSTR, DWORD]
GetDeviceDriverFileNameA.restype = DWORD
GetDeviceDriverFileNameA.errcheck = nonzero

GetDeviceDriverFileNameW = windll.kernel32.K32GetDeviceDriverFileNameW
GetDeviceDriverFileNameW.argtypes = [LPVOID, LPWSTR, DWORD]
GetDeviceDriverFileNameW.restype = DWORD
GetDeviceDriverFileNameW.errcheck = nonzero

QueryWorkingSet = windll.kernel32.K32QueryWorkingSet
QueryWorkingSet.argtypes = [HANDLE, PVOID, DWORD]
QueryWorkingSet.restype = BOOL
QueryWorkingSet.errcheck = nonzero

QueryWorkingSetEx = windll.kernel32.K32QueryWorkingSetEx
QueryWorkingSetEx.argtypes = [HANDLE, PVOID, DWORD]
QueryWorkingSetEx.restype = BOOL
QueryWorkingSetEx.errcheck = nonzero

GetProcessMemoryInfo = windll.kernel32.K32GetProcessMemoryInfo
GetProcessMemoryInfo.argtypes = [HANDLE, PPROCESS_MEMORY_COUNTERS, DWORD]
GetProcessMemoryInfo.restype = BOOL
GetProcessMemoryInfo.errcheck = nonzero

GetPerformanceInfo = windll.kernel32.K32GetPerformanceInfo
GetPerformanceInfo.argtypes = [PPERFORMANCE_INFORMATION, DWORD]
GetPerformanceInfo.restype = BOOL
GetPerformanceInfo.errcheck = nonzero

EnumPageFilesW = windll.kernel32.K32EnumPageFilesW
EnumPageFilesW.argtypes = [PENUM_PAGE_FILE_CALLBACKW, LPVOID]
EnumPageFilesW.restype = BOOL
EnumPageFilesW.errcheck = nonzero

EnumPageFilesA = windll.kernel32.K32EnumPageFilesA
EnumPageFilesA.argtypes = [PENUM_PAGE_FILE_CALLBACKA, LPVOID]
EnumPageFilesA.restype = BOOL
EnumPageFilesA.errcheck = nonzero

GetProcessImageFileNameA = windll.kernel32.K32GetProcessImageFileNameA
GetProcessImageFileNameA.argtypes = [HANDLE, LPSTR, DWORD]
GetProcessImageFileNameA.restype = DWORD
GetProcessImageFileNameA.errcheck = nonzero

GetProcessImageFileNameW = windll.kernel32.K32GetProcessImageFileNameW
GetProcessImageFileNameW.argtypes = [HANDLE, LPWSTR, DWORD]
GetProcessImageFileNameW.restype = DWORD
GetProcessImageFileNameW.errcheck = nonzero
