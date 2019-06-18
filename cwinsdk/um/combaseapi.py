from ctypes.wintypes import LPVOID

from .. import windll

CoTaskMemFree = windll.ole32.CoTaskMemFree
CoTaskMemFree.argtypes = [LPVOID]
CoTaskMemFree.restype = None
