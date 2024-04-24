from ctypes import POINTER, Structure, Union
from ctypes.wintypes import BOOLEAN, LARGE_INTEGER, ULONG

from .. import CEnum, windll
from ..shared.ntdef import NTSTATUS, PVOID, UCHAR
from .lsalookup import LSA_UNICODE_STRING
from .winnt import ACCESS_MASK, PSID

LSA_HANDLE = PVOID
LSA_ENUMERATION_HANDLE = ULONG


class LSA_FOREST_TRUST_RECORD_TYPE(CEnum):
    ForestTrustTopLevelName = 0
    ForestTrustTopLevelNameEx = 1
    ForestTrustDomainInfo = 2
    ForestTrustRecordTypeLast = 2  # ForestTrustDomainInfo


class TRUSTED_INFORMATION_CLASS(CEnum):
    TrustedDomainNameInformation = 1
    TrustedControllersInformation = 2
    TrustedPosixOffsetInformation = 3
    TrustedPasswordInformation = 4
    TrustedDomainInformationBasic = 5
    TrustedDomainInformationEx = 6
    TrustedDomainAuthInformation = 7
    TrustedDomainFullInformation = 8
    TrustedDomainAuthInformationInternal = 9
    TrustedDomainFullInformationInternal = 10
    TrustedDomainInformationEx2Internal = 11
    TrustedDomainFullInformation2Internal = 12
    TrustedDomainSupportedEncryptionTypes = 13


class LSA_FOREST_TRUST_COLLISION_RECORD_TYPE(CEnum):
    CollisionTdo = 0
    CollisionXref = 1
    CollisionOther = 2


class LSA_FOREST_TRUST_DOMAIN_INFO(Structure):
    _fields_ = [
        ("Sid", PSID),
        ("DnsName", LSA_UNICODE_STRING),
        ("NetbiosName", LSA_UNICODE_STRING),
    ]


class LSA_FOREST_TRUST_BINARY_DATA(Structure):
    _fields_ = [
        ("Length", ULONG),
        ("Buffer", POINTER(UCHAR)),
    ]


class _ForestTrustData(Union):
    _fields_ = [
        ("TopLevelName", LSA_UNICODE_STRING),
        ("DomainInfo", LSA_FOREST_TRUST_DOMAIN_INFO),
        ("Data", LSA_FOREST_TRUST_BINARY_DATA),
    ]


class LSA_FOREST_TRUST_RECORD(Structure):
    _fields_ = [
        ("Flags", ULONG),
        ("ForestTrustType", LSA_FOREST_TRUST_RECORD_TYPE),
        ("Time", LARGE_INTEGER),
        ("ForestTrustData", _ForestTrustData),
    ]


class LSA_FOREST_TRUST_INFORMATION(Structure):
    _fields_ = [
        ("RecordCount", ULONG),
        ("Entries", POINTER(POINTER(LSA_FOREST_TRUST_RECORD))),
    ]


class LSA_AUTH_INFORMATION(Structure):
    _fields_ = [
        ("LastUpdateTime", LARGE_INTEGER),
        ("AuthType", ULONG),
        ("AuthInfoLength", ULONG),
        ("AuthInfo", POINTER(UCHAR)),
    ]


class TRUSTED_DOMAIN_AUTH_INFORMATION(Structure):
    _fields_ = [
        ("IncomingAuthInfos", ULONG),
        ("IncomingAuthenticationInformation", POINTER(LSA_AUTH_INFORMATION)),
        ("IncomingPreviousAuthenticationInformation", POINTER(LSA_AUTH_INFORMATION)),
        ("OutgoingAuthInfos", ULONG),
        ("OutgoingAuthenticationInformation", POINTER(LSA_AUTH_INFORMATION)),
        ("OutgoingPreviousAuthenticationInformation", POINTER(LSA_AUTH_INFORMATION)),
    ]


class TRUSTED_DOMAIN_INFORMATION_EX(Structure):
    _fields_ = [
        ("Name", LSA_UNICODE_STRING),
        ("FlatName", LSA_UNICODE_STRING),
        ("Sid", PSID),
        ("TrustDirection", ULONG),
        ("TrustType", ULONG),
        ("TrustAttributes", ULONG),
    ]


class LSA_FOREST_TRUST_COLLISION_RECORD(Structure):
    _fields_ = [
        ("Index", ULONG),
        ("Type", LSA_FOREST_TRUST_COLLISION_RECORD_TYPE),
        ("Flags", ULONG),
        ("Name", LSA_UNICODE_STRING),
    ]


class LSA_FOREST_TRUST_COLLISION_INFORMATION(Structure):
    _fields_ = [
        ("RecordCount", ULONG),
        ("Entries", POINTER(POINTER(LSA_FOREST_TRUST_COLLISION_RECORD))),
    ]


LsaOpenTrustedDomainByName = windll.advapi32.LsaOpenTrustedDomainByName
LsaOpenTrustedDomainByName.argtypes = [LSA_HANDLE, POINTER(LSA_UNICODE_STRING), ACCESS_MASK, POINTER(LSA_HANDLE)]
LsaOpenTrustedDomainByName.restype = NTSTATUS

LsaQueryTrustedDomainInfo = windll.advapi32.LsaQueryTrustedDomainInfo
LsaQueryTrustedDomainInfo.argtypes = [LSA_HANDLE, PSID, TRUSTED_INFORMATION_CLASS, POINTER(PVOID)]
LsaQueryTrustedDomainInfo.restype = NTSTATUS

LsaSetTrustedDomainInformation = windll.advapi32.LsaSetTrustedDomainInformation
LsaSetTrustedDomainInformation.argtypes = [LSA_HANDLE, PSID, TRUSTED_INFORMATION_CLASS, PVOID]
LsaSetTrustedDomainInformation.restype = NTSTATUS

LsaDeleteTrustedDomain = windll.advapi32.LsaDeleteTrustedDomain
LsaDeleteTrustedDomain.argtypes = [LSA_HANDLE, PSID]
LsaDeleteTrustedDomain.restype = NTSTATUS

LsaQueryTrustedDomainInfoByName = windll.advapi32.LsaQueryTrustedDomainInfoByName
LsaQueryTrustedDomainInfoByName.argtypes = [
    LSA_HANDLE,
    POINTER(LSA_UNICODE_STRING),
    TRUSTED_INFORMATION_CLASS,
    POINTER(PVOID),
]
LsaQueryTrustedDomainInfoByName.restype = NTSTATUS

LsaSetTrustedDomainInfoByName = windll.advapi32.LsaSetTrustedDomainInfoByName
LsaSetTrustedDomainInfoByName.argtypes = [LSA_HANDLE, POINTER(LSA_UNICODE_STRING), TRUSTED_INFORMATION_CLASS, PVOID]
LsaSetTrustedDomainInfoByName.restype = NTSTATUS

LsaEnumerateTrustedDomainsEx = windll.advapi32.LsaEnumerateTrustedDomainsEx
LsaEnumerateTrustedDomainsEx.argtypes = [
    LSA_HANDLE,
    POINTER(LSA_ENUMERATION_HANDLE),
    POINTER(PVOID),
    ULONG,
    POINTER(ULONG),
]
LsaEnumerateTrustedDomainsEx.restype = NTSTATUS

LsaCreateTrustedDomainEx = windll.advapi32.LsaCreateTrustedDomainEx
LsaCreateTrustedDomainEx.argtypes = [
    LSA_HANDLE,
    POINTER(TRUSTED_DOMAIN_INFORMATION_EX),
    POINTER(TRUSTED_DOMAIN_AUTH_INFORMATION),
    ACCESS_MASK,
    POINTER(LSA_HANDLE),
]
LsaCreateTrustedDomainEx.restype = NTSTATUS

LsaQueryForestTrustInformation = windll.advapi32.LsaQueryForestTrustInformation
LsaQueryForestTrustInformation.argtypes = [
    LSA_HANDLE,
    POINTER(LSA_UNICODE_STRING),
    POINTER(POINTER(LSA_FOREST_TRUST_INFORMATION)),
]
LsaQueryForestTrustInformation.restype = NTSTATUS

LsaSetForestTrustInformation = windll.advapi32.LsaSetForestTrustInformation
LsaSetForestTrustInformation.argtypes = [
    LSA_HANDLE,
    POINTER(LSA_UNICODE_STRING),
    POINTER(LSA_FOREST_TRUST_INFORMATION),
    BOOLEAN,
    POINTER(POINTER(LSA_FOREST_TRUST_COLLISION_INFORMATION)),
]
LsaSetForestTrustInformation.restype = NTSTATUS

LsaStorePrivateData = windll.advapi32.LsaStorePrivateData
LsaStorePrivateData.argtypes = [LSA_HANDLE, POINTER(LSA_UNICODE_STRING), POINTER(LSA_UNICODE_STRING)]
LsaStorePrivateData.restype = NTSTATUS

LsaRetrievePrivateData = windll.advapi32.LsaRetrievePrivateData
LsaRetrievePrivateData.argtypes = [LSA_HANDLE, POINTER(LSA_UNICODE_STRING), POINTER(POINTER(LSA_UNICODE_STRING))]
LsaRetrievePrivateData.restype = NTSTATUS

LsaNtStatusToWinError = windll.advapi32.LsaNtStatusToWinError
LsaNtStatusToWinError.argtypes = [NTSTATUS]
LsaNtStatusToWinError.restype = ULONG
