from ctypes import Structure
from ctypes.wintypes import LARGE_INTEGER, ULONG


class FILE_FS_FULL_SIZE_INFORMATION(Structure):
    _fields_ = [
        ("TotalAllocationUnits", LARGE_INTEGER),
        ("CallerAvailableAllocationUnits", LARGE_INTEGER),
        ("ActualAvailableAllocationUnits", LARGE_INTEGER),
        ("SectorsPerAllocationUnit", ULONG),
        ("BytesPerSector", ULONG),
    ]
