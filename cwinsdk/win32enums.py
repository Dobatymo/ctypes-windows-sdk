from __future__ import absolute_import, division, print_function, unicode_literals

from enum import IntEnum

class FILE_INFO_BY_HANDLE_CLASS(IntEnum):
	FileBasicInfo = 0
	FileStandardInfo = 1
	FileNameInfo = 2
	FileRenameInfo = 3
	FileDispositionInfo = 4
	FileAllocationInfo = 5
	FileEndOfFileInfo = 6
	FileStreamInfo = 7
	FileCompressionInfo = 8
	FileAttributeTagInfo = 9
	FileIdBothDirectoryInfo = 10
	FileIdBothDirectoryRestartInfo = 11
	FileIoPriorityHintInfo = 12
	FileRemoteProtocolInfo = 13
	FileFullDirectoryInfo = 14
	FileFullDirectoryRestartInfo = 15
	FileStorageInfo = 16
	FileAlignmentInfo = 17
	FileIdInfo = 18
	FileIdExtdDirectoryInfo = 19
	FileIdExtdDirectoryRestartInfo = 20
	MaximumFileInfoByHandlesClass = 21
