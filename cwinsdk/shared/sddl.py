from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, LPCSTR, LPCWSTR, LPSTR, LPWSTR

from .. import nonfalse, windll
from ..shared.minwindef import PULONG
from ..um.winnt import PSECURITY_DESCRIPTOR, PSID, SECURITY_INFORMATION

SDDL_REVISION_1 = 1
SDDL_REVISION = SDDL_REVISION_1

ConvertSidToStringSidA = windll.advapi32.ConvertSidToStringSidA
ConvertSidToStringSidA.argtypes = [PSID, POINTER(LPSTR)]
ConvertSidToStringSidA.restype = BOOL
ConvertSidToStringSidA.errcheck = nonfalse

ConvertSidToStringSidW = windll.advapi32.ConvertSidToStringSidW
ConvertSidToStringSidW.argtypes = [PSID, POINTER(LPWSTR)]
ConvertSidToStringSidW.restype = BOOL
ConvertSidToStringSidW.errcheck = nonfalse

ConvertStringSidToSidA = windll.advapi32.ConvertStringSidToSidA
ConvertStringSidToSidA.argtypes = [LPCSTR, POINTER(PSID)]
ConvertStringSidToSidA.restype = BOOL
ConvertStringSidToSidA.errcheck = nonfalse

ConvertStringSidToSidW = windll.advapi32.ConvertStringSidToSidW
ConvertStringSidToSidW.argtypes = [LPCWSTR, POINTER(PSID)]
ConvertStringSidToSidW.restype = BOOL
ConvertStringSidToSidW.errcheck = nonfalse

ConvertStringSecurityDescriptorToSecurityDescriptorA = (
    windll.advapi32.ConvertStringSecurityDescriptorToSecurityDescriptorA
)
ConvertStringSecurityDescriptorToSecurityDescriptorA.argtypes = [
    LPCSTR,
    DWORD,
    POINTER(PSECURITY_DESCRIPTOR),
    PULONG,
]
ConvertStringSecurityDescriptorToSecurityDescriptorA.restype = BOOL
ConvertStringSecurityDescriptorToSecurityDescriptorA.errcheck = nonfalse

ConvertStringSecurityDescriptorToSecurityDescriptorW = (
    windll.advapi32.ConvertStringSecurityDescriptorToSecurityDescriptorW
)
ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [
    LPCWSTR,
    DWORD,
    POINTER(PSECURITY_DESCRIPTOR),
    PULONG,
]
ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = BOOL
ConvertStringSecurityDescriptorToSecurityDescriptorW.errcheck = nonfalse

ConvertSecurityDescriptorToStringSecurityDescriptorA = (
    windll.advapi32.ConvertSecurityDescriptorToStringSecurityDescriptorA
)
ConvertSecurityDescriptorToStringSecurityDescriptorA.argtypes = [
    PSECURITY_DESCRIPTOR,
    DWORD,
    SECURITY_INFORMATION,
    POINTER(LPSTR),
    PULONG,
]
ConvertSecurityDescriptorToStringSecurityDescriptorA.restype = BOOL
ConvertSecurityDescriptorToStringSecurityDescriptorA.errcheck = nonfalse

ConvertSecurityDescriptorToStringSecurityDescriptorW = (
    windll.advapi32.ConvertSecurityDescriptorToStringSecurityDescriptorW
)
ConvertSecurityDescriptorToStringSecurityDescriptorW.argtypes = [
    PSECURITY_DESCRIPTOR,
    DWORD,
    SECURITY_INFORMATION,
    POINTER(LPWSTR),
    PULONG,
]
ConvertSecurityDescriptorToStringSecurityDescriptorW.restype = BOOL
ConvertSecurityDescriptorToStringSecurityDescriptorW.errcheck = nonfalse
