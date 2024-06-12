from ctypes import POINTER, Structure
from ctypes.wintypes import BOOL, CHAR, DWORD, HWND, PBYTE, WCHAR

from .. import nonzero, validhandle, windll
from ..shared.basetsd import ULONG_PTR
from ..shared.devpropdef import DEVPROPKEY, DEVPROPTYPE
from ..shared.guiddef import GUID
from ..shared.minwindef import PDWORD
from ..shared.ntdef import PCSTR, PSTR, PVOID, PWSTR
from .winnt import ANYSIZE_ARRAY, PCWSTR

HDSKSPC = PVOID
HDEVINFO = PVOID

LINE_LEN = 256


class SP_DEVINFO_DATA(Structure):
    _fields_ = [
        ("cbSize", DWORD),
        ("ClassGuid", GUID),
        ("DevInst", DWORD),
        ("Reserved", ULONG_PTR),
    ]


class SP_DEVICE_INTERFACE_DATA(Structure):
    _fields_ = [
        ("cbSize", DWORD),
        ("InterfaceClassGuid", GUID),
        ("Flags", DWORD),
        ("Reserved", ULONG_PTR),
    ]


class SP_DEVICE_INTERFACE_DETAIL_DATA_A(Structure):
    _fields_ = [
        ("cbSize", DWORD),
        ("DevicePath", CHAR * ANYSIZE_ARRAY),
    ]


def SP_DEVICE_INTERFACE_DETAIL_DATA_W_SIZE(size=ANYSIZE_ARRAY):
    class _SP_DEVICE_INTERFACE_DETAIL_DATA_W(Structure):
        _fields_ = [
            ("cbSize", DWORD),
            ("DevicePath", WCHAR * size),
        ]

    return _SP_DEVICE_INTERFACE_DETAIL_DATA_W


SP_DEVICE_INTERFACE_DETAIL_DATA_W = SP_DEVICE_INTERFACE_DETAIL_DATA_W_SIZE()

DIGCF_DEFAULT = 0x00000001
DIGCF_PRESENT = 0x00000002
DIGCF_ALLCLASSES = 0x00000004
DIGCF_PROFILE = 0x00000008
DIGCF_DEVICEINTERFACE = 0x00000010


# functions

SetupDiGetClassDevsA = windll.setupapi.SetupDiGetClassDevsA
SetupDiGetClassDevsA.argtypes = [POINTER(GUID), PCSTR, HWND, DWORD]
SetupDiGetClassDevsA.restype = HDEVINFO
SetupDiGetClassDevsA.errcheck = validhandle

SetupDiGetClassDevsW = windll.setupapi.SetupDiGetClassDevsW
SetupDiGetClassDevsW.argtypes = [POINTER(GUID), PCWSTR, HWND, DWORD]
SetupDiGetClassDevsW.restype = HDEVINFO
SetupDiGetClassDevsW.errcheck = validhandle

SetupDiGetClassDevsExA = windll.setupapi.SetupDiGetClassDevsExA
SetupDiGetClassDevsExA.argtypes = [POINTER(GUID), PCSTR, HWND, DWORD, HDEVINFO, PCSTR, PVOID]
SetupDiGetClassDevsExA.restype = HDEVINFO
SetupDiGetClassDevsExA.errcheck = validhandle

SetupDiGetClassDevsExW = windll.setupapi.SetupDiGetClassDevsExW
SetupDiGetClassDevsExW.argtypes = [POINTER(GUID), PCWSTR, HWND, DWORD, HDEVINFO, PCWSTR, PVOID]
SetupDiGetClassDevsExW.restype = HDEVINFO
SetupDiGetClassDevsExW.errcheck = validhandle

SetupDiGetINFClassA = windll.setupapi.SetupDiGetINFClassA
SetupDiGetINFClassA.argtypes = [PCSTR, POINTER(GUID), PSTR, DWORD, PDWORD]
SetupDiGetINFClassA.restype = BOOL

SetupDiGetINFClassW = windll.setupapi.SetupDiGetINFClassW
SetupDiGetINFClassW.argtypes = [PCWSTR, POINTER(GUID), PWSTR, DWORD, PDWORD]
SetupDiGetINFClassW.restype = BOOL

SetupDiEnumDeviceInfo = windll.setupapi.SetupDiEnumDeviceInfo
SetupDiEnumDeviceInfo.argtypes = [HDEVINFO, DWORD, POINTER(SP_DEVINFO_DATA)]
SetupDiEnumDeviceInfo.restype = BOOL
SetupDiEnumDeviceInfo.errcheck = nonzero

SetupDiDestroyDeviceInfoList = windll.setupapi.SetupDiDestroyDeviceInfoList
SetupDiDestroyDeviceInfoList.argtypes = [HDEVINFO]
SetupDiDestroyDeviceInfoList.restype = BOOL

SetupDiEnumDeviceInterfaces = windll.setupapi.SetupDiEnumDeviceInterfaces
SetupDiEnumDeviceInterfaces.argtypes = [
    HDEVINFO,
    POINTER(SP_DEVINFO_DATA),
    POINTER(GUID),
    DWORD,
    POINTER(SP_DEVICE_INTERFACE_DATA),
]
SetupDiEnumDeviceInterfaces.restype = BOOL
SetupDiEnumDeviceInterfaces.errcheck = nonzero

SetupDiGetDeviceInterfaceDetailA = windll.setupapi.SetupDiGetDeviceInterfaceDetailA
SetupDiGetDeviceInterfaceDetailA.argtypes = [
    HDEVINFO,
    POINTER(SP_DEVICE_INTERFACE_DATA),
    POINTER(SP_DEVICE_INTERFACE_DETAIL_DATA_A),
    DWORD,
    PDWORD,
    POINTER(SP_DEVINFO_DATA),
]
SetupDiGetDeviceInterfaceDetailA.restype = BOOL
SetupDiGetDeviceInterfaceDetailA.errcheck = nonzero

SetupDiGetDeviceInterfaceDetailW = windll.setupapi.SetupDiGetDeviceInterfaceDetailW
SetupDiGetDeviceInterfaceDetailW.argtypes = [
    HDEVINFO,
    POINTER(SP_DEVICE_INTERFACE_DATA),
    POINTER(SP_DEVICE_INTERFACE_DETAIL_DATA_W),
    DWORD,
    PDWORD,
    POINTER(SP_DEVINFO_DATA),
]
SetupDiGetDeviceInterfaceDetailW.restype = BOOL
SetupDiGetDeviceInterfaceDetailW.errcheck = nonzero


SetupDiGetClassDescriptionA = windll.setupapi.SetupDiGetClassDescriptionA
SetupDiGetClassDescriptionA.argtypes = [POINTER(GUID), PSTR, DWORD, PDWORD]
SetupDiGetClassDescriptionA.restype = BOOL
SetupDiGetClassDescriptionA.errcheck = nonzero

SetupDiGetClassDescriptionW = windll.setupapi.SetupDiGetClassDescriptionW
SetupDiGetClassDescriptionW.argtypes = [POINTER(GUID), PWSTR, DWORD, PDWORD]
SetupDiGetClassDescriptionW.restype = BOOL
SetupDiGetClassDescriptionW.errcheck = nonzero

SetupDiGetDevicePropertyKeys = windll.setupapi.SetupDiGetDevicePropertyKeys
SetupDiGetDevicePropertyKeys.argtypes = [HDEVINFO, POINTER(SP_DEVINFO_DATA), POINTER(DEVPROPKEY), DWORD, PDWORD, DWORD]
SetupDiGetDevicePropertyKeys.restype = BOOL

SetupDiGetDevicePropertyW = windll.setupapi.SetupDiGetDevicePropertyW
SetupDiGetDevicePropertyW.argtypes = [
    HDEVINFO,
    POINTER(SP_DEVINFO_DATA),
    POINTER(DEVPROPKEY),
    POINTER(DEVPROPTYPE),
    PBYTE,
    DWORD,
    PDWORD,
    DWORD,
]
SetupDiGetDevicePropertyW.restype = BOOL
SetupDiGetDevicePropertyW.errcheck = nonzero
