from ctypes import POINTER, Structure
from ctypes.wintypes import BOOL, DWORD, HANDLE, LONG, LPCSTR, LPCWSTR, LPSTR, LPVOID, LPWSTR, UINT, ULARGE_INTEGER

from .. import CEnum, nonzero, validhandle, windll
from ..shared.minwindef import FILETIME, PDWORD
from ..shared.ntdef import LPWCH, PWSTR, ULONGLONG
from .minwinbase import FILE_INFO_BY_HANDLE_CLASS, GET_FILEEX_INFO_LEVELS, LPOVERLAPPED, LPSECURITY_ATTRIBUTES

CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

INVALID_FILE_SIZE = 0xFFFFFFFF
INVALID_SET_FILE_POINTER = DWORD(-1)
INVALID_FILE_ATTRIBUTES = DWORD(-1)


class BY_HANDLE_FILE_INFORMATION(Structure):
    _fields_ = [
        ("dwFileAttributes", DWORD),
        ("ftCreationTime", FILETIME),
        ("ftLastAccessTime", FILETIME),
        ("ftLastWriteTime", FILETIME),
        ("dwVolumeSerialNumber", DWORD),
        ("nFileSizeHigh", DWORD),
        ("nFileSizeLow", DWORD),
        ("nNumberOfLinks", DWORD),
        ("nFileIndexHigh", DWORD),
        ("nFileIndexLow", DWORD),
    ]


class DISK_SPACE_INFORMATION(Structure):
    _fields_ = [
        ("ActualTotalAllocationUnits", ULONGLONG),
        ("ActualAvailableAllocationUnits", ULONGLONG),
        ("ActualPoolUnavailableAllocationUnits", ULONGLONG),
        ("CallerTotalAllocationUnits", ULONGLONG),
        ("CallerAvailableAllocationUnits", ULONGLONG),
        ("CallerPoolUnavailableAllocationUnits", ULONGLONG),
        ("UsedAllocationUnits", ULONGLONG),
        ("TotalReservedAllocationUnits", ULONGLONG),
        ("VolumeStorageReserveAllocationUnits", ULONGLONG),
        ("AvailableCommittedAllocationUnits", ULONGLONG),
        ("PoolAvailableAllocationUnits", ULONGLONG),
        ("SectorsPerAllocationUnit", DWORD),
        ("BytesPerSector", DWORD),
    ]


class STREAM_INFO_LEVELS(CEnum):
    FindStreamInfoStandard = 0
    FindStreamInfoMaxInfoLevel = 1


# functions

AreFileApisANSI = windll.kernel32.AreFileApisANSI
AreFileApisANSI.argtypes = []
AreFileApisANSI.restype = BOOL

CompareFileTime = windll.kernel32.CompareFileTime
CompareFileTime.argtypes = [POINTER(FILETIME), POINTER(FILETIME)]
CompareFileTime.restype = LONG

CreateDirectoryA = windll.kernel32.CreateDirectoryA
CreateDirectoryA.argtypes = [LPCSTR, LPSECURITY_ATTRIBUTES]
CreateDirectoryA.restype = BOOL

CreateDirectoryW = windll.kernel32.CreateDirectoryW
CreateDirectoryW.argtypes = [LPCWSTR, LPSECURITY_ATTRIBUTES]
CreateDirectoryW.restype = BOOL

CreateFileA = windll.kernel32.CreateFileA
CreateFileA.argtypes = [LPCSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE]
CreateFileA.restype = HANDLE

CreateFileW = windll.kernel32.CreateFileW
CreateFileW.argtypes = [LPCWSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE]
CreateFileW.restype = HANDLE
CreateFileW.errcheck = validhandle

GetCompressedFileSizeA = windll.kernel32.GetCompressedFileSizeA
GetCompressedFileSizeA.argtypes = [LPCSTR, POINTER(DWORD)]
GetCompressedFileSizeA.restype = DWORD

GetCompressedFileSizeW = windll.kernel32.GetCompressedFileSizeW
GetCompressedFileSizeW.argtypes = [LPCWSTR, POINTER(DWORD)]
GetCompressedFileSizeW.restype = DWORD

GetDiskFreeSpaceExW = windll.kernel32.GetDiskFreeSpaceExW
GetDiskFreeSpaceExW.argtypes = [LPCWSTR, POINTER(ULARGE_INTEGER), POINTER(ULARGE_INTEGER), POINTER(ULARGE_INTEGER)]
GetDiskFreeSpaceExW.restype = BOOL

GetDriveTypeA = windll.kernel32.GetDriveTypeA
GetDriveTypeA.argtypes = [LPCSTR]
GetDriveTypeA.restype = UINT

GetDriveTypeW = windll.kernel32.GetDriveTypeW
GetDriveTypeW.argtypes = [LPCWSTR]
GetDriveTypeW.restype = UINT

GetFileAttributesA = windll.kernel32.GetFileAttributesA
GetFileAttributesA.argtypes = [LPCSTR]
GetFileAttributesA.restype = DWORD

GetFileAttributesExA = windll.kernel32.GetFileAttributesExA
GetFileAttributesExA.argtypes = [LPCSTR, GET_FILEEX_INFO_LEVELS, LPVOID]
GetFileAttributesExA.restype = BOOL

GetFileAttributesExW = windll.kernel32.GetFileAttributesExW
GetFileAttributesExW.argtypes = [LPCWSTR, GET_FILEEX_INFO_LEVELS, LPVOID]
GetFileAttributesExW.restype = BOOL

GetFileAttributesW = windll.kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [LPCWSTR]
GetFileAttributesW.restype = DWORD

GetFileInformationByHandle = windll.kernel32.GetFileInformationByHandle
GetFileInformationByHandle.argtypes = [HANDLE, POINTER(BY_HANDLE_FILE_INFORMATION)]
GetFileInformationByHandle.restype = BOOL
GetFileInformationByHandle.errcheck = nonzero

SetFileInformationByHandle = windll.kernel32.SetFileInformationByHandle
SetFileInformationByHandle.argtypes = [HANDLE, FILE_INFO_BY_HANDLE_CLASS, LPVOID, DWORD]
SetFileInformationByHandle.restype = BOOL
SetFileInformationByHandle.errcheck = nonzero

GetFileType = windll.kernel32.GetFileType
GetFileType.argtypes = [HANDLE]
GetFileType.restype = DWORD

GetVolumeInformationW = windll.kernel32.GetVolumeInformationW
GetVolumeInformationW.argtypes = [LPCWSTR, LPWSTR, DWORD, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD), LPWSTR, DWORD]
GetVolumeInformationW.restype = BOOL
GetVolumeInformationW.errcheck = nonzero

LockFile = windll.kernel32.LockFile
LockFile.argtypes = [HANDLE, DWORD, DWORD, DWORD, DWORD]
LockFile.restype = BOOL

LockFileEx = windll.kernel32.LockFileEx
LockFileEx.argtypes = [HANDLE, DWORD, DWORD, DWORD, DWORD, LPOVERLAPPED]
LockFileEx.restype = BOOL
LockFileEx.errcheck = nonzero

UnlockFile = windll.kernel32.UnlockFile
UnlockFile.argtypes = [HANDLE, DWORD, DWORD, DWORD, DWORD]
UnlockFile.restype = BOOL

UnlockFileEx = windll.kernel32.UnlockFileEx
UnlockFileEx.argtypes = [HANDLE, DWORD, DWORD, DWORD, LPOVERLAPPED]
UnlockFileEx.restype = BOOL
UnlockFileEx.errcheck = nonzero

GetVolumeNameForVolumeMountPointW = windll.kernel32.GetVolumeNameForVolumeMountPointW
GetVolumeNameForVolumeMountPointW.argtypes = [LPCWSTR, LPWSTR, DWORD]
GetVolumeNameForVolumeMountPointW.restype = BOOL
GetVolumeNameForVolumeMountPointW.errcheck = nonzero

GetFinalPathNameByHandleA = windll.kernel32.GetFinalPathNameByHandleA
GetFinalPathNameByHandleA.argtypes = [HANDLE, LPSTR, DWORD, DWORD]
GetFinalPathNameByHandleA.restype = DWORD

GetFinalPathNameByHandleW = windll.kernel32.GetFinalPathNameByHandleW
GetFinalPathNameByHandleW.argtypes = [HANDLE, LPWSTR, DWORD, DWORD]
GetFinalPathNameByHandleW.restype = DWORD

GetLogicalDrives = windll.kernel32.GetLogicalDrives
GetLogicalDrives.argtypes = []
GetLogicalDrives.restype = DWORD

GetLogicalDriveStringsW = windll.kernel32.GetLogicalDriveStringsW
GetLogicalDriveStringsW.argtypes = [DWORD, LPWSTR]
GetLogicalDriveStringsW.restype = DWORD
GetLogicalDriveStringsW.errcheck = nonzero

FindFirstStreamW = windll.kernel32.FindFirstStreamW
FindFirstStreamW.argtypes = [LPCWSTR, STREAM_INFO_LEVELS, LPVOID, DWORD]
FindFirstStreamW.restype = HANDLE
FindFirstStreamW.errcheck = validhandle

FindNextStreamW = windll.kernel32.FindNextStreamW
FindNextStreamW.argtypes = [HANDLE, LPVOID]
FindNextStreamW.restype = BOOL
FindNextStreamW.errcheck = nonzero

GetTempPathA = windll.kernel32.GetTempPathA
GetTempPathA.argtypes = [DWORD, LPSTR]
GetTempPathA.restype = DWORD

FindFirstFileNameW = windll.kernel32.FindFirstFileNameW
FindFirstFileNameW.argtypes = [LPCWSTR, DWORD, POINTER(DWORD), PWSTR]
FindFirstFileNameW.restype = HANDLE
FindFirstFileNameW.errcheck = validhandle

FindNextFileNameW = windll.kernel32.FindNextFileNameW
FindNextFileNameW.argtypes = [HANDLE, POINTER(DWORD), PWSTR]
FindNextFileNameW.restype = BOOL
FindNextFileNameW.errcheck = nonzero

GetVolumeInformationA = windll.kernel32.GetVolumeInformationA
GetVolumeInformationA.argtypes = [LPCSTR, LPSTR, DWORD, POINTER(DWORD), POINTER(DWORD), POINTER(DWORD), LPSTR, DWORD]
GetVolumeInformationA.restype = BOOL

GetTempFileNameA = windll.kernel32.GetTempFileNameA
GetTempFileNameA.argtypes = [LPCSTR, LPCSTR, UINT, LPSTR]
GetTempFileNameA.restype = UINT

SetFileApisToOEM = windll.kernel32.SetFileApisToOEM
SetFileApisToOEM.argtypes = []
SetFileApisToOEM.restype = None

SetFileApisToANSI = windll.kernel32.SetFileApisToANSI
SetFileApisToANSI.argtypes = []
SetFileApisToANSI.restype = None

GetTempPath2W = windll.kernel32.GetTempPath2W
GetTempPath2W.argtypes = [DWORD, LPWSTR]
GetTempPath2W.restype = DWORD

GetTempPath2A = windll.kernel32.GetTempPath2A
GetTempPath2A.argtypes = [DWORD, LPSTR]
GetTempPath2A.restype = DWORD

QueryDosDeviceW = windll.kernel32.QueryDosDeviceW
QueryDosDeviceW.argtypes = [LPCWSTR, LPWSTR, DWORD]
QueryDosDeviceW.restype = DWORD
QueryDosDeviceW.errcheck = nonzero

FindFirstVolumeW = windll.kernel32.FindFirstVolumeW
FindFirstVolumeW.argtypes = [LPWSTR, DWORD]
FindFirstVolumeW.restype = HANDLE
FindFirstVolumeW.errcheck = validhandle

FindNextVolumeW = windll.kernel32.FindNextVolumeW
FindNextVolumeW.argtypes = [HANDLE, LPWSTR, DWORD]
FindNextVolumeW.restype = BOOL
FindNextVolumeW.errcheck = nonzero

FindVolumeClose = windll.kernel32.FindVolumeClose
FindVolumeClose.argtypes = [HANDLE]
FindVolumeClose.restype = BOOL
FindVolumeClose.errcheck = nonzero

GetVolumePathNamesForVolumeNameW = windll.kernel32.GetVolumePathNamesForVolumeNameW
GetVolumePathNamesForVolumeNameW.argtypes = [LPCWSTR, LPWCH, DWORD, PDWORD]
GetVolumePathNamesForVolumeNameW.restype = BOOL
GetVolumePathNamesForVolumeNameW.errcheck = nonzero
