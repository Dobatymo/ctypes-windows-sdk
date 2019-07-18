from ctypes import POINTER
from ctypes.wintypes import DWORD, HANDLE

from .. import windll, s_ok
from ..shared.ntdef import HRESULT, PWSTR
from ..shared.guiddef import GUID
from .shtypes import REFKNOWNFOLDERID

SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
SHGetKnownFolderPath.argtypes = [REFKNOWNFOLDERID, DWORD, HANDLE, POINTER(PWSTR)]
SHGetKnownFolderPath.restype = HRESULT
SHGetKnownFolderPath.errcheck = s_ok
