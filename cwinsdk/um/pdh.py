"""ctypes bindings for the Windows Performance Data Helper (PDH) API."""

from ctypes import POINTER, Structure, Union, WINFUNCTYPE, c_double, c_longlong, c_ubyte
from ctypes.wintypes import BOOL, BOOLEAN, DWORD, HANDLE, HWND, INT, LONG, LPCSTR, LPCWSTR, LPSTR, LPWSTR

from .. import error_success, windll
from ..shared.basetsd import DWORD_PTR
from ..shared.guiddef import GUID
from ..shared.minwindef import FILETIME
from .winperf import PERF_DETAIL_ADVANCED, PERF_DETAIL_EXPERT, PERF_DETAIL_NOVICE, PERF_DETAIL_WIZARD

PDH_STATUS = LONG
PDH_HCOUNTER = HANDLE
PDH_HQUERY = HANDLE
PDH_HLOG = HANDLE
HCOUNTER = PDH_HCOUNTER
HQUERY = PDH_HQUERY
HLOG = PDH_HLOG
LONGLONG = c_longlong
PZZSTR = LPSTR
PZZWSTR = LPWSTR

PDH_CVERSION_WIN40 = 0x0400
PDH_CVERSION_WIN50 = 0x0500
PDH_VERSION = PDH_CVERSION_WIN50 + 0x0003
MAX_COUNTER_PATH = 256
PDH_MAX_COUNTER_NAME = 1024
PDH_MAX_INSTANCE_NAME = 1024
PDH_MAX_COUNTER_PATH = 2048
PDH_MAX_DATASOURCE_PATH = 1024
PDH_OBJECT_HAS_INSTANCES = 0x00000001
H_REALTIME_DATASOURCE = None
H_WBEM_DATASOURCE = HANDLE(-1).value
MAX_TIME_VALUE = 0x7FFFFFFFFFFFFFFF
MIN_TIME_VALUE = 0

PDH_FMT_RAW = 0x00000010
PDH_FMT_ANSI = 0x00000020
PDH_FMT_UNICODE = 0x00000040
PDH_FMT_LONG = 0x00000100
PDH_FMT_DOUBLE = 0x00000200
PDH_FMT_LARGE = 0x00000400
PDH_FMT_NOSCALE = 0x00001000
PDH_FMT_1000 = 0x00002000
PDH_FMT_NODATA = 0x00004000
PDH_FMT_NOCAP100 = 0x00008000
PERF_DETAIL_COSTLY = 0x00010000
PERF_DETAIL_STANDARD = 0x0000FFFF
PDH_MAX_SCALE = 7
PDH_MIN_SCALE = -7
PDH_PATH_WBEM_RESULT = 0x00000001
PDH_PATH_WBEM_INPUT = 0x00000002
PDH_NOEXPANDCOUNTERS = 1
PDH_NOEXPANDINSTANCES = 2
PDH_REFRESHCOUNTERS = 4
PDH_LOG_READ_ACCESS = 0x00010000
PDH_LOG_WRITE_ACCESS = 0x00020000
PDH_LOG_UPDATE_ACCESS = 0x00040000
PDH_LOG_ACCESS_MASK = 0x000F0000
PDH_LOG_CREATE_NEW = 0x00000001
PDH_LOG_CREATE_ALWAYS = 0x00000002
PDH_LOG_OPEN_ALWAYS = 0x00000003
PDH_LOG_OPEN_EXISTING = 0x00000004
PDH_LOG_CREATE_MASK = 0x0000000F
PDH_LOG_OPT_USER_STRING = 0x01000000
PDH_LOG_OPT_CIRCULAR = 0x02000000
PDH_LOG_OPT_MAX_IS_BYTES = 0x04000000
PDH_LOG_OPT_APPEND = 0x08000000
PDH_LOG_OPT_MASK = 0x0F000000
PDH_LOG_TYPE_UNDEFINED = 0
PDH_LOG_TYPE_CSV = 1
PDH_LOG_TYPE_TSV = 2
PDH_LOG_TYPE_RETIRED_BIN = 3
PDH_LOG_TYPE_TRACE_KERNEL = 4
PDH_LOG_TYPE_TRACE_GENERIC = 5
PDH_LOG_TYPE_PERFMON = 6
PDH_LOG_TYPE_SQL = 7
PDH_LOG_TYPE_BINARY = 8
PDH_FLAGS_CLOSE_QUERY = 0x00000001
PDH_FLAGS_FILE_BROWSER_ONLY = 0x00000001
DATA_SOURCE_REGISTRY = 0x00000001
DATA_SOURCE_LOGFILE = 0x00000002
DATA_SOURCE_WBEM = 0x00000004


def PDH_PATH_LANG_FLAGS(lang_id, flags):
    return ((lang_id & 0xFFFF) << 16) | (flags & 0xFFFF)


def IsSuccessSeverity(error_code):
    return (error_code & 0xC0000000) == 0


def IsInformationalSeverity(error_code):
    return (error_code & 0xC0000000) == 0x40000000


def IsWarningSeverity(error_code):
    return (error_code & 0xC0000000) == 0x80000000


def IsErrorSeverity(error_code):
    return (error_code & 0xC0000000) == 0xC0000000


class PDH_RAW_COUNTER(Structure):
    _fields_ = [
        ("CStatus", DWORD),
        ("TimeStamp", FILETIME),
        ("FirstValue", LONGLONG),
        ("SecondValue", LONGLONG),
        ("MultiCount", DWORD),
    ]


PPDH_RAW_COUNTER = POINTER(PDH_RAW_COUNTER)


class PDH_RAW_COUNTER_ITEM_A(Structure):
    _fields_ = [("szName", LPSTR), ("RawValue", PDH_RAW_COUNTER)]


class PDH_RAW_COUNTER_ITEM_W(Structure):
    _fields_ = [("szName", LPWSTR), ("RawValue", PDH_RAW_COUNTER)]


PPDH_RAW_COUNTER_ITEM_A = POINTER(PDH_RAW_COUNTER_ITEM_A)
PPDH_RAW_COUNTER_ITEM_W = POINTER(PDH_RAW_COUNTER_ITEM_W)


class _PDH_FMT_COUNTERVALUE_UNION(Union):
    _fields_ = [
        ("longValue", LONG),
        ("doubleValue", c_double),
        ("largeValue", LONGLONG),
        ("AnsiStringValue", LPCSTR),
        ("WideStringValue", LPCWSTR),
    ]


class PDH_FMT_COUNTERVALUE(Structure):
    _anonymous_ = ("Value",)
    _fields_ = [("CStatus", DWORD), ("Value", _PDH_FMT_COUNTERVALUE_UNION)]


PPDH_FMT_COUNTERVALUE = POINTER(PDH_FMT_COUNTERVALUE)


class PDH_FMT_COUNTERVALUE_ITEM_A(Structure):
    _fields_ = [("szName", LPSTR), ("FmtValue", PDH_FMT_COUNTERVALUE)]


class PDH_FMT_COUNTERVALUE_ITEM_W(Structure):
    _fields_ = [("szName", LPWSTR), ("FmtValue", PDH_FMT_COUNTERVALUE)]


PPDH_FMT_COUNTERVALUE_ITEM_A = POINTER(PDH_FMT_COUNTERVALUE_ITEM_A)
PPDH_FMT_COUNTERVALUE_ITEM_W = POINTER(PDH_FMT_COUNTERVALUE_ITEM_W)


class PDH_STATISTICS(Structure):
    _fields_ = [
        ("dwFormat", DWORD),
        ("count", DWORD),
        ("min", PDH_FMT_COUNTERVALUE),
        ("max", PDH_FMT_COUNTERVALUE),
        ("mean", PDH_FMT_COUNTERVALUE),
    ]


PPDH_STATISTICS = POINTER(PDH_STATISTICS)


class PDH_COUNTER_PATH_ELEMENTS_A(Structure):
    _fields_ = [
        ("szMachineName", LPSTR),
        ("szObjectName", LPSTR),
        ("szInstanceName", LPSTR),
        ("szParentInstance", LPSTR),
        ("dwInstanceIndex", DWORD),
        ("szCounterName", LPSTR),
    ]


class PDH_COUNTER_PATH_ELEMENTS_W(Structure):
    _fields_ = [
        ("szMachineName", LPWSTR),
        ("szObjectName", LPWSTR),
        ("szInstanceName", LPWSTR),
        ("szParentInstance", LPWSTR),
        ("dwInstanceIndex", DWORD),
        ("szCounterName", LPWSTR),
    ]


PPDH_COUNTER_PATH_ELEMENTS_A = POINTER(PDH_COUNTER_PATH_ELEMENTS_A)
PPDH_COUNTER_PATH_ELEMENTS_W = POINTER(PDH_COUNTER_PATH_ELEMENTS_W)


class PDH_DATA_ITEM_PATH_ELEMENTS_A(Structure):
    _fields_ = [("szMachineName", LPSTR), ("ObjectGUID", GUID), ("dwItemId", DWORD), ("szInstanceName", LPSTR)]


class PDH_DATA_ITEM_PATH_ELEMENTS_W(Structure):
    _fields_ = [("szMachineName", LPWSTR), ("ObjectGUID", GUID), ("dwItemId", DWORD), ("szInstanceName", LPWSTR)]


PPDH_DATA_ITEM_PATH_ELEMENTS_A = POINTER(PDH_DATA_ITEM_PATH_ELEMENTS_A)
PPDH_DATA_ITEM_PATH_ELEMENTS_W = POINTER(PDH_DATA_ITEM_PATH_ELEMENTS_W)


class _PDH_COUNTER_INFO_PATH_A(Union):
    _anonymous_ = ("CounterPathElements",)
    _fields_ = [
        ("DataItemPath", PDH_DATA_ITEM_PATH_ELEMENTS_A),
        ("CounterPath", PDH_COUNTER_PATH_ELEMENTS_A),
        ("CounterPathElements", PDH_COUNTER_PATH_ELEMENTS_A),
    ]


class _PDH_COUNTER_INFO_PATH_W(Union):
    _anonymous_ = ("CounterPathElements",)
    _fields_ = [
        ("DataItemPath", PDH_DATA_ITEM_PATH_ELEMENTS_W),
        ("CounterPath", PDH_COUNTER_PATH_ELEMENTS_W),
        ("CounterPathElements", PDH_COUNTER_PATH_ELEMENTS_W),
    ]


class PDH_COUNTER_INFO_A(Structure):
    _anonymous_ = ("Path",)
    _fields_ = [
        ("dwLength", DWORD),
        ("dwType", DWORD),
        ("CVersion", DWORD),
        ("CStatus", DWORD),
        ("lScale", LONG),
        ("lDefaultScale", LONG),
        ("dwUserData", DWORD_PTR),
        ("dwQueryUserData", DWORD_PTR),
        ("szFullPath", LPSTR),
        ("Path", _PDH_COUNTER_INFO_PATH_A),
        ("szExplainText", LPSTR),
        ("DataBuffer", DWORD * 1),
    ]


class PDH_COUNTER_INFO_W(Structure):
    _anonymous_ = ("Path",)
    _fields_ = [
        ("dwLength", DWORD),
        ("dwType", DWORD),
        ("CVersion", DWORD),
        ("CStatus", DWORD),
        ("lScale", LONG),
        ("lDefaultScale", LONG),
        ("dwUserData", DWORD_PTR),
        ("dwQueryUserData", DWORD_PTR),
        ("szFullPath", LPWSTR),
        ("Path", _PDH_COUNTER_INFO_PATH_W),
        ("szExplainText", LPWSTR),
        ("DataBuffer", DWORD * 1),
    ]


PPDH_COUNTER_INFO_A = POINTER(PDH_COUNTER_INFO_A)
PPDH_COUNTER_INFO_W = POINTER(PDH_COUNTER_INFO_W)


class PDH_TIME_INFO(Structure):
    _fields_ = [("StartTime", LONGLONG), ("EndTime", LONGLONG), ("SampleCount", DWORD)]


PPDH_TIME_INFO = POINTER(PDH_TIME_INFO)


class PDH_RAW_LOG_RECORD(Structure):
    _fields_ = [("dwStructureSize", DWORD), ("dwRecordType", DWORD), ("dwItems", DWORD), ("RawBytes", c_ubyte * 1)]


PPDH_RAW_LOG_RECORD = POINTER(PDH_RAW_LOG_RECORD)


class _PDH_LOG_SERVICE_PDL_A(Structure):
    _fields_ = [
        ("PdlAutoNameInterval", DWORD),
        ("PdlAutoNameUnits", DWORD),
        ("PdlCommandFilename", LPSTR),
        ("PdlCounterList", LPSTR),
        ("PdlAutoNameFormat", DWORD),
        ("PdlSampleInterval", DWORD),
        ("PdlLogStartTime", FILETIME),
        ("PdlLogEndTime", FILETIME),
    ]


class _PDH_LOG_SERVICE_TRACE_A(Structure):
    _fields_ = [
        ("TlNumberOfBuffers", DWORD),
        ("TlMinimumBuffers", DWORD),
        ("TlMaximumBuffers", DWORD),
        ("TlFreeBuffers", DWORD),
        ("TlBufferSize", DWORD),
        ("TlEventsLost", DWORD),
        ("TlLoggerThreadId", DWORD),
        ("TlBuffersWritten", DWORD),
        ("TlLogHandle", DWORD),
        ("TlLogFileName", LPSTR),
    ]


class _PDH_LOG_SERVICE_PDL_W(Structure):
    _fields_ = [
        ("PdlAutoNameInterval", DWORD),
        ("PdlAutoNameUnits", DWORD),
        ("PdlCommandFilename", LPWSTR),
        ("PdlCounterList", LPWSTR),
        ("PdlAutoNameFormat", DWORD),
        ("PdlSampleInterval", DWORD),
        ("PdlLogStartTime", FILETIME),
        ("PdlLogEndTime", FILETIME),
    ]


class _PDH_LOG_SERVICE_TRACE_W(Structure):
    _fields_ = [
        ("TlNumberOfBuffers", DWORD),
        ("TlMinimumBuffers", DWORD),
        ("TlMaximumBuffers", DWORD),
        ("TlFreeBuffers", DWORD),
        ("TlBufferSize", DWORD),
        ("TlEventsLost", DWORD),
        ("TlLoggerThreadId", DWORD),
        ("TlBuffersWritten", DWORD),
        ("TlLogHandle", DWORD),
        ("TlLogFileName", LPWSTR),
    ]


class _PDH_LOG_SERVICE_UNION_A(Union):
    _anonymous_ = ("Pdl", "Trace")
    _fields_ = [("Pdl", _PDH_LOG_SERVICE_PDL_A), ("Trace", _PDH_LOG_SERVICE_TRACE_A)]


class _PDH_LOG_SERVICE_UNION_W(Union):
    _anonymous_ = ("Pdl", "Trace")
    _fields_ = [("Pdl", _PDH_LOG_SERVICE_PDL_W), ("Trace", _PDH_LOG_SERVICE_TRACE_W)]


class PDH_LOG_SERVICE_QUERY_INFO_A(Structure):
    _anonymous_ = ("Details",)
    _fields_ = [
        ("dwSize", DWORD),
        ("dwFlags", DWORD),
        ("dwLogQuota", DWORD),
        ("szLogFileCaption", LPSTR),
        ("szDefaultDir", LPSTR),
        ("szBaseFileName", LPSTR),
        ("dwFileType", DWORD),
        ("dwReserved", DWORD),
        ("Details", _PDH_LOG_SERVICE_UNION_A),
    ]


class PDH_LOG_SERVICE_QUERY_INFO_W(Structure):
    _anonymous_ = ("Details",)
    _fields_ = [
        ("dwSize", DWORD),
        ("dwFlags", DWORD),
        ("dwLogQuota", DWORD),
        ("szLogFileCaption", LPWSTR),
        ("szDefaultDir", LPWSTR),
        ("szBaseFileName", LPWSTR),
        ("dwFileType", DWORD),
        ("dwReserved", DWORD),
        ("Details", _PDH_LOG_SERVICE_UNION_W),
    ]


PPDH_LOG_SERVICE_QUERY_INFO_A = POINTER(PDH_LOG_SERVICE_QUERY_INFO_A)
PPDH_LOG_SERVICE_QUERY_INFO_W = POINTER(PDH_LOG_SERVICE_QUERY_INFO_W)

CounterPathCallBack = WINFUNCTYPE(PDH_STATUS, DWORD_PTR)


class PDH_BROWSE_DLG_CONFIG_HW(Structure):
    _fields_ = [
        ("bIncludeInstanceIndex", DWORD, 1),
        ("bSingleCounterPerAdd", DWORD, 1),
        ("bSingleCounterPerDialog", DWORD, 1),
        ("bLocalCountersOnly", DWORD, 1),
        ("bWildCardInstances", DWORD, 1),
        ("bHideDetailBox", DWORD, 1),
        ("bInitializePath", DWORD, 1),
        ("bDisableMachineSelection", DWORD, 1),
        ("bIncludeCostlyObjects", DWORD, 1),
        ("bShowObjectBrowser", DWORD, 1),
        ("bReserved", DWORD, 22),
        ("hWndOwner", HWND),
        ("hDataSource", PDH_HLOG),
        ("szReturnPathBuffer", LPWSTR),
        ("cchReturnPathLength", DWORD),
        ("pCallBack", CounterPathCallBack),
        ("dwCallBackArg", DWORD_PTR),
        ("CallBackStatus", PDH_STATUS),
        ("dwDefaultDetailLevel", DWORD),
        ("szDialogBoxCaption", LPWSTR),
    ]


class PDH_BROWSE_DLG_CONFIG_HA(Structure):
    _fields_ = [
        ("bIncludeInstanceIndex", DWORD, 1),
        ("bSingleCounterPerAdd", DWORD, 1),
        ("bSingleCounterPerDialog", DWORD, 1),
        ("bLocalCountersOnly", DWORD, 1),
        ("bWildCardInstances", DWORD, 1),
        ("bHideDetailBox", DWORD, 1),
        ("bInitializePath", DWORD, 1),
        ("bDisableMachineSelection", DWORD, 1),
        ("bIncludeCostlyObjects", DWORD, 1),
        ("bShowObjectBrowser", DWORD, 1),
        ("bReserved", DWORD, 22),
        ("hWndOwner", HWND),
        ("hDataSource", PDH_HLOG),
        ("szReturnPathBuffer", LPSTR),
        ("cchReturnPathLength", DWORD),
        ("pCallBack", CounterPathCallBack),
        ("dwCallBackArg", DWORD_PTR),
        ("CallBackStatus", PDH_STATUS),
        ("dwDefaultDetailLevel", DWORD),
        ("szDialogBoxCaption", LPSTR),
    ]


class PDH_BROWSE_DLG_CONFIG_W(Structure):
    _fields_ = [
        ("bIncludeInstanceIndex", DWORD, 1),
        ("bSingleCounterPerAdd", DWORD, 1),
        ("bSingleCounterPerDialog", DWORD, 1),
        ("bLocalCountersOnly", DWORD, 1),
        ("bWildCardInstances", DWORD, 1),
        ("bHideDetailBox", DWORD, 1),
        ("bInitializePath", DWORD, 1),
        ("bDisableMachineSelection", DWORD, 1),
        ("bIncludeCostlyObjects", DWORD, 1),
        ("bShowObjectBrowser", DWORD, 1),
        ("bReserved", DWORD, 22),
        ("hWndOwner", HWND),
        ("szDataSource", LPWSTR),
        ("szReturnPathBuffer", LPWSTR),
        ("cchReturnPathLength", DWORD),
        ("pCallBack", CounterPathCallBack),
        ("dwCallBackArg", DWORD_PTR),
        ("CallBackStatus", PDH_STATUS),
        ("dwDefaultDetailLevel", DWORD),
        ("szDialogBoxCaption", LPWSTR),
    ]


class PDH_BROWSE_DLG_CONFIG_A(Structure):
    _fields_ = [
        ("bIncludeInstanceIndex", DWORD, 1),
        ("bSingleCounterPerAdd", DWORD, 1),
        ("bSingleCounterPerDialog", DWORD, 1),
        ("bLocalCountersOnly", DWORD, 1),
        ("bWildCardInstances", DWORD, 1),
        ("bHideDetailBox", DWORD, 1),
        ("bInitializePath", DWORD, 1),
        ("bDisableMachineSelection", DWORD, 1),
        ("bIncludeCostlyObjects", DWORD, 1),
        ("bReserved", DWORD, 23),
        ("hWndOwner", HWND),
        ("szDataSource", LPSTR),
        ("szReturnPathBuffer", LPSTR),
        ("cchReturnPathLength", DWORD),
        ("pCallBack", CounterPathCallBack),
        ("dwCallBackArg", DWORD_PTR),
        ("CallBackStatus", PDH_STATUS),
        ("dwDefaultDetailLevel", DWORD),
        ("szDialogBoxCaption", LPSTR),
    ]


PPDH_BROWSE_DLG_CONFIG_HW = POINTER(PDH_BROWSE_DLG_CONFIG_HW)
PPDH_BROWSE_DLG_CONFIG_HA = POINTER(PDH_BROWSE_DLG_CONFIG_HA)
PPDH_BROWSE_DLG_CONFIG_W = POINTER(PDH_BROWSE_DLG_CONFIG_W)
PPDH_BROWSE_DLG_CONFIG_A = POINTER(PDH_BROWSE_DLG_CONFIG_A)


PdhGetDllVersion = windll.pdh.PdhGetDllVersion
PdhGetDllVersion.argtypes = [POINTER(DWORD)]
PdhGetDllVersion.restype = PDH_STATUS
PdhGetDllVersion.errcheck = error_success

PdhOpenQueryW = windll.pdh.PdhOpenQueryW
PdhOpenQueryW.argtypes = [LPCWSTR, DWORD_PTR, POINTER(PDH_HQUERY)]
PdhOpenQueryW.restype = PDH_STATUS
PdhOpenQueryW.errcheck = error_success

PdhOpenQueryA = windll.pdh.PdhOpenQueryA
PdhOpenQueryA.argtypes = [LPCSTR, DWORD_PTR, POINTER(PDH_HQUERY)]
PdhOpenQueryA.restype = PDH_STATUS
PdhOpenQueryA.errcheck = error_success

PdhAddCounterW = windll.pdh.PdhAddCounterW
PdhAddCounterW.argtypes = [PDH_HQUERY, LPCWSTR, DWORD_PTR, POINTER(PDH_HCOUNTER)]
PdhAddCounterW.restype = PDH_STATUS
PdhAddCounterW.errcheck = error_success

PdhAddCounterA = windll.pdh.PdhAddCounterA
PdhAddCounterA.argtypes = [PDH_HQUERY, LPCSTR, DWORD_PTR, POINTER(PDH_HCOUNTER)]
PdhAddCounterA.restype = PDH_STATUS
PdhAddCounterA.errcheck = error_success

PdhAddEnglishCounterW = windll.pdh.PdhAddEnglishCounterW
PdhAddEnglishCounterW.argtypes = [PDH_HQUERY, LPCWSTR, DWORD_PTR, POINTER(PDH_HCOUNTER)]
PdhAddEnglishCounterW.restype = PDH_STATUS
PdhAddEnglishCounterW.errcheck = error_success

PdhAddEnglishCounterA = windll.pdh.PdhAddEnglishCounterA
PdhAddEnglishCounterA.argtypes = [PDH_HQUERY, LPCSTR, DWORD_PTR, POINTER(PDH_HCOUNTER)]
PdhAddEnglishCounterA.restype = PDH_STATUS
PdhAddEnglishCounterA.errcheck = error_success

PdhCollectQueryDataWithTime = windll.pdh.PdhCollectQueryDataWithTime
PdhCollectQueryDataWithTime.argtypes = [PDH_HQUERY, POINTER(LONGLONG)]
PdhCollectQueryDataWithTime.restype = PDH_STATUS
PdhCollectQueryDataWithTime.errcheck = error_success

PdhValidatePathExW = windll.pdh.PdhValidatePathExW
PdhValidatePathExW.argtypes = [PDH_HLOG, LPCWSTR]
PdhValidatePathExW.restype = PDH_STATUS
PdhValidatePathExW.errcheck = error_success

PdhValidatePathExA = windll.pdh.PdhValidatePathExA
PdhValidatePathExA.argtypes = [PDH_HLOG, LPCSTR]
PdhValidatePathExA.restype = PDH_STATUS
PdhValidatePathExA.errcheck = error_success

PdhRemoveCounter = windll.pdh.PdhRemoveCounter
PdhRemoveCounter.argtypes = [PDH_HCOUNTER]
PdhRemoveCounter.restype = PDH_STATUS
PdhRemoveCounter.errcheck = error_success

PdhCollectQueryData = windll.pdh.PdhCollectQueryData
PdhCollectQueryData.argtypes = [PDH_HQUERY]
PdhCollectQueryData.restype = PDH_STATUS
PdhCollectQueryData.errcheck = error_success

PdhCloseQuery = windll.pdh.PdhCloseQuery
PdhCloseQuery.argtypes = [PDH_HQUERY]
PdhCloseQuery.restype = PDH_STATUS
PdhCloseQuery.errcheck = error_success

PdhGetFormattedCounterValue = windll.pdh.PdhGetFormattedCounterValue
PdhGetFormattedCounterValue.argtypes = [PDH_HCOUNTER, DWORD, POINTER(DWORD), PPDH_FMT_COUNTERVALUE]
PdhGetFormattedCounterValue.restype = PDH_STATUS
PdhGetFormattedCounterValue.errcheck = error_success

PdhGetFormattedCounterArrayA = windll.pdh.PdhGetFormattedCounterArrayA
PdhGetFormattedCounterArrayA.argtypes = [PDH_HCOUNTER, DWORD, POINTER(DWORD), POINTER(DWORD), PPDH_FMT_COUNTERVALUE_ITEM_A]
PdhGetFormattedCounterArrayA.restype = PDH_STATUS
PdhGetFormattedCounterArrayA.errcheck = error_success

PdhGetFormattedCounterArrayW = windll.pdh.PdhGetFormattedCounterArrayW
PdhGetFormattedCounterArrayW.argtypes = [PDH_HCOUNTER, DWORD, POINTER(DWORD), POINTER(DWORD), PPDH_FMT_COUNTERVALUE_ITEM_W]
PdhGetFormattedCounterArrayW.restype = PDH_STATUS
PdhGetFormattedCounterArrayW.errcheck = error_success

PdhGetRawCounterValue = windll.pdh.PdhGetRawCounterValue
PdhGetRawCounterValue.argtypes = [PDH_HCOUNTER, POINTER(DWORD), PPDH_RAW_COUNTER]
PdhGetRawCounterValue.restype = PDH_STATUS
PdhGetRawCounterValue.errcheck = error_success

PdhGetRawCounterArrayA = windll.pdh.PdhGetRawCounterArrayA
PdhGetRawCounterArrayA.argtypes = [PDH_HCOUNTER, POINTER(DWORD), POINTER(DWORD), PPDH_RAW_COUNTER_ITEM_A]
PdhGetRawCounterArrayA.restype = PDH_STATUS
PdhGetRawCounterArrayA.errcheck = error_success

PdhGetRawCounterArrayW = windll.pdh.PdhGetRawCounterArrayW
PdhGetRawCounterArrayW.argtypes = [PDH_HCOUNTER, POINTER(DWORD), POINTER(DWORD), PPDH_RAW_COUNTER_ITEM_W]
PdhGetRawCounterArrayW.restype = PDH_STATUS
PdhGetRawCounterArrayW.errcheck = error_success

PdhCalculateCounterFromRawValue = windll.pdh.PdhCalculateCounterFromRawValue
PdhCalculateCounterFromRawValue.argtypes = [PDH_HCOUNTER, DWORD, PPDH_RAW_COUNTER, PPDH_RAW_COUNTER, PPDH_FMT_COUNTERVALUE]
PdhCalculateCounterFromRawValue.restype = PDH_STATUS
PdhCalculateCounterFromRawValue.errcheck = error_success

PdhComputeCounterStatistics = windll.pdh.PdhComputeCounterStatistics
PdhComputeCounterStatistics.argtypes = [PDH_HCOUNTER, DWORD, DWORD, DWORD, PPDH_RAW_COUNTER, PPDH_STATISTICS]
PdhComputeCounterStatistics.restype = PDH_STATUS
PdhComputeCounterStatistics.errcheck = error_success

PdhGetCounterInfoA = windll.pdh.PdhGetCounterInfoA
PdhGetCounterInfoA.argtypes = [PDH_HCOUNTER, BOOLEAN, POINTER(DWORD), PPDH_COUNTER_INFO_A]
PdhGetCounterInfoA.restype = PDH_STATUS
PdhGetCounterInfoA.errcheck = error_success

PdhGetCounterInfoW = windll.pdh.PdhGetCounterInfoW
PdhGetCounterInfoW.argtypes = [PDH_HCOUNTER, BOOLEAN, POINTER(DWORD), PPDH_COUNTER_INFO_W]
PdhGetCounterInfoW.restype = PDH_STATUS
PdhGetCounterInfoW.errcheck = error_success

PdhSetCounterScaleFactor = windll.pdh.PdhSetCounterScaleFactor
PdhSetCounterScaleFactor.argtypes = [PDH_HCOUNTER, LONG]
PdhSetCounterScaleFactor.restype = PDH_STATUS
PdhSetCounterScaleFactor.errcheck = error_success

PdhConnectMachineA = windll.pdh.PdhConnectMachineA
PdhConnectMachineA.argtypes = [LPCSTR]
PdhConnectMachineA.restype = PDH_STATUS
PdhConnectMachineA.errcheck = error_success

PdhConnectMachineW = windll.pdh.PdhConnectMachineW
PdhConnectMachineW.argtypes = [LPCWSTR]
PdhConnectMachineW.restype = PDH_STATUS
PdhConnectMachineW.errcheck = error_success

PdhEnumMachinesA = windll.pdh.PdhEnumMachinesA
PdhEnumMachinesA.argtypes = [LPCSTR, PZZSTR, POINTER(DWORD)]
PdhEnumMachinesA.restype = PDH_STATUS
PdhEnumMachinesA.errcheck = error_success

PdhEnumMachinesW = windll.pdh.PdhEnumMachinesW
PdhEnumMachinesW.argtypes = [LPCWSTR, PZZWSTR, POINTER(DWORD)]
PdhEnumMachinesW.restype = PDH_STATUS
PdhEnumMachinesW.errcheck = error_success

PdhEnumObjectsA = windll.pdh.PdhEnumObjectsA
PdhEnumObjectsA.argtypes = [LPCSTR, LPCSTR, PZZSTR, POINTER(DWORD), DWORD, BOOL]
PdhEnumObjectsA.restype = PDH_STATUS
PdhEnumObjectsA.errcheck = error_success

PdhEnumObjectsW = windll.pdh.PdhEnumObjectsW
PdhEnumObjectsW.argtypes = [LPCWSTR, LPCWSTR, PZZWSTR, POINTER(DWORD), DWORD, BOOL]
PdhEnumObjectsW.restype = PDH_STATUS
PdhEnumObjectsW.errcheck = error_success

PdhEnumObjectItemsA = windll.pdh.PdhEnumObjectItemsA
PdhEnumObjectItemsA.argtypes = [LPCSTR, LPCSTR, LPCSTR, PZZSTR, POINTER(DWORD), PZZSTR, POINTER(DWORD), DWORD, DWORD]
PdhEnumObjectItemsA.restype = PDH_STATUS
PdhEnumObjectItemsA.errcheck = error_success

PdhEnumObjectItemsW = windll.pdh.PdhEnumObjectItemsW
PdhEnumObjectItemsW.argtypes = [LPCWSTR, LPCWSTR, LPCWSTR, PZZWSTR, POINTER(DWORD), PZZWSTR, POINTER(DWORD), DWORD, DWORD]
PdhEnumObjectItemsW.restype = PDH_STATUS
PdhEnumObjectItemsW.errcheck = error_success

PdhMakeCounterPathA = windll.pdh.PdhMakeCounterPathA
PdhMakeCounterPathA.argtypes = [PPDH_COUNTER_PATH_ELEMENTS_A, LPSTR, POINTER(DWORD), DWORD]
PdhMakeCounterPathA.restype = PDH_STATUS
PdhMakeCounterPathA.errcheck = error_success

PdhMakeCounterPathW = windll.pdh.PdhMakeCounterPathW
PdhMakeCounterPathW.argtypes = [PPDH_COUNTER_PATH_ELEMENTS_W, LPWSTR, POINTER(DWORD), DWORD]
PdhMakeCounterPathW.restype = PDH_STATUS
PdhMakeCounterPathW.errcheck = error_success

PdhParseCounterPathA = windll.pdh.PdhParseCounterPathA
PdhParseCounterPathA.argtypes = [LPCSTR, PPDH_COUNTER_PATH_ELEMENTS_A, POINTER(DWORD), DWORD]
PdhParseCounterPathA.restype = PDH_STATUS
PdhParseCounterPathA.errcheck = error_success

PdhParseCounterPathW = windll.pdh.PdhParseCounterPathW
PdhParseCounterPathW.argtypes = [LPCWSTR, PPDH_COUNTER_PATH_ELEMENTS_W, POINTER(DWORD), DWORD]
PdhParseCounterPathW.restype = PDH_STATUS
PdhParseCounterPathW.errcheck = error_success

PdhParseInstanceNameA = windll.pdh.PdhParseInstanceNameA
PdhParseInstanceNameA.argtypes = [LPCSTR, LPSTR, POINTER(DWORD), LPSTR, POINTER(DWORD), POINTER(DWORD)]
PdhParseInstanceNameA.restype = PDH_STATUS
PdhParseInstanceNameA.errcheck = error_success

PdhParseInstanceNameW = windll.pdh.PdhParseInstanceNameW
PdhParseInstanceNameW.argtypes = [LPCWSTR, LPWSTR, POINTER(DWORD), LPWSTR, POINTER(DWORD), POINTER(DWORD)]
PdhParseInstanceNameW.restype = PDH_STATUS
PdhParseInstanceNameW.errcheck = error_success

PdhValidatePathA = windll.pdh.PdhValidatePathA
PdhValidatePathA.argtypes = [LPCSTR]
PdhValidatePathA.restype = PDH_STATUS
PdhValidatePathA.errcheck = error_success

PdhValidatePathW = windll.pdh.PdhValidatePathW
PdhValidatePathW.argtypes = [LPCWSTR]
PdhValidatePathW.restype = PDH_STATUS
PdhValidatePathW.errcheck = error_success

PdhGetDefaultPerfObjectA = windll.pdh.PdhGetDefaultPerfObjectA
PdhGetDefaultPerfObjectA.argtypes = [LPCSTR, LPCSTR, LPSTR, POINTER(DWORD)]
PdhGetDefaultPerfObjectA.restype = PDH_STATUS
PdhGetDefaultPerfObjectA.errcheck = error_success

PdhGetDefaultPerfObjectW = windll.pdh.PdhGetDefaultPerfObjectW
PdhGetDefaultPerfObjectW.argtypes = [LPCWSTR, LPCWSTR, LPWSTR, POINTER(DWORD)]
PdhGetDefaultPerfObjectW.restype = PDH_STATUS
PdhGetDefaultPerfObjectW.errcheck = error_success

PdhGetDefaultPerfCounterA = windll.pdh.PdhGetDefaultPerfCounterA
PdhGetDefaultPerfCounterA.argtypes = [LPCSTR, LPCSTR, LPCSTR, LPSTR, POINTER(DWORD)]
PdhGetDefaultPerfCounterA.restype = PDH_STATUS
PdhGetDefaultPerfCounterA.errcheck = error_success

PdhGetDefaultPerfCounterW = windll.pdh.PdhGetDefaultPerfCounterW
PdhGetDefaultPerfCounterW.argtypes = [LPCWSTR, LPCWSTR, LPCWSTR, LPWSTR, POINTER(DWORD)]
PdhGetDefaultPerfCounterW.restype = PDH_STATUS
PdhGetDefaultPerfCounterW.errcheck = error_success

PdhBrowseCountersA = windll.pdh.PdhBrowseCountersA
PdhBrowseCountersA.argtypes = [PPDH_BROWSE_DLG_CONFIG_A]
PdhBrowseCountersA.restype = PDH_STATUS
PdhBrowseCountersA.errcheck = error_success

PdhBrowseCountersW = windll.pdh.PdhBrowseCountersW
PdhBrowseCountersW.argtypes = [PPDH_BROWSE_DLG_CONFIG_W]
PdhBrowseCountersW.restype = PDH_STATUS
PdhBrowseCountersW.errcheck = error_success

PdhExpandCounterPathA = windll.pdh.PdhExpandCounterPathA
PdhExpandCounterPathA.argtypes = [LPCSTR, PZZSTR, POINTER(DWORD)]
PdhExpandCounterPathA.restype = PDH_STATUS
PdhExpandCounterPathA.errcheck = error_success

PdhExpandCounterPathW = windll.pdh.PdhExpandCounterPathW
PdhExpandCounterPathW.argtypes = [LPCWSTR, PZZWSTR, POINTER(DWORD)]
PdhExpandCounterPathW.restype = PDH_STATUS
PdhExpandCounterPathW.errcheck = error_success

PdhLookupPerfNameByIndexA = windll.pdh.PdhLookupPerfNameByIndexA
PdhLookupPerfNameByIndexA.argtypes = [LPCSTR, DWORD, LPSTR, POINTER(DWORD)]
PdhLookupPerfNameByIndexA.restype = PDH_STATUS
PdhLookupPerfNameByIndexA.errcheck = error_success

PdhLookupPerfNameByIndexW = windll.pdh.PdhLookupPerfNameByIndexW
PdhLookupPerfNameByIndexW.argtypes = [LPCWSTR, DWORD, LPWSTR, POINTER(DWORD)]
PdhLookupPerfNameByIndexW.restype = PDH_STATUS
PdhLookupPerfNameByIndexW.errcheck = error_success

PdhLookupPerfIndexByNameA = windll.pdh.PdhLookupPerfIndexByNameA
PdhLookupPerfIndexByNameA.argtypes = [LPCSTR, LPCSTR, POINTER(DWORD)]
PdhLookupPerfIndexByNameA.restype = PDH_STATUS
PdhLookupPerfIndexByNameA.errcheck = error_success

PdhLookupPerfIndexByNameW = windll.pdh.PdhLookupPerfIndexByNameW
PdhLookupPerfIndexByNameW.argtypes = [LPCWSTR, LPCWSTR, POINTER(DWORD)]
PdhLookupPerfIndexByNameW.restype = PDH_STATUS
PdhLookupPerfIndexByNameW.errcheck = error_success

PdhExpandWildCardPathA = windll.pdh.PdhExpandWildCardPathA
PdhExpandWildCardPathA.argtypes = [LPCSTR, LPCSTR, PZZSTR, POINTER(DWORD), DWORD]
PdhExpandWildCardPathA.restype = PDH_STATUS
PdhExpandWildCardPathA.errcheck = error_success

PdhExpandWildCardPathW = windll.pdh.PdhExpandWildCardPathW
PdhExpandWildCardPathW.argtypes = [LPCWSTR, LPCWSTR, PZZWSTR, POINTER(DWORD), DWORD]
PdhExpandWildCardPathW.restype = PDH_STATUS
PdhExpandWildCardPathW.errcheck = error_success

PdhOpenLogA = windll.pdh.PdhOpenLogA
PdhOpenLogA.argtypes = [LPCSTR, DWORD, POINTER(DWORD), PDH_HQUERY, DWORD, LPCSTR, POINTER(PDH_HLOG)]
PdhOpenLogA.restype = PDH_STATUS
PdhOpenLogA.errcheck = error_success

PdhOpenLogW = windll.pdh.PdhOpenLogW
PdhOpenLogW.argtypes = [LPCWSTR, DWORD, POINTER(DWORD), PDH_HQUERY, DWORD, LPCWSTR, POINTER(PDH_HLOG)]
PdhOpenLogW.restype = PDH_STATUS
PdhOpenLogW.errcheck = error_success

PdhUpdateLogA = windll.pdh.PdhUpdateLogA
PdhUpdateLogA.argtypes = [PDH_HLOG, LPCSTR]
PdhUpdateLogA.restype = PDH_STATUS
PdhUpdateLogA.errcheck = error_success

PdhUpdateLogW = windll.pdh.PdhUpdateLogW
PdhUpdateLogW.argtypes = [PDH_HLOG, LPCWSTR]
PdhUpdateLogW.restype = PDH_STATUS
PdhUpdateLogW.errcheck = error_success

PdhUpdateLogFileCatalog = windll.pdh.PdhUpdateLogFileCatalog
PdhUpdateLogFileCatalog.argtypes = [PDH_HLOG]
PdhUpdateLogFileCatalog.restype = PDH_STATUS
PdhUpdateLogFileCatalog.errcheck = error_success

PdhGetLogFileSize = windll.pdh.PdhGetLogFileSize
PdhGetLogFileSize.argtypes = [PDH_HLOG, POINTER(LONGLONG)]
PdhGetLogFileSize.restype = PDH_STATUS
PdhGetLogFileSize.errcheck = error_success

PdhCloseLog = windll.pdh.PdhCloseLog
PdhCloseLog.argtypes = [PDH_HLOG, DWORD]
PdhCloseLog.restype = PDH_STATUS
PdhCloseLog.errcheck = error_success

PdhSelectDataSourceA = windll.pdh.PdhSelectDataSourceA
PdhSelectDataSourceA.argtypes = [HWND, DWORD, LPSTR, POINTER(DWORD)]
PdhSelectDataSourceA.restype = PDH_STATUS
PdhSelectDataSourceA.errcheck = error_success

PdhSelectDataSourceW = windll.pdh.PdhSelectDataSourceW
PdhSelectDataSourceW.argtypes = [HWND, DWORD, LPWSTR, POINTER(DWORD)]
PdhSelectDataSourceW.restype = PDH_STATUS
PdhSelectDataSourceW.errcheck = error_success

PdhIsRealTimeQuery = windll.pdh.PdhIsRealTimeQuery
PdhIsRealTimeQuery.argtypes = [PDH_HQUERY]
PdhIsRealTimeQuery.restype = BOOL

PdhSetQueryTimeRange = windll.pdh.PdhSetQueryTimeRange
PdhSetQueryTimeRange.argtypes = [PDH_HQUERY, PPDH_TIME_INFO]
PdhSetQueryTimeRange.restype = PDH_STATUS
PdhSetQueryTimeRange.errcheck = error_success

PdhGetDataSourceTimeRangeA = windll.pdh.PdhGetDataSourceTimeRangeA
PdhGetDataSourceTimeRangeA.argtypes = [LPCSTR, POINTER(DWORD), PPDH_TIME_INFO, POINTER(DWORD)]
PdhGetDataSourceTimeRangeA.restype = PDH_STATUS
PdhGetDataSourceTimeRangeA.errcheck = error_success

PdhGetDataSourceTimeRangeW = windll.pdh.PdhGetDataSourceTimeRangeW
PdhGetDataSourceTimeRangeW.argtypes = [LPCWSTR, POINTER(DWORD), PPDH_TIME_INFO, POINTER(DWORD)]
PdhGetDataSourceTimeRangeW.restype = PDH_STATUS
PdhGetDataSourceTimeRangeW.errcheck = error_success

PdhCollectQueryDataEx = windll.pdh.PdhCollectQueryDataEx
PdhCollectQueryDataEx.argtypes = [PDH_HQUERY, DWORD, HANDLE]
PdhCollectQueryDataEx.restype = PDH_STATUS
PdhCollectQueryDataEx.errcheck = error_success

PdhFormatFromRawValue = windll.pdh.PdhFormatFromRawValue
PdhFormatFromRawValue.argtypes = [DWORD, DWORD, POINTER(LONGLONG), PPDH_RAW_COUNTER, PPDH_RAW_COUNTER, PPDH_FMT_COUNTERVALUE]
PdhFormatFromRawValue.restype = PDH_STATUS
PdhFormatFromRawValue.errcheck = error_success

PdhGetCounterTimeBase = windll.pdh.PdhGetCounterTimeBase
PdhGetCounterTimeBase.argtypes = [PDH_HCOUNTER, POINTER(LONGLONG)]
PdhGetCounterTimeBase.restype = PDH_STATUS
PdhGetCounterTimeBase.errcheck = error_success

PdhReadRawLogRecord = windll.pdh.PdhReadRawLogRecord
PdhReadRawLogRecord.argtypes = [PDH_HLOG, FILETIME, PPDH_RAW_LOG_RECORD, POINTER(DWORD)]
PdhReadRawLogRecord.restype = PDH_STATUS
PdhReadRawLogRecord.errcheck = error_success

PdhSetDefaultRealTimeDataSource = windll.pdh.PdhSetDefaultRealTimeDataSource
PdhSetDefaultRealTimeDataSource.argtypes = [DWORD]
PdhSetDefaultRealTimeDataSource.restype = PDH_STATUS
PdhSetDefaultRealTimeDataSource.errcheck = error_success

PdhBindInputDataSourceA = windll.pdh.PdhBindInputDataSourceA
PdhBindInputDataSourceA.argtypes = [POINTER(PDH_HLOG), LPCSTR]
PdhBindInputDataSourceA.restype = PDH_STATUS
PdhBindInputDataSourceA.errcheck = error_success

PdhBindInputDataSourceW = windll.pdh.PdhBindInputDataSourceW
PdhBindInputDataSourceW.argtypes = [POINTER(PDH_HLOG), LPCWSTR]
PdhBindInputDataSourceW.restype = PDH_STATUS
PdhBindInputDataSourceW.errcheck = error_success

PdhOpenQueryH = windll.pdh.PdhOpenQueryH
PdhOpenQueryH.argtypes = [PDH_HLOG, DWORD_PTR, POINTER(PDH_HQUERY)]
PdhOpenQueryH.restype = PDH_STATUS
PdhOpenQueryH.errcheck = error_success

PdhEnumMachinesHA = windll.pdh.PdhEnumMachinesHA
PdhEnumMachinesHA.argtypes = [PDH_HLOG, PZZSTR, POINTER(DWORD)]
PdhEnumMachinesHA.restype = PDH_STATUS
PdhEnumMachinesHA.errcheck = error_success

PdhEnumMachinesHW = windll.pdh.PdhEnumMachinesHW
PdhEnumMachinesHW.argtypes = [PDH_HLOG, PZZWSTR, POINTER(DWORD)]
PdhEnumMachinesHW.restype = PDH_STATUS
PdhEnumMachinesHW.errcheck = error_success

PdhEnumObjectsHA = windll.pdh.PdhEnumObjectsHA
PdhEnumObjectsHA.argtypes = [PDH_HLOG, LPCSTR, PZZSTR, POINTER(DWORD), DWORD, BOOL]
PdhEnumObjectsHA.restype = PDH_STATUS
PdhEnumObjectsHA.errcheck = error_success

PdhEnumObjectsHW = windll.pdh.PdhEnumObjectsHW
PdhEnumObjectsHW.argtypes = [PDH_HLOG, LPCWSTR, PZZWSTR, POINTER(DWORD), DWORD, BOOL]
PdhEnumObjectsHW.restype = PDH_STATUS
PdhEnumObjectsHW.errcheck = error_success

PdhEnumObjectItemsHA = windll.pdh.PdhEnumObjectItemsHA
PdhEnumObjectItemsHA.argtypes = [PDH_HLOG, LPCSTR, LPCSTR, PZZSTR, POINTER(DWORD), PZZSTR, POINTER(DWORD), DWORD, DWORD]
PdhEnumObjectItemsHA.restype = PDH_STATUS
PdhEnumObjectItemsHA.errcheck = error_success

PdhEnumObjectItemsHW = windll.pdh.PdhEnumObjectItemsHW
PdhEnumObjectItemsHW.argtypes = [PDH_HLOG, LPCWSTR, LPCWSTR, PZZWSTR, POINTER(DWORD), PZZWSTR, POINTER(DWORD), DWORD, DWORD]
PdhEnumObjectItemsHW.restype = PDH_STATUS
PdhEnumObjectItemsHW.errcheck = error_success

PdhExpandWildCardPathHA = windll.pdh.PdhExpandWildCardPathHA
PdhExpandWildCardPathHA.argtypes = [PDH_HLOG, LPCSTR, PZZSTR, POINTER(DWORD), DWORD]
PdhExpandWildCardPathHA.restype = PDH_STATUS
PdhExpandWildCardPathHA.errcheck = error_success

PdhExpandWildCardPathHW = windll.pdh.PdhExpandWildCardPathHW
PdhExpandWildCardPathHW.argtypes = [PDH_HLOG, LPCWSTR, PZZWSTR, POINTER(DWORD), DWORD]
PdhExpandWildCardPathHW.restype = PDH_STATUS
PdhExpandWildCardPathHW.errcheck = error_success

PdhGetDataSourceTimeRangeH = windll.pdh.PdhGetDataSourceTimeRangeH
PdhGetDataSourceTimeRangeH.argtypes = [PDH_HLOG, POINTER(DWORD), PPDH_TIME_INFO, POINTER(DWORD)]
PdhGetDataSourceTimeRangeH.restype = PDH_STATUS
PdhGetDataSourceTimeRangeH.errcheck = error_success

PdhGetDefaultPerfObjectHA = windll.pdh.PdhGetDefaultPerfObjectHA
PdhGetDefaultPerfObjectHA.argtypes = [PDH_HLOG, LPCSTR, LPSTR, POINTER(DWORD)]
PdhGetDefaultPerfObjectHA.restype = PDH_STATUS
PdhGetDefaultPerfObjectHA.errcheck = error_success

PdhGetDefaultPerfObjectHW = windll.pdh.PdhGetDefaultPerfObjectHW
PdhGetDefaultPerfObjectHW.argtypes = [PDH_HLOG, LPCWSTR, LPWSTR, POINTER(DWORD)]
PdhGetDefaultPerfObjectHW.restype = PDH_STATUS
PdhGetDefaultPerfObjectHW.errcheck = error_success

PdhGetDefaultPerfCounterHA = windll.pdh.PdhGetDefaultPerfCounterHA
PdhGetDefaultPerfCounterHA.argtypes = [PDH_HLOG, LPCSTR, LPCSTR, LPSTR, POINTER(DWORD)]
PdhGetDefaultPerfCounterHA.restype = PDH_STATUS
PdhGetDefaultPerfCounterHA.errcheck = error_success

PdhGetDefaultPerfCounterHW = windll.pdh.PdhGetDefaultPerfCounterHW
PdhGetDefaultPerfCounterHW.argtypes = [PDH_HLOG, LPCWSTR, LPCWSTR, LPWSTR, POINTER(DWORD)]
PdhGetDefaultPerfCounterHW.restype = PDH_STATUS
PdhGetDefaultPerfCounterHW.errcheck = error_success

PdhBrowseCountersHA = windll.pdh.PdhBrowseCountersHA
PdhBrowseCountersHA.argtypes = [PPDH_BROWSE_DLG_CONFIG_HA]
PdhBrowseCountersHA.restype = PDH_STATUS
PdhBrowseCountersHA.errcheck = error_success

PdhBrowseCountersHW = windll.pdh.PdhBrowseCountersHW
PdhBrowseCountersHW.argtypes = [PPDH_BROWSE_DLG_CONFIG_HW]
PdhBrowseCountersHW.restype = PDH_STATUS
PdhBrowseCountersHW.errcheck = error_success

PdhVerifySQLDBA = windll.pdh.PdhVerifySQLDBA
PdhVerifySQLDBA.argtypes = [LPCSTR]
PdhVerifySQLDBA.restype = PDH_STATUS
PdhVerifySQLDBA.errcheck = error_success

PdhVerifySQLDBW = windll.pdh.PdhVerifySQLDBW
PdhVerifySQLDBW.argtypes = [LPCWSTR]
PdhVerifySQLDBW.restype = PDH_STATUS
PdhVerifySQLDBW.errcheck = error_success

PdhCreateSQLTablesA = windll.pdh.PdhCreateSQLTablesA
PdhCreateSQLTablesA.argtypes = [LPCSTR]
PdhCreateSQLTablesA.restype = PDH_STATUS
PdhCreateSQLTablesA.errcheck = error_success

PdhCreateSQLTablesW = windll.pdh.PdhCreateSQLTablesW
PdhCreateSQLTablesW.argtypes = [LPCWSTR]
PdhCreateSQLTablesW.restype = PDH_STATUS
PdhCreateSQLTablesW.errcheck = error_success

PdhEnumLogSetNamesA = windll.pdh.PdhEnumLogSetNamesA
PdhEnumLogSetNamesA.argtypes = [LPCSTR, PZZSTR, POINTER(DWORD)]
PdhEnumLogSetNamesA.restype = PDH_STATUS
PdhEnumLogSetNamesA.errcheck = error_success

PdhEnumLogSetNamesW = windll.pdh.PdhEnumLogSetNamesW
PdhEnumLogSetNamesW.argtypes = [LPCWSTR, PZZWSTR, POINTER(DWORD)]
PdhEnumLogSetNamesW.restype = PDH_STATUS
PdhEnumLogSetNamesW.errcheck = error_success

PdhGetLogSetGUID = windll.pdh.PdhGetLogSetGUID
PdhGetLogSetGUID.argtypes = [PDH_HLOG, POINTER(GUID), POINTER(INT)]
PdhGetLogSetGUID.restype = PDH_STATUS
PdhGetLogSetGUID.errcheck = error_success

PdhSetLogSetRunID = windll.pdh.PdhSetLogSetRunID
PdhSetLogSetRunID.argtypes = [PDH_HLOG, INT]
PdhSetLogSetRunID.restype = PDH_STATUS
PdhSetLogSetRunID.errcheck = error_success

