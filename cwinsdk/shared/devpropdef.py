from ctypes import Structure
from ctypes.wintypes import ULONG

from .guiddef import GUID

DEVPROPTYPE = ULONG

DEVPROP_TYPEMOD_ARRAY = 0x00001000  # array of fixed-sized data elements
DEVPROP_TYPEMOD_LIST = 0x00002000  # list of variable-sized data elements

DEVPROP_TYPE_EMPTY = 0x00000000  # nothing, no property data
DEVPROP_TYPE_NULL = 0x00000001  # null property data
DEVPROP_TYPE_SBYTE = 0x00000002  # 8-bit signed int (SBYTE)
DEVPROP_TYPE_BYTE = 0x00000003  # 8-bit unsigned int (BYTE)
DEVPROP_TYPE_INT16 = 0x00000004  # 16-bit signed int (SHORT)
DEVPROP_TYPE_UINT16 = 0x00000005  # 16-bit unsigned int (USHORT)
DEVPROP_TYPE_INT32 = 0x00000006  # 32-bit signed int (LONG)
DEVPROP_TYPE_UINT32 = 0x00000007  # 32-bit unsigned int (ULONG)
DEVPROP_TYPE_INT64 = 0x00000008  # 64-bit signed int (LONG64)
DEVPROP_TYPE_UINT64 = 0x00000009  # 64-bit unsigned int (ULONG64)
DEVPROP_TYPE_FLOAT = 0x0000000A  # 32-bit floating-point (FLOAT)
DEVPROP_TYPE_DOUBLE = 0x0000000B  # 64-bit floating-point (DOUBLE)
DEVPROP_TYPE_DECIMAL = 0x0000000C  # 128-bit data (DECIMAL)
DEVPROP_TYPE_GUID = 0x0000000D  # 128-bit unique identifier (GUID)
DEVPROP_TYPE_CURRENCY = 0x0000000E  # 64 bit signed int currency value (CURRENCY)
DEVPROP_TYPE_DATE = 0x0000000F  # date (DATE)
DEVPROP_TYPE_FILETIME = 0x00000010  # file time (FILETIME)
DEVPROP_TYPE_BOOLEAN = 0x00000011  # 8-bit boolean (DEVPROP_BOOLEAN)
DEVPROP_TYPE_STRING = 0x00000012  # null-terminated string
DEVPROP_TYPE_STRING_LIST = DEVPROP_TYPE_STRING | DEVPROP_TYPEMOD_LIST  # multi-sz string list
DEVPROP_TYPE_SECURITY_DESCRIPTOR = 0x00000013  # self-relative binary SECURITY_DESCRIPTOR
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = 0x00000014  # security descriptor string (SDDL format)
DEVPROP_TYPE_DEVPROPKEY = 0x00000015  # device property key (DEVPROPKEY)
DEVPROP_TYPE_DEVPROPTYPE = 0x00000016  # device property type (DEVPROPTYPE)
DEVPROP_TYPE_BINARY = DEVPROP_TYPE_BYTE | DEVPROP_TYPEMOD_ARRAY  # custom binary data
DEVPROP_TYPE_ERROR = 0x00000017  # 32-bit Win32 system error code
DEVPROP_TYPE_NTSTATUS = 0x00000018  # 32-bit NTSTATUS code
DEVPROP_TYPE_STRING_INDIRECT = 0x00000019  # string resource (@[path\]<dllname>,-<strId>)

MAX_DEVPROP_TYPE = 0x00000019  # max valid DEVPROP_TYPE_ value
MAX_DEVPROP_TYPEMOD = 0x00002000  # max valid DEVPROP_TYPEMOD_ value

DEVPROP_MASK_TYPE = 0x00000FFF  # range for base DEVPROP_TYPE_ values
DEVPROP_MASK_TYPEMOD = 0x0000F000  # mask for DEVPROP_TYPEMOD_ type modifiers


DEVPROPGUID = GUID
DEVPROPID = ULONG


class DEVPROPKEY(Structure):
    _fields_ = [
        ("fmtid", DEVPROPGUID),
        ("pid", DEVPROPID),
    ]


def DEFINE_DEVPROPKEY(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8, pid):
    return DEVPROPKEY((l, w1, w2, (b1, b2, b3, b4, b5, b6, b7, b8)), pid)
