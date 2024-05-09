from ctypes import POINTER, Structure, Union, c_char
from ctypes.wintypes import WCHAR  # CHAR not in py2
from ctypes.wintypes import (
    BOOL,
    BYTE,
    DWORD,
    HANDLE,
    LARGE_INTEGER,
    LPCSTR,
    LPCWSTR,
    LPSTR,
    LPVOID,
    LPWSTR,
    ULONG,
    WORD,
)

from .. import CEnum, nonzero, validhandle, windll
from ..km.wdm import SECURITY_IMPERSONATION_LEVEL
from ..shared.basetsd import SIZE_T, ULONG64
from ..shared.guiddef import GUID
from ..shared.minwindef import ATOM, PDWORD
from ..shared.ntdef import CHAR, ULONGLONG
from .minwinbase import FILE_INFO_BY_HANDLE_CLASS, LPSECURITY_ATTRIBUTES
from .winnt import (
    FILE_CASE_PRESERVED_NAMES,
    FILE_CASE_SENSITIVE_SEARCH,
    FILE_FILE_COMPRESSION,
    FILE_ID_128,
    FILE_PERSISTENT_ACLS,
    FILE_SUPPORTS_ENCRYPTION,
    FILE_UNICODE_ON_DISK,
    FILE_VOLUME_IS_COMPRESSED,
    LPCH,
    LUID,
    MAXLONG,
    STATUS_ABANDONED_WAIT_0,
    STATUS_USER_APC,
    STATUS_WAIT_0,
    THREAD_BASE_PRIORITY_IDLE,
    THREAD_BASE_PRIORITY_LOWRT,
    THREAD_BASE_PRIORITY_MAX,
    THREAD_BASE_PRIORITY_MIN,
)

FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_END = 2

WAIT_FAILED = 0xFFFFFFFF
WAIT_OBJECT_0 = STATUS_WAIT_0 + 0

WAIT_ABANDONED = STATUS_ABANDONED_WAIT_0 + 0
WAIT_ABANDONED_0 = STATUS_ABANDONED_WAIT_0 + 0

WAIT_IO_COMPLETION = STATUS_USER_APC

FILE_FLAG_WRITE_THROUGH = 0x80000000
FILE_FLAG_OVERLAPPED = 0x40000000
FILE_FLAG_NO_BUFFERING = 0x20000000
FILE_FLAG_RANDOM_ACCESS = 0x10000000
FILE_FLAG_SEQUENTIAL_SCAN = 0x08000000
FILE_FLAG_DELETE_ON_CLOSE = 0x04000000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
FILE_FLAG_POSIX_SEMANTICS = 0x01000000
FILE_FLAG_SESSION_AWARE = 0x00800000
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_OPEN_NO_RECALL = 0x00100000
FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000

FILE_FLAG_OPEN_REQUIRING_OPLOCK = 0x00040000

PROGRESS_CONTINUE = 0
PROGRESS_CANCEL = 1
PROGRESS_STOP = 2
PROGRESS_QUIET = 3

CALLBACK_CHUNK_FINISHED = 0x00000000
CALLBACK_STREAM_SWITCH = 0x00000001

COPY_FILE_FAIL_IF_EXISTS = 0x00000001
COPY_FILE_RESTARTABLE = 0x00000002
COPY_FILE_OPEN_SOURCE_FOR_WRITE = 0x00000004
COPY_FILE_ALLOW_DECRYPTED_DESTINATION = 0x00000008
COPY_FILE_COPY_SYMLINK = 0x00000800
COPY_FILE_NO_BUFFERING = 0x00001000
COPY_FILE_REQUEST_SECURITY_PRIVILEGES = 0x00002000
COPY_FILE_RESUME_FROM_PAUSE = 0x00004000
COPY_FILE_NO_OFFLOAD = 0x00040000
COPY_FILE_IGNORE_EDP_BLOCK = 0x00400000
COPY_FILE_IGNORE_SOURCE_ENCRYPTION = 0x00800000

REPLACEFILE_WRITE_THROUGH = 0x00000001
REPLACEFILE_IGNORE_MERGE_ERRORS = 0x00000002
REPLACEFILE_IGNORE_ACL_ERRORS = 0x00000004

PIPE_ACCESS_INBOUND = 0x00000001
PIPE_ACCESS_OUTBOUND = 0x00000002
PIPE_ACCESS_DUPLEX = 0x00000003
PIPE_CLIENT_END = 0x00000000
PIPE_SERVER_END = 0x00000001
PIPE_WAIT = 0x00000000
PIPE_NOWAIT = 0x00000001
PIPE_READMODE_BYTE = 0x00000000
PIPE_READMODE_MESSAGE = 0x00000002
PIPE_TYPE_BYTE = 0x00000000
PIPE_TYPE_MESSAGE = 0x00000004
PIPE_ACCEPT_REMOTE_CLIENTS = 0x00000000
PIPE_REJECT_REMOTE_CLIENTS = 0x00000008
PIPE_UNLIMITED_INSTANCES = 255

SECURITY_ANONYMOUS = SECURITY_IMPERSONATION_LEVEL.SecurityAnonymous << 16
SECURITY_IDENTIFICATION = SECURITY_IMPERSONATION_LEVEL.SecurityIdentification << 16
SECURITY_IMPERSONATION = SECURITY_IMPERSONATION_LEVEL.SecurityImpersonation << 16
SECURITY_DELEGATION = SECURITY_IMPERSONATION_LEVEL.SecurityDelegation << 16
SECURITY_CONTEXT_TRACKING = 0x00040000
SECURITY_EFFECTIVE_ONLY = 0x00080000
SECURITY_SQOS_PRESENT = 0x00100000
SECURITY_VALID_SQOS_FLAGS = 0x001F0000

FAIL_FAST_GENERATE_EXCEPTION_ADDRESS = 0x1
FAIL_FAST_NO_HARD_ERROR_DLG = 0x2

SP_SERIALCOMM = 0x00000001

PST_UNSPECIFIED = 0x00000000
PST_RS232 = 0x00000001
PST_PARALLELPORT = 0x00000002
PST_RS422 = 0x00000003
PST_RS423 = 0x00000004
PST_RS449 = 0x00000005
PST_MODEM = 0x00000006
PST_FAX = 0x00000021
PST_SCANNER = 0x00000022
PST_NETWORK_BRIDGE = 0x00000100
PST_LAT = 0x00000101
PST_TCPIP_TELNET = 0x00000102
PST_X25 = 0x00000103

PCF_DTRDSR = 0x0001
PCF_RTSCTS = 0x0002
PCF_RLSD = 0x0004
PCF_PARITY_CHECK = 0x0008
PCF_XONXOFF = 0x0010
PCF_SETXCHAR = 0x0020
PCF_TOTALTIMEOUTS = 0x0040
PCF_INTTIMEOUTS = 0x0080
PCF_SPECIALCHARS = 0x0100
PCF_16BITMODE = 0x0200

SP_PARITY = 0x0001
SP_BAUD = 0x0002
SP_DATABITS = 0x0004
SP_STOPBITS = 0x0008
SP_HANDSHAKING = 0x0010
SP_PARITY_CHECK = 0x0020
SP_RLSD = 0x0040

BAUD_075 = 0x00000001
BAUD_110 = 0x00000002
BAUD_134_5 = 0x00000004
BAUD_150 = 0x00000008
BAUD_300 = 0x00000010
BAUD_600 = 0x00000020
BAUD_1200 = 0x00000040
BAUD_1800 = 0x00000080
BAUD_2400 = 0x00000100
BAUD_4800 = 0x00000200
BAUD_7200 = 0x00000400
BAUD_9600 = 0x00000800
BAUD_14400 = 0x00001000
BAUD_19200 = 0x00002000
BAUD_38400 = 0x00004000
BAUD_56K = 0x00008000
BAUD_128K = 0x00010000
BAUD_115200 = 0x00020000
BAUD_57600 = 0x00040000
BAUD_USER = 0x10000000

DATABITS_5 = 0x0001
DATABITS_6 = 0x0002
DATABITS_7 = 0x0004
DATABITS_8 = 0x0008
DATABITS_16 = 0x0010
DATABITS_16X = 0x0020

STOPBITS_10 = 0x0001
STOPBITS_15 = 0x0002
STOPBITS_20 = 0x0004
PARITY_NONE = 0x0100
PARITY_ODD = 0x0200
PARITY_EVEN = 0x0400
PARITY_MARK = 0x0800
PARITY_SPACE = 0x1000


class COMMPROP(Structure):
    _fields_ = [
        ("wPacketLength", WORD),
        ("wPacketVersion", WORD),
        ("dwServiceMask", DWORD),
        ("dwReserved1", DWORD),
        ("dwMaxTxQueue", DWORD),
        ("dwMaxRxQueue", DWORD),
        ("dwMaxBaud", DWORD),
        ("dwProvSubType", DWORD),
        ("dwProvCapabilities", DWORD),
        ("dwSettableParams", DWORD),
        ("dwSettableBaud", DWORD),
        ("wSettableData", WORD),
        ("wSettableStopParity", WORD),
        ("dwCurrentTxQueue", DWORD),
        ("dwCurrentRxQueue", DWORD),
        ("dwProvSpec1", DWORD),
        ("dwProvSpec2", DWORD),
        ("wcProvChar", WCHAR * 1),
    ]


COMMPROP_INITIALIZED = 0xE73CF52E


class COMSTAT(Structure):
    _fields_ = [
        ("fCtsHold", DWORD, 1),
        ("fDsrHold", DWORD, 1),
        ("fRlsdHold", DWORD, 1),
        ("fXoffHold", DWORD, 1),
        ("fXoffSent", DWORD, 1),
        ("fEof", DWORD, 1),
        ("fTxim", DWORD, 1),
        ("fReserved", DWORD, 25),
        ("cbInQue", DWORD),
        ("cbOutQue", DWORD),
    ]


DTR_CONTROL_DISABLE = 0x00
DTR_CONTROL_ENABLE = 0x01
DTR_CONTROL_HANDSHAKE = 0x02

RTS_CONTROL_DISABLE = 0x00
RTS_CONTROL_ENABLE = 0x01
RTS_CONTROL_HANDSHAKE = 0x02
RTS_CONTROL_TOGGLE = 0x03


class DCB(Structure):
    _fields_ = [
        (
            "DCBlength",
            DWORD,
        ),
        (
            "BaudRate",
            DWORD,
        ),
        ("fBinary", DWORD, 1),
        ("fParity", DWORD, 1),
        ("fOutxCtsFlow", DWORD, 1),
        ("fOutxDsrFlow", DWORD, 1),
        ("fDtrControl", DWORD, 2),
        ("fDsrSensitivity", DWORD, 1),
        ("fTXContinueOnXoff", DWORD, 1),
        ("fOutX", DWORD, 1),
        ("fInX", DWORD, 1),
        ("fErrorChar", DWORD, 1),
        ("fNull", DWORD, 1),
        ("fRtsControl", DWORD, 2),
        ("fAbortOnError", DWORD, 1),
        ("fDummy2", DWORD, 17),
        ("wReserved", WORD),
        ("XonLim", WORD),
        ("XoffLim", WORD),
        ("ByteSize", BYTE),
        ("Parity", BYTE),
        ("StopBits", BYTE),
        ("XonChar", c_char),
        ("XoffChar", c_char),
        ("ErrorChar", c_char),
        ("EofChar", c_char),
        ("EvtChar", c_char),
        ("wReserved1", WORD),
    ]


class COMMTIMEOUTS(Structure):
    _fields_ = [
        ("ReadIntervalTimeout", DWORD),
        ("ReadTotalTimeoutMultiplier", DWORD),
        ("ReadTotalTimeoutConstant", WORD),
        ("WriteTotalTimeoutMultiplier", DWORD),
        ("WriteTotalTimeoutConstant", DWORD),
    ]


class COMMCONFIG(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("wVersion", WORD),
        ("wReserved", WORD),
        ("dcb", DCB),
        ("dwProviderSubType", DWORD),
        ("dwProviderOffset", DWORD),
        ("dwProviderSize", DWORD),
        ("wcProviderData", WCHAR * 1),
    ]


GMEM_FIXED = 0x0000
GMEM_MOVEABLE = 0x0002
GMEM_NOCOMPACT = 0x0010
GMEM_NODISCARD = 0x0020
GMEM_ZEROINIT = 0x0040
GMEM_MODIFY = 0x0080
GMEM_DISCARDABLE = 0x0100
GMEM_NOT_BANKED = 0x1000
GMEM_SHARE = 0x2000
GMEM_DDESHARE = 0x2000
GMEM_NOTIFY = 0x4000
GMEM_LOWER = GMEM_NOT_BANKED
GMEM_VALID_FLAGS = 0x7F72
GMEM_INVALID_HANDLE = 0x8000

GHND = GMEM_MOVEABLE | GMEM_ZEROINIT
GPTR = GMEM_FIXED | GMEM_ZEROINIT

GMEM_DISCARDED = 0x4000
GMEM_LOCKCOUNT = 0x00FF


class MEMORYSTATUS(Structure):
    _fields_ = [
        ("dwLength", DWORD),
        ("dwMemoryLoad", DWORD),
        ("dwTotalPhys", SIZE_T),
        ("dwAvailPhys", SIZE_T),
        ("dwTotalPageFile", SIZE_T),
        ("dwAvailPageFile", SIZE_T),
        ("dwTotalVirtual", SIZE_T),
        ("dwAvailVirtual", SIZE_T),
    ]


DEBUG_PROCESS = 0x00000001
DEBUG_ONLY_THIS_PROCESS = 0x00000002
CREATE_SUSPENDED = 0x00000004
DETACHED_PROCESS = 0x00000008

CREATE_NEW_CONSOLE = 0x00000010
NORMAL_PRIORITY_CLASS = 0x00000020
IDLE_PRIORITY_CLASS = 0x00000040
HIGH_PRIORITY_CLASS = 0x00000080

REALTIME_PRIORITY_CLASS = 0x00000100
CREATE_NEW_PROCESS_GROUP = 0x00000200
CREATE_UNICODE_ENVIRONMENT = 0x00000400
CREATE_SEPARATE_WOW_VDM = 0x00000800

CREATE_SHARED_WOW_VDM = 0x00001000
CREATE_FORCEDOS = 0x00002000
BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
ABOVE_NORMAL_PRIORITY_CLASS = 0x00008000

INHERIT_PARENT_AFFINITY = 0x00010000
INHERIT_CALLER_PRIORITY = 0x00020000  # Deprecated
CREATE_PROTECTED_PROCESS = 0x00040000
EXTENDED_STARTUPINFO_PRESENT = 0x00080000

PROCESS_MODE_BACKGROUND_BEGIN = 0x00100000
PROCESS_MODE_BACKGROUND_END = 0x00200000
CREATE_SECURE_PROCESS = 0x00400000

CREATE_BREAKAWAY_FROM_JOB = 0x01000000
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = 0x02000000
CREATE_DEFAULT_ERROR_MODE = 0x04000000
CREATE_NO_WINDOW = 0x08000000

PROFILE_USER = 0x10000000
PROFILE_KERNEL = 0x20000000
PROFILE_SERVER = 0x40000000
CREATE_IGNORE_SYSTEM_DEFAULT = 0x80000000

# CREATE_SUSPENDED = 0x00000004

STACK_SIZE_PARAM_IS_A_RESERVATION = 0x00010000

THREAD_PRIORITY_LOWEST = THREAD_BASE_PRIORITY_MIN
THREAD_PRIORITY_BELOW_NORMAL = THREAD_PRIORITY_LOWEST + 1
THREAD_PRIORITY_NORMAL = 0
THREAD_PRIORITY_HIGHEST = THREAD_BASE_PRIORITY_MAX
THREAD_PRIORITY_ABOVE_NORMAL = THREAD_PRIORITY_HIGHEST - 1
THREAD_PRIORITY_ERROR_RETURN = MAXLONG

THREAD_PRIORITY_TIME_CRITICAL = THREAD_BASE_PRIORITY_LOWRT
THREAD_PRIORITY_IDLE = THREAD_BASE_PRIORITY_IDLE

THREAD_MODE_BACKGROUND_BEGIN = 0x00010000
THREAD_MODE_BACKGROUND_END = 0x00020000

VOLUME_NAME_DOS = 0x0  # default
VOLUME_NAME_GUID = 0x1
VOLUME_NAME_NT = 0x2
VOLUME_NAME_NONE = 0x4

FILE_NAME_NORMALIZED = 0x0  # default
FILE_NAME_OPENED = 0x8


class JIT_DEBUG_INFO(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("dwProcessorArchitecture", DWORD),
        ("dwThreadID", DWORD),
        ("dwReserved0", DWORD),
        ("lpExceptionAddress", ULONG64),
        ("lpExceptionRecord", ULONG64),
        ("lpContextRecord", ULONG64),
    ]


DRIVE_UNKNOWN = 0
DRIVE_NO_ROOT_DIR = 1
DRIVE_REMOVABLE = 2
DRIVE_FIXED = 3
DRIVE_REMOTE = 4
DRIVE_CDROM = 5
DRIVE_RAMDISK = 6

FILE_TYPE_UNKNOWN = 0x0000
FILE_TYPE_DISK = 0x0001
FILE_TYPE_CHAR = 0x0002
FILE_TYPE_PIPE = 0x0003
FILE_TYPE_REMOTE = 0x8000

STD_INPUT_HANDLE = DWORD(-10)
STD_OUTPUT_HANDLE = DWORD(-11)
STD_ERROR_HANDLE = DWORD(-12)

NOPARITY = 0
ODDPARITY = 1
EVENPARITY = 2
MARKPARITY = 3
SPACEPARITY = 4

ONESTOPBIT = 0
ONE5STOPBITS = 1
TWOSTOPBITS = 2

IGNORE = 0
INFINITE = 0xFFFFFFFF

CBR_110 = 110
CBR_300 = 300
CBR_600 = 600
CBR_1200 = 1200
CBR_2400 = 2400
CBR_4800 = 4800
CBR_9600 = 9600
CBR_14400 = 14400
CBR_19200 = 19200
CBR_38400 = 38400
CBR_56000 = 56000
CBR_57600 = 57600
CBR_115200 = 115200
CBR_128000 = 128000
CBR_256000 = 256000

CE_RXOVER = 0x0001
CE_OVERRUN = 0x0002
CE_RXPARITY = 0x0004
CE_FRAME = 0x0008
CE_BREAK = 0x0010
CE_TXFULL = 0x0100
CE_PTO = 0x0200
CE_IOE = 0x0400
CE_DNS = 0x0800
CE_OOP = 0x1000
CE_MODE = 0x8000

IE_BADID = -1
IE_OPEN = -2
IE_NOPEN = -3
IE_MEMORY = -4
IE_DEFAULT = -5
IE_HARDWARE = -10
IE_BYTESIZE = -11
IE_BAUDRATE = -12

EV_RXCHAR = 0x0001
EV_RXFLAG = 0x0002
EV_TXEMPTY = 0x0004
EV_CTS = 0x0008
EV_DSR = 0x0010
EV_RLSD = 0x0020
EV_BREAK = 0x0040
EV_ERR = 0x0080
EV_RING = 0x0100
EV_PERR = 0x0200
EV_RX80FULL = 0x0400
EV_EVENT1 = 0x0800
EV_EVENT2 = 0x1000

SETXOFF = 1
SETXON = 2
SETRTS = 3
CLRRTS = 4
SETDTR = 5
CLRDTR = 6
RESETDEV = 7
SETBREAK = 8
CLRBREAK = 9

PURGE_TXABORT = 0x0001
PURGE_RXABORT = 0x0002
PURGE_TXCLEAR = 0x0004
PURGE_RXCLEAR = 0x0008

LPTx = 0x80

MS_CTS_ON = 0x0010
MS_DSR_ON = 0x0020
MS_RING_ON = 0x0040
MS_RLSD_ON = 0x0080

S_QUEUEEMPTY = 0
S_THRESHOLD = 1
S_ALLTHRESHOLD = 2

S_NORMAL = 0
S_LEGATO = 1
S_STACCATO = 2

S_PERIOD512 = 0
S_PERIOD1024 = 1
S_PERIOD2048 = 2
S_PERIODVOICE = 3
S_WHITE512 = 4
S_WHITE1024 = 5
S_WHITE2048 = 6
S_WHITEVOICE = 7

S_SERDVNA = -1
S_SEROFM = -2
S_SERMACT = -3
S_SERQFUL = -4
S_SERBDNT = -5
S_SERDLN = -6
S_SERDCC = -7
S_SERDTP = -8
S_SERDVL = -9
S_SERDMD = -10
S_SERDSH = -11
S_SERDPT = -12
S_SERDFQ = -13
S_SERDDR = -14
S_SERDSR = -15
S_SERDST = -16

NMPWAIT_WAIT_FOREVER = 0xFFFFFFFF
NMPWAIT_NOWAIT = 0x00000001
NMPWAIT_USE_DEFAULT_WAIT = 0x00000000

FS_CASE_IS_PRESERVED = FILE_CASE_PRESERVED_NAMES
FS_CASE_SENSITIVE = FILE_CASE_SENSITIVE_SEARCH
FS_UNICODE_STORED_ON_DISK = FILE_UNICODE_ON_DISK
FS_PERSISTENT_ACLS = FILE_PERSISTENT_ACLS
FS_VOL_IS_COMPRESSED = FILE_VOLUME_IS_COMPRESSED
FS_FILE_COMPRESSION = FILE_FILE_COMPRESSION
FS_FILE_ENCRYPTION = FILE_SUPPORTS_ENCRYPTION

OF_READ = 0x00000000
OF_WRITE = 0x00000001
OF_READWRITE = 0x00000002
OF_SHARE_COMPAT = 0x00000000
OF_SHARE_EXCLUSIVE = 0x00000010
OF_SHARE_DENY_WRITE = 0x00000020
OF_SHARE_DENY_READ = 0x00000030
OF_SHARE_DENY_NONE = 0x00000040
OF_PARSE = 0x00000100
OF_DELETE = 0x00000200
OF_VERIFY = 0x00000400
OF_CANCEL = 0x00000800
OF_CREATE = 0x00001000
OF_PROMPT = 0x00002000
OF_EXIST = 0x00004000
OF_REOPEN = 0x00008000

OFS_MAXPATHNAME = 128


class OFSTRUCT(Structure):
    _fields_ = [
        ("cBytes", BYTE),
        ("fFixedDisk", BYTE),
        ("nErrCode", WORD),
        ("Reserved1", WORD),
        ("Reserved2", WORD),
        ("szPathName", CHAR * OFS_MAXPATHNAME),
    ]


MAXINTATOM = 0xC000
INVALID_ATOM = ATOM(0)

MOVEFILE_REPLACE_EXISTING = 0x00000001
MOVEFILE_COPY_ALLOWED = 0x00000002
MOVEFILE_DELAY_UNTIL_REBOOT = 0x00000004
MOVEFILE_WRITE_THROUGH = 0x00000008
MOVEFILE_CREATE_HARDLINK = 0x00000010
MOVEFILE_FAIL_IF_NOT_TRACKABLE = 0x00000020


class FILE_ALIGNMENT_INFO(Structure):
    _fields_ = [
        ("AlignmentRequirement", ULONG),
    ]


STORAGE_INFO_FLAGS_ALIGNED_DEVICE = 0x00000001
STORAGE_INFO_FLAGS_PARTITION_ALIGNED_ON_DEVICE = 0x00000002
STORAGE_INFO_OFFSET_UNKNOWN = 0xFFFFFFFF


class FILE_STORAGE_INFO(Structure):
    _fields_ = [
        ("LogicalBytesPerSector", ULONG),
        ("PhysicalBytesPerSectorForAtomicity", ULONG),
        ("PhysicalBytesPerSectorForPerformance", ULONG),
        ("FileSystemEffectivePhysicalBytesPerSectorForAtomicity", ULONG),
        ("Flags", ULONG),
        ("ByteOffsetForSectorAlignment", ULONG),
        ("ByteOffsetForPartitionAlignment", ULONG),
    ]


class FILE_ID_INFO(Structure):
    _fields_ = [
        ("VolumeSerialNumber", ULONGLONG),
        ("FileId", FILE_ID_128),
    ]


class FILE_ID_EXTD_DIR_INFO(Structure):
    _fields_ = [
        ("NextEntryOffset", ULONG),
        ("FileIndex", ULONG),
        ("CreationTime", LARGE_INTEGER),
        ("LastAccessTime", LARGE_INTEGER),
        ("LastWriteTime", LARGE_INTEGER),
        ("ChangeTime", LARGE_INTEGER),
        ("EndOfFile", LARGE_INTEGER),
        ("AllocationSize", LARGE_INTEGER),
        ("FileAttributes", ULONG),
        ("FileNameLength", ULONG),
        ("EaSize", ULONG),
        ("ReparsePointTag", ULONG),
        ("FileId", FILE_ID_128),
        ("FileName", WCHAR * 1),
    ]


class FILE_ID_TYPE(CEnum):
    FileIdType = 0
    ObjectIdType = 1
    ExtendedFileIdType = 2
    MaximumFileIdType = 3


class FILE_ID_DESCRIPTOR_UNION(Union):
    _fields_ = [
        ("FileId", LARGE_INTEGER),
        ("ObjectId", GUID),
        ("ExtendedFileId", FILE_ID_128),
    ]


class FILE_ID_DESCRIPTOR(Structure):
    _anonymous_ = ("u",)
    _fields_ = [
        ("dwSize", DWORD),
        ("Type", FILE_ID_TYPE),
        ("u", FILE_ID_DESCRIPTOR_UNION),
    ]


# advapi32 functions

LookupPrivilegeNameA = windll.advapi32.LookupPrivilegeNameA
LookupPrivilegeNameA.argtypes = [LPCSTR, POINTER(LUID), LPSTR, POINTER(DWORD)]
LookupPrivilegeNameA.restype = BOOL

LookupPrivilegeNameW = windll.advapi32.LookupPrivilegeNameW
LookupPrivilegeNameW.argtypes = [LPCWSTR, POINTER(LUID), LPWSTR, POINTER(DWORD)]
LookupPrivilegeNameW.restype = BOOL

LookupPrivilegeValueA = windll.advapi32.LookupPrivilegeValueA
LookupPrivilegeValueA.argtypes = [LPCSTR, LPCSTR, POINTER(LUID)]
LookupPrivilegeValueA.restype = BOOL

LookupPrivilegeValueW = windll.advapi32.LookupPrivilegeValueW
LookupPrivilegeValueW.argtypes = [LPCWSTR, LPCWSTR, POINTER(LUID)]
LookupPrivilegeValueW.restype = BOOL

# kernel32 functions

GetFileInformationByHandleEx = windll.kernel32.GetFileInformationByHandleEx
GetFileInformationByHandleEx.argtypes = [HANDLE, FILE_INFO_BY_HANDLE_CLASS, LPVOID, DWORD]
GetFileInformationByHandleEx.restype = BOOL

MoveFileExA = windll.kernel32.MoveFileExA
MoveFileExA.argtypes = [LPCSTR, LPCSTR, DWORD]
MoveFileExA.restype = BOOL

MoveFileExW = windll.kernel32.MoveFileExW
MoveFileExW.argtypes = [LPCWSTR, LPCWSTR, DWORD]
MoveFileExW.restype = BOOL

OpenFileById = windll.kernel32.OpenFileById
OpenFileById.argtypes = [HANDLE, POINTER(FILE_ID_DESCRIPTOR), DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD]
OpenFileById.restype = HANDLE

ReOpenFile = windll.kernel32.ReOpenFile
ReOpenFile.argtypes = [HANDLE, DWORD, DWORD, DWORD]
ReOpenFile.restype = HANDLE

FindFirstVolumeA = windll.kernel32.FindFirstVolumeA
FindFirstVolumeA.argtypes = [LPSTR, DWORD]
FindFirstVolumeA.restype = HANDLE
FindFirstVolumeA.errcheck = validhandle

FindNextVolumeA = windll.kernel32.FindNextVolumeA
FindNextVolumeA.argtypes = [HANDLE, LPSTR, DWORD]
FindNextVolumeA.restype = BOOL
FindNextVolumeA.errcheck = nonzero

FindFirstVolumeMountPointA = windll.kernel32.FindFirstVolumeMountPointA
FindFirstVolumeMountPointA.argtypes = [LPCSTR, LPSTR, DWORD]
FindFirstVolumeMountPointA.restype = HANDLE
FindFirstVolumeMountPointA.errcheck = validhandle

FindFirstVolumeMountPointW = windll.kernel32.FindFirstVolumeMountPointW
FindFirstVolumeMountPointW.argtypes = [LPCWSTR, LPWSTR, DWORD]
FindFirstVolumeMountPointW.restype = HANDLE
FindFirstVolumeMountPointW.errcheck = validhandle

FindNextVolumeMountPointA = windll.kernel32.FindNextVolumeMountPointA
FindNextVolumeMountPointA.argtypes = [HANDLE, LPSTR, DWORD]
FindNextVolumeMountPointA.restype = BOOL
FindNextVolumeMountPointA.errcheck = nonzero

FindNextVolumeMountPointW = windll.kernel32.FindNextVolumeMountPointW
FindNextVolumeMountPointW.argtypes = [HANDLE, LPWSTR, DWORD]
FindNextVolumeMountPointW.restype = BOOL
FindNextVolumeMountPointA.errcheck = nonzero

FindVolumeMountPointClose = windll.kernel32.FindVolumeMountPointClose
FindVolumeMountPointClose.argtypes = [HANDLE]
FindVolumeMountPointClose.restype = BOOL
FindVolumeMountPointClose.errcheck = nonzero

SetVolumeMountPointA = windll.kernel32.SetVolumeMountPointA
SetVolumeMountPointA.argtypes = [LPCSTR, LPCSTR]
SetVolumeMountPointA.restype = BOOL

SetVolumeMountPointW = windll.kernel32.SetVolumeMountPointW
SetVolumeMountPointW.argtypes = [LPCWSTR, LPCWSTR]
SetVolumeMountPointW.restype = BOOL

DeleteVolumeMountPointA = windll.kernel32.DeleteVolumeMountPointA
DeleteVolumeMountPointA.argtypes = [LPCSTR]
DeleteVolumeMountPointA.restype = BOOL

GetVolumeNameForVolumeMountPointA = windll.kernel32.GetVolumeNameForVolumeMountPointA
GetVolumeNameForVolumeMountPointA.argtypes = [LPCSTR, LPSTR, DWORD]
GetVolumeNameForVolumeMountPointA.restype = BOOL

GetVolumePathNameA = windll.kernel32.GetVolumePathNameA
GetVolumePathNameA.argtypes = [LPCSTR, LPSTR, DWORD]
GetVolumePathNameA.restype = BOOL

GetVolumePathNamesForVolumeNameA = windll.kernel32.GetVolumePathNamesForVolumeNameA
GetVolumePathNamesForVolumeNameA.argtypes = [LPCSTR, LPCH, DWORD, PDWORD]
GetVolumePathNamesForVolumeNameA.restype = BOOL
