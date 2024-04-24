from ctypes import POINTER
from ctypes.wintypes import BOOL, BOOLEAN, BYTE, DWORD, HANDLE, LONG, LPCWSTR, LPVOID, LPWSTR, ULONG

from .. import nonzero, windll
from ..km.wdm import SECURITY_IMPERSONATION_LEVEL
from ..shared.guiddef import GUID
from ..shared.minwindef import LPBOOL, LPDWORD, PBOOL, PDWORD, PUCHAR, PULONG, UCHAR
from ..shared.ntdef import PVOID
from .minwinbase import SECURITY_ATTRIBUTES
from .winnt import (
    ACL_INFORMATION_CLASS,
    AUDIT_EVENT_TYPE,
    CLAIM_SECURITY_ATTRIBUTES_INFORMATION,
    LUID,
    LUID_AND_ATTRIBUTES,
    PACL,
    PCWSTR,
    PGENERIC_MAPPING,
    PHANDLE,
    POBJECT_TYPE_LIST,
    PPRIVILEGE_SET,
    PSECURITY_DESCRIPTOR,
    PSID,
    PTOKEN_PRIVILEGES,
    SECURITY_DESCRIPTOR_CONTROL,
    SECURITY_INFORMATION,
    SID_AND_ATTRIBUTES,
    SID_IDENTIFIER_AUTHORITY,
    TOKEN_GROUPS,
    TOKEN_INFORMATION_CLASS,
    TOKEN_TYPE,
    WELL_KNOWN_SID_TYPE,
)

AccessCheck = windll.advapi32.AccessCheck
AccessCheck.argtypes = [PSECURITY_DESCRIPTOR, HANDLE, DWORD, PGENERIC_MAPPING, PPRIVILEGE_SET, LPDWORD, LPDWORD, LPBOOL]
AccessCheck.restype = BOOL

AccessCheckAndAuditAlarmW = windll.advapi32.AccessCheckAndAuditAlarmW
AccessCheckAndAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    LPWSTR,
    LPWSTR,
    PSECURITY_DESCRIPTOR,
    DWORD,
    PGENERIC_MAPPING,
    BOOL,
    LPDWORD,
    LPBOOL,
    LPBOOL,
]
AccessCheckAndAuditAlarmW.restype = BOOL

AccessCheckByType = windll.advapi32.AccessCheckByType
AccessCheckByType.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSID,
    HANDLE,
    DWORD,
    POBJECT_TYPE_LIST,
    DWORD,
    PGENERIC_MAPPING,
    PPRIVILEGE_SET,
    LPDWORD,
    LPDWORD,
    LPBOOL,
]
AccessCheckByType.restype = BOOL

AccessCheckByTypeResultList = windll.advapi32.AccessCheckByTypeResultList
AccessCheckByTypeResultList.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSID,
    HANDLE,
    DWORD,
    POBJECT_TYPE_LIST,
    DWORD,
    PGENERIC_MAPPING,
    PPRIVILEGE_SET,
    LPDWORD,
    LPDWORD,
    LPDWORD,
]
AccessCheckByTypeResultList.restype = BOOL

AccessCheckByTypeAndAuditAlarmW = windll.advapi32.AccessCheckByTypeAndAuditAlarmW
AccessCheckByTypeAndAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    LPCWSTR,
    LPCWSTR,
    PSECURITY_DESCRIPTOR,
    PSID,
    DWORD,
    AUDIT_EVENT_TYPE,
    DWORD,
    POBJECT_TYPE_LIST,
    DWORD,
    PGENERIC_MAPPING,
    BOOL,
    POINTER(DWORD),
    POINTER(BOOL),
    POINTER(BOOL),
]
AccessCheckByTypeAndAuditAlarmW.restype = BOOL

AccessCheckByTypeResultListAndAuditAlarmW = windll.advapi32.AccessCheckByTypeResultListAndAuditAlarmW
AccessCheckByTypeResultListAndAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    LPCWSTR,
    LPCWSTR,
    PSECURITY_DESCRIPTOR,
    PSID,
    DWORD,
    AUDIT_EVENT_TYPE,
    DWORD,
    POBJECT_TYPE_LIST,
    DWORD,
    PGENERIC_MAPPING,
    BOOL,
    LPDWORD,
    LPDWORD,
    POINTER(BOOL),
]
AccessCheckByTypeResultListAndAuditAlarmW.restype = BOOL

AccessCheckByTypeResultListAndAuditAlarmByHandleW = windll.advapi32.AccessCheckByTypeResultListAndAuditAlarmByHandleW
AccessCheckByTypeResultListAndAuditAlarmByHandleW.argtypes = [
    LPCWSTR,
    LPVOID,
    HANDLE,
    LPCWSTR,
    LPCWSTR,
    PSECURITY_DESCRIPTOR,
    PSID,
    DWORD,
    AUDIT_EVENT_TYPE,
    DWORD,
    POBJECT_TYPE_LIST,
    DWORD,
    PGENERIC_MAPPING,
    BOOL,
    LPDWORD,
    LPDWORD,
    POINTER(BOOL),
]
AccessCheckByTypeResultListAndAuditAlarmByHandleW.restype = BOOL

AddAccessAllowedAce = windll.advapi32.AddAccessAllowedAce
AddAccessAllowedAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    PSID,
]
AddAccessAllowedAce.restype = BOOL

AddAccessAllowedAceEx = windll.advapi32.AddAccessAllowedAceEx
AddAccessAllowedAceEx.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    PSID,
]
AddAccessAllowedAceEx.restype = BOOL

AddAccessAllowedObjectAce = windll.advapi32.AddAccessAllowedObjectAce
AddAccessAllowedObjectAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    POINTER(GUID),
    POINTER(GUID),
    PSID,
]
AddAccessAllowedObjectAce.restype = BOOL

AddAccessDeniedAce = windll.advapi32.AddAccessDeniedAce
AddAccessDeniedAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    PSID,
]
AddAccessDeniedAce.restype = BOOL

AddAccessDeniedAceEx = windll.advapi32.AddAccessDeniedAceEx
AddAccessDeniedAceEx.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    PSID,
]
AddAccessDeniedAceEx.restype = BOOL

AddAccessDeniedObjectAce = windll.advapi32.AddAccessDeniedObjectAce
AddAccessDeniedObjectAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    POINTER(GUID),
    POINTER(GUID),
    PSID,
]
AddAccessDeniedObjectAce.restype = BOOL

AddAce = windll.advapi32.AddAce
AddAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    LPVOID,
    DWORD,
]
AddAce.restype = BOOL

AddAuditAccessAce = windll.advapi32.AddAuditAccessAce
AddAuditAccessAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    PSID,
    BOOL,
    BOOL,
]
AddAuditAccessAce.restype = BOOL

AddAuditAccessAceEx = windll.advapi32.AddAuditAccessAceEx
AddAuditAccessAceEx.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    PSID,
    BOOL,
    BOOL,
]
AddAuditAccessAceEx.restype = BOOL

AddAuditAccessObjectAce = windll.advapi32.AddAuditAccessObjectAce
AddAuditAccessObjectAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    POINTER(GUID),
    POINTER(GUID),
    PSID,
    BOOL,
    BOOL,
]
AddAuditAccessObjectAce.restype = BOOL

AddMandatoryAce = windll.advapi32.AddMandatoryAce
AddMandatoryAce.argtypes = [
    PACL,
    DWORD,
    DWORD,
    DWORD,
    PSID,
]
AddMandatoryAce.restype = BOOL

try:  # Windows 8+
    AddResourceAttributeAce = windll.kernel32.AddResourceAttributeAce
    AddResourceAttributeAce.argtypes = [
        PACL,
        DWORD,
        DWORD,
        DWORD,
        PSID,
        POINTER(CLAIM_SECURITY_ATTRIBUTES_INFORMATION),
        PDWORD,
    ]
    AddResourceAttributeAce.restype = BOOL
except AttributeError:
    pass

try:  # Windows 8+
    AddScopedPolicyIDAce = windll.kernel32.AddScopedPolicyIDAce
    AddScopedPolicyIDAce.argtypes = [
        PACL,
        DWORD,
        DWORD,
        DWORD,
        PSID,
    ]
    AddScopedPolicyIDAce.restype = BOOL
except AttributeError:
    pass

AdjustTokenGroups = windll.advapi32.AdjustTokenGroups
AdjustTokenGroups.argtypes = [
    HANDLE,
    BOOL,
    POINTER(TOKEN_GROUPS),
    DWORD,
    POINTER(TOKEN_GROUPS),
    PDWORD,
]
AdjustTokenGroups.restype = BOOL

AdjustTokenPrivileges = windll.advapi32.AdjustTokenPrivileges
AdjustTokenPrivileges.argtypes = [HANDLE, BOOL, PTOKEN_PRIVILEGES, DWORD, PTOKEN_PRIVILEGES, PDWORD]
AdjustTokenPrivileges.restype = BOOL

AllocateAndInitializeSid = windll.advapi32.AllocateAndInitializeSid
AllocateAndInitializeSid.argtypes = [
    POINTER(SID_IDENTIFIER_AUTHORITY),
    BYTE,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    DWORD,
    POINTER(PSID),
]
AllocateAndInitializeSid.restype = BOOL

AllocateLocallyUniqueId = windll.advapi32.AllocateLocallyUniqueId
AllocateLocallyUniqueId.argtypes = [
    POINTER(LUID),
]
AllocateLocallyUniqueId.restype = BOOL

AreAllAccessesGranted = windll.advapi32.AreAllAccessesGranted
AreAllAccessesGranted.argtypes = [
    DWORD,
    DWORD,
]
AreAllAccessesGranted.restype = BOOL

AreAnyAccessesGranted = windll.advapi32.AreAnyAccessesGranted
AreAnyAccessesGranted.argtypes = [
    DWORD,
    DWORD,
]
AreAnyAccessesGranted.restype = BOOL

CheckTokenMembership = windll.advapi32.CheckTokenMembership
CheckTokenMembership.argtypes = [
    HANDLE,
    PSID,
    PBOOL,
]
CheckTokenMembership.restype = BOOL

try:
    CheckTokenCapability = windll.kernel32.CheckTokenCapability
    CheckTokenCapability.argtypes = [
        HANDLE,
        PSID,
        PBOOL,
    ]
    CheckTokenCapability.restype = BOOL
except AttributeError:
    pass

try:
    GetAppContainerAce = windll.kernel32.GetAppContainerAce
    GetAppContainerAce.argtypes = [
        PACL,
        DWORD,
        POINTER(PVOID),
        POINTER(DWORD),
    ]
    GetAppContainerAce.restype = BOOL
except AttributeError:
    pass

try:
    CheckTokenMembershipEx = windll.kernel32.CheckTokenMembershipEx
    CheckTokenMembershipEx.argtypes = [
        HANDLE,
        PSID,
        DWORD,
        PBOOL,
    ]
    CheckTokenMembershipEx.restype = BOOL
except AttributeError:
    pass

ConvertToAutoInheritPrivateObjectSecurity = windll.advapi32.ConvertToAutoInheritPrivateObjectSecurity
ConvertToAutoInheritPrivateObjectSecurity.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    POINTER(GUID),
    BOOLEAN,
    PGENERIC_MAPPING,
]
ConvertToAutoInheritPrivateObjectSecurity.restype = BOOL

CopySid = windll.advapi32.CopySid
CopySid.argtypes = [
    DWORD,
    PSID,
    PSID,
]
CopySid.restype = BOOL

CreatePrivateObjectSecurity = windll.advapi32.CreatePrivateObjectSecurity
CreatePrivateObjectSecurity.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    BOOL,
    HANDLE,
    PGENERIC_MAPPING,
]
CreatePrivateObjectSecurity.restype = BOOL

CreatePrivateObjectSecurityEx = windll.advapi32.CreatePrivateObjectSecurityEx
CreatePrivateObjectSecurityEx.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    POINTER(GUID),
    BOOL,
    ULONG,
    HANDLE,
    PGENERIC_MAPPING,
]
CreatePrivateObjectSecurityEx.restype = BOOL

CreatePrivateObjectSecurityWithMultipleInheritance = windll.advapi32.CreatePrivateObjectSecurityWithMultipleInheritance
CreatePrivateObjectSecurityWithMultipleInheritance.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    POINTER(POINTER(GUID)),
    ULONG,
    BOOL,
    ULONG,
    HANDLE,
    PGENERIC_MAPPING,
]
CreatePrivateObjectSecurityWithMultipleInheritance.restype = BOOL

CreateRestrictedToken = windll.advapi32.CreateRestrictedToken
CreateRestrictedToken.argtypes = [
    HANDLE,
    DWORD,
    DWORD,
    POINTER(SID_AND_ATTRIBUTES),
    DWORD,
    POINTER(LUID_AND_ATTRIBUTES),
    DWORD,
    POINTER(SID_AND_ATTRIBUTES),
    PHANDLE,
]
CreateRestrictedToken.restype = BOOL

CreateWellKnownSid = windll.advapi32.CreateWellKnownSid
CreateWellKnownSid.argtypes = [
    WELL_KNOWN_SID_TYPE,
    PSID,
    PSID,
    POINTER(DWORD),
]
CreateWellKnownSid.restype = BOOL

EqualDomainSid = windll.advapi32.EqualDomainSid
EqualDomainSid.argtypes = [
    PSID,
    PSID,
    POINTER(BOOL),
]
EqualDomainSid.restype = BOOL

DeleteAce = windll.advapi32.DeleteAce
DeleteAce.argtypes = [
    PACL,
    DWORD,
]
DeleteAce.restype = BOOL

DestroyPrivateObjectSecurity = windll.advapi32.DestroyPrivateObjectSecurity
DestroyPrivateObjectSecurity.argtypes = [
    POINTER(PSECURITY_DESCRIPTOR),
]
DestroyPrivateObjectSecurity.restype = BOOL

DuplicateToken = windll.advapi32.DuplicateToken
DuplicateToken.argtypes = [
    HANDLE,
    SECURITY_IMPERSONATION_LEVEL,
    PHANDLE,
]
DuplicateToken.restype = BOOL

DuplicateTokenEx = windll.advapi32.DuplicateTokenEx
DuplicateTokenEx.argtypes = [
    HANDLE,
    DWORD,
    POINTER(SECURITY_ATTRIBUTES),
    SECURITY_IMPERSONATION_LEVEL,
    TOKEN_TYPE,
    PHANDLE,
]
DuplicateTokenEx.restype = BOOL

EqualPrefixSid = windll.advapi32.EqualPrefixSid
EqualPrefixSid.argtypes = [
    PSID,
    PSID,
]
EqualPrefixSid.restype = BOOL

EqualSid = windll.advapi32.EqualSid
EqualSid.argtypes = [
    PSID,
    PSID,
]
EqualSid.restype = BOOL

FindFirstFreeAce = windll.advapi32.FindFirstFreeAce
FindFirstFreeAce.argtypes = [
    PACL,
    POINTER(LPVOID),
]
FindFirstFreeAce.restype = BOOL

FreeSid = windll.advapi32.FreeSid
FreeSid.argtypes = [
    PSID,
]
FreeSid.restype = PVOID

GetAce = windll.advapi32.GetAce
GetAce.argtypes = [
    PACL,
    DWORD,
    POINTER(LPVOID),
]
GetAce.restype = BOOL

GetAclInformation = windll.advapi32.GetAclInformation
GetAclInformation.argtypes = [
    PACL,
    LPVOID,
    DWORD,
    ACL_INFORMATION_CLASS,
]
GetAclInformation.restype = BOOL

GetFileSecurityW = windll.advapi32.GetFileSecurityW
GetFileSecurityW.argtypes = [
    LPCWSTR,
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
    DWORD,
    POINTER(DWORD),
]
GetFileSecurityW.restype = BOOL

GetKernelObjectSecurity = windll.advapi32.GetKernelObjectSecurity
GetKernelObjectSecurity.argtypes = [HANDLE, SECURITY_INFORMATION, PSECURITY_DESCRIPTOR, DWORD, POINTER(DWORD)]
GetKernelObjectSecurity.restype = BOOL

GetLengthSid = windll.advapi32.GetLengthSid
GetLengthSid.argtypes = [
    PSID,
]
GetLengthSid.restype = DWORD

GetPrivateObjectSecurity = windll.advapi32.GetPrivateObjectSecurity
GetPrivateObjectSecurity.argtypes = [
    PSECURITY_DESCRIPTOR,
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
    DWORD,
    PDWORD,
]
GetPrivateObjectSecurity.restype = BOOL
GetPrivateObjectSecurity.errcheck = nonzero

GetSecurityDescriptorControl = windll.advapi32.GetSecurityDescriptorControl
GetSecurityDescriptorControl.argtypes = [
    PSECURITY_DESCRIPTOR,
    POINTER(SECURITY_DESCRIPTOR_CONTROL),
    POINTER(DWORD),
]
GetSecurityDescriptorControl.restype = BOOL

GetSecurityDescriptorDacl = windll.advapi32.GetSecurityDescriptorDacl
GetSecurityDescriptorDacl.argtypes = [
    PSECURITY_DESCRIPTOR,
    POINTER(BOOL),
    POINTER(PACL),
    POINTER(BOOL),
]
GetSecurityDescriptorDacl.restype = BOOL

GetSecurityDescriptorGroup = windll.advapi32.GetSecurityDescriptorGroup
GetSecurityDescriptorGroup.argtypes = [
    PSECURITY_DESCRIPTOR,
    POINTER(PSID),
    POINTER(BOOL),
]
GetSecurityDescriptorGroup.restype = BOOL

GetSecurityDescriptorLength = windll.advapi32.GetSecurityDescriptorLength
GetSecurityDescriptorLength.argtypes = [
    PSECURITY_DESCRIPTOR,
]
GetSecurityDescriptorLength.restype = DWORD

GetSecurityDescriptorOwner = windll.advapi32.GetSecurityDescriptorOwner
GetSecurityDescriptorOwner.argtypes = [
    PSECURITY_DESCRIPTOR,
    POINTER(PSID),
    POINTER(BOOL),
]
GetSecurityDescriptorOwner.restype = BOOL

GetSecurityDescriptorRMControl = windll.advapi32.GetSecurityDescriptorRMControl
GetSecurityDescriptorRMControl.argtypes = [
    PSECURITY_DESCRIPTOR,
    PUCHAR,
]
GetSecurityDescriptorRMControl.restype = DWORD

GetSecurityDescriptorSacl = windll.advapi32.GetSecurityDescriptorSacl
GetSecurityDescriptorSacl.argtypes = [
    PSECURITY_DESCRIPTOR,
    POINTER(BOOL),
    POINTER(PACL),
    POINTER(BOOL),
]
GetSecurityDescriptorSacl.restype = BOOL

GetSidIdentifierAuthority = windll.advapi32.GetSidIdentifierAuthority
GetSidIdentifierAuthority.argtypes = [
    PSID,
]
GetSidIdentifierAuthority.restype = POINTER(SID_IDENTIFIER_AUTHORITY)

GetSidLengthRequired = windll.advapi32.GetSidLengthRequired
GetSidLengthRequired.argtypes = [
    UCHAR,
]
GetSidLengthRequired.restype = DWORD

GetSidSubAuthority = windll.advapi32.GetSidSubAuthority
GetSidSubAuthority.argtypes = [
    PSID,
    DWORD,
]
GetSidSubAuthority.restype = PDWORD

GetSidSubAuthorityCount = windll.advapi32.GetSidSubAuthorityCount
GetSidSubAuthorityCount.argtypes = [
    PSID,
]
GetSidSubAuthorityCount.restype = PUCHAR

GetTokenInformation = windll.advapi32.GetTokenInformation
GetTokenInformation.argtypes = [
    HANDLE,
    TOKEN_INFORMATION_CLASS,
    LPVOID,
    DWORD,
    PDWORD,
]
GetTokenInformation.restype = BOOL

GetWindowsAccountDomainSid = windll.advapi32.GetWindowsAccountDomainSid
GetWindowsAccountDomainSid.argtypes = [
    PSID,
    PSID,
    POINTER(DWORD),
]
GetWindowsAccountDomainSid.restype = BOOL

ImpersonateAnonymousToken = windll.advapi32.ImpersonateAnonymousToken
ImpersonateAnonymousToken.argtypes = [
    HANDLE,
]
ImpersonateAnonymousToken.restype = BOOL

ImpersonateLoggedOnUser = windll.advapi32.ImpersonateLoggedOnUser
ImpersonateLoggedOnUser.argtypes = [
    HANDLE,
]
ImpersonateLoggedOnUser.restype = BOOL

ImpersonateSelf = windll.advapi32.ImpersonateSelf
ImpersonateSelf.argtypes = [
    SECURITY_IMPERSONATION_LEVEL,
]
ImpersonateSelf.restype = BOOL

InitializeAcl = windll.advapi32.InitializeAcl
InitializeAcl.argtypes = [
    PACL,
    DWORD,
    DWORD,
]
InitializeAcl.restype = BOOL

InitializeSecurityDescriptor = windll.advapi32.InitializeSecurityDescriptor
InitializeSecurityDescriptor.argtypes = [
    PSECURITY_DESCRIPTOR,
    DWORD,
]
InitializeSecurityDescriptor.restype = BOOL

InitializeSid = windll.advapi32.InitializeSid
InitializeSid.argtypes = [
    PSID,
    POINTER(SID_IDENTIFIER_AUTHORITY),
    BYTE,
]
InitializeSid.restype = BOOL

IsTokenRestricted = windll.advapi32.IsTokenRestricted
IsTokenRestricted.argtypes = [
    HANDLE,
]
IsTokenRestricted.restype = BOOL

IsValidAcl = windll.advapi32.IsValidAcl
IsValidAcl.argtypes = [
    PACL,
]
IsValidAcl.restype = BOOL

IsValidSecurityDescriptor = windll.advapi32.IsValidSecurityDescriptor
IsValidSecurityDescriptor.argtypes = [
    PSECURITY_DESCRIPTOR,
]
IsValidSecurityDescriptor.restype = BOOL

IsValidSid = windll.advapi32.IsValidSid
IsValidSid.argtypes = [
    PSID,
]
IsValidSid.restype = BOOL

IsWellKnownSid = windll.advapi32.IsWellKnownSid
IsWellKnownSid.argtypes = [
    PSID,
    WELL_KNOWN_SID_TYPE,
]
IsWellKnownSid.restype = BOOL

MakeAbsoluteSD = windll.advapi32.MakeAbsoluteSD
MakeAbsoluteSD.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    LPDWORD,
    PACL,
    LPDWORD,
    PACL,
    LPDWORD,
    PSID,
    LPDWORD,
    PSID,
    LPDWORD,
]
MakeAbsoluteSD.restype = BOOL

MakeSelfRelativeSD = windll.advapi32.MakeSelfRelativeSD
MakeSelfRelativeSD.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSECURITY_DESCRIPTOR,
    LPDWORD,
]
MakeSelfRelativeSD.restype = BOOL

MapGenericMask = windll.advapi32.MapGenericMask
MapGenericMask.argtypes = [
    PDWORD,
    PGENERIC_MAPPING,
]
MapGenericMask.restype = None

ObjectCloseAuditAlarmW = windll.advapi32.ObjectCloseAuditAlarmW
ObjectCloseAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    BOOL,
]
ObjectCloseAuditAlarmW.restype = BOOL

ObjectDeleteAuditAlarmW = windll.advapi32.ObjectDeleteAuditAlarmW
ObjectDeleteAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    BOOL,
]
ObjectDeleteAuditAlarmW.restype = BOOL

ObjectOpenAuditAlarmW = windll.advapi32.ObjectOpenAuditAlarmW
ObjectOpenAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    LPWSTR,
    LPWSTR,
    PSECURITY_DESCRIPTOR,
    HANDLE,
    DWORD,
    DWORD,
    PPRIVILEGE_SET,
    BOOL,
    BOOL,
    POINTER(BOOL),
]
ObjectOpenAuditAlarmW.restype = BOOL

ObjectPrivilegeAuditAlarmW = windll.advapi32.ObjectPrivilegeAuditAlarmW
ObjectPrivilegeAuditAlarmW.argtypes = [
    LPCWSTR,
    LPVOID,
    HANDLE,
    DWORD,
    PPRIVILEGE_SET,
    BOOL,
]
ObjectPrivilegeAuditAlarmW.restype = BOOL

PrivilegeCheck = windll.advapi32.PrivilegeCheck
PrivilegeCheck.argtypes = [
    HANDLE,
    PPRIVILEGE_SET,
    POINTER(BOOL),
]
PrivilegeCheck.restype = BOOL

PrivilegedServiceAuditAlarmW = windll.advapi32.PrivilegedServiceAuditAlarmW
PrivilegedServiceAuditAlarmW.argtypes = [
    LPCWSTR,
    LPCWSTR,
    HANDLE,
    PPRIVILEGE_SET,
    BOOL,
]
PrivilegedServiceAuditAlarmW.restype = BOOL

QuerySecurityAccessMask = windll.advapi32.QuerySecurityAccessMask
QuerySecurityAccessMask.argtypes = [
    SECURITY_INFORMATION,
    POINTER(DWORD),
]
QuerySecurityAccessMask.restype = None

RevertToSelf = windll.advapi32.RevertToSelf
RevertToSelf.argtypes = []
RevertToSelf.restype = BOOL

SetAclInformation = windll.advapi32.SetAclInformation
SetAclInformation.argtypes = [
    PACL,
    LPVOID,
    DWORD,
    ACL_INFORMATION_CLASS,
]
SetAclInformation.restype = BOOL

SetFileSecurityW = windll.advapi32.SetFileSecurityW
SetFileSecurityW.argtypes = [
    LPCWSTR,
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
]
SetFileSecurityW.restype = BOOL

SetKernelObjectSecurity = windll.advapi32.SetKernelObjectSecurity
SetKernelObjectSecurity.argtypes = [
    HANDLE,
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
]
SetKernelObjectSecurity.restype = BOOL

SetPrivateObjectSecurity = windll.advapi32.SetPrivateObjectSecurity
SetPrivateObjectSecurity.argtypes = [
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    PGENERIC_MAPPING,
    HANDLE,
]
SetPrivateObjectSecurity.restype = BOOL

SetPrivateObjectSecurityEx = windll.advapi32.SetPrivateObjectSecurityEx
SetPrivateObjectSecurityEx.argtypes = [
    SECURITY_INFORMATION,
    PSECURITY_DESCRIPTOR,
    POINTER(PSECURITY_DESCRIPTOR),
    ULONG,
    PGENERIC_MAPPING,
    HANDLE,
]
SetPrivateObjectSecurityEx.restype = BOOL

SetSecurityAccessMask = windll.advapi32.SetSecurityAccessMask
SetSecurityAccessMask.argtypes = [
    SECURITY_INFORMATION,
    POINTER(DWORD),
]
SetSecurityAccessMask.restype = None

SetSecurityDescriptorControl = windll.advapi32.SetSecurityDescriptorControl
SetSecurityDescriptorControl.argtypes = [
    PSECURITY_DESCRIPTOR,
    SECURITY_DESCRIPTOR_CONTROL,
    SECURITY_DESCRIPTOR_CONTROL,
]
SetSecurityDescriptorControl.restype = BOOL

SetSecurityDescriptorDacl = windll.advapi32.SetSecurityDescriptorDacl
SetSecurityDescriptorDacl.argtypes = [
    PSECURITY_DESCRIPTOR,
    BOOL,
    PACL,
    BOOL,
]
SetSecurityDescriptorDacl.restype = BOOL

SetSecurityDescriptorGroup = windll.advapi32.SetSecurityDescriptorGroup
SetSecurityDescriptorGroup.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSID,
    BOOL,
]
SetSecurityDescriptorGroup.restype = BOOL

SetSecurityDescriptorOwner = windll.advapi32.SetSecurityDescriptorOwner
SetSecurityDescriptorOwner.argtypes = [
    PSECURITY_DESCRIPTOR,
    PSID,
    BOOL,
]
SetSecurityDescriptorOwner.restype = BOOL

SetSecurityDescriptorRMControl = windll.advapi32.SetSecurityDescriptorRMControl
SetSecurityDescriptorRMControl.argtypes = [
    PSECURITY_DESCRIPTOR,
    PUCHAR,
]
SetSecurityDescriptorRMControl.restype = DWORD

SetSecurityDescriptorSacl = windll.advapi32.SetSecurityDescriptorSacl
SetSecurityDescriptorSacl.argtypes = [
    PSECURITY_DESCRIPTOR,
    BOOL,
    PACL,
    BOOL,
]
SetSecurityDescriptorSacl.restype = BOOL

SetTokenInformation = windll.advapi32.SetTokenInformation
SetTokenInformation.argtypes = [
    HANDLE,
    TOKEN_INFORMATION_CLASS,
    LPVOID,
    DWORD,
]
SetTokenInformation.restype = BOOL

try:
    SetCachedSigningLevel = windll.kernel32.SetCachedSigningLevel
    SetCachedSigningLevel.argtypes = [
        PHANDLE,
        ULONG,
        ULONG,
        HANDLE,
    ]
    SetCachedSigningLevel.restype = BOOL
except AttributeError:
    pass

try:
    GetCachedSigningLevel = windll.kernel32.GetCachedSigningLevel
    GetCachedSigningLevel.argtypes = [
        HANDLE,
        PULONG,
        PULONG,
        PUCHAR,
        PULONG,
        PULONG,
    ]
    GetCachedSigningLevel.restype = BOOL
except AttributeError:
    pass

try:
    CveEventWrite = windll.advapi32.CveEventWrite
    CveEventWrite.argtypes = [
        PCWSTR,
        PCWSTR,
    ]
    CveEventWrite.restype = LONG
except AttributeError:
    pass

try:
    DeriveCapabilitySidsFromName = windll.kernelbase.DeriveCapabilitySidsFromName  # documented as kernel32.dll
    DeriveCapabilitySidsFromName.argtypes = [
        LPCWSTR,
        POINTER(POINTER(PSID)),
        POINTER(DWORD),
        POINTER(POINTER(PSID)),
        POINTER(DWORD),
    ]
    DeriveCapabilitySidsFromName.restype = BOOL
except AttributeError:
    pass
