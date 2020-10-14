from ctypes.wintypes import DWORD, LPVOID

from .. import windll
from ..shared.basetsd import SIZE_T
from ..shared.guiddef import LPIID, REFCLSID, REFIID
from ..shared.ntdef import HRESULT
from ..shared.WTypesbase import LPCOLESTR
from .Unknwn import LPUNKNOWN

CoCreateInstance = windll.ole32.CoCreateInstance
CoCreateInstance.argtypes = [REFCLSID, LPUNKNOWN, DWORD, REFIID, LPVOID]
CoCreateInstance.restype = HRESULT

CoInitializeEx = windll.ole32.CoInitializeEx
CoInitializeEx.argtypes = [LPVOID, DWORD]
CoInitializeEx.restype = HRESULT

CoTaskMemAlloc = windll.ole32.CoTaskMemAlloc
CoTaskMemAlloc.argtypes = [SIZE_T]
CoTaskMemAlloc.restype = LPVOID

CoTaskMemFree = windll.ole32.CoTaskMemFree
CoTaskMemFree.argtypes = [LPVOID]
CoTaskMemFree.restype = None

CoUninitialize = windll.ole32.CoUninitialize
CoUninitialize.argtypes = []
CoUninitialize.restype = None

IIDFromString = windll.ole32.IIDFromString
IIDFromString.argtypes = [LPCOLESTR, LPIID]
IIDFromString.restype = HRESULT
