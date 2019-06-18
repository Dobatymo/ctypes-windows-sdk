from ctypes import POINTER

from .. import windll
from ..shared.guiddef import GUID

KNOWNFOLDERID = GUID
REFKNOWNFOLDERID = POINTER(KNOWNFOLDERID)
