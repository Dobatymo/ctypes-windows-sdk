from ctypes import POINTER, Structure
from ctypes.wintypes import LPVOID, ULONG, USHORT

from .basetsd import ULONG_PTR
from .devioctl import (
    CTL_CODE,
    FILE_ANY_ACCESS,
    FILE_DEVICE_CONTROLLER,
    FILE_READ_ACCESS,
    FILE_WRITE_ACCESS,
    METHOD_BUFFERED,
)
from .ntdef import ANYSIZE_ARRAY, PVOID, UCHAR

IOCTL_SCSI_BASE = FILE_DEVICE_CONTROLLER
FILE_DEVICE_SCSI = 0x0000001B

DD_SCSI_DEVICE_NAME = b"\\Device\\ScsiPort"

IOCTL_SCSI_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x0401, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_MINIPORT = CTL_CODE(IOCTL_SCSI_BASE, 0x0402, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_GET_INQUIRY_DATA = CTL_CODE(IOCTL_SCSI_BASE, 0x0403, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_GET_CAPABILITIES = CTL_CODE(IOCTL_SCSI_BASE, 0x0404, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_PASS_THROUGH_DIRECT = CTL_CODE(
    IOCTL_SCSI_BASE, 0x0405, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)
IOCTL_SCSI_GET_ADDRESS = CTL_CODE(IOCTL_SCSI_BASE, 0x0406, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_RESCAN_BUS = CTL_CODE(IOCTL_SCSI_BASE, 0x0407, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_GET_DUMP_POINTERS = CTL_CODE(IOCTL_SCSI_BASE, 0x0408, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_FREE_DUMP_POINTERS = CTL_CODE(IOCTL_SCSI_BASE, 0x0409, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_IDE_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x040A, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x040B, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_PASS_THROUGH_DIRECT = CTL_CODE(IOCTL_SCSI_BASE, 0x040C, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_MINIPORT = CTL_CODE(IOCTL_SCSI_BASE, 0x040D, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MINIPORT_PROCESS_SERVICE_IRP = CTL_CODE(
    IOCTL_SCSI_BASE, 0x040E, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)
IOCTL_MPIO_PASS_THROUGH_PATH = CTL_CODE(IOCTL_SCSI_BASE, 0x040F, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT = CTL_CODE(
    IOCTL_SCSI_BASE, 0x0410, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)

IOCTL_SCSI_PASS_THROUGH_EX = CTL_CODE(IOCTL_SCSI_BASE, 0x0411, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_PASS_THROUGH_DIRECT_EX = CTL_CODE(
    IOCTL_SCSI_BASE, 0x0412, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)

IOCTL_MPIO_PASS_THROUGH_PATH_EX = CTL_CODE(
    IOCTL_SCSI_BASE, 0x0413, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX = CTL_CODE(
    IOCTL_SCSI_BASE, 0x0414, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS
)

SCSI_IOCTL_DATA_OUT = 0
SCSI_IOCTL_DATA_IN = 1
SCSI_IOCTL_DATA_UNSPECIFIED = 2

SCSI_IOCTL_DATA_BIDIRECTIONAL = 3

MPIO_IOCTL_FLAG_USE_PATHID = 1
MPIO_IOCTL_FLAG_USE_SCSIADDRESS = 2
MPIO_IOCTL_FLAG_INVOLVE_DSM = 4


class SRB_IO_CONTROL(Structure):
    _fields_ = [
        ("HeaderLength", ULONG),
        ("Signature", UCHAR * 8),
        ("Timeout", ULONG),
        ("ControlCode", ULONG),
        ("ReturnCode", ULONG),
        ("Length", ULONG),
    ]


PSRB_IO_CONTROL = POINTER(SRB_IO_CONTROL)


class SCSI_PASS_THROUGH(Structure):
    _fields_ = [
        ("Length", USHORT),
        ("ScsiStatus", UCHAR),
        ("PathId", UCHAR),
        ("TargetId", UCHAR),
        ("Lun", UCHAR),
        ("CdbLength", UCHAR),
        ("SenseInfoLength", UCHAR),
        ("DataIn", UCHAR),
        ("DataTransferLength", ULONG),
        ("TimeOutValue", ULONG),
        ("DataBufferOffset", ULONG_PTR),
        ("SenseInfoOffset", ULONG),
        ("Cdb", UCHAR * 16),
    ]


PSCSI_PASS_THROUGH = POINTER(SCSI_PASS_THROUGH)


class SCSI_PASS_THROUGH_DIRECT(Structure):
    _fields_ = [
        ("Length", USHORT),
        ("ScsiStatus", UCHAR),
        ("PathId", UCHAR),
        ("TargetId", UCHAR),
        ("Lun", UCHAR),
        ("CdbLength", UCHAR),
        ("SenseInfoLength", UCHAR),
        ("DataIn", UCHAR),
        ("DataTransferLength", ULONG),
        ("TimeOutValue", ULONG),
        ("DataBuffer", PVOID),
        ("SenseInfoOffset", ULONG),
        ("Cdb", UCHAR * 16),
    ]


PSCSI_PASS_THROUGH_DIRECT = POINTER(SCSI_PASS_THROUGH_DIRECT)


class SCSI_PASS_THROUGH_EX(Structure):
    _fields_ = [
        ("Version", ULONG),
        ("Length", ULONG),  # size of the structure
        ("CdbLength", ULONG),  # non-zero value should be set by caller
        ("StorAddressLength", ULONG),  # non-zero value should be set by caller
        ("ScsiStatus", UCHAR),
        ("SenseInfoLength", UCHAR),  # optional, can be zero
        ("DataDirection", UCHAR),  # data transfer direction
        ("Reserved", UCHAR),  # padding
        ("TimeOutValue", ULONG),
        ("StorAddressOffset", ULONG),  # a value bigger than (structure size + CdbLength) should be set by caller
        ("SenseInfoOffset", ULONG),
        ("DataOutTransferLength", ULONG),  # optional, can be zero
        ("DataInTransferLength", ULONG),  # optional, can be zero
        ("DataOutBufferOffset", ULONG_PTR),
        ("DataInBufferOffset", ULONG_PTR),
        ("Cdb", UCHAR * ANYSIZE_ARRAY),
    ]


PSCSI_PASS_THROUGH_EX = POINTER(SCSI_PASS_THROUGH_EX)


class SCSI_PASS_THROUGH_DIRECT_EX(Structure):
    _fields_ = [
        ("Version", ULONG),
        ("Length", ULONG),  # size of the structure
        ("CdbLength", ULONG),  # non-zero value should be set by caller
        ("StorAddressLength", ULONG),  # non-zero value should be set by caller
        ("ScsiStatus", UCHAR),
        ("SenseInfoLength", UCHAR),  # optional, can be zero
        ("DataDirection", UCHAR),  # data transfer direction
        ("Reserved", UCHAR),  # padding
        ("TimeOutValue", ULONG),
        ("StorAddressOffset", ULONG),  # a value bigger than (structure size + CdbLength) should be set by caller
        ("SenseInfoOffset", ULONG),
        ("DataOutTransferLength", ULONG),  # optional, can be zero
        ("DataInTransferLength", ULONG),  # optional, can be zero
        ("DataOutBuffer", LPVOID),
        ("DataInBuffer", LPVOID),
        ("Cdb", UCHAR * ANYSIZE_ARRAY),
    ]


PSCSI_PASS_THROUGH_DIRECT_EX = POINTER(SCSI_PASS_THROUGH_DIRECT_EX)


class SCSI_ADDRESS(Structure):
    _fields_ = [
        ("Length", ULONG),
        ("PortNumber", UCHAR),
        ("PathId", UCHAR),
        ("TargetId", UCHAR),
        ("Lun", UCHAR),
    ]


PSCSI_ADDRESS = POINTER(SCSI_ADDRESS)
