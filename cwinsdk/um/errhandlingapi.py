"""ctypes bindings for the Windows error-handling API."""

from ctypes import POINTER, WINFUNCTYPE
from ctypes.wintypes import BOOL, DWORD, LONG, LPCSTR, LPCWSTR, LPDWORD, LPVOID, UINT, ULONG

from .. import nonzero, windll
from ..shared.basetsd import SIZE_T, ULONG_PTR
from ..um.winnt import EXCEPTION_POINTERS, PCONTEXT, PEXCEPTION_RECORD, PVECTORED_EXCEPTION_HANDLER

PTOP_LEVEL_EXCEPTION_FILTER = WINFUNCTYPE(LONG, POINTER(EXCEPTION_POINTERS))
LPTOP_LEVEL_EXCEPTION_FILTER = PTOP_LEVEL_EXCEPTION_FILTER


RaiseException = windll.kernel32.RaiseException
RaiseException.argtypes = [DWORD, DWORD, DWORD, POINTER(ULONG_PTR)]
RaiseException.restype = None

UnhandledExceptionFilter = windll.kernel32.UnhandledExceptionFilter
UnhandledExceptionFilter.argtypes = [POINTER(EXCEPTION_POINTERS)]
UnhandledExceptionFilter.restype = LONG

SetUnhandledExceptionFilter = windll.kernel32.SetUnhandledExceptionFilter
SetUnhandledExceptionFilter.argtypes = [LPTOP_LEVEL_EXCEPTION_FILTER]
SetUnhandledExceptionFilter.restype = LPTOP_LEVEL_EXCEPTION_FILTER

GetLastError = windll.kernel32.GetLastError
GetLastError.argtypes = []
GetLastError.restype = DWORD

SetLastError = windll.kernel32.SetLastError
SetLastError.argtypes = [DWORD]
SetLastError.restype = None

RestoreLastError = windll.kernel32.RestoreLastError
RestoreLastError.argtypes = [DWORD]
RestoreLastError.restype = None

GetErrorMode = windll.kernel32.GetErrorMode
GetErrorMode.argtypes = []
GetErrorMode.restype = UINT

SetErrorMode = windll.kernel32.SetErrorMode
SetErrorMode.argtypes = [UINT]
SetErrorMode.restype = UINT

AddVectoredExceptionHandler = windll.kernel32.AddVectoredExceptionHandler
AddVectoredExceptionHandler.argtypes = [ULONG, PVECTORED_EXCEPTION_HANDLER]
AddVectoredExceptionHandler.restype = LPVOID

RemoveVectoredExceptionHandler = windll.kernel32.RemoveVectoredExceptionHandler
RemoveVectoredExceptionHandler.argtypes = [LPVOID]
RemoveVectoredExceptionHandler.restype = ULONG

AddVectoredContinueHandler = windll.kernel32.AddVectoredContinueHandler
AddVectoredContinueHandler.argtypes = [ULONG, PVECTORED_EXCEPTION_HANDLER]
AddVectoredContinueHandler.restype = LPVOID

RemoveVectoredContinueHandler = windll.kernel32.RemoveVectoredContinueHandler
RemoveVectoredContinueHandler.argtypes = [LPVOID]
RemoveVectoredContinueHandler.restype = ULONG

RaiseFailFastException = windll.kernel32.RaiseFailFastException
RaiseFailFastException.argtypes = [PEXCEPTION_RECORD, PCONTEXT, DWORD]
RaiseFailFastException.restype = None

FatalAppExitA = windll.kernel32.FatalAppExitA
FatalAppExitA.argtypes = [UINT, LPCSTR]
FatalAppExitA.restype = None

FatalAppExitW = windll.kernel32.FatalAppExitW
FatalAppExitW.argtypes = [UINT, LPCWSTR]
FatalAppExitW.restype = None

GetThreadErrorMode = windll.kernel32.GetThreadErrorMode
GetThreadErrorMode.argtypes = []
GetThreadErrorMode.restype = DWORD

SetThreadErrorMode = windll.kernel32.SetThreadErrorMode
SetThreadErrorMode.argtypes = [DWORD, LPDWORD]
SetThreadErrorMode.restype = BOOL
SetThreadErrorMode.errcheck = nonzero
TerminateProcessOnMemoryExhaustion = windll.kernelbase.TerminateProcessOnMemoryExhaustion
TerminateProcessOnMemoryExhaustion.argtypes = [SIZE_T]
TerminateProcessOnMemoryExhaustion.restype = None
