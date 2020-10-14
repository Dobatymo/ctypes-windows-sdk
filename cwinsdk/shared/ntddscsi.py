from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure
from ctypes.wintypes import ULONG, USHORT

from .basetsd import ULONG_PTR
from .devioctl import (
    CTL_CODE,
    FILE_ANY_ACCESS,
    FILE_DEVICE_CONTROLLER,
    FILE_READ_ACCESS,
    FILE_WRITE_ACCESS,
    METHOD_BUFFERED,
)
from .ntdef import PVOID, UCHAR

IOCTL_SCSI_BASE = FILE_DEVICE_CONTROLLER
FILE_DEVICE_SCSI = 0x0000001b

DD_SCSI_DEVICE_NAME = br"\Device\ScsiPort"

IOCTL_SCSI_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x0401, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_MINIPORT = CTL_CODE(IOCTL_SCSI_BASE, 0x0402, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_GET_INQUIRY_DATA = CTL_CODE(IOCTL_SCSI_BASE, 0x0403, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_GET_CAPABILITIES = CTL_CODE(IOCTL_SCSI_BASE, 0x0404, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_PASS_THROUGH_DIRECT = CTL_CODE(IOCTL_SCSI_BASE, 0x0405, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_GET_ADDRESS = CTL_CODE(IOCTL_SCSI_BASE, 0x0406, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_RESCAN_BUS = CTL_CODE(IOCTL_SCSI_BASE, 0x0407, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_GET_DUMP_POINTERS = CTL_CODE(IOCTL_SCSI_BASE, 0x0408, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_SCSI_FREE_DUMP_POINTERS = CTL_CODE(IOCTL_SCSI_BASE, 0x0409, METHOD_BUFFERED, FILE_ANY_ACCESS)
IOCTL_IDE_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x040a, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_PASS_THROUGH = CTL_CODE(IOCTL_SCSI_BASE, 0x040b, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_PASS_THROUGH_DIRECT = CTL_CODE(IOCTL_SCSI_BASE, 0x040c, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_ATA_MINIPORT = CTL_CODE(IOCTL_SCSI_BASE, 0x040d, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MINIPORT_PROCESS_SERVICE_IRP = CTL_CODE(IOCTL_SCSI_BASE, 0x040e, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MPIO_PASS_THROUGH_PATH = CTL_CODE(IOCTL_SCSI_BASE, 0x040f, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT = CTL_CODE(IOCTL_SCSI_BASE, 0x0410, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

IOCTL_SCSI_PASS_THROUGH_EX = CTL_CODE(IOCTL_SCSI_BASE, 0x0411, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_SCSI_PASS_THROUGH_DIRECT_EX = CTL_CODE(IOCTL_SCSI_BASE, 0x0412, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

IOCTL_MPIO_PASS_THROUGH_PATH_EX = CTL_CODE(IOCTL_SCSI_BASE, 0x0413, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)
IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX = CTL_CODE(IOCTL_SCSI_BASE, 0x0414, METHOD_BUFFERED, FILE_READ_ACCESS | FILE_WRITE_ACCESS)

SCSI_IOCTL_DATA_OUT = 0
SCSI_IOCTL_DATA_IN = 1
SCSI_IOCTL_DATA_UNSPECIFIED = 2

SCSI_IOCTL_DATA_BIDIRECTIONAL = 3

MPIO_IOCTL_FLAG_USE_PATHID = 1
MPIO_IOCTL_FLAG_USE_SCSIADDRESS = 2
MPIO_IOCTL_FLAG_INVOLVE_DSM = 4

class SRB_IO_CONTROL(Structure):
	__slots__ = ()
	_fields_ = [
		("HeaderLength", ULONG),
		("Signature", UCHAR*8),
		("Timeout", ULONG),
		("ControlCode", ULONG),
		("ReturnCode", ULONG),
		("Length", ULONG),
	]

class SCSI_PASS_THROUGH(Structure):
	__slots__ = ()
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
		("Cdb", UCHAR*16),
	]

class SCSI_PASS_THROUGH_DIRECT(Structure):
	__slots__ = ()
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
		("Cdb", UCHAR*16),
	]
