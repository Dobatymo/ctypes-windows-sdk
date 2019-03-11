from __future__ import absolute_import, division, print_function, unicode_literals

from enum import IntEnum

class SECURITY_IMPERSONATION_LEVEL(IntEnum):
	SecurityAnonymous = 0
	SecurityIdentification = 1
	SecurityImpersonation = 2
	SecurityDelegation = 3
