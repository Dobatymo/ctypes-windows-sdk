from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure
from ctypes import c_int as ENUM_TYPE
from ctypes.wintypes import SHORT, WORD, DWORD, ULONG, USHORT, BOOLEAN

from .win32types import BYTE
from .shared.basetsd import ULONG_PTR
from .shared.ntdef import UCHAR, PVOID

# ntdddisk.h

class GETVERSIONINPARAMS(Structure):
	__slots__ = ()
	_pack_ = 1
	_fields_ = [
		("bVersion", UCHAR),
		("bRevision", UCHAR),
		("bReserved", UCHAR),
		("bIDEDeviceMap", UCHAR),
		("fCapabilities", ULONG),
		("dwReserved", ULONG*4),
	]

class IDEREGS(Structure):
	__slots__ = ()
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
	__slots__ = ()
	_pack_ = 1
	_fields_ = [
		("cBufferSize", ULONG),
		("irDriveRegs", IDEREGS),
		("bDriveNumber", UCHAR),
		("bReserved", UCHAR*3),
		("dwReserved", ULONG*4),
		("bBuffer", UCHAR*1),
	]

class DRIVERSTATUS(Structure):
	__slots__ = ()
	_pack_ = 1
	_fields_ = [
		("bDriverError", UCHAR),
		("bIDEError", UCHAR),
		("bReserved", UCHAR*2),
		("dwReserved", ULONG*2),
	]

class SENDCMDOUTPARAMS(Structure):
	__slots__ = ()
	_pack_ = 1
	_fields_ = [
		("cBufferSize", ULONG),
		("DriverStatus", DRIVERSTATUS),
		("bBuffer", UCHAR*1),
	]


# ntddscsi.h

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


# winioctl.h

class STORAGE_PROPERTY_QUERY(Structure):
	__slots__ = ()
	# no pack
	_fields_ = [
		("PropertyId", ENUM_TYPE), # STORAGE_PROPERTY_ID
		("QueryType", ENUM_TYPE), # STORAGE_QUERY_TYPE
		("AdditionalParameters", BYTE*1),
	]

class STORAGE_DEVICE_DESCRIPTOR(Structure):
	__slots__ = ()
	# no pack
	_fields_ = [
		("Version", DWORD),
		("Size", DWORD),
		("DeviceType", BYTE),
		("DeviceTypeModifier", BYTE),
		("RemovableMedia", BOOLEAN),
		("CommandQueueing", BOOLEAN),
		("VendorIdOffset", DWORD),
		("ProductIdOffset", DWORD),
		("ProductRevisionOffset", DWORD),
		("SerialNumberOffset", DWORD),
		("BusType", ENUM_TYPE), # STORAGE_BUS_TYPE
		("RawPropertiesLength", DWORD),
		("RawDeviceProperties", BYTE*1),
	]
