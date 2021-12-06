from ctypes import POINTER, Structure, Union, c_void_p
from ctypes.wintypes import BOOL, DWORD, SHORT, UINT, WCHAR, WORD

from ..shared.ntdef import CHAR


class COORD(Structure):
    # no pack
    _fields_ = [("X", SHORT), ("Y", SHORT)]


class SMALL_RECT(Structure):
    # no pack
    _fields_ = [("Left", SHORT), ("Top", SHORT), ("Right", SHORT), ("Bottom", SHORT)]


class KEY_EVENT_RECORD_UNION(Union):
    _fields_ = [
        ("UnicodeChar", WCHAR),
        ("AsciiChar", CHAR),
    ]


class KEY_EVENT_RECORD(Structure):
    # no pack
    _fields_ = [
        ("bKeyDown", BOOL),
        ("wRepeatCount", WORD),
        ("wVirtualKeyCode", WORD),
        ("wVirtualScanCode", WORD),
        ("uChar", KEY_EVENT_RECORD_UNION),
        ("dwControlKeyState", DWORD),
    ]


RIGHT_ALT_PRESSED = 0x0001  # the right alt key is pressed.
LEFT_ALT_PRESSED = 0x0002  # the left alt key is pressed.
RIGHT_CTRL_PRESSED = 0x0004  # the right ctrl key is pressed.
LEFT_CTRL_PRESSED = 0x0008  # the left ctrl key is pressed.
SHIFT_PRESSED = 0x0010  # the shift key is pressed.
NUMLOCK_ON = 0x0020  # the numlock light is on.
SCROLLLOCK_ON = 0x0040  # the scrolllock light is on.
CAPSLOCK_ON = 0x0080  # the capslock light is on.
ENHANCED_KEY = 0x0100  # the key is enhanced.
NLS_DBCSCHAR = 0x00010000  # DBCS for JPN: SBCS/DBCS mode.
NLS_ALPHANUMERIC = 0x00000000  # DBCS for JPN: Alphanumeric mode.
NLS_KATAKANA = 0x00020000  # DBCS for JPN: Katakana mode.
NLS_HIRAGANA = 0x00040000  # DBCS for JPN: Hiragana mode.
NLS_ROMAN = 0x00400000  # DBCS for JPN: Roman/Noroman mode.
NLS_IME_CONVERSION = 0x00800000  # DBCS for JPN: IME conversion.
ALTNUMPAD_BIT = 0x04000000  # AltNumpad OEM char (copied from ntuser\inc\kbd.h) ;internal_NT
NLS_IME_DISABLE = 0x20000000  # DBCS for JPN: IME enable/disable.


class MOUSE_EVENT_RECORD(Structure):
    _fields_ = [
        ("dwMousePosition", COORD),
        ("dwButtonState", DWORD),
        ("dwControlKeyState", DWORD),
        ("dwEventFlags", DWORD),
    ]


FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001
RIGHTMOST_BUTTON_PRESSED = 0x0002
FROM_LEFT_2ND_BUTTON_PRESSED = 0x0004
FROM_LEFT_3RD_BUTTON_PRESSED = 0x0008
FROM_LEFT_4TH_BUTTON_PRESSED = 0x0010

MOUSE_MOVED = 0x0001
DOUBLE_CLICK = 0x0002
MOUSE_WHEELED = 0x0004
MOUSE_HWHEELED = 0x0008


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    _fields_ = [
        ("dwSize", COORD),
    ]


class MENU_EVENT_RECORD(Structure):
    _fields_ = [
        ("dwCommandId", UINT),
    ]


class FOCUS_EVENT_RECORD(Structure):
    _fields_ = [
        ("bSetFocus", BOOL),
    ]


class INPUT_RECORD_UNION(Union):
    _fields_ = [
        ("KeyEvent", KEY_EVENT_RECORD),
        ("MouseEvent", MOUSE_EVENT_RECORD),
        ("WindowBufferSizeEvent", WINDOW_BUFFER_SIZE_RECORD),
        ("MenuEvent", MENU_EVENT_RECORD),
        ("FocusEvent", FOCUS_EVENT_RECORD),
    ]


class INPUT_RECORD(Structure):
    _fields_ = [
        ("EventType", WORD),
        ("Event", INPUT_RECORD_UNION),
        ("bSetFocus", BOOL),
        ("bSetFocus", BOOL),
        ("bSetFocus", BOOL),
        ("bSetFocus", BOOL),
    ]


PINPUT_RECORD = POINTER(INPUT_RECORD)

KEY_EVENT = 0x0001  # Event contains key event record
MOUSE_EVENT = 0x0002  # Event contains mouse event record
WINDOW_BUFFER_SIZE_EVENT = 0x0004  # Event contains window change event record
MENU_EVENT = 0x0008  # Event contains menu event record
FOCUS_EVENT = 0x0010  # event contains focus change


class CHAR_INFO_UNION(Union):
    _fields_ = [
        ("UnicodeChar", WCHAR),
        ("AsciiChar", CHAR),
    ]


class CHAR_INFO(Structure):
    _fields_ = [
        ("Char", CHAR_INFO_UNION),
        ("Attributes", WORD),
    ]


class CONSOLE_FONT_INFO(Structure):
    _fields_ = [
        ("nFont", DWORD),
        ("dwFontSize", COORD),
    ]


PCONSOLE_FONT_INFO = POINTER(CONSOLE_FONT_INFO)

HPCON = c_void_p
