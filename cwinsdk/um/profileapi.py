"""ctypes bindings for Windows performance counters."""

from ctypes import POINTER
from ctypes.wintypes import BOOL

from .. import nonzero, windll
from .winnt import LARGE_INTEGER

QueryPerformanceCounter = windll.kernel32.QueryPerformanceCounter
QueryPerformanceCounter.argtypes = [POINTER(LARGE_INTEGER)]
QueryPerformanceCounter.restype = BOOL
QueryPerformanceCounter.errcheck = nonzero

QueryPerformanceFrequency = windll.kernel32.QueryPerformanceFrequency
QueryPerformanceFrequency.argtypes = [POINTER(LARGE_INTEGER)]
QueryPerformanceFrequency.restype = BOOL
QueryPerformanceFrequency.errcheck = nonzero
