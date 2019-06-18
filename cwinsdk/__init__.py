from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import c_int, LibraryLoader, WinDLL

windll = LibraryLoader(WinDLL)

class CEnum(c_int):
	pass
