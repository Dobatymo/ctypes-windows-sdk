from ctypes import POINTER, Structure, c_ubyte, c_ulong, c_ushort


class GUID(Structure):
    _fields_ = [
        ("Data1", c_ulong),
        ("Data2", c_ushort),
        ("Data3", c_ushort),
        ("Data4", c_ubyte * 8),
    ]

    def __str__(self) -> str:
        return f"{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-{bytes(self.Data4)[:2].hex().zfill(4)}-{bytes(self.Data4)[2:].hex().zfill(12)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, GUID):
            return memoryview(self).cast("B") == memoryview(other).cast("B")
        return NotImplemented

    def __hash__(self):
        return hash(bytes(self))


IID = GUID
LPIID = POINTER(IID)
CLSID = GUID
LPCLSID = POINTER(CLSID)
FMTID = GUID
LPFMTID = POINTER(FMTID)
REFCLSID = POINTER(IID)  # const POINTER
REFIID = POINTER(IID)  # const POINTER
