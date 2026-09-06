from ctypes import POINTER, Structure
from ctypes.wintypes import DWORD, WCHAR

from .ifdef import IF_INDEX
from .ipifcons import IFTYPE, INTERNAL_IF_OPER_STATUS, MAX_INTERFACE_NAME_LEN, MAXLEN_IFDESCR, MAXLEN_PHYSADDR
from .ntdef import ANYSIZE_ARRAY, UCHAR


class MIB_IFNUMBER(Structure):
    _fields_ = [("dwValue", DWORD)]


PMIB_IFNUMBER = POINTER(MIB_IFNUMBER)


class MIB_IFROW(Structure):
    _fields_ = [
        ("wszName", WCHAR * MAX_INTERFACE_NAME_LEN),
        ("dwIndex", IF_INDEX),
        ("dwType", IFTYPE),
        ("dwMtu", DWORD),
        ("dwSpeed", DWORD),
        ("dwPhysAddrLen", DWORD),
        ("bPhysAddr", UCHAR * MAXLEN_PHYSADDR),
        ("dwAdminStatus", DWORD),
        ("dwOperStatus", INTERNAL_IF_OPER_STATUS),
        ("dwLastChange", DWORD),
        ("dwInOctets", DWORD),
        ("dwInUcastPkts", DWORD),
        ("dwInNUcastPkts", DWORD),
        ("dwInDiscards", DWORD),
        ("dwInErrors", DWORD),
        ("dwInUnknownProtos", DWORD),
        ("dwOutOctets", DWORD),
        ("dwOutUcastPkts", DWORD),
        ("dwOutNUcastPkts", DWORD),
        ("dwOutDiscards", DWORD),
        ("dwOutErrors", DWORD),
        ("dwOutQLen", DWORD),
        ("dwDescrLen", DWORD),
        ("bDescr", UCHAR * MAXLEN_IFDESCR),
    ]


PMIB_IFROW = POINTER(MIB_IFROW)


class MIB_IFTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_IFROW * ANYSIZE_ARRAY)]


PMIB_IFTABLE = POINTER(MIB_IFTABLE)
