from ctypes import POINTER, Structure, c_int
from ctypes.wintypes import BOOL, BYTE, DWORD, HANDLE, LONG, LPCSTR, LPCWSTR, LPVOID, UINT, WORD

from .. import windll

HDC = HANDLE
HGDIOBJ = HANDLE
HBITMAP = HANDLE

DIB_RGB_COLORS = 0
HORZRES = 8
VERTRES = 10
SRCCOPY = 0x00CC0020
CAPTUREBLT = 0x40000000

from warnings import warn

warn("Don't use last parameter of `CreateDCA` or `CreateDCW`, as `DEVMODEA` and `DEVMODEW` are not defined correctly.")
DEVMODEA = c_int
DEVMODEW = c_int


class RGBQUAD(Structure):
    _fields_ = [
        ("rgbBlue", BYTE),
        ("rgbGreen", BYTE),
        ("rgbRed", BYTE),
        ("rgbReserved", BYTE),
    ]


class BITMAPCOREHEADER(Structure):
    _fields_ = [
        ("bcSize", DWORD),
        ("bcWidth", WORD),
        ("bcHeight", WORD),
        ("bcPlanes", WORD),
        ("bcBitCount", WORD),
    ]


class BITMAPINFOHEADER(Structure):
    _fields_ = [
        ("biSize", DWORD),
        ("biWidth", LONG),
        ("biHeight", LONG),
        ("biPlanes", WORD),
        ("biBitCount", WORD),
        ("biCompression", DWORD),
        ("biSizeImage", DWORD),
        ("biXPelsPerMeter", LONG),
        ("biYPelsPerMeter", LONG),
        ("biClrUsed", DWORD),
        ("biClrImportant", DWORD),
    ]


class BITMAPINFO(Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", RGBQUAD * 1),
    ]


# functions

BitBlt = windll.Gdi32.BitBlt
BitBlt.argtypes = [HDC, c_int, c_int, c_int, c_int, HDC, c_int, c_int, DWORD]
BitBlt.restype = BOOL

CreateCompatibleBitmap = windll.Gdi32.CreateCompatibleBitmap
CreateCompatibleBitmap.argtypes = [HDC, c_int, c_int]
CreateCompatibleBitmap.restype = HBITMAP

CreateCompatibleDC = windll.Gdi32.CreateCompatibleDC
CreateCompatibleDC.argtypes = [HDC]
CreateCompatibleDC.restype = HDC

CreateDCA = windll.Gdi32.CreateDCA
CreateDCA.argtypes = [LPCSTR, LPCSTR, LPCSTR, POINTER(DEVMODEA)]
CreateDCA.restype = HDC

CreateDCW = windll.Gdi32.CreateDCW
CreateDCW.argtypes = [LPCWSTR, LPCWSTR, LPCWSTR, POINTER(DEVMODEW)]
CreateDCW.restype = HDC

DeleteDC = windll.Gdi32.DeleteDC
DeleteDC.argtypes = [HDC]
DeleteDC.restype = BOOL

DeleteObject = windll.Gdi32.DeleteObject
DeleteObject.argtypes = [HGDIOBJ]
DeleteObject.restype = BOOL

GetDeviceCaps = windll.Gdi32.GetDeviceCaps
GetDeviceCaps.argtypes = [HDC, c_int]
GetDeviceCaps.restype = c_int

GetDIBits = windll.Gdi32.GetDIBits
GetDIBits.argtypes = [HDC, HBITMAP, UINT, UINT, LPVOID, POINTER(BITMAPINFO), UINT]
GetDIBits.restype = c_int

SelectObject = windll.Gdi32.SelectObject
SelectObject.argtypes = [HDC, HGDIOBJ]
SelectObject.restype = HGDIOBJ
