from ctypes import c_int
from ctypes.wintypes import BYTE


class BOOLEAN(BYTE):
    __slots__ = ()
    pass


class BOOL(c_int):
    __slots__ = ()
    pass
