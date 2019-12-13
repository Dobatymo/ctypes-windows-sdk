from __future__ import absolute_import, division, print_function, unicode_literals

import platform
from ctypes import c_int, LibraryLoader, WinDLL, WinError
from ctypes.wintypes import HANDLE

windll = LibraryLoader(WinDLL)

INVALID_HANDLE_VALUE = HANDLE(-1).value # copied from cwinsdk.um.handleapi to prevent cyclic imports
S_OK = 0 # copied from cwinsdk.shared.winerror

class CEnum(c_int):
	pass

class WinApiError(OSError):
	pass

def _struct2pairs(struct):

	for name, _ in struct._fields_:
		value = getattr(struct, name)

		if hasattr(value, "_fields_"):
			value = dict(_struct2pairs(value))
		elif hasattr(value, "_length_"):
			value = list(value)
		elif hasattr(value, "value"):
			value = value.value

		yield name, value

def struct2dict(struct):
	return dict(_struct2pairs(struct))

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

def _not_available(funcname):
	# type: (str) -> None

	def inner(*args, **kwargs):
		raise OSError("{}() is not available on {}".format(funcname, platform.platform()))

	return inner
