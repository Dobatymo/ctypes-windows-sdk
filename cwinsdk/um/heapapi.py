"""ctypes bindings for the Windows heap API."""

import ctypes
from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPVOID

from .. import nonzero, windll
from ..shared.basetsd import PSIZE_T, SIZE_T
from ..shared.minwindef import LPCVOID
from ..shared.ntdef import PVOID
from .minwinbase import LPPROCESS_HEAP_ENTRY
from .winnt import HEAP_INFORMATION_CLASS, PHANDLE


class HEAP_SUMMARY(ctypes.Structure):
    _fields_ = [
        ("cb", DWORD),
        ("cbAllocated", SIZE_T),
        ("cbCommitted", SIZE_T),
        ("cbReserved", SIZE_T),
        ("cbMaxReserve", SIZE_T),
    ]


PHEAP_SUMMARY = POINTER(HEAP_SUMMARY)
LPHEAP_SUMMARY = PHEAP_SUMMARY


HeapCreate = windll.kernel32.HeapCreate
HeapCreate.argtypes = [DWORD, SIZE_T, SIZE_T]
HeapCreate.restype = HANDLE

HeapDestroy = windll.kernel32.HeapDestroy
HeapDestroy.argtypes = [HANDLE]
HeapDestroy.restype = BOOL
HeapDestroy.errcheck = nonzero

HeapAlloc = windll.kernel32.HeapAlloc
HeapAlloc.argtypes = [HANDLE, DWORD, SIZE_T]
HeapAlloc.restype = LPVOID

HeapReAlloc = windll.kernel32.HeapReAlloc
HeapReAlloc.argtypes = [HANDLE, DWORD, LPVOID, SIZE_T]
HeapReAlloc.restype = LPVOID

HeapFree = windll.kernel32.HeapFree
HeapFree.argtypes = [HANDLE, DWORD, LPVOID]
HeapFree.restype = BOOL
HeapFree.errcheck = nonzero

HeapSize = windll.kernel32.HeapSize
HeapSize.argtypes = [HANDLE, DWORD, LPCVOID]
HeapSize.restype = SIZE_T

GetProcessHeap = windll.kernel32.GetProcessHeap
GetProcessHeap.argtypes = []
GetProcessHeap.restype = HANDLE

HeapCompact = windll.kernel32.HeapCompact
HeapCompact.argtypes = [HANDLE, DWORD]
HeapCompact.restype = SIZE_T

HeapSetInformation = windll.kernel32.HeapSetInformation
HeapSetInformation.argtypes = [HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T]
HeapSetInformation.restype = BOOL
HeapSetInformation.errcheck = nonzero

HeapValidate = windll.kernel32.HeapValidate
HeapValidate.argtypes = [HANDLE, DWORD, LPCVOID]
HeapValidate.restype = BOOL

HeapSummary = windll.kernel32.HeapSummary
HeapSummary.argtypes = [HANDLE, DWORD, LPHEAP_SUMMARY]
HeapSummary.restype = BOOL
HeapSummary.errcheck = nonzero

GetProcessHeaps = windll.kernel32.GetProcessHeaps
GetProcessHeaps.argtypes = [DWORD, PHANDLE]
GetProcessHeaps.restype = DWORD

HeapLock = windll.kernel32.HeapLock
HeapLock.argtypes = [HANDLE]
HeapLock.restype = BOOL
HeapLock.errcheck = nonzero

HeapUnlock = windll.kernel32.HeapUnlock
HeapUnlock.argtypes = [HANDLE]
HeapUnlock.restype = BOOL
HeapUnlock.errcheck = nonzero

HeapWalk = windll.kernel32.HeapWalk
HeapWalk.argtypes = [HANDLE, LPPROCESS_HEAP_ENTRY]
HeapWalk.restype = BOOL
HeapWalk.errcheck = nonzero

HeapQueryInformation = windll.kernel32.HeapQueryInformation
HeapQueryInformation.argtypes = [HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T, PSIZE_T]
HeapQueryInformation.restype = BOOL
HeapQueryInformation.errcheck = nonzero
