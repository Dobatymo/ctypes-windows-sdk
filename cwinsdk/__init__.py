from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import c_int, LibraryLoader, WinDLL, WinError
from ctypes.wintypes import HANDLE

windll = LibraryLoader(WinDLL)

INVALID_HANDLE_VALUE = HANDLE(-1).value # copied from cwinsdk.um.handleapi to prevent cyclic imports
S_OK = 0 # copied from cwinsdk.shared.winerror

class CEnum(c_int):
	pass

class WinApiError(OSError):
	pass

def nonzero(result, func, arguments):
	if result == 0:
		raise WinError()

	return result

def validhandle(result, func, arguments):
	if result == INVALID_HANDLE_VALUE:
		raise WinError()

	return result

def s_ok(result, func, arguments):
	if result != S_OK:
		raise WinError(result) # no error code set in windows

	return result
