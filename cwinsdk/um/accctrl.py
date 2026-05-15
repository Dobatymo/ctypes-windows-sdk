from ctypes import POINTER, Structure
from ctypes.wintypes import DWORD, LONG, LPSTR, LPWSTR, ULONG

from .. import CEnum
from ..shared.guiddef import GUID
from .winnt import LPCH, LPWCH, SID


class SE_OBJECT_TYPE(CEnum):
    SE_UNKNOWN_OBJECT_TYPE = 0
    SE_FILE_OBJECT = 1
    SE_SERVICE = 2
    SE_PRINTER = 3
    SE_REGISTRY_KEY = 4
    SE_LMSHARE = 5
    SE_KERNEL_OBJECT = 6
    SE_WINDOW_OBJECT = 7
    SE_DS_OBJECT = 8
    SE_DS_OBJECT_ALL = 9
    SE_PROVIDER_DEFINED_OBJECT = 10
    SE_WMIGUID_OBJECT = 11
    SE_REGISTRY_WOW64_32KEY = 12
    SE_REGISTRY_WOW64_64KEY = 13


class TRUSTEE_TYPE(CEnum):
    TRUSTEE_IS_UNKNOWN = 0
    TRUSTEE_IS_USER = 1
    TRUSTEE_IS_GROUP = 2
    TRUSTEE_IS_DOMAIN = 3
    TRUSTEE_IS_ALIAS = 4
    TRUSTEE_IS_WELL_KNOWN_GROUP = 5
    TRUSTEE_IS_DELETED = 6
    TRUSTEE_IS_INVALID = 7
    TRUSTEE_IS_COMPUTER = 8


class TRUSTEE_FORM(CEnum):
    TRUSTEE_IS_SID = 0
    TRUSTEE_IS_NAME = 1
    TRUSTEE_BAD_FORM = 2
    TRUSTEE_IS_OBJECTS_AND_SID = 3
    TRUSTEE_IS_OBJECTS_AND_NAME = 4


class MULTIPLE_TRUSTEE_OPERATION(CEnum):
    NO_MULTIPLE_TRUSTEE = 0
    TRUSTEE_IS_IMPERSONATE = 1


class OBJECTS_AND_SID(Structure):
    _fields_ = [
        ("ObjectsPresent", DWORD),
        ("ObjectTypeGuid", GUID),
        ("InheritedObjectTypeGuid", GUID),
        ("pSid", POINTER(SID)),
    ]


class OBJECTS_AND_NAME_A(Structure):
    _fields_ = [
        ("ObjectsPresent", DWORD),
        ("ObjectType", SE_OBJECT_TYPE),
        ("ObjectTypeName", LPSTR),
        ("InheritedObjectTypeName", LPSTR),
        ("ptstrName", LPSTR),
    ]


class OBJECTS_AND_NAME_W(Structure):
    _fields_ = [
        ("ObjectsPresent", DWORD),
        ("ObjectType", SE_OBJECT_TYPE),
        ("ObjectTypeName", LPWSTR),
        ("InheritedObjectTypeName", LPWSTR),
        ("ptstrName", LPWSTR),
    ]


class TRUSTEE_A(Structure):
    pass


TRUSTEE_A._fields_ = [
    ("pMultipleTrustee", POINTER(TRUSTEE_A)),
    ("MultipleTrusteeOperation", MULTIPLE_TRUSTEE_OPERATION),
    ("TrusteeForm", TRUSTEE_FORM),
    ("TrusteeType", TRUSTEE_TYPE),
    ("ptstrName", LPCH),
]


class TRUSTEE_A(Structure):
    _fields_ = [
        ("pMultipleTrustee", POINTER(TRUSTEE_A)),
        ("MultipleTrusteeOperation", MULTIPLE_TRUSTEE_OPERATION),
        ("TrusteeForm", TRUSTEE_FORM),
        ("TrusteeType", TRUSTEE_TYPE),
        ("ptstrName", LPCH),
    ]


TRUSTEEA = TRUSTEE_A


class TRUSTEE_W(Structure):
    pass


TRUSTEE_W._fields_ = [
    ("pMultipleTrustee", POINTER(TRUSTEE_W)),
    ("MultipleTrusteeOperation", MULTIPLE_TRUSTEE_OPERATION),
    ("TrusteeForm", TRUSTEE_FORM),
    ("TrusteeType", TRUSTEE_TYPE),
    ("ptstrName", LPWCH),
]

TRUSTEEW = TRUSTEE_W


class ACCESS_MODE(CEnum):
    NOT_USED_ACCESS = 0
    GRANT_ACCESS = 1
    SET_ACCESS = 2
    DENY_ACCESS = 3
    REVOKE_ACCESS = 4
    SET_AUDIT_SUCCESS = 5
    SET_AUDIT_FAILURE = 6


class EXPLICIT_ACCESS_A(Structure):
    _fields_ = [
        ("grfAccessPermissions", DWORD),
        ("grfAccessMode", ACCESS_MODE),
        ("grfInheritance", DWORD),
        ("Trustee", TRUSTEE_A),
    ]


EXPLICIT_ACCESSA = EXPLICIT_ACCESS_A


class EXPLICIT_ACCESS_W(Structure):
    _fields_ = [
        ("grfAccessPermissions", DWORD),
        ("grfAccessMode", ACCESS_MODE),
        ("grfInheritance", DWORD),
        ("Trustee", TRUSTEE_W),
    ]


EXPLICIT_ACCESSW = EXPLICIT_ACCESS_W


class PROGRESS_INVOKE_SETTING(CEnum):
    ProgressInvokeNever = 1  # Never invoke the progress function
    ProgressInvokeEveryObject = 2  # Invoke for each object
    ProgressInvokeOnError = 3  # Invoke only for each error case
    ProgressCancelOperation = 4  # Stop propagation and return
    ProgressRetryOperation = 5  # Retry operation on subtree
    ProgressInvokePrePostError = 6  # Invoke Pre, Post, Error


PROG_INVOKE_SETTING = PROGRESS_INVOKE_SETTING


class FN_OBJECT_MGR_FUNCTIONS(Structure):
    _fields_ = [
        ("Placeholder", ULONG),
    ]


FN_OBJECT_MGR_FUNCTS = FN_OBJECT_MGR_FUNCTIONS


class INHERITED_FROMA(Structure):
    _fields_ = [
        ("GenerationGap", LONG),
        ("AncestorName", LPSTR),
    ]


class INHERITED_FROMW(Structure):
    _fields_ = [
        ("GenerationGap", LONG),
        ("AncestorName", LPWSTR),
    ]
