from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import POINTER
from ctypes.wintypes import LPVOID, BOOL, HANDLE, DWORD, ULONG

from .. import windll, _not_available
from ..shared.basetsd import ULONG_PTR, PULONG_PTR
from ..shared.minwindef import PULONG, LPDWORD
from .minwinbase import LPOVERLAPPED, LPOVERLAPPED_ENTRY

CreateIoCompletionPort = windll.kernel32.CreateIoCompletionPort
CreateIoCompletionPort.argtypes = [HANDLE, HANDLE, ULONG_PTR, DWORD]
CreateIoCompletionPort.restype = HANDLE 
 
GetQueuedCompletionStatus = windll.kernel32.GetQueuedCompletionStatus
GetQueuedCompletionStatus.argtypes = [HANDLE, LPDWORD, PULONG_PTR, POINTER(LPOVERLAPPED), DWORD]
GetQueuedCompletionStatus.restype = BOOL 

GetQueuedCompletionStatusEx = windll.kernel32.GetQueuedCompletionStatusEx
GetQueuedCompletionStatusEx.argtypes = [HANDLE, LPOVERLAPPED_ENTRY, ULONG, PULONG, DWORD, BOOL]
GetQueuedCompletionStatusEx.restype = BOOL 
 
PostQueuedCompletionStatus = windll.kernel32.PostQueuedCompletionStatus
PostQueuedCompletionStatus.argtypes = [HANDLE, DWORD, ULONG_PTR, LPOVERLAPPED]
PostQueuedCompletionStatus.restype = BOOL 
 
DeviceIoControl = windll.kernel32.DeviceIoControl
DeviceIoControl.argtypes = [HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
DeviceIoControl.restype = BOOL 

GetOverlappedResult = windll.kernel32.GetOverlappedResult
GetOverlappedResult.argtypes = [HANDLE, LPOVERLAPPED, LPDWORD, BOOL]
GetOverlappedResult.restype = BOOL 

CancelIoEx = windll.kernel32.CancelIoEx
CancelIoEx.argtypes = [HANDLE, LPOVERLAPPED]
CancelIoEx.restype = BOOL 

CancelIo = windll.kernel32.CancelIo
CancelIo.argtypes = [HANDLE]
CancelIo.restype = BOOL 

try: # only windows 8+
	GetOverlappedResultEx = windll.kernel32.GetOverlappedResultEx
	GetOverlappedResultEx.argtypes = [HANDLE, LPOVERLAPPED, LPDWORD, DWORD, BOOL]
	GetOverlappedResultEx.restype = BOOL 
except AttributeError:
	GetOverlappedResultEx = _not_available("GetOverlappedResultEx")

CancelSynchronousIo = windll.kernel32.CancelSynchronousIo
CancelSynchronousIo.argtypes = [HANDLE]
CancelSynchronousIo.restype = BOOL 
