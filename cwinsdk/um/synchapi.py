from ctypes.wintypes import BOOL, HANDLE, LPCSTR, LPCWSTR

from .. import nonnull, nonzero, windll
from .minwinbase import LPSECURITY_ATTRIBUTES

CreateEventA = windll.kernel32.CreateEventA
CreateEventA.argtypes = [LPSECURITY_ATTRIBUTES, BOOL, BOOL, LPCSTR]
CreateEventA.restype = HANDLE
CreateEventA.errcheck = nonnull

CreateEventW = windll.kernel32.CreateEventW
CreateEventW.argtypes = [LPSECURITY_ATTRIBUTES, BOOL, BOOL, LPCWSTR]
CreateEventW.restype = HANDLE
CreateEventW.errcheck = nonnull

ResetEvent = windll.kernel32.ResetEvent
ResetEvent.argtypes = [HANDLE]
ResetEvent.restype = BOOL
ResetEvent.errcheck = nonzero
