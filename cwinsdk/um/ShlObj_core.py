from ctypes import POINTER
from ctypes.wintypes import DWORD, HANDLE, UINT

from .. import s_ok, windll
from ..shared.guiddef import GUID
from ..shared.ntdef import HRESULT, PWSTR
from .shtypes import PCIDLIST_ABSOLUTE, PCUITEMID_CHILD_ARRAY, REFKNOWNFOLDERID

SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
SHGetKnownFolderPath.argtypes = [REFKNOWNFOLDERID, DWORD, HANDLE, POINTER(PWSTR)]
SHGetKnownFolderPath.restype = HRESULT
SHGetKnownFolderPath.errcheck = s_ok

SHOpenFolderAndSelectItems = windll.shell32.SHOpenFolderAndSelectItems
SHOpenFolderAndSelectItems.argtypes = [PCIDLIST_ABSOLUTE, UINT, PCUITEMID_CHILD_ARRAY, DWORD]
SHOpenFolderAndSelectItems.restype = None
