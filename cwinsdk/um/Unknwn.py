from ctypes import POINTER, Structure


class IUnknown(Structure):
    pass


LPUNKNOWN = POINTER(IUnknown)
