from __future__ import absolute_import, division, print_function, unicode_literals

from enum import IntEnum

class EXCEPTION_DISPOSITION(IntEnum):
	ExceptionContinueExecution = 0
	ExceptionContinueSearch = 1
	ExceptionNestedException = 2
	ExceptionCollidedUnwind = 3

EXCEPTION_EXECUTE_HANDLER = 1
EXCEPTION_CONTINUE_SEARCH = 0
EXCEPTION_CONTINUE_EXECUTION = -1
