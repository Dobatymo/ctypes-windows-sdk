from ctypes import POINTER, Structure, Union, c_ubyte, c_ulong, c_ushort


class GUID(Structure):
    _fields_ = [
        ("Data1", c_ulong),
        ("Data2", c_ushort),
        ("Data3", c_ushort),
        ("Data4", c_ubyte * 8),
    ]


IID = GUID
LPIID = POINTER(IID)
CLSID = GUID
LPCLSID = POINTER(CLSID)
FMTID = GUID
LPFMTID = POINTER(FMTID)
REFCLSID = POINTER(IID)  # const POINTER
REFIID = POINTER(IID)  # const POINTER
