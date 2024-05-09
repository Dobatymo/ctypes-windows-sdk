from ctypes import POINTER, Structure
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCWSTR, LPVOID, ULONG

from .. import CEnum, windll
from ..shared.basetsd import SIZE_T, ULONG_PTR
from ..shared.minwindef import LPCVOID, LPDWORD, PBOOL, PDWORD, UINT
from ..shared.ntdef import PVOID
from .minwinbase import SECURITY_ATTRIBUTES
from .winnt import (
    MEMORY_BASIC_INFORMATION,
    SECTION_ALL_ACCESS,
    SECTION_MAP_EXECUTE_EXPLICIT,
    SECTION_MAP_READ,
    SECTION_MAP_WRITE,
)

FILE_MAP_WRITE = SECTION_MAP_WRITE
FILE_MAP_READ = SECTION_MAP_READ
FILE_MAP_ALL_ACCESS = SECTION_ALL_ACCESS
FILE_MAP_EXECUTE = SECTION_MAP_EXECUTE_EXPLICIT  # not included in FILE_MAP_ALL_ACCESS
FILE_MAP_COPY = 0x00000001
FILE_MAP_RESERVE = 0x80000000
FILE_MAP_TARGETS_INVALID = 0x40000000
FILE_MAP_LARGE_PAGES = 0x20000000

VirtualAlloc = windll.kernel32.VirtualAlloc
VirtualAlloc.argtypes = [LPVOID, SIZE_T, DWORD, DWORD]
VirtualAlloc.restype = LPVOID

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = [LPVOID, SIZE_T, DWORD, PDWORD]
VirtualProtect.restype = BOOL

VirtualFree = windll.kernel32.VirtualFree
VirtualFree.argtypes = [LPVOID, SIZE_T, DWORD]
VirtualFree.restype = BOOL

VirtualQuery = windll.kernel32.VirtualQuery
VirtualQuery.argtypes = [LPCVOID, POINTER(MEMORY_BASIC_INFORMATION), SIZE_T]
VirtualQuery.restype = SIZE_T

VirtualAllocEx = windll.kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD, DWORD]
VirtualAllocEx.restype = LPVOID

VirtualProtectEx = windll.kernel32.VirtualProtectEx
VirtualProtectEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD, PDWORD]
VirtualProtectEx.restype = BOOL

VirtualQueryEx = windll.kernel32.VirtualQueryEx
VirtualQueryEx.argtypes = [HANDLE, LPCVOID, POINTER(MEMORY_BASIC_INFORMATION), SIZE_T]
VirtualQueryEx.restype = SIZE_T

ReadProcessMemory = windll.kernel32.ReadProcessMemory
ReadProcessMemory.argtypes = [HANDLE, LPCVOID, LPVOID, SIZE_T, POINTER(SIZE_T)]
ReadProcessMemory.restype = BOOL

WriteProcessMemory = windll.kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, SIZE_T, POINTER(SIZE_T)]
WriteProcessMemory.restype = BOOL

CreateFileMappingW = windll.kernel32.CreateFileMappingW
CreateFileMappingW.argtypes = [HANDLE, POINTER(SECURITY_ATTRIBUTES), DWORD, DWORD, DWORD, LPCWSTR]
CreateFileMappingW.restype = HANDLE

OpenFileMappingW = windll.kernel32.OpenFileMappingW
OpenFileMappingW.argtypes = [DWORD, BOOL, LPCWSTR]
OpenFileMappingW.restype = HANDLE

MapViewOfFile = windll.kernel32.MapViewOfFile
MapViewOfFile.argtypes = [HANDLE, DWORD, DWORD, DWORD, SIZE_T]
MapViewOfFile.restype = LPVOID

MapViewOfFileEx = windll.kernel32.MapViewOfFileEx
MapViewOfFileEx.argtypes = [HANDLE, DWORD, DWORD, DWORD, SIZE_T, LPVOID]
MapViewOfFileEx.restype = LPVOID

VirtualFreeEx = windll.kernel32.VirtualFreeEx
VirtualFreeEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD]
VirtualFreeEx.restype = BOOL

FlushViewOfFile = windll.kernel32.FlushViewOfFile
FlushViewOfFile.argtypes = [LPCVOID, SIZE_T]
FlushViewOfFile.restype = BOOL

UnmapViewOfFile = windll.kernel32.UnmapViewOfFile
UnmapViewOfFile.argtypes = [LPCVOID]
UnmapViewOfFile.restype = BOOL

GetLargePageMinimum = windll.kernel32.GetLargePageMinimum
GetLargePageMinimum.argtypes = []
GetLargePageMinimum.restype = SIZE_T

GetProcessWorkingSetSize = windll.kernel32.GetProcessWorkingSetSize
GetProcessWorkingSetSize.argtypes = [HANDLE, POINTER(SIZE_T), POINTER(SIZE_T)]
GetProcessWorkingSetSize.restype = BOOL

GetProcessWorkingSetSizeEx = windll.kernel32.GetProcessWorkingSetSizeEx
GetProcessWorkingSetSizeEx.argtypes = [HANDLE, POINTER(SIZE_T), POINTER(SIZE_T), PDWORD]
GetProcessWorkingSetSizeEx.restype = BOOL

SetProcessWorkingSetSize = windll.kernel32.SetProcessWorkingSetSize
SetProcessWorkingSetSize.argtypes = [HANDLE, SIZE_T, SIZE_T]
SetProcessWorkingSetSize.restype = BOOL

SetProcessWorkingSetSizeEx = windll.kernel32.SetProcessWorkingSetSizeEx
SetProcessWorkingSetSizeEx.argtypes = [HANDLE, SIZE_T, SIZE_T, DWORD]
SetProcessWorkingSetSizeEx.restype = BOOL

VirtualLock = windll.kernel32.VirtualLock
VirtualLock.argtypes = [LPVOID, SIZE_T]
VirtualLock.restype = BOOL

VirtualUnlock = windll.kernel32.VirtualUnlock
VirtualUnlock.argtypes = [LPVOID, SIZE_T]
VirtualUnlock.restype = BOOL

GetWriteWatch = windll.kernel32.GetWriteWatch
GetWriteWatch.argtypes = [DWORD, PVOID, SIZE_T, POINTER(PVOID), POINTER(ULONG_PTR), LPDWORD]
GetWriteWatch.restype = UINT

ResetWriteWatch = windll.kernel32.ResetWriteWatch
ResetWriteWatch.argtypes = [LPVOID, SIZE_T]
ResetWriteWatch.restype = UINT


class MEMORY_RESOURCE_NOTIFICATION_TYPE(CEnum):
    LowMemoryResourceNotification = 0
    HighMemoryResourceNotification = 1


CreateMemoryResourceNotification = windll.kernel32.CreateMemoryResourceNotification
CreateMemoryResourceNotification.argtypes = [MEMORY_RESOURCE_NOTIFICATION_TYPE]
CreateMemoryResourceNotification.restype = HANDLE

QueryMemoryResourceNotification = windll.kernel32.QueryMemoryResourceNotification
QueryMemoryResourceNotification.argtypes = [HANDLE, PBOOL]
QueryMemoryResourceNotification.restype = BOOL

FILE_CACHE_MAX_HARD_ENABLE = 0x00000001
FILE_CACHE_MAX_HARD_DISABLE = 0x00000002
FILE_CACHE_MIN_HARD_ENABLE = 0x00000004
FILE_CACHE_MIN_HARD_DISABLE = 0x00000008

GetSystemFileCacheSize = windll.kernel32.GetSystemFileCacheSize
GetSystemFileCacheSize.argtypes = [POINTER(SIZE_T), POINTER(SIZE_T), PDWORD]
GetSystemFileCacheSize.restype = BOOL

SetSystemFileCacheSize = windll.kernel32.SetSystemFileCacheSize
SetSystemFileCacheSize.argtypes = [SIZE_T, SIZE_T, DWORD]
SetSystemFileCacheSize.restype = BOOL

CreateFileMappingNumaW = windll.kernel32.CreateFileMappingNumaW
CreateFileMappingNumaW.argtypes = [HANDLE, POINTER(SECURITY_ATTRIBUTES), DWORD, DWORD, DWORD, LPCWSTR, DWORD]
CreateFileMappingNumaW.restype = HANDLE


class WIN32_MEMORY_RANGE_ENTRY(Structure):
    _fields_ = [
        ("VirtualAddress", PVOID),
        ("NumberOfBytes", SIZE_T),
    ]


PrefetchVirtualMemory = windll.kernel32.PrefetchVirtualMemory
PrefetchVirtualMemory.argtypes = [HANDLE, ULONG_PTR, POINTER(WIN32_MEMORY_RANGE_ENTRY), ULONG]
PrefetchVirtualMemory.restype = BOOL

# VirtualAllocFromApp = windll.kernel32.VirtualAllocFromApp
# VirtualAllocFromApp.argtypes = [PVOID, SIZE_T, ULONG, ULONG]
# VirtualAllocFromApp.restype = PVOID

# VirtualProtectFromApp = windll.kernel32.VirtualProtectFromApp
# VirtualProtectFromApp.argtypes = [PVOID, SIZE_T, ULONG, PULONG]
# VirtualProtectFromApp.restype = BOOL

# OpenFileMappingFromApp = windll.kernel32.OpenFileMappingFromApp
# OpenFileMappingFromApp.argtypes = [ULONG, BOOL, PCWSTR]
# OpenFileMappingFromApp.restype = HANDLE


VirtualAlloc = windll.kernel32.VirtualAlloc
VirtualAlloc.argtypes = [LPVOID, SIZE_T, DWORD, DWORD]
VirtualAlloc.restype = LPVOID

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = [LPVOID, SIZE_T, DWORD, PDWORD]
VirtualProtect.restype = BOOL

OpenFileMappingW = windll.kernel32.OpenFileMappingW
OpenFileMappingW.argtypes = [DWORD, BOOL, LPCWSTR]
OpenFileMappingW.restype = HANDLE
