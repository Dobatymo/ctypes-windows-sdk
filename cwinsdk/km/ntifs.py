from ctypes import POINTER
from ctypes.wintypes import CHAR, HANDLE, ULONG

from .. import status_success, windll
from ..shared.ntdef import NTSTATUS, PVOID
from .wdm import FS_INFORMATION_CLASS, IO_STATUS_BLOCK

RtlQueryThreadPlaceholderCompatibilityMode = windll.ntdll.RtlQueryThreadPlaceholderCompatibilityMode
RtlQueryThreadPlaceholderCompatibilityMode.argtypes = []
RtlQueryThreadPlaceholderCompatibilityMode.restype = CHAR

RtlSetThreadPlaceholderCompatibilityMode = windll.ntdll.RtlSetThreadPlaceholderCompatibilityMode
RtlSetThreadPlaceholderCompatibilityMode.argtypes = [CHAR]
RtlSetThreadPlaceholderCompatibilityMode.restype = CHAR

RtlQueryProcessPlaceholderCompatibilityMode = windll.ntdll.RtlQueryProcessPlaceholderCompatibilityMode
RtlQueryProcessPlaceholderCompatibilityMode.argtypes = []
RtlQueryProcessPlaceholderCompatibilityMode.restype = CHAR

RtlSetProcessPlaceholderCompatibilityMode = windll.ntdll.RtlSetProcessPlaceholderCompatibilityMode
RtlSetProcessPlaceholderCompatibilityMode.argtypes = [CHAR]
RtlSetProcessPlaceholderCompatibilityMode.restype = CHAR

NtQueryVolumeInformationFile = windll.ntdll.NtQueryVolumeInformationFile
NtQueryVolumeInformationFile.argtypes = [HANDLE, POINTER(IO_STATUS_BLOCK), PVOID, ULONG, FS_INFORMATION_CLASS]
NtQueryVolumeInformationFile.restype = NTSTATUS
NtQueryVolumeInformationFile.errcheck = status_success

RtlNtStatusToDosError = windll.ntdll.RtlNtStatusToDosError
RtlNtStatusToDosError.argtypes = [NTSTATUS]
RtlNtStatusToDosError.restype = ULONG
