from ctypes import Structure
from ctypes.wintypes import ULONG

from .devioctl import CTL_CODE, FILE_DEVICE_DISK, FILE_READ_ACCESS, FILE_WRITE_ACCESS, METHOD_BUFFERED
from .ntdef import UCHAR

IOCTL_DISK_BASE = FILE_DEVICE_DISK
SMART_GET_VERSION = CTL_CODE(IOCTL_DISK_BASE, 0x0020, METHOD_BUFFERED, FILE_READ_ACCESS)
SMART_SEND_DRIVE_COMMAND = CTL_CODE(IOCTL_DISK_BASE, 0x0021, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
SMART_RCV_DRIVE_DATA = CTL_CODE(IOCTL_DISK_BASE, 0x0022, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

CAP_ATA_ID_CMD = 1
CAP_ATAPI_ID_CMD = 2
CAP_SMART_CMD = 4

READ_ATTRIBUTE_BUFFER_SIZE = 512
IDENTIFY_BUFFER_SIZE = 512
READ_THRESHOLD_BUFFER_SIZE = 512
SMART_LOG_SECTOR_SIZE = 512

ATAPI_ID_CMD = 0xA1
ID_CMD = 0xEC
SMART_CMD = 0xB0

SMART_CYL_LOW = 0x4F
SMART_CYL_HI = 0xC2

READ_ATTRIBUTES = 0xD0
READ_THRESHOLDS = 0xD1
ENABLE_DISABLE_AUTOSAVE = 0xD2
SAVE_ATTRIBUTE_VALUES = 0xD3
EXECUTE_OFFLINE_DIAGS = 0xD4
SMART_READ_LOG = 0xD5
SMART_WRITE_LOG = 0xD6
ENABLE_SMART = 0xD8
DISABLE_SMART = 0xD9
RETURN_SMART_STATUS = 0xDA
ENABLE_DISABLE_AUTO_OFFLINE = 0xDB


class GETVERSIONINPARAMS(Structure):
    _pack_ = 1
    _fields_ = [
        ("bVersion", UCHAR),
        ("bRevision", UCHAR),
        ("bReserved", UCHAR),
        ("bIDEDeviceMap", UCHAR),
        ("fCapabilities", ULONG),
        ("dwReserved", ULONG * 4),
    ]


class IDEREGS(Structure):
    _pack_ = 1
    _fields_ = [
        ("bFeaturesReg", UCHAR),
        ("bSectorCountReg", UCHAR),
        ("bSectorNumberReg", UCHAR),
        ("bCylLowReg", UCHAR),
        ("bCylHighReg", UCHAR),
        ("bDriveHeadReg", UCHAR),
        ("bCommandReg", UCHAR),
        ("bReserved", UCHAR),
    ]


class SENDCMDINPARAMS(Structure):
    _pack_ = 1
    _fields_ = [
        ("cBufferSize", ULONG),
        ("irDriveRegs", IDEREGS),
        ("bDriveNumber", UCHAR),
        ("bReserved", UCHAR * 3),
        ("dwReserved", ULONG * 4),
        ("bBuffer", UCHAR * 1),
    ]


class DRIVERSTATUS(Structure):
    _pack_ = 1
    _fields_ = [
        ("bDriverError", UCHAR),
        ("bIDEError", UCHAR),
        ("bReserved", UCHAR * 2),
        ("dwReserved", ULONG * 2),
    ]


# bDriverError values

SMART_NO_ERROR = 0  # No error
SMART_IDE_ERROR = 1  # Error from IDE controller
SMART_INVALID_FLAG = 2  # Invalid command flag
SMART_INVALID_COMMAND = 3  # Invalid command byte
SMART_INVALID_BUFFER = 4  # Bad buffer (null, invalid addr..)
SMART_INVALID_DRIVE = 5  # Drive number not valid
SMART_INVALID_IOCTL = 6  # Invalid IOCTL
SMART_ERROR_NO_MEM = 7  # Could not lock user's buffer
SMART_INVALID_REGISTER = 8  # Some IDE Register not valid
SMART_NOT_SUPPORTED = 9  # Invalid cmd flag set
SMART_NO_IDE_DEVICE = 10  # Cmd issued to device not present


class SENDCMDOUTPARAMS(Structure):
    _pack_ = 1
    _fields_ = [
        ("cBufferSize", ULONG),
        ("DriverStatus", DRIVERSTATUS),
        ("bBuffer", UCHAR * 1),
    ]
