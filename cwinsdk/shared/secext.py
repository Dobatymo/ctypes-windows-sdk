from ctypes.wintypes import BOOLEAN, LPCSTR, LPCWSTR, LPSTR, LPWSTR

from .. import CEnum, windll
from .minwindef import PULONG


class EXTENDED_NAME_FORMAT(CEnum):
    NameUnknown = 0
    NameFullyQualifiedDN = 1
    NameSamCompatible = 2
    NameDisplay = 3
    NameUniqueId = 6
    NameCanonical = 7
    NameUserPrincipal = 8
    NameCanonicalEx = 9
    NameServicePrincipal = 10
    NameDnsDomain = 12
    NameGivenName = 13
    NameSurname = 14


GetUserNameExA = windll.secur32.GetUserNameExA
GetUserNameExA.argtypes = [EXTENDED_NAME_FORMAT, LPSTR, PULONG]
GetUserNameExA.restype = BOOLEAN

GetUserNameExW = windll.secur32.GetUserNameExW
GetUserNameExW.argtypes = [EXTENDED_NAME_FORMAT, LPWSTR, PULONG]
GetUserNameExW.restype = BOOLEAN

GetComputerObjectNameA = windll.secur32.GetComputerObjectNameA
GetComputerObjectNameA.argtypes = [EXTENDED_NAME_FORMAT, LPSTR, PULONG]
GetComputerObjectNameA.restype = BOOLEAN

GetComputerObjectNameW = windll.secur32.GetComputerObjectNameW
GetComputerObjectNameW.argtypes = [EXTENDED_NAME_FORMAT, LPWSTR, PULONG]
GetComputerObjectNameW.restype = BOOLEAN

TranslateNameA = windll.secur32.TranslateNameA
TranslateNameA.argtypes = [LPCSTR, EXTENDED_NAME_FORMAT, EXTENDED_NAME_FORMAT, LPSTR, PULONG]
TranslateNameA.restype = BOOLEAN

TranslateNameW = windll.secur32.TranslateNameW
TranslateNameW.argtypes = [LPCWSTR, EXTENDED_NAME_FORMAT, EXTENDED_NAME_FORMAT, LPWSTR, PULONG]
TranslateNameW.restype = BOOLEAN
