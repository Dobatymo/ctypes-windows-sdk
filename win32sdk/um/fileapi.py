from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure
from ctypes.wintypes import DWORD

from ..shared.ntdef import ULONGLONG

CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

INVALID_FILE_SIZE = 0xFFFFFFFF
INVALID_SET_FILE_POINTER = DWORD(-1)
INVALID_FILE_ATTRIBUTES = DWORD(-1)

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
