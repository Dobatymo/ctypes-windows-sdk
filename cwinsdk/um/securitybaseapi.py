from ctypes import POINTER
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCWSTR, LPVOID, LPWSTR

from .. import windll
from ..shared.minwindef import LPBOOL, LPDWORD, PDWORD
from .winnt import PGENERIC_MAPPING, POBJECT_TYPE_LIST, PPRIVILEGE_SET, PSECURITY_DESCRIPTOR, PSID, PTOKEN_PRIVILEGES

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

"""
BOOL

AccessCheckByTypeAndAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ LPCWSTR ObjectTypeName,
    _In_opt_ LPCWSTR ObjectName,
    _In_ PSECURITY_DESCRIPTOR SecurityDescriptor,
    _In_opt_ PSID PrincipalSelfSid,
    _In_ DWORD DesiredAccess,
    _In_ AUDIT_EVENT_TYPE AuditType,
    _In_ DWORD Flags,
    _Inout_updates_opt_(ObjectTypeListLength) POBJECT_TYPE_LIST ObjectTypeList,
    _In_ DWORD ObjectTypeListLength,
    _In_ PGENERIC_MAPPING GenericMapping,
    _In_ BOOL ObjectCreation,
    _Out_ LPDWORD GrantedAccess,
    _Out_ LPBOOL AccessStatus,
    _Out_ LPBOOL pfGenerateOnClose
    );


BOOL

AccessCheckByTypeResultListAndAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ LPCWSTR ObjectTypeName,
    _In_opt_ LPCWSTR ObjectName,
    _In_ PSECURITY_DESCRIPTOR SecurityDescriptor,
    _In_opt_ PSID PrincipalSelfSid,
    _In_ DWORD DesiredAccess,
    _In_ AUDIT_EVENT_TYPE AuditType,
    _In_ DWORD Flags,
    _Inout_updates_opt_(ObjectTypeListLength) POBJECT_TYPE_LIST ObjectTypeList,
    _In_ DWORD ObjectTypeListLength,
    _In_ PGENERIC_MAPPING GenericMapping,
    _In_ BOOL ObjectCreation,
    _Out_writes_(ObjectTypeListLength) LPDWORD GrantedAccessList,
    _Out_writes_(ObjectTypeListLength) LPDWORD AccessStatusList,
    _Out_ LPBOOL pfGenerateOnClose
    );

BOOL

AccessCheckByTypeResultListAndAuditAlarmByHandleW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ HANDLE ClientToken,
    _In_ LPCWSTR ObjectTypeName,
    _In_opt_ LPCWSTR ObjectName,
    _In_ PSECURITY_DESCRIPTOR SecurityDescriptor,
    _In_opt_ PSID PrincipalSelfSid,
    _In_ DWORD DesiredAccess,
    _In_ AUDIT_EVENT_TYPE AuditType,
    _In_ DWORD Flags,
    _Inout_updates_opt_(ObjectTypeListLength) POBJECT_TYPE_LIST ObjectTypeList,
    _In_ DWORD ObjectTypeListLength,
    _In_ PGENERIC_MAPPING GenericMapping,
    _In_ BOOL ObjectCreation,
    _Out_writes_(ObjectTypeListLength) LPDWORD GrantedAccessList,
    _Out_writes_(ObjectTypeListLength) LPDWORD AccessStatusList,
    _Out_ LPBOOL pfGenerateOnClose
    );

BOOL

AddAccessAllowedAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AccessMask,
    _In_ PSID pSid
    );



BOOL

AddAccessAllowedAceEx(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_ PSID pSid
    );


BOOL

AddAccessAllowedObjectAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_opt_ GUID* ObjectTypeGuid,
    _In_opt_ GUID* InheritedObjectTypeGuid,
    _In_ PSID pSid
    );



BOOL

AddAccessDeniedAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AccessMask,
    _In_ PSID pSid
    );



BOOL

AddAccessDeniedAceEx(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_ PSID pSid
    );



BOOL

AddAccessDeniedObjectAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_opt_ GUID* ObjectTypeGuid,
    _In_opt_ GUID* InheritedObjectTypeGuid,
    _In_ PSID pSid
    );



BOOL

AddAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD dwStartingAceIndex,
    _In_reads_bytes_(nAceListLength) LPVOID pAceList,
    _In_ DWORD nAceListLength
    );



BOOL

AddAuditAccessAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD dwAccessMask,
    _In_ PSID pSid,
    _In_ BOOL bAuditSuccess,
    _In_ BOOL bAuditFailure
    );



BOOL

AddAuditAccessAceEx(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD dwAccessMask,
    _In_ PSID pSid,
    _In_ BOOL bAuditSuccess,
    _In_ BOOL bAuditFailure
    );



BOOL

AddAuditAccessObjectAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_opt_ GUID* ObjectTypeGuid,
    _In_opt_ GUID* InheritedObjectTypeGuid,
    _In_ PSID pSid,
    _In_ BOOL bAuditSuccess,
    _In_ BOOL bAuditFailure
    );



BOOL

AddMandatoryAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD MandatoryPolicy,
    _In_ PSID pLabelSid
    );



BOOL

AddResourceAttributeAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_ PSID pSid,
    _In_ PCLAIM_SECURITY_ATTRIBUTES_INFORMATION pAttributeInfo,
    _Out_ PDWORD pReturnLength
    );



BOOL

AddScopedPolicyIDAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceRevision,
    _In_ DWORD AceFlags,
    _In_ DWORD AccessMask,
    _In_ PSID pSid
    );



BOOL

AdjustTokenGroups(
    _In_ HANDLE TokenHandle,
    _In_ BOOL ResetToDefault,
    _In_opt_ PTOKEN_GROUPS NewState,
    _In_ DWORD BufferLength,
    _Out_writes_bytes_to_opt_(BufferLength,*ReturnLength) PTOKEN_GROUPS PreviousState,
    _Out_opt_ PDWORD ReturnLength
    );
"""

AdjustTokenPrivileges = windll.advapi32.AdjustTokenPrivileges
AdjustTokenPrivileges.argtypes = [HANDLE, BOOL, PTOKEN_PRIVILEGES, DWORD, PTOKEN_PRIVILEGES, PDWORD]
AdjustTokenPrivileges.restype = BOOL


"""
BOOL

AllocateAndInitializeSid(
    _In_ PSID_IDENTIFIER_AUTHORITY pIdentifierAuthority,
    _In_ BYTE nSubAuthorityCount,
    _In_ DWORD nSubAuthority0,
    _In_ DWORD nSubAuthority1,
    _In_ DWORD nSubAuthority2,
    _In_ DWORD nSubAuthority3,
    _In_ DWORD nSubAuthority4,
    _In_ DWORD nSubAuthority5,
    _In_ DWORD nSubAuthority6,
    _In_ DWORD nSubAuthority7,
    _Outptr_ PSID* pSid
    );



BOOL

AllocateLocallyUniqueId(
    _Out_ PLUID Luid
    );



BOOL

AreAllAccessesGranted(
    _In_ DWORD GrantedAccess,
    _In_ DWORD DesiredAccess
    );



BOOL

AreAnyAccessesGranted(
    _In_ DWORD GrantedAccess,
    _In_ DWORD DesiredAccess
    );




BOOL

CheckTokenMembership(
    _In_opt_ HANDLE TokenHandle,
    _In_ PSID SidToCheck,
    _Out_ PBOOL IsMember
    );



BOOL

CheckTokenCapability(
    _In_opt_ HANDLE TokenHandle,
    _In_ PSID CapabilitySidToCheck,
    _Out_ PBOOL HasCapability
    );



BOOL

GetAppContainerAce(
    _In_ PACL Acl,
    _In_ DWORD StartingAceIndex,
    _Outptr_ PVOID* AppContainerAce,
    _Out_opt_ DWORD* AppContainerAceIndex
    );



BOOL

CheckTokenMembershipEx(
    _In_opt_ HANDLE TokenHandle,
    _In_ PSID SidToCheck,
    _In_ DWORD Flags,
    _Out_ PBOOL IsMember
    );



BOOL

ConvertToAutoInheritPrivateObjectSecurity(
    _In_opt_ PSECURITY_DESCRIPTOR ParentDescriptor,
    _In_ PSECURITY_DESCRIPTOR CurrentSecurityDescriptor,
    _Outptr_ PSECURITY_DESCRIPTOR* NewSecurityDescriptor,
    _In_opt_ GUID* ObjectType,
    _In_ BOOLEAN IsDirectoryObject,
    _In_ PGENERIC_MAPPING GenericMapping
    );



BOOL

CopySid(
    _In_ DWORD nDestinationSidLength,
    _Out_writes_bytes_(nDestinationSidLength) PSID pDestinationSid,
    _In_ PSID pSourceSid
    );



BOOL

CreatePrivateObjectSecurity(
    _In_opt_ PSECURITY_DESCRIPTOR ParentDescriptor,
    _In_opt_ PSECURITY_DESCRIPTOR CreatorDescriptor,
    _Outptr_ PSECURITY_DESCRIPTOR* NewDescriptor,
    _In_ BOOL IsDirectoryObject,
    _In_opt_ HANDLE Token,
    _In_ PGENERIC_MAPPING GenericMapping
    );



BOOL

CreatePrivateObjectSecurityEx(
    _In_opt_ PSECURITY_DESCRIPTOR ParentDescriptor,
    _In_opt_ PSECURITY_DESCRIPTOR CreatorDescriptor,
    _Outptr_ PSECURITY_DESCRIPTOR* NewDescriptor,
    _In_opt_ GUID* ObjectType,
    _In_ BOOL IsContainerObject,
    _In_ ULONG AutoInheritFlags,
    _In_opt_ HANDLE Token,
    _In_ PGENERIC_MAPPING GenericMapping
    );



BOOL

CreatePrivateObjectSecurityWithMultipleInheritance(
    _In_opt_ PSECURITY_DESCRIPTOR ParentDescriptor,
    _In_opt_ PSECURITY_DESCRIPTOR CreatorDescriptor,
    _Outptr_ PSECURITY_DESCRIPTOR* NewDescriptor,
    _In_reads_opt_(GuidCount) GUID** ObjectTypes,
    _In_ ULONG GuidCount,
    _In_ BOOL IsContainerObject,
    _In_ ULONG AutoInheritFlags,
    _In_opt_ HANDLE Token,
    _In_ PGENERIC_MAPPING GenericMapping
    );



BOOL

CreateRestrictedToken(
    _In_ HANDLE ExistingTokenHandle,
    _In_ DWORD Flags,
    _In_ DWORD DisableSidCount,
    _In_reads_opt_(DisableSidCount) PSID_AND_ATTRIBUTES SidsToDisable,
    _In_ DWORD DeletePrivilegeCount,
    _In_reads_opt_(DeletePrivilegeCount) PLUID_AND_ATTRIBUTES PrivilegesToDelete,
    _In_ DWORD RestrictedSidCount,
    _In_reads_opt_(RestrictedSidCount) PSID_AND_ATTRIBUTES SidsToRestrict,
    _Outptr_ PHANDLE NewTokenHandle
    );



BOOL

CreateWellKnownSid(
    _In_ WELL_KNOWN_SID_TYPE WellKnownSidType,
    _In_opt_ PSID DomainSid,
    _Out_writes_bytes_to_opt_(*cbSid,*cbSid) PSID pSid,
    _Inout_ DWORD* cbSid
    );



BOOL

EqualDomainSid(
    _In_ PSID pSid1,
    _In_ PSID pSid2,
    _Out_ BOOL* pfEqual
    );




BOOL

DeleteAce(
    _Inout_ PACL pAcl,
    _In_ DWORD dwAceIndex
    );


BOOL

DestroyPrivateObjectSecurity(
    _Pre_valid_ _Post_invalid_ PSECURITY_DESCRIPTOR* ObjectDescriptor
    );


BOOL

DuplicateToken(
    _In_ HANDLE ExistingTokenHandle,
    _In_ SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
    _Outptr_ PHANDLE DuplicateTokenHandle
    );



BOOL

DuplicateTokenEx(
    _In_ HANDLE hExistingToken,
    _In_ DWORD dwDesiredAccess,
    _In_opt_ LPSECURITY_ATTRIBUTES lpTokenAttributes,
    _In_ SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
    _In_ TOKEN_TYPE TokenType,
    _Outptr_ PHANDLE phNewToken
    );



BOOL

EqualPrefixSid(
    _In_ PSID pSid1,
    _In_ PSID pSid2
    );



BOOL

EqualSid(
    _In_ PSID pSid1,
    _In_ PSID pSid2
    );



BOOL

FindFirstFreeAce(
    _In_ PACL pAcl,
    _Outptr_ LPVOID* pAce
    );



PVOID

FreeSid(
    _In_ PSID pSid
    );



BOOL

GetAce(
    _In_ PACL pAcl,
    _In_ DWORD dwAceIndex,
    _Outptr_ LPVOID* pAce
    );



BOOL

GetAclInformation(
    _In_ PACL pAcl,
    _Out_writes_bytes_(nAclInformationLength) LPVOID pAclInformation,
    _In_ DWORD nAclInformationLength,
    _In_ ACL_INFORMATION_CLASS dwAclInformationClass
    );




BOOL

GetFileSecurityW(
    _In_ LPCWSTR lpFileName,
    _In_ SECURITY_INFORMATION RequestedInformation,
    _Out_writes_bytes_to_opt_(nLength,*lpnLengthNeeded) PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ DWORD nLength,
    _Out_ LPDWORD lpnLengthNeeded
    );



BOOL

GetKernelObjectSecurity(
    _In_ HANDLE Handle,
    _In_ SECURITY_INFORMATION RequestedInformation,
    _Out_writes_bytes_opt_(nLength) PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ DWORD nLength,
    _Out_ LPDWORD lpnLengthNeeded
    );



DWORD

GetLengthSid(
    _In_ _Post_readable_byte_size_(return) PSID pSid
    );



_Success_(return != FALSE)
BOOL

GetPrivateObjectSecurity(
    _In_ PSECURITY_DESCRIPTOR ObjectDescriptor,
    _In_ SECURITY_INFORMATION SecurityInformation,
    _Out_writes_bytes_to_opt_(DescriptorLength,*ReturnLength) PSECURITY_DESCRIPTOR ResultantDescriptor,
    _In_ DWORD DescriptorLength,
    _Out_ PDWORD ReturnLength
    );



BOOL

GetSecurityDescriptorControl(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _Out_ PSECURITY_DESCRIPTOR_CONTROL pControl,
    _Out_ LPDWORD lpdwRevision
    );



BOOL

GetSecurityDescriptorDacl(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _Out_ LPBOOL lpbDaclPresent,
    _Outptr_ PACL* pDacl,
    _Out_ LPBOOL lpbDaclDefaulted
    );



BOOL

GetSecurityDescriptorGroup(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _Outptr_ PSID* pGroup,
    _Out_ LPBOOL lpbGroupDefaulted
    );



DWORD

GetSecurityDescriptorLength(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor
    );



BOOL

GetSecurityDescriptorOwner(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _Outptr_ PSID* pOwner,
    _Out_ LPBOOL lpbOwnerDefaulted
    );



DWORD

GetSecurityDescriptorRMControl(
    _In_ PSECURITY_DESCRIPTOR SecurityDescriptor,
    _Out_ PUCHAR RMControl
    );



BOOL

GetSecurityDescriptorSacl(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _Out_ LPBOOL lpbSaclPresent,
    _Outptr_ PACL* pSacl,
    _Out_ LPBOOL lpbSaclDefaulted
    );



PSID_IDENTIFIER_AUTHORITY

GetSidIdentifierAuthority(
    _In_ PSID pSid
    );



DWORD

GetSidLengthRequired(
    _In_ UCHAR nSubAuthorityCount
    );



PDWORD

GetSidSubAuthority(
    _In_ PSID pSid,
    _In_ DWORD nSubAuthority
    );



PUCHAR

GetSidSubAuthorityCount(
    _In_ PSID pSid
    );



BOOL

GetTokenInformation(
    _In_ HANDLE TokenHandle,
    _In_ TOKEN_INFORMATION_CLASS TokenInformationClass,
    _Out_writes_bytes_to_opt_(TokenInformationLength,*ReturnLength) LPVOID TokenInformation,
    _In_ DWORD TokenInformationLength,
    _Out_ PDWORD ReturnLength
    );


BOOL

GetWindowsAccountDomainSid(
    _In_ PSID pSid,
    _Out_writes_bytes_to_opt_(*cbDomainSid,*cbDomainSid) PSID pDomainSid,
    _Inout_ DWORD* cbDomainSid
    );



BOOL

ImpersonateAnonymousToken(
    _In_ HANDLE ThreadHandle
    );


_Must_inspect_result_

BOOL

ImpersonateLoggedOnUser(
    _In_ HANDLE hToken
    );


_Must_inspect_result_

BOOL

ImpersonateSelf(
    _In_ SECURITY_IMPERSONATION_LEVEL ImpersonationLevel
    );



BOOL

InitializeAcl(
    _Out_writes_bytes_(nAclLength) PACL pAcl,
    _In_ DWORD nAclLength,
    _In_ DWORD dwAclRevision
    );



BOOL

InitializeSecurityDescriptor(
    _Out_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ DWORD dwRevision
    );



BOOL

InitializeSid(
    _Out_writes_bytes_(_Inexpressible_(GetSidLengthRequired(nSubAuthorityCount))) PSID Sid,
    _In_ PSID_IDENTIFIER_AUTHORITY pIdentifierAuthority,
    _In_ BYTE nSubAuthorityCount
    );



BOOL

IsTokenRestricted(
    _In_ HANDLE TokenHandle
    );




BOOL

IsValidAcl(
    _In_ PACL pAcl
    );



BOOL

IsValidSecurityDescriptor(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor
    );



BOOL

IsValidSid(
    _In_ PSID pSid
    );




BOOL

IsWellKnownSid(
    _In_ PSID pSid,
    _In_ WELL_KNOWN_SID_TYPE WellKnownSidType
    );



BOOL

MakeAbsoluteSD(
    _In_ PSECURITY_DESCRIPTOR pSelfRelativeSecurityDescriptor,
    _Out_writes_bytes_to_opt_(*lpdwAbsoluteSecurityDescriptorSize,*lpdwAbsoluteSecurityDescriptorSize) PSECURITY_DESCRIPTOR pAbsoluteSecurityDescriptor,
    _Inout_ LPDWORD lpdwAbsoluteSecurityDescriptorSize,
    _Out_writes_bytes_to_opt_(*lpdwDaclSize,*lpdwDaclSize) PACL pDacl,
    _Inout_ LPDWORD lpdwDaclSize,
    _Out_writes_bytes_to_opt_(*lpdwSaclSize,*lpdwSaclSize) PACL pSacl,
    _Inout_ LPDWORD lpdwSaclSize,
    _Out_writes_bytes_to_opt_(*lpdwOwnerSize,*lpdwOwnerSize) PSID pOwner,
    _Inout_ LPDWORD lpdwOwnerSize,
    _Out_writes_bytes_to_opt_(*lpdwPrimaryGroupSize,*lpdwPrimaryGroupSize) PSID pPrimaryGroup,
    _Inout_ LPDWORD lpdwPrimaryGroupSize
    );



BOOL

MakeSelfRelativeSD(
    _In_ PSECURITY_DESCRIPTOR pAbsoluteSecurityDescriptor,
    _Out_writes_bytes_to_opt_(*lpdwBufferLength,*lpdwBufferLength) PSECURITY_DESCRIPTOR pSelfRelativeSecurityDescriptor,
    _Inout_ LPDWORD lpdwBufferLength
    );




VOID

MapGenericMask(
    _Inout_ PDWORD AccessMask,
    _In_ PGENERIC_MAPPING GenericMapping
    );



BOOL

ObjectCloseAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ BOOL GenerateOnClose
    );




BOOL

ObjectDeleteAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ BOOL GenerateOnClose
    );



BOOL

ObjectOpenAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ LPWSTR ObjectTypeName,
    _In_opt_ LPWSTR ObjectName,
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ HANDLE ClientToken,
    _In_ DWORD DesiredAccess,
    _In_ DWORD GrantedAccess,
    _In_opt_ PPRIVILEGE_SET Privileges,
    _In_ BOOL ObjectCreation,
    _In_ BOOL AccessGranted,
    _Out_ LPBOOL GenerateOnClose
    );


BOOL

ObjectPrivilegeAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPVOID HandleId,
    _In_ HANDLE ClientToken,
    _In_ DWORD DesiredAccess,
    _In_ PPRIVILEGE_SET Privileges,
    _In_ BOOL AccessGranted
    );



BOOL

PrivilegeCheck(
    _In_ HANDLE ClientToken,
    _Inout_ PPRIVILEGE_SET RequiredPrivileges,
    _Out_ LPBOOL pfResult
    );



BOOL

PrivilegedServiceAuditAlarmW(
    _In_ LPCWSTR SubsystemName,
    _In_ LPCWSTR ServiceName,
    _In_ HANDLE ClientToken,
    _In_ PPRIVILEGE_SET Privileges,
    _In_ BOOL AccessGranted
    );



VOID

QuerySecurityAccessMask(
    _In_ SECURITY_INFORMATION SecurityInformation,
    _Out_ LPDWORD DesiredAccess
    );



BOOL

RevertToSelf(
    VOID
    );



BOOL

SetAclInformation(
    _Inout_ PACL pAcl,
    _In_reads_bytes_(nAclInformationLength) LPVOID pAclInformation,
    _In_ DWORD nAclInformationLength,
    _In_ ACL_INFORMATION_CLASS dwAclInformationClass
    );



BOOL

SetFileSecurityW(
    _In_ LPCWSTR lpFileName,
    _In_ SECURITY_INFORMATION SecurityInformation,
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor
    );


BOOL

SetKernelObjectSecurity(
    _In_ HANDLE Handle,
    _In_ SECURITY_INFORMATION SecurityInformation,
    _In_ PSECURITY_DESCRIPTOR SecurityDescriptor
    );



BOOL

SetPrivateObjectSecurity(
    _In_ SECURITY_INFORMATION SecurityInformation,
    _In_ PSECURITY_DESCRIPTOR ModificationDescriptor,
    _Inout_ PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor,
    _In_ PGENERIC_MAPPING GenericMapping,
    _In_opt_ HANDLE Token
    );



BOOL

SetPrivateObjectSecurityEx(
    _In_ SECURITY_INFORMATION SecurityInformation,
    _In_ PSECURITY_DESCRIPTOR ModificationDescriptor,
    _Inout_ PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor,
    _In_ ULONG AutoInheritFlags,
    _In_ PGENERIC_MAPPING GenericMapping,
    _In_opt_ HANDLE Token
    );


VOID

SetSecurityAccessMask(
    _In_ SECURITY_INFORMATION SecurityInformation,
    _Out_ LPDWORD DesiredAccess
    );




BOOL

SetSecurityDescriptorControl(
    _In_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ SECURITY_DESCRIPTOR_CONTROL ControlBitsOfInterest,
    _In_ SECURITY_DESCRIPTOR_CONTROL ControlBitsToSet
    );



BOOL

SetSecurityDescriptorDacl(
    _Inout_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ BOOL bDaclPresent,
    _In_opt_ PACL pDacl,
    _In_ BOOL bDaclDefaulted
    );



BOOL

SetSecurityDescriptorGroup(
    _Inout_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_opt_ PSID pGroup,
    _In_ BOOL bGroupDefaulted
    );



BOOL

SetSecurityDescriptorOwner(
    _Inout_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_opt_ PSID pOwner,
    _In_ BOOL bOwnerDefaulted
    );



DWORD

SetSecurityDescriptorRMControl(
    _Inout_ PSECURITY_DESCRIPTOR SecurityDescriptor,
    _In_opt_ PUCHAR RMControl
    );



BOOL

SetSecurityDescriptorSacl(
    _Inout_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
    _In_ BOOL bSaclPresent,
    _In_opt_ PACL pSacl,
    _In_ BOOL bSaclDefaulted
    );



BOOL

SetTokenInformation(
    _In_ HANDLE TokenHandle,
    _In_ TOKEN_INFORMATION_CLASS TokenInformationClass,
    _In_reads_bytes_(TokenInformationLength) LPVOID TokenInformation,
    _In_ DWORD TokenInformationLength
    );



BOOL

SetCachedSigningLevel(
    _In_reads_(SourceFileCount) PHANDLE SourceFiles,
    _In_ ULONG SourceFileCount,
    _In_ ULONG Flags,
    _In_opt_ HANDLE TargetFile
    );



BOOL

GetCachedSigningLevel(
    _In_ HANDLE File,
    _Out_ PULONG Flags,
    _Out_ PULONG SigningLevel,
    _Out_writes_bytes_to_opt_(*ThumbprintSize,*ThumbprintSize) PUCHAR Thumbprint,
    _Inout_opt_ PULONG ThumbprintSize,
    _Out_opt_ PULONG ThumbprintAlgorithm
    );



LONG

CveEventWrite(
    _In_ PCWSTR CveId,
    _In_opt_ PCWSTR AdditionalDetails
    );



BOOL

DeriveCapabilitySidsFromName(
    _In_ LPCWSTR CapName,
    _Outptr_result_buffer_maybenull_(*CapabilityGroupSidCount) PSID** CapabilityGroupSids,
    _Out_ DWORD* CapabilityGroupSidCount,
    _Outptr_result_buffer_maybenull_(*CapabilitySidCount) PSID** CapabilitySids,
    _Out_ DWORD* CapabilitySidCount
    );
"""
