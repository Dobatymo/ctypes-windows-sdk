from ctypes import Structure
from ctypes.wintypes import DWORD, LONG

COLORREF = DWORD


class POINTL(Structure):
    _fields_ = [
        ("x", LONG),
        ("y", LONG),
    ]
