from ctypes import POINTER, Structure, Union
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPVOID, WORD

from .. import CEnum, windll
from ..shared.basetsd import ULONG_PTR
from ..shared.ntdef import PVOID


class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", LPVOID),
        ("bInheritHandle", BOOL),
    ]


LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)


class OVERLAPPED_STRUCT(Structure):
    _fields_ = [
        ("Offset", DWORD),
        ("OffsetHigh", DWORD),
    ]


class OVERLAPPED_UNION(Union):
    _anonymous_ = ("u",)
    _fields_ = [
        ("u", OVERLAPPED_STRUCT),
        ("Pointer", PVOID),
    ]


class OVERLAPPED(Structure):
    _anonymous_ = ("u",)
    _fields_ = [
        ("Internal", ULONG_PTR),
        ("InternalHigh", ULONG_PTR),
        ("u", OVERLAPPED_UNION),
        ("hEvent", HANDLE),
    ]


LPOVERLAPPED = POINTER(OVERLAPPED)


class OVERLAPPED_ENTRY(Structure):
    _fields_ = [
        ("lpCompletionKey", ULONG_PTR),
        ("lpOverlapped", LPOVERLAPPED),
        ("dwNumberOfBytesTransferred", ULONG_PTR),
        ("hEvent", DWORD),
    ]


LPOVERLAPPED_ENTRY = POINTER(OVERLAPPED_ENTRY)


class FILETIME(Structure):
    _fields_ = [
        ("dwLowDateTime", DWORD),
        ("dwHighDateTime", DWORD),
    ]


LPFILETIME = POINTER(FILETIME)


class SYSTEMTIME(Structure):
    _fields_ = [
        ("wYear", WORD),
        ("wMonth", WORD),
        ("wDayOfWeek", WORD),
        ("wDay", WORD),
        ("wHour", WORD),
        ("wMinute", WORD),
        ("wSecond", WORD),
        ("wMilliseconds", WORD),
    ]


LPSYSTEMTIME = POINTER(SYSTEMTIME)


class FILE_INFO_BY_HANDLE_CLASS(CEnum):
    FileBasicInfo = 0
    FileStandardInfo = 1
    FileNameInfo = 2
    FileRenameInfo = 3
    FileDispositionInfo = 4
    FileAllocationInfo = 5
    FileEndOfFileInfo = 6
    FileStreamInfo = 7
    FileCompressionInfo = 8
    FileAttributeTagInfo = 9
    FileIdBothDirectoryInfo = 10
    FileIdBothDirectoryRestartInfo = 11
    FileIoPriorityHintInfo = 12
    FileRemoteProtocolInfo = 13
    FileFullDirectoryInfo = 14
    FileFullDirectoryRestartInfo = 15
    FileStorageInfo = 16
    FileAlignmentInfo = 17
    FileIdInfo = 18
    FileIdExtdDirectoryInfo = 19
    FileIdExtdDirectoryRestartInfo = 20
    FileDispositionInfoEx = 21
    FileRenameInfoEx = 22
    MaximumFileInfoByHandleClass = 23


class GET_FILEEX_INFO_LEVELS(CEnum):
    GetFileExInfoStandard = 0
    GetFileExMaxInfoLevel = 1


LOCKFILE_FAIL_IMMEDIATELY = 0x00000001
LOCKFILE_EXCLUSIVE_LOCK = 0x00000002
