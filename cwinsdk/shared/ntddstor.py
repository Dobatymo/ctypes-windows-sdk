from ctypes import POINTER, Structure
from ctypes.wintypes import ULONG

from .. import CEnum
from .ntdef import UCHAR


class STORAGE_BUS_TYPE(CEnum):
    BusTypeUnknown = 0x00
    BusTypeScsi = 0x1
    BusTypeAtapi = 0x2
    BusTypeAta = 0x3
    BusType1394 = 0x4
    BusTypeSsa = 0x5
    BusTypeFibre = 0x6
    BusTypeUsb = 0x7
    BusTypeRAID = 0x8
    BusTypeiScsi = 0x9
    BusTypeSas = 0xA
    BusTypeSata = 0xB
    BusTypeSd = 0xC
    BusTypeMmc = 0xD
    BusTypeVirtual = 0xE
    BusTypeFileBackedVirtual = 0xF
    BusTypeSpaces = 0x10
    BusTypeNvme = 0x11
    BusTypeSCM = 0x12
    BusTypeUfs = 0x13
    BusTypeNvmeof = 0x14
    BusTypeMax = 0x15
    BusTypeMaxReserved = 0x7F


# IOCTL_STORAGE_PREDICT_FAILURE
# input - none
# output - STORAGE_PREDICT_FAILURE structure
#          PredictFailure returns zero if no failure predicted and non zero
#                         if a failure is predicted.
#          VendorSpecific returns 512 bytes of vendor specific information
#                         if a failure is predicted
class STORAGE_PREDICT_FAILURE(Structure):
    _fields_ = [
        ("PredictFailure", ULONG),
        ("VendorSpecific", UCHAR * 512),
    ]


PSTORAGE_PREDICT_FAILURE = POINTER(STORAGE_PREDICT_FAILURE)
