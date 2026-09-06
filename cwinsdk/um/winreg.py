"""ctypes bindings for the Windows registry API."""

from ctypes import CFUNCTYPE, POINTER, Structure, c_int, c_long, c_void_p, cast, sizeof
from ctypes.wintypes import BOOL, BYTE, DWORD, HANDLE, LONG, LPBYTE, LPCSTR, LPCWSTR, LPSTR, LPWSTR, ULONG

from .. import error_success, nonfalse, windll
from ..shared.basetsd import DWORD_PTR, ULONG_PTR
from ..shared.minwindef import HKEY, LPCVOID, LPDWORD, LPVOID
from ..shared.ntdef import PVOID
from ..wintypes import BOOLEAN
from .minwinbase import FILETIME, LPSECURITY_ATTRIBUTES
from .reason import (
    SHTDN_REASON_FLAG_PLANNED,
    SHTDN_REASON_LEGACY_API,
    SHTDN_REASON_MAJOR_HARDWARE,
    SHTDN_REASON_MAJOR_OTHER,
    SHTDN_REASON_MAJOR_SOFTWARE,
    SHTDN_REASON_MAJOR_SYSTEM,
    SHTDN_REASON_MINOR_HUNG,
    SHTDN_REASON_MINOR_INSTALLATION,
    SHTDN_REASON_MINOR_OTHER,
    SHTDN_REASON_MINOR_RECONFIG,
    SHTDN_REASON_MINOR_UNSTABLE,
    SHTDN_REASON_UNKNOWN,
)
from .winnt import ACCESS_MASK, PSECURITY_DESCRIPTOR, SECURITY_INFORMATION

LSTATUS = c_long
REGSAM = ACCESS_MASK
PHKEY = POINTER(HKEY)
PBOOLEAN = POINTER(BOOLEAN)
PLONG = POINTER(LONG)

PROVIDER_KEEPS_VALUE_LENGTH = 0x1

RRF_RT_REG_NONE = 0x00000001
RRF_RT_REG_SZ = 0x00000002
RRF_RT_REG_EXPAND_SZ = 0x00000004
RRF_RT_REG_BINARY = 0x00000008
RRF_RT_REG_DWORD = 0x00000010
RRF_RT_REG_MULTI_SZ = 0x00000020
RRF_RT_REG_QWORD = 0x00000040
RRF_RT_DWORD = RRF_RT_REG_BINARY | RRF_RT_REG_DWORD
RRF_RT_QWORD = RRF_RT_REG_BINARY | RRF_RT_REG_QWORD
RRF_RT_ANY = 0x0000FFFF
RRF_SUBKEY_WOW6464KEY = 0x00010000
RRF_SUBKEY_WOW6432KEY = 0x00020000
RRF_WOW64_MASK = 0x00030000
RRF_NOEXPAND = 0x10000000
RRF_ZEROONFAILURE = 0x20000000

REG_PROCESS_APPKEY = 0x00000001
REG_USE_CURRENT_SECURITY_CONTEXT = 0x00000002
REG_MUI_STRING_TRUNCATE = 0x00000001
REG_SECURE_CONNECTION = 0x00000001
REG_ALLOW_TRANSPORT_FALLBACK = 0x00000002
REG_ALLOW_UNSECURE_CONNECTION = 0x00000004
WIN31_CLASS = None

REASON_SWINSTALL = SHTDN_REASON_MAJOR_SOFTWARE | SHTDN_REASON_MINOR_INSTALLATION
REASON_HWINSTALL = SHTDN_REASON_MAJOR_HARDWARE | SHTDN_REASON_MINOR_INSTALLATION
REASON_SERVICEHANG = SHTDN_REASON_MAJOR_SOFTWARE | SHTDN_REASON_MINOR_HUNG
REASON_UNSTABLE = SHTDN_REASON_MAJOR_SYSTEM | SHTDN_REASON_MINOR_UNSTABLE
REASON_SWHWRECONF = SHTDN_REASON_MAJOR_SOFTWARE | SHTDN_REASON_MINOR_RECONFIG
REASON_OTHER = SHTDN_REASON_MAJOR_OTHER | SHTDN_REASON_MINOR_OTHER
REASON_UNKNOWN = SHTDN_REASON_UNKNOWN
REASON_LEGACY_API = SHTDN_REASON_LEGACY_API
REASON_PLANNED_FLAG = SHTDN_REASON_FLAG_PLANNED
MAX_SHUTDOWN_TIMEOUT = 10 * 365 * 24 * 60 * 60

SHUTDOWN_FORCE_OTHERS = 0x00000001
SHUTDOWN_FORCE_SELF = 0x00000002
SHUTDOWN_RESTART = 0x00000004
SHUTDOWN_POWEROFF = 0x00000008
SHUTDOWN_NOREBOOT = 0x00000010
SHUTDOWN_GRACE_OVERRIDE = 0x00000020
SHUTDOWN_INSTALL_UPDATES = 0x00000040
SHUTDOWN_RESTARTAPPS = 0x00000080
SHUTDOWN_SKIP_SVC_PRESHUTDOWN = 0x00000100
SHUTDOWN_HYBRID = 0x00000200
SHUTDOWN_RESTART_BOOTOPTIONS = 0x00000400
SHUTDOWN_SOFT_REBOOT = 0x00000800
SHUTDOWN_MOBILE_UI = 0x00001000
SHUTDOWN_ARSO = 0x00002000
SHUTDOWN_CHECK_SAFE_FOR_SERVER = 0x00004000
SHUTDOWN_VAIL_CONTAINER = 0x00008000
SHUTDOWN_SYSTEM_INITIATED = 0x00010000
SHUTDOWN_UPDATE_POWEROFF = 0x00020000


def _hkey(value):
    if value & 0x80000000 and sizeof(ULONG_PTR) == 8:
        value |= 0xFFFFFFFF00000000
    return cast(c_void_p(value), HKEY)


HKEY_CLASSES_ROOT = _hkey(0x80000000)
HKEY_CURRENT_USER = _hkey(0x80000001)
HKEY_LOCAL_MACHINE = _hkey(0x80000002)
HKEY_USERS = _hkey(0x80000003)
HKEY_PERFORMANCE_DATA = _hkey(0x80000004)
HKEY_PERFORMANCE_TEXT = _hkey(0x80000050)
HKEY_PERFORMANCE_NLSTEXT = _hkey(0x80000060)
HKEY_CURRENT_CONFIG = _hkey(0x80000005)
HKEY_DYN_DATA = _hkey(0x80000006)
HKEY_CURRENT_USER_LOCAL_SETTINGS = _hkey(0x80000007)


class val_context(Structure):
    _fields_ = [("valuelen", c_int), ("value_context", LPVOID), ("val_buff_ptr", LPVOID)]


PVALCONTEXT = POINTER(val_context)


class PVALUEA(Structure):
    _fields_ = [
        ("pv_valuename", LPSTR),
        ("pv_valuelen", c_int),
        ("pv_value_context", LPVOID),
        ("pv_type", DWORD),
    ]


PPVALUEA = POINTER(PVALUEA)


class PVALUEW(Structure):
    _fields_ = [
        ("pv_valuename", LPWSTR),
        ("pv_valuelen", c_int),
        ("pv_value_context", LPVOID),
        ("pv_type", DWORD),
    ]


PPVALUEW = POINTER(PVALUEW)

QUERYHANDLER = CFUNCTYPE(DWORD, LPVOID, PVALCONTEXT, DWORD, LPVOID, POINTER(DWORD), DWORD)
PQUERYHANDLER = QUERYHANDLER


class REG_PROVIDER(Structure):
    _fields_ = [
        ("pi_R0_1val", PQUERYHANDLER),
        ("pi_R0_allvals", PQUERYHANDLER),
        ("pi_R3_1val", PQUERYHANDLER),
        ("pi_R3_allvals", PQUERYHANDLER),
        ("pi_flags", DWORD),
        ("pi_key_context", LPVOID),
    ]


PPROVIDER = POINTER(REG_PROVIDER)


class VALENTA(Structure):
    _fields_ = [
        ("ve_valuename", LPSTR),
        ("ve_valuelen", DWORD),
        ("ve_valueptr", DWORD_PTR),
        ("ve_type", DWORD),
    ]


PVALENTA = POINTER(VALENTA)


class VALENTW(Structure):
    _fields_ = [
        ("ve_valuename", LPWSTR),
        ("ve_valuelen", DWORD),
        ("ve_valueptr", DWORD_PTR),
        ("ve_type", DWORD),
    ]


PVALENTW = POINTER(VALENTW)

advapi32 = windll.advapi32

RegCloseKey = advapi32.RegCloseKey
RegCloseKey.argtypes = [HKEY]
RegCloseKey.restype = LSTATUS
RegCloseKey.errcheck = error_success

RegOverridePredefKey = advapi32.RegOverridePredefKey
RegOverridePredefKey.argtypes = [HKEY, HKEY]
RegOverridePredefKey.restype = LSTATUS
RegOverridePredefKey.errcheck = error_success

RegOpenUserClassesRoot = advapi32.RegOpenUserClassesRoot
RegOpenUserClassesRoot.argtypes = [HANDLE, DWORD, REGSAM, PHKEY]
RegOpenUserClassesRoot.restype = LSTATUS
RegOpenUserClassesRoot.errcheck = error_success

RegOpenCurrentUser = advapi32.RegOpenCurrentUser
RegOpenCurrentUser.argtypes = [REGSAM, PHKEY]
RegOpenCurrentUser.restype = LSTATUS
RegOpenCurrentUser.errcheck = error_success

RegDisablePredefinedCache = advapi32.RegDisablePredefinedCache
RegDisablePredefinedCache.argtypes = []
RegDisablePredefinedCache.restype = LSTATUS
RegDisablePredefinedCache.errcheck = error_success

RegDisablePredefinedCacheEx = advapi32.RegDisablePredefinedCacheEx
RegDisablePredefinedCacheEx.argtypes = []
RegDisablePredefinedCacheEx.restype = LSTATUS
RegDisablePredefinedCacheEx.errcheck = error_success

RegConnectRegistryA = advapi32.RegConnectRegistryA
RegConnectRegistryA.argtypes = [LPCSTR, HKEY, PHKEY]
RegConnectRegistryA.restype = LSTATUS
RegConnectRegistryA.errcheck = error_success

RegConnectRegistryW = advapi32.RegConnectRegistryW
RegConnectRegistryW.argtypes = [LPCWSTR, HKEY, PHKEY]
RegConnectRegistryW.restype = LSTATUS
RegConnectRegistryW.errcheck = error_success

RegConnectRegistryExA = advapi32.RegConnectRegistryExA
RegConnectRegistryExA.argtypes = [LPCSTR, HKEY, ULONG, PHKEY]
RegConnectRegistryExA.restype = LSTATUS
RegConnectRegistryExA.errcheck = error_success

RegConnectRegistryExW = advapi32.RegConnectRegistryExW
RegConnectRegistryExW.argtypes = [LPCWSTR, HKEY, ULONG, PHKEY]
RegConnectRegistryExW.restype = LSTATUS
RegConnectRegistryExW.errcheck = error_success

RegCreateKeyA = advapi32.RegCreateKeyA
RegCreateKeyA.argtypes = [HKEY, LPCSTR, PHKEY]
RegCreateKeyA.restype = LSTATUS
RegCreateKeyA.errcheck = error_success

RegCreateKeyW = advapi32.RegCreateKeyW
RegCreateKeyW.argtypes = [HKEY, LPCWSTR, PHKEY]
RegCreateKeyW.restype = LSTATUS
RegCreateKeyW.errcheck = error_success

RegCreateKeyExA = advapi32.RegCreateKeyExA
RegCreateKeyExA.argtypes = [HKEY, LPCSTR, DWORD, LPSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD]
RegCreateKeyExA.restype = LSTATUS
RegCreateKeyExA.errcheck = error_success

RegCreateKeyExW = advapi32.RegCreateKeyExW
RegCreateKeyExW.argtypes = [HKEY, LPCWSTR, DWORD, LPWSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD]
RegCreateKeyExW.restype = LSTATUS
RegCreateKeyExW.errcheck = error_success

RegCreateKeyTransactedA = advapi32.RegCreateKeyTransactedA
RegCreateKeyTransactedA.argtypes = [
    HKEY,
    LPCSTR,
    DWORD,
    LPSTR,
    DWORD,
    REGSAM,
    LPSECURITY_ATTRIBUTES,
    PHKEY,
    LPDWORD,
    HANDLE,
    PVOID,
]
RegCreateKeyTransactedA.restype = LSTATUS
RegCreateKeyTransactedA.errcheck = error_success

RegCreateKeyTransactedW = advapi32.RegCreateKeyTransactedW
RegCreateKeyTransactedW.argtypes = [
    HKEY,
    LPCWSTR,
    DWORD,
    LPWSTR,
    DWORD,
    REGSAM,
    LPSECURITY_ATTRIBUTES,
    PHKEY,
    LPDWORD,
    HANDLE,
    PVOID,
]
RegCreateKeyTransactedW.restype = LSTATUS
RegCreateKeyTransactedW.errcheck = error_success

RegDeleteKeyA = advapi32.RegDeleteKeyA
RegDeleteKeyA.argtypes = [HKEY, LPCSTR]
RegDeleteKeyA.restype = LSTATUS
RegDeleteKeyA.errcheck = error_success

RegDeleteKeyW = advapi32.RegDeleteKeyW
RegDeleteKeyW.argtypes = [HKEY, LPCWSTR]
RegDeleteKeyW.restype = LSTATUS
RegDeleteKeyW.errcheck = error_success

RegDeleteKeyExA = advapi32.RegDeleteKeyExA
RegDeleteKeyExA.argtypes = [HKEY, LPCSTR, REGSAM, DWORD]
RegDeleteKeyExA.restype = LSTATUS
RegDeleteKeyExA.errcheck = error_success

RegDeleteKeyExW = advapi32.RegDeleteKeyExW
RegDeleteKeyExW.argtypes = [HKEY, LPCWSTR, REGSAM, DWORD]
RegDeleteKeyExW.restype = LSTATUS
RegDeleteKeyExW.errcheck = error_success

RegDeleteKeyTransactedA = advapi32.RegDeleteKeyTransactedA
RegDeleteKeyTransactedA.argtypes = [HKEY, LPCSTR, REGSAM, DWORD, HANDLE, PVOID]
RegDeleteKeyTransactedA.restype = LSTATUS
RegDeleteKeyTransactedA.errcheck = error_success

RegDeleteKeyTransactedW = advapi32.RegDeleteKeyTransactedW
RegDeleteKeyTransactedW.argtypes = [HKEY, LPCWSTR, REGSAM, DWORD, HANDLE, PVOID]
RegDeleteKeyTransactedW.restype = LSTATUS
RegDeleteKeyTransactedW.errcheck = error_success

RegDisableReflectionKey = advapi32.RegDisableReflectionKey
RegDisableReflectionKey.argtypes = [HKEY]
RegDisableReflectionKey.restype = LSTATUS
RegDisableReflectionKey.errcheck = error_success

RegEnableReflectionKey = advapi32.RegEnableReflectionKey
RegEnableReflectionKey.argtypes = [HKEY]
RegEnableReflectionKey.restype = LSTATUS
RegEnableReflectionKey.errcheck = error_success

RegQueryReflectionKey = advapi32.RegQueryReflectionKey
RegQueryReflectionKey.argtypes = [HKEY, POINTER(BOOL)]
RegQueryReflectionKey.restype = LSTATUS
RegQueryReflectionKey.errcheck = error_success

RegDeleteValueA = advapi32.RegDeleteValueA
RegDeleteValueA.argtypes = [HKEY, LPCSTR]
RegDeleteValueA.restype = LSTATUS
RegDeleteValueA.errcheck = error_success

RegDeleteValueW = advapi32.RegDeleteValueW
RegDeleteValueW.argtypes = [HKEY, LPCWSTR]
RegDeleteValueW.restype = LSTATUS
RegDeleteValueW.errcheck = error_success

RegEnumKeyA = advapi32.RegEnumKeyA
RegEnumKeyA.argtypes = [HKEY, DWORD, LPSTR, DWORD]
RegEnumKeyA.restype = LSTATUS
RegEnumKeyA.errcheck = error_success

RegEnumKeyW = advapi32.RegEnumKeyW
RegEnumKeyW.argtypes = [HKEY, DWORD, LPWSTR, DWORD]
RegEnumKeyW.restype = LSTATUS
RegEnumKeyW.errcheck = error_success

RegEnumKeyExA = advapi32.RegEnumKeyExA
RegEnumKeyExA.argtypes = [HKEY, DWORD, LPSTR, LPDWORD, LPDWORD, LPSTR, LPDWORD, POINTER(FILETIME)]
RegEnumKeyExA.restype = LSTATUS
RegEnumKeyExA.errcheck = error_success

RegEnumKeyExW = advapi32.RegEnumKeyExW
RegEnumKeyExW.argtypes = [HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPWSTR, LPDWORD, POINTER(FILETIME)]
RegEnumKeyExW.restype = LSTATUS
RegEnumKeyExW.errcheck = error_success

RegEnumValueA = advapi32.RegEnumValueA
RegEnumValueA.argtypes = [HKEY, DWORD, LPSTR, LPDWORD, LPDWORD, LPDWORD, LPBYTE, LPDWORD]
RegEnumValueA.restype = LSTATUS
RegEnumValueA.errcheck = error_success

RegEnumValueW = advapi32.RegEnumValueW
RegEnumValueW.argtypes = [HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPDWORD, LPBYTE, LPDWORD]
RegEnumValueW.restype = LSTATUS
RegEnumValueW.errcheck = error_success

RegFlushKey = advapi32.RegFlushKey
RegFlushKey.argtypes = [HKEY]
RegFlushKey.restype = LSTATUS
RegFlushKey.errcheck = error_success

RegGetKeySecurity = advapi32.RegGetKeySecurity
RegGetKeySecurity.argtypes = [HKEY, SECURITY_INFORMATION, PSECURITY_DESCRIPTOR, LPDWORD]
RegGetKeySecurity.restype = LSTATUS
RegGetKeySecurity.errcheck = error_success

RegLoadKeyA = advapi32.RegLoadKeyA
RegLoadKeyA.argtypes = [HKEY, LPCSTR, LPCSTR]
RegLoadKeyA.restype = LSTATUS
RegLoadKeyA.errcheck = error_success

RegLoadKeyW = advapi32.RegLoadKeyW
RegLoadKeyW.argtypes = [HKEY, LPCWSTR, LPCWSTR]
RegLoadKeyW.restype = LSTATUS
RegLoadKeyW.errcheck = error_success

RegNotifyChangeKeyValue = advapi32.RegNotifyChangeKeyValue
RegNotifyChangeKeyValue.argtypes = [HKEY, BOOL, DWORD, HANDLE, BOOL]
RegNotifyChangeKeyValue.restype = LSTATUS
RegNotifyChangeKeyValue.errcheck = error_success

RegOpenKeyA = advapi32.RegOpenKeyA
RegOpenKeyA.argtypes = [HKEY, LPCSTR, PHKEY]
RegOpenKeyA.restype = LSTATUS
RegOpenKeyA.errcheck = error_success

RegOpenKeyW = advapi32.RegOpenKeyW
RegOpenKeyW.argtypes = [HKEY, LPCWSTR, PHKEY]
RegOpenKeyW.restype = LSTATUS
RegOpenKeyW.errcheck = error_success

RegOpenKeyExA = advapi32.RegOpenKeyExA
RegOpenKeyExA.argtypes = [HKEY, LPCSTR, DWORD, REGSAM, PHKEY]
RegOpenKeyExA.restype = LSTATUS
RegOpenKeyExA.errcheck = error_success

RegOpenKeyExW = advapi32.RegOpenKeyExW
RegOpenKeyExW.argtypes = [HKEY, LPCWSTR, DWORD, REGSAM, PHKEY]
RegOpenKeyExW.restype = LSTATUS
RegOpenKeyExW.errcheck = error_success

RegOpenKeyTransactedA = advapi32.RegOpenKeyTransactedA
RegOpenKeyTransactedA.argtypes = [HKEY, LPCSTR, DWORD, REGSAM, PHKEY, HANDLE, PVOID]
RegOpenKeyTransactedA.restype = LSTATUS
RegOpenKeyTransactedA.errcheck = error_success

RegOpenKeyTransactedW = advapi32.RegOpenKeyTransactedW
RegOpenKeyTransactedW.argtypes = [HKEY, LPCWSTR, DWORD, REGSAM, PHKEY, HANDLE, PVOID]
RegOpenKeyTransactedW.restype = LSTATUS
RegOpenKeyTransactedW.errcheck = error_success

RegQueryInfoKeyA = advapi32.RegQueryInfoKeyA
RegQueryInfoKeyA.argtypes = [
    HKEY,
    LPSTR,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    POINTER(FILETIME),
]
RegQueryInfoKeyA.restype = LSTATUS
RegQueryInfoKeyA.errcheck = error_success

RegQueryInfoKeyW = advapi32.RegQueryInfoKeyW
RegQueryInfoKeyW.argtypes = [
    HKEY,
    LPWSTR,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    LPDWORD,
    POINTER(FILETIME),
]
RegQueryInfoKeyW.restype = LSTATUS
RegQueryInfoKeyW.errcheck = error_success

RegQueryValueA = advapi32.RegQueryValueA
RegQueryValueA.argtypes = [HKEY, LPCSTR, LPSTR, PLONG]
RegQueryValueA.restype = LSTATUS
RegQueryValueA.errcheck = error_success

RegQueryValueW = advapi32.RegQueryValueW
RegQueryValueW.argtypes = [HKEY, LPCWSTR, LPWSTR, PLONG]
RegQueryValueW.restype = LSTATUS
RegQueryValueW.errcheck = error_success

RegQueryMultipleValuesA = advapi32.RegQueryMultipleValuesA
RegQueryMultipleValuesA.argtypes = [HKEY, PVALENTA, DWORD, LPSTR, LPDWORD]
RegQueryMultipleValuesA.restype = LSTATUS
RegQueryMultipleValuesA.errcheck = error_success

RegQueryMultipleValuesW = advapi32.RegQueryMultipleValuesW
RegQueryMultipleValuesW.argtypes = [HKEY, PVALENTW, DWORD, LPWSTR, LPDWORD]
RegQueryMultipleValuesW.restype = LSTATUS
RegQueryMultipleValuesW.errcheck = error_success

RegQueryValueExA = advapi32.RegQueryValueExA
RegQueryValueExA.argtypes = [HKEY, LPCSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD]
RegQueryValueExA.restype = LSTATUS
RegQueryValueExA.errcheck = error_success

RegQueryValueExW = advapi32.RegQueryValueExW
RegQueryValueExW.argtypes = [HKEY, LPCWSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD]
RegQueryValueExW.restype = LSTATUS
RegQueryValueExW.errcheck = error_success

RegReplaceKeyA = advapi32.RegReplaceKeyA
RegReplaceKeyA.argtypes = [HKEY, LPCSTR, LPCSTR, LPCSTR]
RegReplaceKeyA.restype = LSTATUS
RegReplaceKeyA.errcheck = error_success

RegReplaceKeyW = advapi32.RegReplaceKeyW
RegReplaceKeyW.argtypes = [HKEY, LPCWSTR, LPCWSTR, LPCWSTR]
RegReplaceKeyW.restype = LSTATUS
RegReplaceKeyW.errcheck = error_success

RegRestoreKeyA = advapi32.RegRestoreKeyA
RegRestoreKeyA.argtypes = [HKEY, LPCSTR, DWORD]
RegRestoreKeyA.restype = LSTATUS
RegRestoreKeyA.errcheck = error_success

RegRestoreKeyW = advapi32.RegRestoreKeyW
RegRestoreKeyW.argtypes = [HKEY, LPCWSTR, DWORD]
RegRestoreKeyW.restype = LSTATUS
RegRestoreKeyW.errcheck = error_success

RegRenameKey = advapi32.RegRenameKey
RegRenameKey.argtypes = [HKEY, LPCWSTR, LPCWSTR]
RegRenameKey.restype = LSTATUS
RegRenameKey.errcheck = error_success

RegSaveKeyA = advapi32.RegSaveKeyA
RegSaveKeyA.argtypes = [HKEY, LPCSTR, LPSECURITY_ATTRIBUTES]
RegSaveKeyA.restype = LSTATUS
RegSaveKeyA.errcheck = error_success

RegSaveKeyW = advapi32.RegSaveKeyW
RegSaveKeyW.argtypes = [HKEY, LPCWSTR, LPSECURITY_ATTRIBUTES]
RegSaveKeyW.restype = LSTATUS
RegSaveKeyW.errcheck = error_success

RegSetKeySecurity = advapi32.RegSetKeySecurity
RegSetKeySecurity.argtypes = [HKEY, SECURITY_INFORMATION, PSECURITY_DESCRIPTOR]
RegSetKeySecurity.restype = LSTATUS
RegSetKeySecurity.errcheck = error_success

RegSetValueA = advapi32.RegSetValueA
RegSetValueA.argtypes = [HKEY, LPCSTR, DWORD, LPCSTR, DWORD]
RegSetValueA.restype = LSTATUS
RegSetValueA.errcheck = error_success

RegSetValueW = advapi32.RegSetValueW
RegSetValueW.argtypes = [HKEY, LPCWSTR, DWORD, LPCWSTR, DWORD]
RegSetValueW.restype = LSTATUS
RegSetValueW.errcheck = error_success

RegSetValueExA = advapi32.RegSetValueExA
RegSetValueExA.argtypes = [HKEY, LPCSTR, DWORD, DWORD, POINTER(BYTE), DWORD]
RegSetValueExA.restype = LSTATUS
RegSetValueExA.errcheck = error_success

RegSetValueExW = advapi32.RegSetValueExW
RegSetValueExW.argtypes = [HKEY, LPCWSTR, DWORD, DWORD, POINTER(BYTE), DWORD]
RegSetValueExW.restype = LSTATUS
RegSetValueExW.errcheck = error_success

RegUnLoadKeyA = advapi32.RegUnLoadKeyA
RegUnLoadKeyA.argtypes = [HKEY, LPCSTR]
RegUnLoadKeyA.restype = LSTATUS
RegUnLoadKeyA.errcheck = error_success

RegUnLoadKeyW = advapi32.RegUnLoadKeyW
RegUnLoadKeyW.argtypes = [HKEY, LPCWSTR]
RegUnLoadKeyW.restype = LSTATUS
RegUnLoadKeyW.errcheck = error_success

RegDeleteKeyValueA = advapi32.RegDeleteKeyValueA
RegDeleteKeyValueA.argtypes = [HKEY, LPCSTR, LPCSTR]
RegDeleteKeyValueA.restype = LSTATUS
RegDeleteKeyValueA.errcheck = error_success

RegDeleteKeyValueW = advapi32.RegDeleteKeyValueW
RegDeleteKeyValueW.argtypes = [HKEY, LPCWSTR, LPCWSTR]
RegDeleteKeyValueW.restype = LSTATUS
RegDeleteKeyValueW.errcheck = error_success

RegSetKeyValueA = advapi32.RegSetKeyValueA
RegSetKeyValueA.argtypes = [HKEY, LPCSTR, LPCSTR, DWORD, LPCVOID, DWORD]
RegSetKeyValueA.restype = LSTATUS
RegSetKeyValueA.errcheck = error_success

RegSetKeyValueW = advapi32.RegSetKeyValueW
RegSetKeyValueW.argtypes = [HKEY, LPCWSTR, LPCWSTR, DWORD, LPCVOID, DWORD]
RegSetKeyValueW.restype = LSTATUS
RegSetKeyValueW.errcheck = error_success

RegDeleteTreeA = advapi32.RegDeleteTreeA
RegDeleteTreeA.argtypes = [HKEY, LPCSTR]
RegDeleteTreeA.restype = LSTATUS
RegDeleteTreeA.errcheck = error_success

RegDeleteTreeW = advapi32.RegDeleteTreeW
RegDeleteTreeW.argtypes = [HKEY, LPCWSTR]
RegDeleteTreeW.restype = LSTATUS
RegDeleteTreeW.errcheck = error_success

RegCopyTreeA = advapi32.RegCopyTreeA
RegCopyTreeA.argtypes = [HKEY, LPCSTR, HKEY]
RegCopyTreeA.restype = LSTATUS
RegCopyTreeA.errcheck = error_success

RegCopyTreeW = advapi32.RegCopyTreeW
RegCopyTreeW.argtypes = [HKEY, LPCWSTR, HKEY]
RegCopyTreeW.restype = LSTATUS
RegCopyTreeW.errcheck = error_success

RegGetValueA = advapi32.RegGetValueA
RegGetValueA.argtypes = [HKEY, LPCSTR, LPCSTR, DWORD, LPDWORD, PVOID, LPDWORD]
RegGetValueA.restype = LSTATUS
RegGetValueA.errcheck = error_success

RegGetValueW = advapi32.RegGetValueW
RegGetValueW.argtypes = [HKEY, LPCWSTR, LPCWSTR, DWORD, LPDWORD, PVOID, LPDWORD]
RegGetValueW.restype = LSTATUS
RegGetValueW.errcheck = error_success

RegLoadMUIStringA = advapi32.RegLoadMUIStringA
RegLoadMUIStringA.argtypes = [HKEY, LPCSTR, LPSTR, DWORD, LPDWORD, DWORD, LPCSTR]
RegLoadMUIStringA.restype = LSTATUS
RegLoadMUIStringA.errcheck = error_success

RegLoadMUIStringW = advapi32.RegLoadMUIStringW
RegLoadMUIStringW.argtypes = [HKEY, LPCWSTR, LPWSTR, DWORD, LPDWORD, DWORD, LPCWSTR]
RegLoadMUIStringW.restype = LSTATUS
RegLoadMUIStringW.errcheck = error_success

RegLoadAppKeyA = advapi32.RegLoadAppKeyA
RegLoadAppKeyA.argtypes = [LPCSTR, PHKEY, REGSAM, DWORD, DWORD]
RegLoadAppKeyA.restype = LSTATUS
RegLoadAppKeyA.errcheck = error_success

RegLoadAppKeyW = advapi32.RegLoadAppKeyW
RegLoadAppKeyW.argtypes = [LPCWSTR, PHKEY, REGSAM, DWORD, DWORD]
RegLoadAppKeyW.restype = LSTATUS
RegLoadAppKeyW.errcheck = error_success

InitiateSystemShutdownA = advapi32.InitiateSystemShutdownA
InitiateSystemShutdownA.argtypes = [LPSTR, LPSTR, DWORD, BOOL, BOOL]
InitiateSystemShutdownA.restype = BOOL
InitiateSystemShutdownA.errcheck = nonfalse

InitiateSystemShutdownW = advapi32.InitiateSystemShutdownW
InitiateSystemShutdownW.argtypes = [LPWSTR, LPWSTR, DWORD, BOOL, BOOL]
InitiateSystemShutdownW.restype = BOOL
InitiateSystemShutdownW.errcheck = nonfalse

AbortSystemShutdownA = advapi32.AbortSystemShutdownA
AbortSystemShutdownA.argtypes = [LPSTR]
AbortSystemShutdownA.restype = BOOL
AbortSystemShutdownA.errcheck = nonfalse

AbortSystemShutdownW = advapi32.AbortSystemShutdownW
AbortSystemShutdownW.argtypes = [LPWSTR]
AbortSystemShutdownW.restype = BOOL
AbortSystemShutdownW.errcheck = nonfalse

InitiateSystemShutdownExA = advapi32.InitiateSystemShutdownExA
InitiateSystemShutdownExA.argtypes = [LPSTR, LPSTR, DWORD, BOOL, BOOL, DWORD]
InitiateSystemShutdownExA.restype = BOOL
InitiateSystemShutdownExA.errcheck = nonfalse

InitiateSystemShutdownExW = advapi32.InitiateSystemShutdownExW
InitiateSystemShutdownExW.argtypes = [LPWSTR, LPWSTR, DWORD, BOOL, BOOL, DWORD]
InitiateSystemShutdownExW.restype = BOOL
InitiateSystemShutdownExW.errcheck = nonfalse

InitiateShutdownA = advapi32.InitiateShutdownA
InitiateShutdownA.argtypes = [LPSTR, LPSTR, DWORD, DWORD, DWORD]
InitiateShutdownA.restype = DWORD
InitiateShutdownA.errcheck = error_success

InitiateShutdownW = advapi32.InitiateShutdownW
InitiateShutdownW.argtypes = [LPWSTR, LPWSTR, DWORD, DWORD, DWORD]
InitiateShutdownW.restype = DWORD
InitiateShutdownW.errcheck = error_success

CheckForHiberboot = advapi32.CheckForHiberboot
CheckForHiberboot.argtypes = [PBOOLEAN, BOOLEAN]
CheckForHiberboot.restype = DWORD

RegSaveKeyExA = advapi32.RegSaveKeyExA
RegSaveKeyExA.argtypes = [HKEY, LPCSTR, LPSECURITY_ATTRIBUTES, DWORD]
RegSaveKeyExA.restype = LSTATUS
RegSaveKeyExA.errcheck = error_success

RegSaveKeyExW = advapi32.RegSaveKeyExW
RegSaveKeyExW.argtypes = [HKEY, LPCWSTR, LPSECURITY_ATTRIBUTES, DWORD]
RegSaveKeyExW.restype = LSTATUS
RegSaveKeyExW.errcheck = error_success
