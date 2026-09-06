"""ctypes bindings for process and thread processor-group affinity."""

from ctypes import POINTER
from ctypes.wintypes import BOOL, HANDLE, PUSHORT

from .. import nonzero, windll
from .winnt import GROUP_AFFINITY, PGROUP_AFFINITY

GetProcessGroupAffinity = windll.kernel32.GetProcessGroupAffinity
GetProcessGroupAffinity.argtypes = [HANDLE, PUSHORT, PUSHORT]
GetProcessGroupAffinity.restype = BOOL
GetProcessGroupAffinity.errcheck = nonzero

GetThreadGroupAffinity = windll.kernel32.GetThreadGroupAffinity
GetThreadGroupAffinity.argtypes = [HANDLE, PGROUP_AFFINITY]
GetThreadGroupAffinity.restype = BOOL
GetThreadGroupAffinity.errcheck = nonzero

SetThreadGroupAffinity = windll.kernel32.SetThreadGroupAffinity
SetThreadGroupAffinity.argtypes = [HANDLE, POINTER(GROUP_AFFINITY), PGROUP_AFFINITY]
SetThreadGroupAffinity.restype = BOOL
SetThreadGroupAffinity.errcheck = nonzero
