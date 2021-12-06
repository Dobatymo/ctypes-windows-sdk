from ctypes import CFUNCTYPE, POINTER, Structure
from ctypes.wintypes import BOOL, DWORD, HANDLE, LPVOID, UINT, ULONG

from .. import nonzero, windll
from ..shared.minwindef import LPDWORD
from ..shared.ntdef import HRESULT
from .wincontypes import COORD, HPCON, PINPUT_RECORD

# defines

ATTACH_PARENT_PROCESS = DWORD(-1)

ENABLE_PROCESSED_INPUT = 0x0001
ENABLE_LINE_INPUT = 0x0002
ENABLE_ECHO_INPUT = 0x0004
ENABLE_WINDOW_INPUT = 0x0008
ENABLE_MOUSE_INPUT = 0x0010
ENABLE_INSERT_MODE = 0x0020
ENABLE_QUICK_EDIT_MODE = 0x0040
ENABLE_EXTENDED_FLAGS = 0x0080
ENABLE_AUTO_POSITION = 0x0100
ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200

ENABLE_PROCESSED_OUTPUT = 0x0001
ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
DISABLE_NEWLINE_AUTO_RETURN = 0x0008
ENABLE_LVB_GRID_WORLDWIDE = 0x0010

CTRL_C_EVENT = 0
CTRL_BREAK_EVENT = 1
CTRL_CLOSE_EVENT = 2
CTRL_LOGOFF_EVENT = 5
CTRL_SHUTDOWN_EVENT = 6

PSEUDOCONSOLE_INHERIT_CURSOR = 0x1

# structs


class CONSOLE_READCONSOLE_CONTROL(Structure):
    _fields_ = [
        ("nLength", ULONG),
        ("nInitialChars", ULONG),
        ("dwCtrlWakeupMask", ULONG),
        ("dwControlKeyState", ULONG),
    ]


PCONSOLE_READCONSOLE_CONTROL = POINTER(CONSOLE_READCONSOLE_CONTROL)

# typedef

PHANDLER_ROUTINE = CFUNCTYPE(BOOL, DWORD)

# functions

AllocConsole = windll.kernel32.AllocConsole
AllocConsole.argtypes = []
AllocConsole.restype = BOOL

FreeConsole = windll.kernel32.FreeConsole
FreeConsole.argtypes = []
FreeConsole.restype = BOOL

AttachConsole = windll.kernel32.AttachConsole
AttachConsole.argtypes = [DWORD]
AttachConsole.restype = BOOL

GetConsoleCP = windll.kernel32.GetConsoleCP
GetConsoleCP.argtypes = []
GetConsoleCP.restype = UINT

GetConsoleOutputCP = windll.kernel32.GetConsoleOutputCP
GetConsoleOutputCP.argtypes = []
GetConsoleOutputCP.restype = UINT

GetConsoleMode = windll.kernel32.GetConsoleOutputCP
GetConsoleMode.argtypes = [HANDLE, LPDWORD]
GetConsoleMode.restype = BOOL
GetConsoleMode.errcheck = nonzero

SetConsoleMode = windll.kernel32.SetConsoleMode
SetConsoleMode.argtypes = [HANDLE, DWORD]
SetConsoleMode.restype = BOOL
SetConsoleMode.errcheck = nonzero

GetNumberOfConsoleInputEvents = windll.kernel32.GetNumberOfConsoleInputEvents
GetNumberOfConsoleInputEvents.argtypes = [HANDLE, LPDWORD]
GetNumberOfConsoleInputEvents.restype = BOOL

ReadConsoleInputA = windll.kernel32.ReadConsoleInputA
ReadConsoleInputA.argtypes = [HANDLE, PINPUT_RECORD, DWORD, LPDWORD]
ReadConsoleInputA.restype = BOOL

ReadConsoleInputW = windll.kernel32.ReadConsoleInputW
ReadConsoleInputW.argtypes = [HANDLE, PINPUT_RECORD, DWORD, LPDWORD]
ReadConsoleInputW.restype = BOOL

PeekConsoleInputA = windll.kernel32.PeekConsoleInputA
PeekConsoleInputA.argtypes = [HANDLE, PINPUT_RECORD, DWORD, LPDWORD]
PeekConsoleInputA.restype = BOOL

PeekConsoleInputW = windll.kernel32.PeekConsoleInputW
PeekConsoleInputW.argtypes = [HANDLE, PINPUT_RECORD, DWORD, LPDWORD]
PeekConsoleInputW.restype = BOOL

ReadConsoleA = windll.kernel32.ReadConsoleA
ReadConsoleA.argtypes = [HANDLE, LPVOID, DWORD, LPDWORD, PCONSOLE_READCONSOLE_CONTROL]
ReadConsoleA.restype = BOOL

ReadConsoleW = windll.kernel32.ReadConsoleW
ReadConsoleW.argtypes = [HANDLE, LPVOID, DWORD, LPDWORD, PCONSOLE_READCONSOLE_CONTROL]
ReadConsoleW.restype = BOOL

WriteConsoleA = windll.kernel32.WriteConsoleA
WriteConsoleA.argtypes = [HANDLE, LPVOID, DWORD, LPDWORD, LPVOID]  # const
WriteConsoleA.restype = BOOL

WriteConsoleW = windll.kernel32.WriteConsoleW
WriteConsoleW.argtypes = [HANDLE, LPVOID, DWORD, LPDWORD, LPVOID]  # const
WriteConsoleW.restype = BOOL

SetConsoleCtrlHandler = windll.kernel32.SetConsoleCtrlHandler
SetConsoleCtrlHandler.argtypes = [PHANDLER_ROUTINE, BOOL]
SetConsoleCtrlHandler.restype = BOOL

try:  # Windows 10 1809
    CreatePseudoConsole = windll.kernel32.CreatePseudoConsole
    CreatePseudoConsole.argtypes = [COORD, HANDLE, HANDLE, DWORD, POINTER(HPCON)]
    CreatePseudoConsole.restype = HRESULT

    ResizePseudoConsole = windll.kernel32.ResizePseudoConsole
    ResizePseudoConsole.argtypes = [HPCON, COORD]
    ResizePseudoConsole.restype = HRESULT

    ClosePseudoConsole = windll.kernel32.ClosePseudoConsole
    ClosePseudoConsole.argtypes = [HPCON]
    ClosePseudoConsole.restype = None

except AttributeError:
    pass
