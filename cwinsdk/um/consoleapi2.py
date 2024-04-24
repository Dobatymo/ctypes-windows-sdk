from ctypes import POINTER, Structure
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPCSTR, LPCWSTR, LPSTR, LPVOID, LPWSTR, ULONG, WCHAR, WORD

from .. import nonzero, windll
from ..shared.minwindef import LPDWORD, UINT
from ..shared.ntdef import CHAR
from ..shared.windef import COLORREF
from .minwinbase import SECURITY_ATTRIBUTES
from .wincontypes import CHAR_INFO, COORD, INPUT_RECORD, SMALL_RECT

FOREGROUND_BLUE = 0x0001
FOREGROUND_GREEN = 0x0002
FOREGROUND_RED = 0x0004
FOREGROUND_INTENSITY = 0x0008
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_RED = 0x0040
BACKGROUND_INTENSITY = 0x0080
COMMON_LVB_LEADING_BYTE = 0x0100
COMMON_LVB_TRAILING_BYTE = 0x0200
COMMON_LVB_GRID_HORIZONTAL = 0x0400
COMMON_LVB_GRID_LVERTICAL = 0x0800
COMMON_LVB_GRID_RVERTICAL = 0x1000
COMMON_LVB_REVERSE_VIDEO = 0x4000
COMMON_LVB_UNDERSCORE = 0x8000
COMMON_LVB_SBCSDBCS = 0x0300


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
    ]


LP_CONSOLE_SCREEN_BUFFER_INFO = POINTER(CONSOLE_SCREEN_BUFFER_INFO)


class CONSOLE_SCREEN_BUFFER_INFOEX(Structure):
    # no pack
    _fields_ = [
        ("cbSize", ULONG),
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
        ("wPopupAttributes", WORD),
        ("bFullscreenSupported", BOOL),
        ("ColorTable", COLORREF * 16),
    ]


LP_CONSOLE_SCREEN_BUFFER_INFOEX = POINTER(CONSOLE_SCREEN_BUFFER_INFOEX)


class CONSOLE_CURSOR_INFO(Structure):
    # no pack
    _fields_ = [
        ("dwSize", DWORD),
        ("bVisible", BOOL),
    ]


PCONSOLE_CURSOR_INFO = POINTER(CONSOLE_CURSOR_INFO)

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
FillConsoleOutputCharacterA.argtypes = [HANDLE, CHAR, DWORD, COORD, LPDWORD]
FillConsoleOutputCharacterA.restype = BOOL
FillConsoleOutputCharacterA.errcheck = nonzero

FillConsoleOutputCharacterW = windll.kernel32.FillConsoleOutputCharacterW
FillConsoleOutputCharacterW.argtypes = [HANDLE, WCHAR, DWORD, COORD, LPDWORD]
FillConsoleOutputCharacterW.restype = BOOL
FillConsoleOutputCharacterW.errcheck = nonzero

FillConsoleOutputAttribute = windll.kernel32.FillConsoleOutputAttribute
FillConsoleOutputAttribute.argtypes = [HANDLE, WORD, DWORD, COORD, LPDWORD]
FillConsoleOutputAttribute.restype = BOOL
FillConsoleOutputAttribute.errcheck = nonzero

GenerateConsoleCtrlEvent = windll.kernel32.GenerateConsoleCtrlEvent
GenerateConsoleCtrlEvent.argtypes = [DWORD, DWORD]
GenerateConsoleCtrlEvent.restype = BOOL
GenerateConsoleCtrlEvent.errcheck = nonzero

CreateConsoleScreenBuffer = windll.kernel32.CreateConsoleScreenBuffer
CreateConsoleScreenBuffer.argtypes = [DWORD, DWORD, POINTER(SECURITY_ATTRIBUTES), DWORD, LPVOID]
CreateConsoleScreenBuffer.restype = HANDLE

SetConsoleActiveScreenBuffer = windll.kernel32.SetConsoleActiveScreenBuffer
SetConsoleActiveScreenBuffer.argtypes = [HANDLE]
SetConsoleActiveScreenBuffer.restype = BOOL
SetConsoleActiveScreenBuffer.errcheck = nonzero

FlushConsoleInputBuffer = windll.kernel32.FlushConsoleInputBuffer
FlushConsoleInputBuffer.argtypes = [HANDLE]
FlushConsoleInputBuffer.restype = BOOL
FlushConsoleInputBuffer.errcheck = nonzero

SetConsoleCP = windll.kernel32.SetConsoleCP
SetConsoleCP.argtypes = [UINT]
SetConsoleCP.restype = BOOL
SetConsoleCP.errcheck = nonzero

SetConsoleOutputCP = windll.kernel32.SetConsoleOutputCP
SetConsoleOutputCP.argtypes = [UINT]
SetConsoleOutputCP.restype = BOOL
SetConsoleOutputCP.errcheck = nonzero

GetConsoleCursorInfo = windll.kernel32.GetConsoleCursorInfo
GetConsoleCursorInfo.argtypes = [HANDLE, PCONSOLE_CURSOR_INFO]
GetConsoleCursorInfo.restype = BOOL
GetConsoleCursorInfo.errcheck = nonzero

SetConsoleCursorInfo = windll.kernel32.SetConsoleCursorInfo
SetConsoleCursorInfo.argtypes = [HANDLE, POINTER(CONSOLE_CURSOR_INFO)]
SetConsoleCursorInfo.restype = BOOL

GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
GetConsoleScreenBufferInfo.argtypes = [HANDLE, LP_CONSOLE_SCREEN_BUFFER_INFO]
GetConsoleScreenBufferInfo.restype = BOOL

GetConsoleScreenBufferInfoEx = windll.kernel32.GetConsoleScreenBufferInfoEx
GetConsoleScreenBufferInfoEx.argtypes = [HANDLE, LP_CONSOLE_SCREEN_BUFFER_INFOEX]
GetConsoleScreenBufferInfoEx.restype = BOOL

SetConsoleScreenBufferInfoEx = windll.kernel32.SetConsoleScreenBufferInfoEx
SetConsoleScreenBufferInfoEx.argtypes = [HANDLE, LP_CONSOLE_SCREEN_BUFFER_INFOEX]
SetConsoleScreenBufferInfoEx.restype = BOOL

SetConsoleScreenBufferSize = windll.kernel32.SetConsoleScreenBufferSize
SetConsoleScreenBufferSize.argtypes = [HANDLE, COORD]
SetConsoleScreenBufferSize.restype = BOOL

SetConsoleCursorPosition = windll.kernel32.SetConsoleCursorPosition
SetConsoleCursorPosition.argtypes = [HANDLE, COORD]
SetConsoleCursorPosition.restype = BOOL

GetLargestConsoleWindowSize = windll.kernel32.GetLargestConsoleWindowSize
GetLargestConsoleWindowSize.argtypes = [HANDLE]
GetLargestConsoleWindowSize.restype = COORD

SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
SetConsoleTextAttribute.argtypes = [HANDLE, WORD]
SetConsoleTextAttribute.restype = BOOL

SetConsoleWindowInfo = windll.kernel32.SetConsoleWindowInfo
SetConsoleWindowInfo.argtypes = [HANDLE, BOOL, POINTER(SMALL_RECT)]
SetConsoleWindowInfo.restype = BOOL

WriteConsoleOutputCharacterA = windll.kernel32.WriteConsoleOutputCharacterA
WriteConsoleOutputCharacterA.argtypes = [HANDLE, LPCSTR, DWORD, COORD, POINTER(DWORD)]
WriteConsoleOutputCharacterA.restype = BOOL

WriteConsoleOutputCharacterW = windll.kernel32.WriteConsoleOutputCharacterW
WriteConsoleOutputCharacterW.argtypes = [HANDLE, LPCWSTR, DWORD, COORD, POINTER(DWORD)]
WriteConsoleOutputCharacterW.restype = BOOL

WriteConsoleOutputAttribute = windll.kernel32.WriteConsoleOutputAttribute
WriteConsoleOutputAttribute.argtypes = [HANDLE, POINTER(WORD), DWORD, COORD, POINTER(DWORD)]
WriteConsoleOutputAttribute.restype = BOOL

ReadConsoleOutputCharacterA = windll.kernel32.ReadConsoleOutputCharacterA
ReadConsoleOutputCharacterA.argtypes = [HANDLE, LPSTR, DWORD, COORD, POINTER(DWORD)]
ReadConsoleOutputCharacterA.restype = BOOL

ReadConsoleOutputCharacterW = windll.kernel32.ReadConsoleOutputCharacterW
ReadConsoleOutputCharacterW.argtypes = [HANDLE, LPWSTR, DWORD, COORD, POINTER(DWORD)]
ReadConsoleOutputCharacterW.restype = BOOL

ReadConsoleOutputAttribute = windll.kernel32.ReadConsoleOutputAttribute
ReadConsoleOutputAttribute.argtypes = [HANDLE, POINTER(WORD), DWORD, COORD, POINTER(DWORD)]
ReadConsoleOutputAttribute.restype = BOOL

WriteConsoleInputA = windll.kernel32.WriteConsoleInputA
WriteConsoleInputA.argtypes = [HANDLE, POINTER(INPUT_RECORD), DWORD, POINTER(DWORD)]
WriteConsoleInputA.restype = BOOL

WriteConsoleInputW = windll.kernel32.WriteConsoleInputW
WriteConsoleInputW.argtypes = [HANDLE, POINTER(INPUT_RECORD), DWORD, POINTER(DWORD)]
WriteConsoleInputW.restype = BOOL

ScrollConsoleScreenBufferA = windll.kernel32.ScrollConsoleScreenBufferA
ScrollConsoleScreenBufferA.argtypes = [HANDLE, POINTER(SMALL_RECT), POINTER(SMALL_RECT), COORD, POINTER(CHAR_INFO)]
ScrollConsoleScreenBufferA.restype = BOOL

ScrollConsoleScreenBufferW = windll.kernel32.ScrollConsoleScreenBufferW
ScrollConsoleScreenBufferW.argtypes = [HANDLE, POINTER(SMALL_RECT), POINTER(SMALL_RECT), COORD, POINTER(CHAR_INFO)]
ScrollConsoleScreenBufferW.restype = BOOL

WriteConsoleOutputA = windll.kernel32.WriteConsoleOutputA
WriteConsoleOutputA.argtypes = [HANDLE, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
WriteConsoleOutputA.restype = BOOL

WriteConsoleOutputW = windll.kernel32.WriteConsoleOutputW
WriteConsoleOutputW.argtypes = [HANDLE, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
WriteConsoleOutputW.restype = BOOL

ReadConsoleOutputA = windll.kernel32.ReadConsoleOutputA
ReadConsoleOutputA.argtypes = [HANDLE, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
ReadConsoleOutputA.restype = BOOL

ReadConsoleOutputW = windll.kernel32.ReadConsoleOutputW
ReadConsoleOutputW.argtypes = [HANDLE, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
ReadConsoleOutputW.restype = BOOL

GetConsoleTitleA = windll.kernel32.GetConsoleTitleA
GetConsoleTitleA.argtypes = [LPSTR, DWORD]
GetConsoleTitleA.restype = DWORD

GetConsoleTitleW = windll.kernel32.GetConsoleTitleW
GetConsoleTitleW.argtypes = [LPWSTR, DWORD]
GetConsoleTitleW.restype = DWORD

GetConsoleOriginalTitleA = windll.kernel32.GetConsoleOriginalTitleA
GetConsoleOriginalTitleA.argtypes = [LPSTR, DWORD]
GetConsoleOriginalTitleA.restype = DWORD

GetConsoleOriginalTitleW = windll.kernel32.GetConsoleOriginalTitleW
GetConsoleOriginalTitleW.argtypes = [LPWSTR, DWORD]
GetConsoleOriginalTitleW.restype = DWORD

SetConsoleTitleA = windll.kernel32.SetConsoleTitleA
SetConsoleTitleA.argtypes = [LPCSTR]
SetConsoleTitleA.restype = BOOL

SetConsoleTitleW = windll.kernel32.SetConsoleTitleW
SetConsoleTitleW.argtypes = [LPCWSTR]
SetConsoleTitleW.restype = BOOL
