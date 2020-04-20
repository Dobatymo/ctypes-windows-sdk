from ctypes import Structure, POINTER

class IUnknown(Structure):
	pass

LPUNKNOWN = POINTER(IUnknown)
