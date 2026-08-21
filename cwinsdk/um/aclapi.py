from ctypes import POINTER, WINFUNCTYPE
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCSTR, LPCWSTR, LPSTR, LPWSTR, PULONG, ULONG, USHORT

from .. import error_success, windll
from ..shared.guiddef import GUID
from ..shared.ntdef import PVOID
from .accctrl import (
    ACCESS_MODE,
    EXPLICIT_ACCESS_A,
    EXPLICIT_ACCESS_W,
    FN_OBJECT_MGR_FUNCTS,
    INHERITED_FROMA,
    INHERITED_FROMW,
    MULTIPLE_TRUSTEE_OPERATION,
    OBJECTS_AND_NAME_A,
    OBJECTS_AND_NAME_W,
    OBJECTS_AND_SID,
    PROG_INVOKE_SETTING,
    SE_OBJECT_TYPE,
    TRUSTEE_A,
    TRUSTEE_FORM,
    TRUSTEE_TYPE,
    TRUSTEE_W,
)
from .winnt import ACCESS_MASK, PACL, PGENERIC_MAPPING, PSID, SECURITY_DESCRIPTOR, SECURITY_INFORMATION

FN_PROGRESS = WINFUNCTYPE(
    None,
    LPWSTR,
    DWORD,
    POINTER(PROG_INVOKE_SETTING),
    PVOID,
    BOOL,
)

SetEntriesInAclA = windll.advapi32.SetEntriesInAclA
SetEntriesInAclA.argtypes = [ULONG, POINTER(EXPLICIT_ACCESS_A), PACL, POINTER(PACL)]
SetEntriesInAclA.restype = DWORD

SetEntriesInAclW = windll.advapi32.SetEntriesInAclW
SetEntriesInAclW.argtypes = [ULONG, POINTER(EXPLICIT_ACCESS_W), PACL, POINTER(PACL)]
SetEntriesInAclW.restype = DWORD

GetExplicitEntriesFromAclA = windll.advapi32.GetExplicitEntriesFromAclA
GetExplicitEntriesFromAclA.argtypes = [PACL, PULONG, POINTER(POINTER(EXPLICIT_ACCESS_A))]
GetExplicitEntriesFromAclA.restype = DWORD

GetExplicitEntriesFromAclW = windll.advapi32.GetExplicitEntriesFromAclW
GetExplicitEntriesFromAclW.argtypes = [PACL, PULONG, POINTER(POINTER(EXPLICIT_ACCESS_W))]
GetExplicitEntriesFromAclW.restype = DWORD

GetEffectiveRightsFromAclA = windll.advapi32.GetEffectiveRightsFromAclA
GetEffectiveRightsFromAclA.argtypes = [PACL, POINTER(TRUSTEE_A), POINTER(ACCESS_MASK)]
GetEffectiveRightsFromAclA.restype = DWORD

GetEffectiveRightsFromAclW = windll.advapi32.GetEffectiveRightsFromAclW
GetEffectiveRightsFromAclW.argtypes = [PACL, POINTER(TRUSTEE_W), POINTER(ACCESS_MASK)]
GetEffectiveRightsFromAclW.restype = DWORD

GetAuditedPermissionsFromAclA = windll.advapi32.GetAuditedPermissionsFromAclA
GetAuditedPermissionsFromAclA.argtypes = [PACL, POINTER(TRUSTEE_A), POINTER(ACCESS_MASK), POINTER(ACCESS_MASK)]
GetAuditedPermissionsFromAclA.restype = DWORD

GetAuditedPermissionsFromAclW = windll.advapi32.GetAuditedPermissionsFromAclW
GetAuditedPermissionsFromAclW.argtypes = [PACL, POINTER(TRUSTEE_W), POINTER(ACCESS_MASK), POINTER(ACCESS_MASK)]
GetAuditedPermissionsFromAclW.restype = DWORD

GetNamedSecurityInfoA = windll.advapi32.GetNamedSecurityInfoA
GetNamedSecurityInfoA.argtypes = [
    LPCSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    POINTER(PSID),
    POINTER(PSID),
    POINTER(PACL),
    POINTER(PACL),
    POINTER(POINTER(SECURITY_DESCRIPTOR)),
]
GetNamedSecurityInfoA.restype = DWORD
GetNamedSecurityInfoA.errcheck = error_success

GetNamedSecurityInfoW = windll.advapi32.GetNamedSecurityInfoW
GetNamedSecurityInfoW.argtypes = [
    LPCWSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    POINTER(PSID),
    POINTER(PSID),
    POINTER(PACL),
    POINTER(PACL),
    POINTER(POINTER(SECURITY_DESCRIPTOR)),
]
GetNamedSecurityInfoW.restype = DWORD
GetNamedSecurityInfoW.errcheck = error_success

GetSecurityInfo = windll.advapi32.GetSecurityInfo
GetSecurityInfo.argtypes = [
    HANDLE,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    POINTER(PSID),
    POINTER(PSID),
    POINTER(PACL),
    POINTER(PACL),
    POINTER(POINTER(SECURITY_DESCRIPTOR)),
]
GetSecurityInfo.restype = DWORD
GetSecurityInfo.errcheck = error_success

SetNamedSecurityInfoA = windll.advapi32.SetNamedSecurityInfoA
SetNamedSecurityInfoA.argtypes = [LPSTR, SE_OBJECT_TYPE, SECURITY_INFORMATION, PSID, PSID, PACL, PACL]
SetNamedSecurityInfoA.restype = DWORD

SetNamedSecurityInfoW = windll.advapi32.SetNamedSecurityInfoW
SetNamedSecurityInfoW.argtypes = [LPWSTR, SE_OBJECT_TYPE, SECURITY_INFORMATION, PSID, PSID, PACL, PACL]
SetNamedSecurityInfoW.restype = DWORD

SetSecurityInfo = windll.advapi32.SetSecurityInfo
SetSecurityInfo.argtypes = [HANDLE, SE_OBJECT_TYPE, SECURITY_INFORMATION, PSID, PSID, PACL, PACL]
SetSecurityInfo.restype = DWORD

GetInheritanceSourceA = windll.advapi32.GetInheritanceSourceA
GetInheritanceSourceA.argtypes = [
    LPSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    BOOL,
    POINTER(POINTER(GUID)),
    DWORD,
    PACL,
    POINTER(FN_OBJECT_MGR_FUNCTS),
    PGENERIC_MAPPING,
    POINTER(INHERITED_FROMA),
]
GetInheritanceSourceA.restype = DWORD
GetInheritanceSourceA.errcheck = error_success

GetInheritanceSourceW = windll.advapi32.GetInheritanceSourceW
GetInheritanceSourceW.argtypes = [
    LPWSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    BOOL,
    POINTER(POINTER(GUID)),
    DWORD,
    PACL,
    POINTER(FN_OBJECT_MGR_FUNCTS),
    PGENERIC_MAPPING,
    POINTER(INHERITED_FROMW),
]
GetInheritanceSourceW.restype = DWORD
GetInheritanceSourceW.errcheck = error_success

FreeInheritedFromArray = windll.advapi32.FreeInheritedFromArray
FreeInheritedFromArray.argtypes = [POINTER(INHERITED_FROMW), USHORT, POINTER(FN_OBJECT_MGR_FUNCTS)]
FreeInheritedFromArray.restype = DWORD

TreeResetNamedSecurityInfoA = windll.advapi32.TreeResetNamedSecurityInfoA
TreeResetNamedSecurityInfoA.argtypes = [
    LPSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    PSID,
    PSID,
    PACL,
    PACL,
    BOOL,
    FN_PROGRESS,
    PROG_INVOKE_SETTING,
    PVOID,
]
TreeResetNamedSecurityInfoA.restype = DWORD

TreeResetNamedSecurityInfoW = windll.advapi32.TreeResetNamedSecurityInfoW
TreeResetNamedSecurityInfoW.argtypes = [
    LPWSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    PSID,
    PSID,
    PACL,
    PACL,
    BOOL,
    FN_PROGRESS,
    PROG_INVOKE_SETTING,
    PVOID,
]
TreeResetNamedSecurityInfoW.restype = DWORD

TreeSetNamedSecurityInfoA = windll.advapi32.TreeSetNamedSecurityInfoA
TreeSetNamedSecurityInfoA.argtypes = [
    LPSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    PSID,
    PSID,
    PACL,
    PACL,
    DWORD,
    FN_PROGRESS,
    PROG_INVOKE_SETTING,
    PVOID,
]
TreeSetNamedSecurityInfoA.restype = DWORD

TreeSetNamedSecurityInfoW = windll.advapi32.TreeSetNamedSecurityInfoW
TreeSetNamedSecurityInfoW.argtypes = [
    LPWSTR,
    SE_OBJECT_TYPE,
    SECURITY_INFORMATION,
    PSID,
    PSID,
    PACL,
    PACL,
    DWORD,
    FN_PROGRESS,
    PROG_INVOKE_SETTING,
    PVOID,
]
TreeSetNamedSecurityInfoW.restype = DWORD

BuildSecurityDescriptorA = windll.advapi32.BuildSecurityDescriptorA
BuildSecurityDescriptorA.argtypes = [
    POINTER(TRUSTEE_A),
    POINTER(TRUSTEE_A),
    ULONG,
    POINTER(EXPLICIT_ACCESS_A),
    ULONG,
    POINTER(EXPLICIT_ACCESS_A),
    POINTER(SECURITY_DESCRIPTOR),
    PULONG,
    POINTER(POINTER(SECURITY_DESCRIPTOR)),
]
BuildSecurityDescriptorA.restype = DWORD

BuildSecurityDescriptorW = windll.advapi32.BuildSecurityDescriptorW
BuildSecurityDescriptorW.argtypes = [
    POINTER(TRUSTEE_W),
    POINTER(TRUSTEE_W),
    ULONG,
    POINTER(EXPLICIT_ACCESS_W),
    ULONG,
    POINTER(EXPLICIT_ACCESS_W),
    POINTER(SECURITY_DESCRIPTOR),
    PULONG,
    POINTER(POINTER(SECURITY_DESCRIPTOR)),
]
BuildSecurityDescriptorW.restype = DWORD

LookupSecurityDescriptorPartsA = windll.advapi32.LookupSecurityDescriptorPartsA
LookupSecurityDescriptorPartsA.argtypes = [
    POINTER(POINTER(TRUSTEE_A)),
    POINTER(POINTER(TRUSTEE_A)),
    PULONG,
    POINTER(POINTER(EXPLICIT_ACCESS_A)),
    PULONG,
    POINTER(POINTER(EXPLICIT_ACCESS_A)),
    POINTER(SECURITY_DESCRIPTOR),
]
LookupSecurityDescriptorPartsA.restype = DWORD

LookupSecurityDescriptorPartsW = windll.advapi32.LookupSecurityDescriptorPartsW
LookupSecurityDescriptorPartsW.argtypes = [
    POINTER(POINTER(TRUSTEE_W)),
    POINTER(POINTER(TRUSTEE_W)),
    PULONG,
    POINTER(POINTER(EXPLICIT_ACCESS_W)),
    PULONG,
    POINTER(POINTER(EXPLICIT_ACCESS_W)),
    POINTER(SECURITY_DESCRIPTOR),
]
LookupSecurityDescriptorPartsW.restype = DWORD

BuildExplicitAccessWithNameA = windll.advapi32.BuildExplicitAccessWithNameA
BuildExplicitAccessWithNameA.argtypes = [POINTER(EXPLICIT_ACCESS_A), LPSTR, DWORD, ACCESS_MODE, DWORD]
BuildExplicitAccessWithNameA.restype = None

BuildExplicitAccessWithNameW = windll.advapi32.BuildExplicitAccessWithNameW
BuildExplicitAccessWithNameW.argtypes = [POINTER(EXPLICIT_ACCESS_W), LPWSTR, DWORD, ACCESS_MODE, DWORD]
BuildExplicitAccessWithNameW.restype = None

BuildImpersonateExplicitAccessWithNameA = windll.advapi32.BuildImpersonateExplicitAccessWithNameA
BuildImpersonateExplicitAccessWithNameA.argtypes = [
    POINTER(EXPLICIT_ACCESS_A),
    LPSTR,
    POINTER(TRUSTEE_A),
    DWORD,
    ACCESS_MODE,
    DWORD,
]
BuildImpersonateExplicitAccessWithNameA.restype = None

BuildImpersonateExplicitAccessWithNameW = windll.advapi32.BuildImpersonateExplicitAccessWithNameW
BuildImpersonateExplicitAccessWithNameW.argtypes = [
    POINTER(EXPLICIT_ACCESS_W),
    LPWSTR,
    POINTER(TRUSTEE_W),
    DWORD,
    ACCESS_MODE,
    DWORD,
]
BuildImpersonateExplicitAccessWithNameW.restype = None

BuildTrusteeWithNameA = windll.advapi32.BuildTrusteeWithNameA
BuildTrusteeWithNameA.argtypes = [POINTER(TRUSTEE_A), LPSTR]
BuildTrusteeWithNameA.restype = None

BuildTrusteeWithNameW = windll.advapi32.BuildTrusteeWithNameW
BuildTrusteeWithNameW.argtypes = [POINTER(TRUSTEE_W), LPWSTR]
BuildTrusteeWithNameW.restype = None

BuildImpersonateTrusteeA = windll.advapi32.BuildImpersonateTrusteeA
BuildImpersonateTrusteeA.argtypes = [POINTER(TRUSTEE_A), POINTER(TRUSTEE_A)]
BuildImpersonateTrusteeA.restype = None

BuildImpersonateTrusteeW = windll.advapi32.BuildImpersonateTrusteeW
BuildImpersonateTrusteeW.argtypes = [POINTER(TRUSTEE_W), POINTER(TRUSTEE_W)]
BuildImpersonateTrusteeW.restype = None

BuildTrusteeWithSidA = windll.advapi32.BuildTrusteeWithSidA
BuildTrusteeWithSidA.argtypes = [POINTER(TRUSTEE_A), PSID]
BuildTrusteeWithSidA.restype = None

BuildTrusteeWithSidW = windll.advapi32.BuildTrusteeWithSidW
BuildTrusteeWithSidW.argtypes = [POINTER(TRUSTEE_W), PSID]
BuildTrusteeWithSidW.restype = None

BuildTrusteeWithObjectsAndSidA = windll.advapi32.BuildTrusteeWithObjectsAndSidA
BuildTrusteeWithObjectsAndSidA.argtypes = [
    POINTER(TRUSTEE_A),
    POINTER(OBJECTS_AND_SID),
    POINTER(GUID),
    POINTER(GUID),
    PSID,
]
BuildTrusteeWithObjectsAndSidA.restype = None

BuildTrusteeWithObjectsAndSidW = windll.advapi32.BuildTrusteeWithObjectsAndSidW
BuildTrusteeWithObjectsAndSidW.argtypes = [
    POINTER(TRUSTEE_W),
    POINTER(OBJECTS_AND_SID),
    POINTER(GUID),
    POINTER(GUID),
    PSID,
]
BuildTrusteeWithObjectsAndSidW.restype = None

BuildTrusteeWithObjectsAndNameA = windll.advapi32.BuildTrusteeWithObjectsAndNameA
BuildTrusteeWithObjectsAndNameA.argtypes = [
    POINTER(TRUSTEE_A),
    POINTER(OBJECTS_AND_NAME_A),
    SE_OBJECT_TYPE,
    LPSTR,
    LPSTR,
    LPSTR,
]
BuildTrusteeWithObjectsAndNameA.restype = None

BuildTrusteeWithObjectsAndNameW = windll.advapi32.BuildTrusteeWithObjectsAndNameW
BuildTrusteeWithObjectsAndNameW.argtypes = [
    POINTER(TRUSTEE_W),
    POINTER(OBJECTS_AND_NAME_W),
    SE_OBJECT_TYPE,
    LPWSTR,
    LPWSTR,
    LPWSTR,
]
BuildTrusteeWithObjectsAndNameW.restype = None

GetTrusteeNameA = windll.advapi32.GetTrusteeNameA
GetTrusteeNameA.argtypes = [POINTER(TRUSTEE_A)]
GetTrusteeNameA.restype = LPSTR

GetTrusteeNameW = windll.advapi32.GetTrusteeNameW
GetTrusteeNameW.argtypes = [POINTER(TRUSTEE_W)]
GetTrusteeNameW.restype = LPWSTR

GetTrusteeTypeA = windll.advapi32.GetTrusteeTypeA
GetTrusteeTypeA.argtypes = [POINTER(TRUSTEE_A)]
GetTrusteeTypeA.restype = TRUSTEE_TYPE

GetTrusteeTypeW = windll.advapi32.GetTrusteeTypeW
GetTrusteeTypeW.argtypes = [POINTER(TRUSTEE_W)]
GetTrusteeTypeW.restype = TRUSTEE_TYPE

GetTrusteeFormA = windll.advapi32.GetTrusteeFormA
GetTrusteeFormA.argtypes = [POINTER(TRUSTEE_A)]
GetTrusteeFormA.restype = TRUSTEE_FORM

GetTrusteeFormW = windll.advapi32.GetTrusteeFormW
GetTrusteeFormW.argtypes = [POINTER(TRUSTEE_W)]
GetTrusteeFormW.restype = TRUSTEE_FORM

GetMultipleTrusteeOperationA = windll.advapi32.GetMultipleTrusteeOperationA
GetMultipleTrusteeOperationA.argtypes = [POINTER(TRUSTEE_A)]
GetMultipleTrusteeOperationA.restype = MULTIPLE_TRUSTEE_OPERATION

GetMultipleTrusteeOperationW = windll.advapi32.GetMultipleTrusteeOperationW
GetMultipleTrusteeOperationW.argtypes = [POINTER(TRUSTEE_W)]
GetMultipleTrusteeOperationW.restype = MULTIPLE_TRUSTEE_OPERATION

GetMultipleTrusteeA = windll.advapi32.GetMultipleTrusteeA
GetMultipleTrusteeA.argtypes = [POINTER(TRUSTEE_A)]
GetMultipleTrusteeA.restype = POINTER(TRUSTEE_A)

GetMultipleTrusteeW = windll.advapi32.GetMultipleTrusteeW
GetMultipleTrusteeW.argtypes = [POINTER(TRUSTEE_W)]
GetMultipleTrusteeW.restype = POINTER(TRUSTEE_W)
