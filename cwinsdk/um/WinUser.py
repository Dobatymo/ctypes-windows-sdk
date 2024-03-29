from ctypes import c_int
from ctypes.wintypes import BOOL, DWORD, UINT

from .. import windll

# constants

SB_HORZ = 0
SB_VERT = 1
SB_CTL = 2
SB_BOTH = 3

SB_LINEUP = 0
SB_LINELEFT = 0
SB_LINEDOWN = 1
SB_LINERIGHT = 1
SB_PAGEUP = 2
SB_PAGELEFT = 2
SB_PAGEDOWN = 3
SB_PAGERIGHT = 3
SB_THUMBPOSITION = 4
SB_THUMBTRACK = 5
SB_TOP = 6
SB_LEFT = 6
SB_BOTTOM = 7
SB_RIGHT = 7
SB_ENDSCROLL = 8

SW_HIDE = 0
SW_SHOWNORMAL = 1
SW_NORMAL = 1
SW_SHOWMINIMIZED = 2
SW_SHOWMAXIMIZED = 3
SW_MAXIMIZE = 3
SW_SHOWNOACTIVATE = 4
SW_SHOW = 5
SW_MINIMIZE = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_RESTORE = 9
SW_SHOWDEFAULT = 10
SW_FORCEMINIMIZE = 11
SW_MAX = 11

HIDE_WINDOW = 0
SHOW_OPENWINDOW = 1
SHOW_ICONWINDOW = 2
SHOW_FULLSCREEN = 3
SHOW_OPENNOACTIVATE = 4

SW_PARENTCLOSING = 1
SW_OTHERZOOM = 2
SW_PARENTOPENING = 3
SW_OTHERUNZOOM = 4

AW_HOR_POSITIVE = 0x00000001
AW_HOR_NEGATIVE = 0x00000002
AW_VER_POSITIVE = 0x00000004
AW_VER_NEGATIVE = 0x00000008
AW_CENTER = 0x00000010
AW_HIDE = 0x00010000
AW_ACTIVATE = 0x00020000
AW_SLIDE = 0x00040000
AW_BLEND = 0x00080000

KF_EXTENDED = 0x0100
KF_DLGMODE = 0x0800
KF_MENUMODE = 0x1000
KF_ALTDOWN = 0x2000
KF_REPEAT = 0x4000
KF_UP = 0x8000

VK_LBUTTON = 0x01
VK_RBUTTON = 0x02
VK_CANCEL = 0x03
VK_MBUTTON = 0x04

VK_XBUTTON1 = 0x05
VK_XBUTTON2 = 0x06
VK_BACK = 0x08
VK_TAB = 0x09
VK_CLEAR = 0x0C
VK_RETURN = 0x0D
VK_SHIFT = 0x10
VK_CONTROL = 0x11
VK_MENU = 0x12
VK_PAUSE = 0x13
VK_CAPITAL = 0x14
VK_KANA = 0x15
VK_HANGEUL = 0x15
VK_HANGUL = 0x15
VK_JUNJA = 0x17
VK_FINAL = 0x18
VK_HANJA = 0x19
VK_KANJI = 0x19
VK_ESCAPE = 0x1B
VK_CONVERT = 0x1C
VK_NONCONVERT = 0x1D
VK_ACCEPT = 0x1E
VK_MODECHANGE = 0x1F
VK_SPACE = 0x20
VK_PRIOR = 0x21
VK_NEXT = 0x22
VK_END = 0x23
VK_HOME = 0x24
VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_SELECT = 0x29
VK_PRINT = 0x2A
VK_EXECUTE = 0x2B
VK_SNAPSHOT = 0x2C
VK_INSERT = 0x2D
VK_DELETE = 0x2E
VK_HELP = 0x2F
VK_LWIN = 0x5B
VK_RWIN = 0x5C
VK_APPS = 0x5D
VK_SLEEP = 0x5F
VK_NUMPAD0 = 0x60
VK_NUMPAD1 = 0x61
VK_NUMPAD2 = 0x62
VK_NUMPAD3 = 0x63
VK_NUMPAD4 = 0x64
VK_NUMPAD5 = 0x65
VK_NUMPAD6 = 0x66
VK_NUMPAD7 = 0x67
VK_NUMPAD8 = 0x68
VK_NUMPAD9 = 0x69
VK_MULTIPLY = 0x6A
VK_ADD = 0x6B
VK_SEPARATOR = 0x6C
VK_SUBTRACT = 0x6D
VK_DECIMAL = 0x6E
VK_DIVIDE = 0x6F
VK_F1 = 0x70
VK_F2 = 0x71
VK_F3 = 0x72
VK_F4 = 0x73
VK_F5 = 0x74
VK_F6 = 0x75
VK_F7 = 0x76
VK_F8 = 0x77
VK_F9 = 0x78
VK_F10 = 0x79
VK_F11 = 0x7A
VK_F12 = 0x7B
VK_F13 = 0x7C
VK_F14 = 0x7D
VK_F15 = 0x7E
VK_F16 = 0x7F
VK_F17 = 0x80
VK_F18 = 0x81
VK_F19 = 0x82
VK_F20 = 0x83
VK_F21 = 0x84
VK_F22 = 0x85
VK_F23 = 0x86
VK_F24 = 0x87
VK_NAVIGATION_VIEW = 0x88
VK_NAVIGATION_MENU = 0x89
VK_NAVIGATION_UP = 0x8A
VK_NAVIGATION_DOWN = 0x8B
VK_NAVIGATION_LEFT = 0x8C
VK_NAVIGATION_RIGHT = 0x8D
VK_NAVIGATION_ACCEPT = 0x8E
VK_NAVIGATION_CANCEL = 0x8F
VK_NUMLOCK = 0x90
VK_SCROLL = 0x91
VK_OEM_NEC_EQUAL = 0x92
VK_OEM_FJ_JISHO = 0x92
VK_OEM_FJ_MASSHOU = 0x93
VK_OEM_FJ_TOUROKU = 0x94
VK_OEM_FJ_LOYA = 0x95
VK_OEM_FJ_ROYA = 0x96
VK_LSHIFT = 0xA0
VK_RSHIFT = 0xA1
VK_LCONTROL = 0xA2
VK_RCONTROL = 0xA3
VK_LMENU = 0xA4
VK_RMENU = 0xA5
VK_BROWSER_BACK = 0xA6
VK_BROWSER_FORWARD = 0xA7
VK_BROWSER_REFRESH = 0xA8
VK_BROWSER_STOP = 0xA9
VK_BROWSER_SEARCH = 0xAA
VK_BROWSER_FAVORITES = 0xAB
VK_BROWSER_HOME = 0xAC

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_STOP = 0xB2
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_LAUNCH_MAIL = 0xB4
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_LAUNCH_APP1 = 0xB6
VK_LAUNCH_APP2 = 0xB7
VK_OEM_1 = 0xBA
VK_OEM_PLUS = 0xBB
VK_OEM_COMMA = 0xBC
VK_OEM_MINUS = 0xBD
VK_OEM_PERIOD = 0xBE
VK_OEM_2 = 0xBF
VK_OEM_3 = 0xC0
VK_GAMEPAD_A = 0xC3
VK_GAMEPAD_B = 0xC4
VK_GAMEPAD_X = 0xC5
VK_GAMEPAD_Y = 0xC6
VK_GAMEPAD_RIGHT_SHOULDER = 0xC7
VK_GAMEPAD_LEFT_SHOULDER = 0xC8
VK_GAMEPAD_LEFT_TRIGGER = 0xC9
VK_GAMEPAD_RIGHT_TRIGGER = 0xCA
VK_GAMEPAD_DPAD_UP = 0xCB
VK_GAMEPAD_DPAD_DOWN = 0xCC
VK_GAMEPAD_DPAD_LEFT = 0xCD
VK_GAMEPAD_DPAD_RIGHT = 0xCE
VK_GAMEPAD_MENU = 0xCF
VK_GAMEPAD_VIEW = 0xD0
VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON = 0xD1
VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 0xD2
VK_GAMEPAD_LEFT_THUMBSTICK_UP = 0xD3
VK_GAMEPAD_LEFT_THUMBSTICK_DOWN = 0xD4
VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT = 0xD5
VK_GAMEPAD_LEFT_THUMBSTICK_LEFT = 0xD6
VK_GAMEPAD_RIGHT_THUMBSTICK_UP = 0xD7
VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN = 0xD8
VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT = 0xD9
VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT = 0xDA
VK_OEM_4 = 0xDB
VK_OEM_5 = 0xDC
VK_OEM_6 = 0xDD
VK_OEM_7 = 0xDE
VK_OEM_8 = 0xDF
VK_OEM_AX = 0xE1
VK_OEM_102 = 0xE2
VK_ICO_HELP = 0xE3
VK_ICO_00 = 0xE4
VK_PROCESSKEY = 0xE5
VK_ICO_CLEAR = 0xE6
VK_PACKET = 0xE7
VK_OEM_RESET = 0xE9
VK_OEM_JUMP = 0xEA
VK_OEM_PA1 = 0xEB
VK_OEM_PA2 = 0xEC
VK_OEM_PA3 = 0xED
VK_OEM_WSCTRL = 0xEE
VK_OEM_CUSEL = 0xEF
VK_OEM_ATTN = 0xF0
VK_OEM_FINISH = 0xF1
VK_OEM_COPY = 0xF2
VK_OEM_AUTO = 0xF3
VK_OEM_ENLW = 0xF4
VK_OEM_BACKTAB = 0xF5
VK_ATTN = 0xF6
VK_CRSEL = 0xF7
VK_EXSEL = 0xF8
VK_EREOF = 0xF9
VK_PLAY = 0xFA
VK_ZOOM = 0xFB
VK_NONAME = 0xFC
VK_PA1 = 0xFD
VK_OEM_CLEAR = 0xFE

WH_MIN = -1
WH_MSGFILTER = -1
WH_JOURNALRECORD = 0
WH_JOURNALPLAYBACK = 1
WH_KEYBOARD = 2
WH_GETMESSAGE = 3
WH_CALLWNDPROC = 4
WH_CBT = 5
WH_SYSMSGFILTER = 6
WH_MOUSE = 7
WH_HARDWARE = 8
WH_DEBUG = 9
WH_SHELL = 10
WH_FOREGROUNDIDLE = 11
WH_CALLWNDPROCRET = 12
WH_KEYBOARD_LL = 13
WH_MOUSE_LL = 14

WH_MAX = 14

WH_MINHOOK = WH_MIN
WH_MAXHOOK = WH_MAX

HC_ACTION = 0
HC_GETNEXT = 1
HC_SKIP = 2
HC_NOREMOVE = 3
HC_NOREM = HC_NOREMOVE
HC_SYSMODALON = 4
HC_SYSMODALOFF = 5

HCBT_MOVESIZE = 0
HCBT_MINMAX = 1
HCBT_QS = 2
HCBT_CREATEWND = 3
HCBT_DESTROYWND = 4
HCBT_ACTIVATE = 5
HCBT_CLICKSKIPPED = 6
HCBT_KEYSKIPPED = 7
HCBT_SYSCOMMAND = 8
HCBT_SETFOCUS = 9

WTS_CONSOLE_CONNECT = 0x1
WTS_CONSOLE_DISCONNECT = 0x2
WTS_REMOTE_CONNECT = 0x3
WTS_REMOTE_DISCONNECT = 0x4
WTS_SESSION_LOGON = 0x5
WTS_SESSION_LOGOFF = 0x6
WTS_SESSION_LOCK = 0x7
WTS_SESSION_UNLOCK = 0x8
WTS_SESSION_REMOTE_CONTROL = 0x9
WTS_SESSION_CREATE = 0xA
WTS_SESSION_TERMINATE = 0xB

MSGF_DIALOGBOX = 0
MSGF_MESSAGEBOX = 1
MSGF_MENU = 2
MSGF_SCROLLBAR = 5
MSGF_NEXTWINDOW = 6
MSGF_MAX = 8
MSGF_USER = 4096

HSHELL_WINDOWCREATED = 1
HSHELL_WINDOWDESTROYED = 2
HSHELL_ACTIVATESHELLWINDOW = 3

HSHELL_WINDOWACTIVATED = 4
HSHELL_GETMINRECT = 5
HSHELL_REDRAW = 6
HSHELL_TASKMAN = 7
HSHELL_LANGUAGE = 8
HSHELL_SYSMENU = 9
HSHELL_ENDTASK = 10
HSHELL_ACCESSIBILITYSTATE = 11
HSHELL_APPCOMMAND = 12
HSHELL_WINDOWREPLACED = 13
HSHELL_WINDOWREPLACING = 14
HSHELL_MONITORCHANGED = 16

HSHELL_HIGHBIT = 0x8000
HSHELL_FLASH = HSHELL_REDRAW | HSHELL_HIGHBIT
HSHELL_RUDEAPPACTIVATED = HSHELL_WINDOWACTIVATED | HSHELL_HIGHBIT

APPCOMMAND_BROWSER_BACKWARD = 1
APPCOMMAND_BROWSER_FORWARD = 2
APPCOMMAND_BROWSER_REFRESH = 3
APPCOMMAND_BROWSER_STOP = 4
APPCOMMAND_BROWSER_SEARCH = 5
APPCOMMAND_BROWSER_FAVORITES = 6
APPCOMMAND_BROWSER_HOME = 7
APPCOMMAND_VOLUME_MUTE = 8
APPCOMMAND_VOLUME_DOWN = 9
APPCOMMAND_VOLUME_UP = 10
APPCOMMAND_MEDIA_NEXTTRACK = 11
APPCOMMAND_MEDIA_PREVIOUSTRACK = 12
APPCOMMAND_MEDIA_STOP = 13
APPCOMMAND_MEDIA_PLAY_PAUSE = 14
APPCOMMAND_LAUNCH_MAIL = 15
APPCOMMAND_LAUNCH_MEDIA_SELECT = 16
APPCOMMAND_LAUNCH_APP1 = 17
APPCOMMAND_LAUNCH_APP2 = 18
APPCOMMAND_BASS_DOWN = 19
APPCOMMAND_BASS_BOOST = 20
APPCOMMAND_BASS_UP = 21
APPCOMMAND_TREBLE_DOWN = 22
APPCOMMAND_TREBLE_UP = 23
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 24
APPCOMMAND_MICROPHONE_VOLUME_DOWN = 25
APPCOMMAND_MICROPHONE_VOLUME_UP = 26
APPCOMMAND_HELP = 27
APPCOMMAND_FIND = 28
APPCOMMAND_NEW = 29
APPCOMMAND_OPEN = 30
APPCOMMAND_CLOSE = 31
APPCOMMAND_SAVE = 32
APPCOMMAND_PRINT = 33
APPCOMMAND_UNDO = 34
APPCOMMAND_REDO = 35
APPCOMMAND_COPY = 36
APPCOMMAND_CUT = 37
APPCOMMAND_PASTE = 38
APPCOMMAND_REPLY_TO_MAIL = 39
APPCOMMAND_FORWARD_MAIL = 40
APPCOMMAND_SEND_MAIL = 41
APPCOMMAND_SPELL_CHECK = 42
APPCOMMAND_DICTATE_OR_COMMAND_CONTROL_TOGGLE = 43
APPCOMMAND_MIC_ON_OFF_TOGGLE = 44
APPCOMMAND_CORRECTION_LIST = 45
APPCOMMAND_MEDIA_PLAY = 46
APPCOMMAND_MEDIA_PAUSE = 47
APPCOMMAND_MEDIA_RECORD = 48
APPCOMMAND_MEDIA_FAST_FORWARD = 49
APPCOMMAND_MEDIA_REWIND = 50
APPCOMMAND_MEDIA_CHANNEL_UP = 51
APPCOMMAND_MEDIA_CHANNEL_DOWN = 52
APPCOMMAND_DELETE = 53
APPCOMMAND_DWM_FLIP3D = 54

FAPPCOMMAND_MOUSE = 0x8000
FAPPCOMMAND_KEY = 0
FAPPCOMMAND_OEM = 0x1000
FAPPCOMMAND_MASK = 0xF000

LLKHF_EXTENDED = KF_EXTENDED >> 8
LLKHF_INJECTED = 0x00000010
LLKHF_ALTDOWN = KF_ALTDOWN >> 8
LLKHF_UP = KF_UP >> 8
LLKHF_LOWER_IL_INJECTED = 0x00000002

LLMHF_INJECTED = 0x00000001
LLMHF_LOWER_IL_INJECTED = 0x00000002

HKL_PREV = 0
HKL_NEXT = 1

KLF_ACTIVATE = 0x00000001
KLF_SUBSTITUTE_OK = 0x00000002
KLF_REORDER = 0x00000008
KLF_REPLACELANG = 0x00000010
KLF_NOTELLSHELL = 0x00000080
KLF_SETFORPROCESS = 0x00000100
KLF_SHIFTLOCK = 0x00010000
KLF_RESET = 0x40000000

INPUTLANGCHANGE_SYSCHARSET = 0x0001
INPUTLANGCHANGE_FORWARD = 0x0002
INPUTLANGCHANGE_BACKWARD = 0x0004

KL_NAMELENGTH = 9

ENDSESSION_CLOSEAPP = 0x00000001
ENDSESSION_CRITICAL = 0x40000000
ENDSESSION_LOGOFF = 0x80000000

EWX_LOGOFF = 0x00000000
EWX_SHUTDOWN = 0x00000001
EWX_REBOOT = 0x00000002
EWX_FORCE = 0x00000004
EWX_POWEROFF = 0x00000008
EWX_FORCEIFHUNG = 0x00000010
EWX_QUICKRESOLVE = 0x00000020
EWX_RESTARTAPPS = 0x00000040
EWX_HYBRID_SHUTDOWN = 0x00400000
EWX_BOOTOPTIONS = 0x01000000

SM_CXSCREEN = 0
SM_CYSCREEN = 1
SM_CXVSCROLL = 2
SM_CYHSCROLL = 3
SM_CYCAPTION = 4
SM_CXBORDER = 5
SM_CYBORDER = 6
SM_CXDLGFRAME = 7
SM_CYDLGFRAME = 8
SM_CYVTHUMB = 9
SM_CXHTHUMB = 10
SM_CXICON = 11
SM_CYICON = 12
SM_CXCURSOR = 13
SM_CYCURSOR = 14
SM_CYMENU = 15
SM_CXFULLSCREEN = 16
SM_CYFULLSCREEN = 17
SM_CYKANJIWINDOW = 18
SM_MOUSEPRESENT = 19
SM_CYVSCROLL = 20
SM_CXHSCROLL = 21
SM_DEBUG = 22
SM_SWAPBUTTON = 23
SM_RESERVED1 = 24
SM_RESERVED2 = 25
SM_RESERVED3 = 26
SM_RESERVED4 = 27
SM_CXMIN = 28
SM_CYMIN = 29
SM_CXSIZE = 30
SM_CYSIZE = 31
SM_CXFRAME = 32
SM_CYFRAME = 33
SM_CXMINTRACK = 34
SM_CYMINTRACK = 35
SM_CXDOUBLECLK = 36
SM_CYDOUBLECLK = 37
SM_CXICONSPACING = 38
SM_CYICONSPACING = 39
SM_MENUDROPALIGNMENT = 40
SM_PENWINDOWS = 41
SM_DBCSENABLED = 42
SM_CMOUSEBUTTONS = 43
SM_CXFIXEDFRAME = SM_CXDLGFRAME
SM_CYFIXEDFRAME = SM_CYDLGFRAME
SM_CXSIZEFRAME = SM_CXFRAME
SM_CYSIZEFRAME = SM_CYFRAME
SM_SECURE = 44
SM_CXEDGE = 45
SM_CYEDGE = 46
SM_CXMINSPACING = 47
SM_CYMINSPACING = 48
SM_CXSMICON = 49
SM_CYSMICON = 50
SM_CYSMCAPTION = 51
SM_CXSMSIZE = 52
SM_CYSMSIZE = 53
SM_CXMENUSIZE = 54
SM_CYMENUSIZE = 55
SM_ARRANGE = 56
SM_CXMINIMIZED = 57
SM_CYMINIMIZED = 58
SM_CXMAXTRACK = 59
SM_CYMAXTRACK = 60
SM_CXMAXIMIZED = 61
SM_CYMAXIMIZED = 62
SM_NETWORK = 63
SM_CLEANBOOT = 67
SM_CXDRAG = 68
SM_CYDRAG = 69
SM_SHOWSOUNDS = 70
SM_CXMENUCHECK = 71
SM_CYMENUCHECK = 72
SM_SLOWMACHINE = 73
SM_MIDEASTENABLED = 74
SM_MOUSEWHEELPRESENT = 75
SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79
SM_CMONITORS = 80
SM_SAMEDISPLAYFORMAT = 81
SM_IMMENABLED = 82
SM_CXFOCUSBORDER = 83
SM_CYFOCUSBORDER = 84
SM_TABLETPC = 86
SM_MEDIACENTER = 87
SM_STARTER = 88
SM_SERVERR2 = 89
SM_MOUSEHORIZONTALWHEELPRESENT = 91
SM_CXPADDEDBORDER = 92
SM_DIGITIZER = 94
SM_MAXIMUMTOUCHES = 95
SM_CMETRICS = 97

SM_REMOTESESSION = 0x1000
SM_SHUTTINGDOWN = 0x2000
SM_REMOTECONTROL = 0x2001
SM_CARETBLINKINGENABLED = 0x2002
SM_CONVERTIBLESLATEMODE = 0x2003
SM_SYSTEMDOCKED = 0x2004

# functions

GetSystemMetrics = windll.user32.GetSystemMetrics
GetSystemMetrics.argtypes = [c_int]
GetSystemMetrics.restype = c_int

ExitWindowsEx = windll.user32.ExitWindowsEx
ExitWindowsEx.argtypes = [UINT, DWORD]
ExitWindowsEx.restype = BOOL
