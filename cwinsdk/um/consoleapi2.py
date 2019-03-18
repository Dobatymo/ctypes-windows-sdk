from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import windll, Structure, POINTER
from ctypes.wintypes import BOOL, WORD, HANDLE, ULONG, DWORD
from ctypes.wintypes import LPSTR, LPWSTR, LPCSTR, LPCWSTR

from .wincontypes import COORD, SMALL_RECT, INPUT_RECORD, CHAR_INFO
from ..shared.windef import COLORREF

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
	# no pack
	_fields_ = [
		("dwSize", COORD),
		("dwCursorPosition", COORD),
		("wAttributes", WORD),
		("srWindow", SMALL_RECT),
		("dwMaximumWindowSize", COORD)
	]

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
		("ColorTable", COLORREF*16),
	]

class CONSOLE_CURSOR_INFO(Structure):
	# no pack
	_fields_ = [
		("dwSize", DWORD),
		("bVisible", BOOL),
	]

'''
FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
BOOL
 _In_ HANDLE hConsoleOutput,
 _In_ CHAR cCharacter,
 _In_ DWORD nLength,
 _In_ COORD dwWriteCoord,
 _Out_ LPDWORD lpNumberOfCharsWritten
 );


BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
FillConsoleOutputCharacterW(
 _In_ HANDLE hConsoleOutput,
 _In_ WCHAR cCharacter,
 _In_ DWORD nLength,
 _In_ COORD dwWriteCoord,
 _Out_ LPDWORD lpNumberOfCharsWritten
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
FillConsoleOutputAttribute(
 _In_ HANDLE hConsoleOutput,
 _In_ WORD wAttribute,
 _In_ DWORD nLength,
 _In_ COORD dwWriteCoord,
 _Out_ LPDWORD lpNumberOfAttrsWritten
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
GenerateConsoleCtrlEvent(
 _In_ DWORD dwCtrlEvent,
 _In_ DWORD dwProcessGroupId
 );



HANDLE

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
CreateConsoleScreenBuffer(
 _In_ DWORD dwDesiredAccess,
 _In_ DWORD dwShareMode,
 _In_opt_ CONST SECURITY_ATTRIBUTES* lpSecurityAttributes,
 _In_ DWORD dwFlags,
 _Reserved_ LPVOID lpScreenBufferData
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
SetConsoleActiveScreenBuffer(
 _In_ HANDLE hConsoleOutput
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
FlushConsoleInputBuffer(
 _In_ HANDLE hConsoleInput
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
SetConsoleCP(
 _In_ UINT wCodePageID
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
SetConsoleOutputCP(
 _In_ UINT wCodePageID
 );


BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
GetConsoleCursorInfo(
 _In_ HANDLE hConsoleOutput,
 _Out_ PCONSOLE_CURSOR_INFO lpConsoleCursorInfo
 );



BOOL

FillConsoleOutputCharacterA = windll.kernel32.FillConsoleOutputCharacterA
SetConsoleCursorInfo(
 _In_ HANDLE hConsoleOutput,
 _In_ CONST CONSOLE_CURSOR_INFO* lpConsoleCursorInfo
 );
'''
GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo
GetConsoleScreenBufferInfo.argtypes = [HANDLE, POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
GetConsoleScreenBufferInfo.restype = BOOL

GetConsoleScreenBufferInfoEx = windll.kernel32.GetConsoleScreenBufferInfoEx
GetConsoleScreenBufferInfoEx.argtypes = [HANDLE, POINTER(CONSOLE_SCREEN_BUFFER_INFOEX)]
GetConsoleScreenBufferInfoEx.restype = BOOL

SetConsoleScreenBufferInfoEx = windll.kernel32.SetConsoleScreenBufferInfoEx
SetConsoleScreenBufferInfoEx.argtypes = [HANDLE, POINTER(CONSOLE_SCREEN_BUFFER_INFOEX)]
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
