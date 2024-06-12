import re
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

    def __repr__(self) -> str:
        return f"GUID.from_str('{str(self)}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, GUID):
            return memoryview(self).cast("B") == memoryview(other).cast("B")
        return NotImplemented

    def __hash__(self):
        return hash(bytes(self))

    @classmethod
    def from_str(cls, s: str) -> "GUID":
        m = re.match(r"^{?([0-9a-f]{8})-([0-9a-f]{4})-([0-9a-f]{4})-([0-9a-f]{4})-([0-9a-f]{12})}?$", s)
        if m is None:
            raise ValueError(f"Invalid GUID: {s}")

        groups = m.groups()
        d1 = int(groups[0], 16)
        d2 = int(groups[1], 16)
        d3 = int(groups[2], 16)
        d4 = (c_ubyte * 8).from_buffer(bytearray.fromhex(groups[3] + groups[4]))
        return cls(d1, d2, d3, d4)


def DEFINE_GUID(l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8) -> GUID:
    return GUID(l, w1, w2, (b1, b2, b3, b4, b5, b6, b7, b8))


IID = GUID
LPIID = POINTER(IID)
CLSID = GUID
LPCLSID = POINTER(CLSID)
FMTID = GUID
LPFMTID = POINTER(FMTID)
REFCLSID = POINTER(IID)  # const POINTER
REFIID = POINTER(IID)  # const POINTER
