from ctypes import POINTER, Structure, Union, sizeof
from ctypes.wintypes import LARGE_INTEGER, ULONG, USHORT

from cwinsdk import DECLSPEC_ALIGN, CEnum, make_struct, make_union
from cwinsdk.shared.ntdef import ANYSIZE_ARRAY, UCHAR, ULONGLONG

_pack_ = 0
"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    scsi.h

Abstract:

    These are the structures and defines that are used in the
    SCSI port and class drivers.

Authors:

Revision History:

--"""


# ifndef _NTSCSI_
# define _NTSCSI_

# include <winapifamily.h>

# pragma region Desktop Family or Storage Package
# if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE)

# ifndef _NTSCSI_USER_MODE_
# ifndef _NTSRB_

# ifndef _MINIPORT_
# ifndef _NTDDK_

# For user-mode application development, make sure to add the line "#define _NTSCSI_USER_MODE_" prior to "#include <scsi.h>"
# For example,
#   #define _NTSCSI_USER_MODE_
#   #include <scsi.h>
#   #undef _NTSCSI_USER_MODE_
# Also see the SPTI sample (located in src\storage\tools\spti directory under the Windows Kits root directory)
# error "For user-mode application development, make sure to #define _NTSCSI_USER_MODE_ prior to #include <scsi.h>"

# endif # !defined _NTDDK_
# endif # !defined _MINIPORT_

# include "srb.h"

# endif # !defined _NTSRB_
# endif # !defined _NTSCSI_USER_MODE_

# pragma warning(push)
# pragma warning(disable:4200) # array[0] is not a warning for this file
# pragma warning(disable:4201) # nonstandard extension used : nameless struct/union
# pragma warning(disable:4214) # nonstandard extension used : bit field types other than int

# pragma pack(push, _scsi_)

# begin_ntminitape

# begin_storport begin_storportp

# Calculate the byte offset of a field in a structure of type type.

# ifndef FIELD_OFFSET
# define FIELD_OFFSET(type, field)    ((LONG)(LONG_PTR)&(((type *)0)->field))
# endif

# Calculate the size of a field in a structure of type type, without
# knowing or stating the type of the field.

# ifndef RTL_FIELD_SIZE
# define RTL_FIELD_SIZE(type, field) (sizeof(((type *)0)->field))
# endif

# Calculate the size of a structure of type type up through and
# including a field.

# ifndef RTL_SIZEOF_THROUGH_FIELD
# define RTL_SIZEOF_THROUGH_FIELD(type, field)     (FIELD_OFFSET(type, field) + RTL_FIELD_SIZE(type, field))
# endif

#  RTL_CONTAINS_FIELD usage:
#      if (RTL_CONTAINS_FIELD(pBlock, pBlock->cbSize, dwMumble)) { # safe to use pBlock->dwMumble

# ifndef RTL_CONTAINS_FIELD
# define RTL_CONTAINS_FIELD(Struct, Size, Field)     ( (((PCHAR)(&(Struct)->Field)) + sizeof((Struct)->Field)) <= (((PCHAR)(Struct))+(Size)) )
# endif

# ifndef RtlZeroMemory
# define RtlZeroMemory(Destination,Length) memset((Destination),0,(Length))
# endif

# Command Descriptor Block. Passed by SCSI controller chip over the SCSI bus

_pack_ += 1


class CDB(Union):
    _pack_ = _pack_
    _fields_ = [
        # Generic 6-Byte CDB
        (
            "CDB6GENERIC",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("Immediate", UCHAR, 1),
                    ("CommandUniqueBits", UCHAR, 4),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("CommandUniqueBytes", UCHAR * 3),
                    ("Link", UCHAR, 1),
                    ("Flag", UCHAR, 1),
                    ("Reserved", UCHAR, 4),
                    ("VendorUnique", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        # Standard 6-byte CDB
        (
            "CDB6READWRITE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x08, 0x0A - SCSIOP_READ, SCSIOP_WRITE
                    ("LogicalBlockMsb1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlockMsb0", UCHAR),
                    ("LogicalBlockLsb", UCHAR),
                    ("TransferBlocks", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # SCSI-1 Inquiry CDB
        (
            "CDB6INQUIRY",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x12 - SCSIOP_INQUIRY
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("PageCode", UCHAR),
                    ("IReserved", UCHAR),
                    ("AllocationLength", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # SCSI-3 Inquiry CDB
        (
            "CDB6INQUIRY3",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x12 - SCSIOP_INQUIRY
                    ("EnableVitalProductData", UCHAR, 1),
                    ("CommandSupportData", UCHAR, 1),
                    ("Reserved1", UCHAR, 6),
                    ("PageCode", UCHAR),
                    ("Reserved2", UCHAR),
                    ("AllocationLength", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "CDB6VERIFY",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x13 - SCSIOP_VERIFY
                    ("Fixed", UCHAR, 1),
                    ("ByteCompare", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved", UCHAR, 2),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("VerificationLength", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "RECEIVE_DIAGNOSTIC",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1C - SCSIOP_RECEIVE_DIAGNOSTIC
                    ("PageCodeValid", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                    ("PageCode", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_DIAGNOSTIC",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1D - SCSIOP_SEND_DIAGNOSTIC
                    ("UnitOffline", UCHAR, 1),
                    ("DeviceOffline", UCHAR, 1),
                    ("SelfTest", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("PageFormat", UCHAR, 1),
                    ("SelfTestCode", UCHAR, 3),
                    ("Reserved2", UCHAR),
                    ("ParameterListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # SCSI Format CDB
        (
            "CDB6FORMAT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x04 - SCSIOP_FORMAT_UNIT
                    ("FormatControl", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("FReserved1", UCHAR),
                    ("InterleaveMsb", UCHAR),
                    ("InterleaveLsb", UCHAR),
                    ("FReserved2", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Standard 10-byte CDB
        (
            "CDB10",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlockByte0", UCHAR),
                    ("LogicalBlockByte1", UCHAR),
                    ("LogicalBlockByte2", UCHAR),
                    ("LogicalBlockByte3", UCHAR),
                    ("Reserved2", UCHAR),
                    ("TransferBlocksMsb", UCHAR),
                    ("TransferBlocksLsb", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Standard 12-byte CDB
        (
            "CDB12",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 4),
                    ("TransferLength", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Standard 16-byte CDB
        (
            "CDB16",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("Reserved1", UCHAR, 3),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("Protection", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 8),
                    ("TransferLength", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Read Buffer(10) command from SPC-5
        (
            "READ_BUFFER_10",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x3c - SCSIOP_READ_DATA_BUFF
                    ("Mode", UCHAR, 5),
                    ("ModeSpecific", UCHAR, 3),
                    ("BufferId", UCHAR),
                    ("BufferOffset", UCHAR * 3),
                    ("AllocationLength", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Read Buffer(16) command from SPC-5
        (
            "READ_BUFFER_16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x9b - SCSIOP_READ_DATA_BUFF16
                    ("Mode", UCHAR, 5),
                    ("ModeSpecific", UCHAR, 3),
                    ("BufferOffset", UCHAR * 8),
                    ("AllocationLength", UCHAR * 4),
                    ("BufferId", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Security-related commands from SPC-4
        (
            "SECURITY_PROTOCOL_IN",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("SecurityProtocol", UCHAR),
                    ("SecurityProtocolSpecific", UCHAR * 2),
                    ("Reserved1", UCHAR, 7),
                    ("INC_512", UCHAR, 1),
                    ("Reserved2", UCHAR),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SECURITY_PROTOCOL_OUT",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("SecurityProtocol", UCHAR),
                    ("SecurityProtocolSpecific", UCHAR * 2),
                    ("Reserved1", UCHAR, 7),
                    ("INC_512", UCHAR, 1),
                    ("Reserved2", UCHAR),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Block Device UNMAP CDB
        (
            "UNMAP",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x42 - SCSIOP_UNMAP
                    ("Anchor", UCHAR, 1),
                    ("Reserved1", UCHAR, 7),
                    ("Reserved2", UCHAR * 4),
                    ("GroupNumber", UCHAR, 5),
                    ("Reserved3", UCHAR, 3),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Block Device SANITIZE CDB (SBC-4)
        (
            "SANITIZE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x48 - SCSIOP_SANITIZE
                    ("ServiceAction", UCHAR, 5),
                    ("AUSE", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved2", UCHAR * 5),
                    ("ParameterListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # CD Rom Audio CDBs
        (
            "PAUSE_RESUME",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x4B - SCSIOP_PAUSE_RESUME
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 6),
                    ("Action", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Read Table of Contents
        (
            "READ_TOC",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x43 - SCSIOP_READ_TOC
                    ("Reserved0", UCHAR, 1),
                    ("Msf", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Format2", UCHAR, 4),
                    ("Reserved2", UCHAR, 4),
                    ("Reserved3", UCHAR * 3),
                    ("StartingTrack", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR, 6),
                    ("Format", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        (
            "READ_DISK_INFORMATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x51 - SCSIOP_READ_DISC_INFORMATION
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 5),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),  # READ_DISC_INFORMATION
        (
            "READ_TRACK_INFORMATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x52 - SCSIOP_READ_TRACK_INFORMATION
                    ("Track", UCHAR, 2),
                    ("Reserved4", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    ("BlockAddress", UCHAR * 4),  # or Track Number
                    ("Reserved3", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "RESERVE_TRACK_RZONE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x53 - SCSIOP_RESERVE_TRACK_RZONE
                    ("Reserved1", UCHAR * 4),
                    ("ReservationSize", UCHAR * 4),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_OPC_INFORMATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x54 - SCSIOP_SEND_OPC_INFORMATION
                    ("DoOpc", UCHAR, 1),  # perform OPC
                    ("Reserved1", UCHAR, 7),
                    ("Exclude0", UCHAR, 1),  # exclude layer 0
                    ("Exclude1", UCHAR, 1),  # exclude layer 1
                    ("Reserved2", UCHAR, 6),
                    ("Reserved3", UCHAR * 4),
                    ("ParameterListLength", UCHAR * 2),
                    ("Reserved4", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REPAIR_TRACK",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x58 - SCSIOP_REPAIR_TRACK
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 7),
                    ("Reserved2", UCHAR * 2),
                    ("TrackNumber", UCHAR * 2),
                    ("Reserved3", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "CLOSE_TRACK",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5B - SCSIOP_CLOSE_TRACK_SESSION
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 7),
                    ("Track", UCHAR, 1),
                    ("Session", UCHAR, 1),
                    ("Reserved2", UCHAR, 6),
                    ("Reserved3", UCHAR),
                    ("TrackNumber", UCHAR * 2),
                    ("Reserved4", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_BUFFER_CAPACITY",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5C - SCSIOP_READ_BUFFER_CAPACITY
                    ("BlockInfo", UCHAR, 1),
                    ("Reserved1", UCHAR, 7),
                    ("Reserved2", UCHAR * 5),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_CUE_SHEET",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5D - SCSIOP_SEND_CUE_SHEET
                    ("Reserved", UCHAR * 5),
                    ("CueSheetSize", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_HEADER",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x44 - SCSIOP_READ_HEADER
                    ("Reserved1", UCHAR, 1),
                    ("Msf", UCHAR, 1),
                    ("Reserved2", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    ("LogicalBlockAddress", UCHAR * 4),
                    ("Reserved3", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PLAY_AUDIO",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x45 - SCSIOP_PLAY_AUDIO
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("StartingBlockAddress", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("PlayLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PLAY_AUDIO_MSF",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x47 - SCSIOP_PLAY_AUDIO_MSF
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR),
                    ("StartingM", UCHAR),
                    ("StartingS", UCHAR),
                    ("StartingF", UCHAR),
                    ("EndingM", UCHAR),
                    ("EndingS", UCHAR),
                    ("EndingF", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "BLANK_MEDIA",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA1 - SCSIOP_BLANK
                    ("BlankType", UCHAR, 3),
                    ("Reserved1", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved2", UCHAR, 3),
                    ("AddressOrTrack", UCHAR * 4),
                    ("Reserved3", UCHAR * 5),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PLAY_CD",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xBC - SCSIOP_PLAY_CD
                    ("Reserved1", UCHAR, 1),
                    ("CMSF", UCHAR, 1),  # LBA = 0, MSF = 1
                    ("ExpectedSectorType", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    (
                        "_unnamed_union",
                        make_union(
                            [
                                (
                                    "LBA",
                                    make_struct(
                                        [
                                            ("StartingBlockAddress", UCHAR * 4),
                                            ("PlayLength", UCHAR * 4),
                                        ],
                                        _pack_,
                                    ),
                                ),
                                (
                                    "MSF",
                                    make_struct(
                                        [
                                            ("Reserved1", UCHAR),
                                            ("StartingM", UCHAR),
                                            ("StartingS", UCHAR),
                                            ("StartingF", UCHAR),
                                            ("EndingM", UCHAR),
                                            ("EndingS", UCHAR),
                                            ("EndingF", UCHAR),
                                            ("Reserved2", UCHAR),
                                        ],
                                        _pack_,
                                    ),
                                ),
                            ],
                            _pack_,
                        ),
                    ),
                    ("Audio", UCHAR, 1),
                    ("Composite", UCHAR, 1),
                    ("Port1", UCHAR, 1),
                    ("Port2", UCHAR, 1),
                    ("Reserved2", UCHAR, 3),
                    ("Speed", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SCAN_CD",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xBA - SCSIOP_SCAN_CD
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("Direct", UCHAR, 1),
                    ("Lun", UCHAR, 3),
                    ("StartingAddress", UCHAR * 4),
                    ("Reserved2", UCHAR * 3),
                    ("Reserved3", UCHAR, 6),
                    ("Type", UCHAR, 2),
                    ("Reserved4", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "STOP_PLAY_SCAN",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x4E - SCSIOP_STOP_PLAY_SCAN
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Read SubChannel Data
        (
            "SUBCHANNEL",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x42 - SCSIOP_READ_SUB_CHANNEL
                    ("Reserved0", UCHAR, 1),
                    ("Msf", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR, 6),
                    ("SubQ", UCHAR, 1),
                    ("Reserved3", UCHAR, 1),
                    ("Format", UCHAR),
                    ("Reserved4", UCHAR * 2),
                    ("TrackNumber", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Read CD. Used by Atapi for raw sector reads.
        (
            "READ_CD",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xBE - SCSIOP_READ_CD
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved0", UCHAR, 1),
                    ("ExpectedSectorType", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    ("StartingLBA", UCHAR * 4),
                    ("TransferBlocks", UCHAR * 3),
                    ("Reserved2", UCHAR, 1),
                    ("ErrorFlags", UCHAR, 2),
                    ("IncludeEDC", UCHAR, 1),
                    ("IncludeUserData", UCHAR, 1),
                    ("HeaderCode", UCHAR, 2),
                    ("IncludeSyncData", UCHAR, 1),
                    ("SubChannelSelection", UCHAR, 3),
                    ("Reserved3", UCHAR, 5),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_CD_MSF",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xB9 - SCSIOP_READ_CD_MSF
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("ExpectedSectorType", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR),
                    ("StartingM", UCHAR),
                    ("StartingS", UCHAR),
                    ("StartingF", UCHAR),
                    ("EndingM", UCHAR),
                    ("EndingS", UCHAR),
                    ("EndingF", UCHAR),
                    ("Reserved4", UCHAR, 1),
                    ("ErrorFlags", UCHAR, 2),
                    ("IncludeEDC", UCHAR, 1),
                    ("IncludeUserData", UCHAR, 1),
                    ("HeaderCode", UCHAR, 2),
                    ("IncludeSyncData", UCHAR, 1),
                    ("SubChannelSelection", UCHAR, 3),
                    ("Reserved5", UCHAR, 5),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Plextor Read CD-DA
        (
            "PLXTR_READ_CDDA",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("Reserved0", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlockByte0", UCHAR),
                    ("LogicalBlockByte1", UCHAR),
                    ("LogicalBlockByte2", UCHAR),
                    ("LogicalBlockByte3", UCHAR),
                    ("TransferBlockByte0", UCHAR),
                    ("TransferBlockByte1", UCHAR),
                    ("TransferBlockByte2", UCHAR),
                    ("TransferBlockByte3", UCHAR),
                    ("SubCode", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # NEC Read CD-DA
        (
            "NEC_READ_CDDA",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("Reserved0", UCHAR),
                    ("LogicalBlockByte0", UCHAR),
                    ("LogicalBlockByte1", UCHAR),
                    ("LogicalBlockByte2", UCHAR),
                    ("LogicalBlockByte3", UCHAR),
                    ("Reserved1", UCHAR),
                    ("TransferBlockByte0", UCHAR),
                    ("TransferBlockByte1", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Mode sense
        # if (NTDDI_VERSION >= NTDDI_WIN8)
        (
            "MODE_SENSE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1A - SCSIOP_MODE_SENSE
                    ("Reserved1", UCHAR, 3),
                    ("Dbd", UCHAR, 1),
                    ("Reserved2", UCHAR, 4),
                    ("PageCode", UCHAR, 6),
                    ("Pc", UCHAR, 2),
                    ("SubPageCode", UCHAR),
                    ("AllocationLength", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "MODE_SENSE10",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5A - SCSIOP_MODE_SENSE10
                    ("Reserved1", UCHAR, 3),
                    ("Dbd", UCHAR, 1),
                    ("LongLBAAccepted", UCHAR, 1),
                    ("Reserved2", UCHAR, 3),
                    ("PageCode", UCHAR, 6),
                    ("Pc", UCHAR, 2),
                    ("SubPageCode", UCHAR),
                    ("Reserved3", UCHAR * 3),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # else
        (
            "MODE_SENSE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1A - SCSIOP_MODE_SENSE
                    ("Reserved1", UCHAR, 3),
                    ("Dbd", UCHAR, 1),
                    ("Reserved2", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("PageCode", UCHAR, 6),
                    ("Pc", UCHAR, 2),
                    ("Reserved3", UCHAR),
                    ("AllocationLength", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "MODE_SENSE10",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5A - SCSIOP_MODE_SENSE10
                    ("Reserved1", UCHAR, 3),
                    ("Dbd", UCHAR, 1),
                    ("Reserved2", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("PageCode", UCHAR, 6),
                    ("Pc", UCHAR, 2),
                    ("Reserved3", UCHAR * 4),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # endif
        # Mode select
        (
            "MODE_SELECT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x15 - SCSIOP_MODE_SELECT
                    ("SPBit", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("PFBit", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 2),
                    ("ParameterListLength", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "MODE_SELECT10",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x55 - SCSIOP_MODE_SELECT10
                    ("SPBit", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("PFBit", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 5),
                    ("ParameterListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "LOCATE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x2B - SCSIOP_LOCATE
                    ("Immediate", UCHAR, 1),
                    ("CPBit", UCHAR, 1),
                    ("BTBit", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved3", UCHAR),
                    ("LogicalBlockAddress", UCHAR * 4),
                    ("Reserved4", UCHAR),
                    ("Partition", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "LOGSENSE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x4D - SCSIOP_LOG_SENSE
                    ("SPBit", UCHAR, 1),
                    ("PPCBit", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("PageCode", UCHAR, 6),
                    ("PCBit", UCHAR, 2),
                    (
                        "_unnamed_union",
                        make_union(
                            [
                                ("SubPageCode", UCHAR),
                                ("Reserved2", UCHAR),
                            ],
                            _pack_,
                        ),
                    ),
                    ("Reserved3", UCHAR),
                    ("ParameterPointer", UCHAR * 2),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "LOGSELECT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x4C - SCSIOP_LOG_SELECT
                    ("SPBit", UCHAR, 1),
                    ("PCRBit", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved", UCHAR, 6),
                    ("PCBit", UCHAR, 2),
                    ("Reserved2", UCHAR * 4),
                    ("ParameterListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PRINT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x0A - SCSIOP_PRINT
                    ("Reserved", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("TransferLength", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEEK",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x2B - SCSIOP_SEEK
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlockAddress", UCHAR * 4),
                    ("Reserved2", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "ERASE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x19 - SCSIOP_ERASE
                    ("Long", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "START_STOP",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1B - SCSIOP_START_STOP_UNIT
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 4),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 2),
                    ("Start", UCHAR, 1),
                    ("LoadEject", UCHAR, 1),
                    ("Reserved3", UCHAR, 6),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "MEDIA_REMOVAL",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x1E - SCSIOP_MEDIUM_REMOVAL
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("Reserved2", UCHAR * 2),
                    ("Prevent", UCHAR, 1),
                    ("Persistant", UCHAR, 1),
                    ("Reserved3", UCHAR, 6),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Tape CDBs
        (
            "SEEK_BLOCK",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x0C - SCSIOP_SEEK_BLOCK
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 7),
                    ("BlockAddress", UCHAR * 3),
                    ("Link", UCHAR, 1),
                    ("Flag", UCHAR, 1),
                    ("Reserved2", UCHAR, 4),
                    ("VendorUnique", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        (
            "REQUEST_BLOCK_ADDRESS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x02 - SCSIOP_REQUEST_BLOCK_ADDR
                    ("Reserved1", UCHAR * 3),
                    ("AllocationLength", UCHAR),
                    ("Link", UCHAR, 1),
                    ("Flag", UCHAR, 1),
                    ("Reserved2", UCHAR, 4),
                    ("VendorUnique", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        (
            "PARTITION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x0D - SCSIOP_PARTITION
                    ("Immediate", UCHAR, 1),
                    ("Sel", UCHAR, 1),
                    ("PartitionSelect", UCHAR, 6),
                    ("Reserved1", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "WRITE_TAPE_MARKS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("Immediate", UCHAR, 1),
                    ("WriteSetMarks", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("TransferLength", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SPACE_TAPE_MARKS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("Code", UCHAR, 3),
                    ("Reserved", UCHAR, 2),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("NumMarksMSB", UCHAR),
                    ("NumMarks", UCHAR),
                    ("NumMarksLSB", UCHAR),
                    (
                        "Byte6",
                        make_union(
                            [
                                ("value", UCHAR),
                                (
                                    "Fields",
                                    make_struct(
                                        [
                                            ("Link", UCHAR, 1),
                                            ("Flag", UCHAR, 1),
                                            ("Reserved", UCHAR, 4),
                                            ("VendorUnique", UCHAR, 2),
                                        ],
                                        _pack_,
                                    ),
                                ),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        # Read tape position
        (
            "READ_POSITION",
            make_struct(
                [
                    ("Operation", UCHAR),  # 0x43 - SCSIOP_READ_POSITION
                    ("BlockType", UCHAR, 1),
                    ("Reserved1", UCHAR, 4),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # ReadWrite for Tape
        (
            "CDB6READWRITETAPE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("VendorSpecific", UCHAR, 5),
                    ("Reserved", UCHAR, 3),
                    ("TransferLenMSB", UCHAR),
                    ("TransferLen", UCHAR),
                    ("TransferLenLSB", UCHAR),
                    ("Link", UCHAR, 1),
                    ("Flag", UCHAR, 1),
                    ("Reserved1", UCHAR, 4),
                    ("VendorUnique", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        # Medium changer CDB's
        (
            "INIT_ELEMENT_STATUS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x07 - SCSIOP_INIT_ELEMENT_STATUS
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNubmer", UCHAR, 3),
                    ("Reserved2", UCHAR * 3),
                    ("Reserved3", UCHAR, 7),
                    ("NoBarCode", UCHAR, 1),
                ],
                _pack_,
            ),
        ),
        (
            "INITIALIZE_ELEMENT_RANGE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xE7 - SCSIOP_INIT_ELEMENT_RANGE
                    ("Range", UCHAR, 1),
                    ("Reserved1", UCHAR, 4),
                    ("LogicalUnitNubmer", UCHAR, 3),
                    ("FirstElementAddress", UCHAR * 2),
                    ("Reserved2", UCHAR * 2),
                    ("NumberOfElements", UCHAR * 2),
                    ("Reserved3", UCHAR),
                    ("Reserved4", UCHAR, 7),
                    ("NoBarCode", UCHAR, 1),
                ],
                _pack_,
            ),
        ),
        (
            "POSITION_TO_ELEMENT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x2B - SCSIOP_POSITION_TO_ELEMENT
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("TransportElementAddress", UCHAR * 2),
                    ("DestinationElementAddress", UCHAR * 2),
                    ("Reserved2", UCHAR * 2),
                    ("Flip", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "MOVE_MEDIUM",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA5 - SCSIOP_MOVE_MEDIUM
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("TransportElementAddress", UCHAR * 2),
                    ("SourceElementAddress", UCHAR * 2),
                    ("DestinationElementAddress", UCHAR * 2),
                    ("Reserved2", UCHAR * 2),
                    ("Flip", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "EXCHANGE_MEDIUM",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA6 - SCSIOP_EXCHANGE_MEDIUM
                    ("Reserved1", UCHAR, 5),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("TransportElementAddress", UCHAR * 2),
                    ("SourceElementAddress", UCHAR * 2),
                    ("Destination1ElementAddress", UCHAR * 2),
                    ("Destination2ElementAddress", UCHAR * 2),
                    ("Flip1", UCHAR, 1),
                    ("Flip2", UCHAR, 1),
                    ("Reserved3", UCHAR, 6),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_ELEMENT_STATUS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xB8 - SCSIOP_READ_ELEMENT_STATUS
                    ("ElementType", UCHAR, 4),
                    ("VolTag", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("StartingElementAddress", UCHAR * 2),
                    ("NumberOfElements", UCHAR * 2),
                    ("Reserved1", UCHAR),
                    ("AllocationLength", UCHAR * 3),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_VOLUME_TAG",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xB6 - SCSIOP_SEND_VOLUME_TAG
                    ("ElementType", UCHAR, 4),
                    ("Reserved1", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("StartingElementAddress", UCHAR * 2),
                    ("Reserved2", UCHAR),
                    ("ActionCode", UCHAR, 5),
                    ("Reserved3", UCHAR, 3),
                    ("Reserved4", UCHAR * 2),
                    ("ParameterListLength", UCHAR * 2),
                    ("Reserved5", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REQUEST_VOLUME_ELEMENT_ADDRESS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Unknown -- vendor-unique?
                    ("ElementType", UCHAR, 4),
                    ("VolTag", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("StartingElementAddress", UCHAR * 2),
                    ("NumberElements", UCHAR * 2),
                    ("Reserved1", UCHAR),
                    ("AllocationLength", UCHAR * 3),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # Atapi 2.5 Changer 12-byte CDBs
        (
            "LOAD_UNLOAD",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA6 - SCSIOP_LOAD_UNLOAD_SLOT
                    ("Immediate", UCHAR, 1),
                    ("Reserved1", UCHAR, 4),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 2),
                    ("Start", UCHAR, 1),
                    ("LoadEject", UCHAR, 1),
                    ("Reserved3", UCHAR, 6),
                    ("Reserved4", UCHAR * 3),
                    ("Slot", UCHAR),
                    ("Reserved5", UCHAR * 3),
                ],
                _pack_,
            ),
        ),
        (
            "MECH_STATUS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xBD - SCSIOP_MECHANISM_STATUS
                    ("Reserved", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved1", UCHAR * 6),
                    ("AllocationLength", UCHAR * 2),
                    ("Reserved2", UCHAR * 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # C/DVD 0.9 CDBs
        (
            "SYNCHRONIZE_CACHE10",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x35 - SCSIOP_SYNCHRONIZE_CACHE
                    ("RelAddr", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                    ("Lun", UCHAR, 3),
                    ("LogicalBlockAddress", UCHAR * 4),  # Unused - set to zero
                    ("Reserved2", UCHAR),
                    ("BlockCount", UCHAR * 2),  # Unused - set to zero
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "GET_EVENT_STATUS_NOTIFICATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x4A - SCSIOP_GET_EVENT_STATUS_NOTIFICATION
                    ("Immediate", UCHAR, 1),
                    ("Reserved", UCHAR, 4),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 2),
                    ("NotificationClassRequest", UCHAR),
                    ("Reserved3", UCHAR * 2),
                    ("EventListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "GET_PERFORMANCE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xAC - SCSIOP_GET_PERFORMANCE
                    ("Except", UCHAR, 2),
                    ("Write", UCHAR, 1),
                    ("Tolerance", UCHAR, 2),
                    ("Reserved0", UCHAR, 3),
                    ("StartingLBA", UCHAR * 4),
                    ("Reserved1", UCHAR * 2),
                    ("MaximumNumberOfDescriptors", UCHAR * 2),
                    ("Type", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_DVD_STRUCTURE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xAD - SCSIOP_READ_DVD_STRUCTURE
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("RMDBlockNumber", UCHAR * 4),
                    ("LayerNumber", UCHAR),
                    ("Format", UCHAR),
                    ("AllocationLength", UCHAR * 2),
                    ("Reserved3", UCHAR, 6),
                    ("AGID", UCHAR, 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SET_STREAMING",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xB6 - SCSIOP_SET_STREAMING
                    ("Reserved", UCHAR * 8),
                    ("ParameterListLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_DVD_STRUCTURE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xBF - SCSIOP_SEND_DVD_STRUCTURE
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 5),
                    ("Format", UCHAR),
                    ("ParameterListLength", UCHAR * 2),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SEND_KEY",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA3 - SCSIOP_SEND_KEY
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 6),
                    ("ParameterListLength", UCHAR * 2),
                    ("KeyFormat", UCHAR, 6),
                    ("AGID", UCHAR, 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REPORT_KEY",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA4 - SCSIOP_REPORT_KEY
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("LogicalBlockAddress", UCHAR * 4),  # for title key
                    ("Reserved2", UCHAR * 2),
                    ("AllocationLength", UCHAR * 2),
                    ("KeyFormat", UCHAR, 6),
                    ("AGID", UCHAR, 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SET_READ_AHEAD",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA7 - SCSIOP_SET_READ_AHEAD
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("TriggerLBA", UCHAR * 4),
                    ("ReadAheadLBA", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_FORMATTED_CAPACITIES",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x23 - SCSIOP_READ_FORMATTED_CAPACITY
                    ("Reserved1", UCHAR, 5),
                    ("Lun", UCHAR, 3),
                    ("Reserved2", UCHAR * 5),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # SCSI-3
        (
            "REPORT_LUNS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA0 - SCSIOP_REPORT_LUNS
                    ("Reserved1", UCHAR * 5),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved2", UCHAR * 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PERSISTENT_RESERVE_IN",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5E - SCSIOP_PERSISTENT_RESERVE_IN
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("Reserved2", UCHAR * 5),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "PERSISTENT_RESERVE_OUT",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x5F - SCSIOP_PERSISTENT_RESERVE_OUT
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("Type", UCHAR, 4),
                    ("Scope", UCHAR, 4),
                    ("Reserved2", UCHAR * 4),
                    ("ParameterListLength", UCHAR * 2),  # 0x18
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REPORT_TIMESTAMP",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Byte  0          : SCSIOP_MAINTENANCE_IN
                    ("ServiceAction", UCHAR, 5),  # Byte  1, bit 0-4 : SERVICE_ACTION_REPORT_TIMESTAMP
                    ("Reserved1", UCHAR, 3),  # Byte  1, bit 5-7
                    ("Reserved2", UCHAR * 4),  # Byte  2-5
                    ("AllocationLength", UCHAR * 4),  # Byte  6-9
                    ("Reserved3", UCHAR),  # Byte 10
                    ("Control", UCHAR),  # Byte 11
                ],
                _pack_,
            ),
        ),
        (
            "SET_TIMESTAMP",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # Byte  0          : SCSIOP_MAINTENANCE_OUT
                    ("ServiceAction", UCHAR, 5),  # Byte  1, bit 0-4 : SERVICE_ACTION_SET_TIMESTAMP
                    ("Reserved1", UCHAR, 3),  # Byte  1, bit 5-7
                    ("Reserved2", UCHAR * 4),  # Byte  2-5
                    ("ParameterListLength", UCHAR * 4),  # Byte  6-9
                    ("Reserved3", UCHAR),  # Byte 10
                    ("Control", UCHAR),  # Byte 11
                ],
                _pack_,
            ),
        ),
        (
            "REPORT_SUPPORTED_OPERATION_CODES",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA3 SCSIOP_MAINTENANCE_IN
                    ("ServiceAction", UCHAR, 5),  # 0x0C SERVICE_ACTION_REPORT_SUPPORTED_OPERATION_CODES
                    ("Reserved0", UCHAR, 3),
                    ("ReportOptions", UCHAR, 3),
                    ("Reserved1", UCHAR, 4),
                    ("ReturnCommandTimeoutsDescriptor", UCHAR, 1),
                    ("RequestedOperationCode", UCHAR),
                    ("RequestedServiceAction", UCHAR * 2),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # MMC / SFF-8090 commands
        (
            "GET_CONFIGURATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x46 - SCSIOP_GET_CONFIGURATION
                    ("RequestType", UCHAR, 2),  # SCSI_GET_CONFIGURATION_REQUEST_TYPE_*
                    ("Reserved1", UCHAR, 6),  # includes obsolete LUN field
                    ("StartingFeature", UCHAR * 2),
                    ("Reserved2", UCHAR * 3),
                    ("AllocationLength", UCHAR * 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SET_CD_SPEED",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xB8 - SCSIOP_SET_CD_SPEED
                    (
                        "_unnamed_union",
                        make_union(
                            [
                                ("Reserved1", UCHAR),
                                (
                                    "_unnamed_struct",
                                    make_struct(
                                        [
                                            ("RotationControl", UCHAR, 2),
                                            ("Reserved3", UCHAR, 6),
                                        ],
                                        _pack_,
                                    ),
                                ),
                            ],
                            _pack_,
                        ),
                    ),
                    ("ReadSpeed", UCHAR * 2),  # 1x == (75 * 2352)
                    ("WriteSpeed", UCHAR * 2),  # 1x == (75 * 2352)
                    ("Reserved2", UCHAR * 5),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ12",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA8 - SCSIOP_READ12
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 4),
                    ("TransferLength", UCHAR * 4),
                    ("Reserved2", UCHAR, 7),
                    ("Streaming", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "WRITE12",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xAA - SCSIOP_WRITE12
                    ("RelativeAddress", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("EBP", UCHAR, 1),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("LogicalUnitNumber", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 4),
                    ("TransferLength", UCHAR * 4),
                    ("Reserved2", UCHAR, 7),
                    ("Streaming", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "ATA_PASSTHROUGH12",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0xA1 - SCSIOP_ATA_PASSTHROUGH12
                    ("Reserved1", UCHAR, 1),
                    ("Protocol", UCHAR, 4),
                    ("MultipleCount", UCHAR, 3),
                    ("TLength", UCHAR, 2),
                    ("ByteBlock", UCHAR, 1),
                    ("TDir", UCHAR, 1),
                    ("Reserved2", UCHAR, 1),
                    ("CkCond", UCHAR, 1),
                    ("Offline", UCHAR, 2),
                    ("Features", UCHAR),
                    ("SectorCount", UCHAR),
                    ("LbaLow", UCHAR),
                    ("LbaMid", UCHAR),
                    ("LbaHigh", UCHAR),
                    ("Device", UCHAR),
                    ("Command", UCHAR),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        # 16-byte CDBs
        (
            "READ16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x88 - SCSIOP_READ16
                    ("DurationLimitDescriptor2", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("RebuildAssistRecoveryControl", UCHAR, 1),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("ReadProtect", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 8),
                    ("TransferLength", UCHAR * 4),
                    ("Group", UCHAR, 6),
                    ("DurationLimitDescriptor0", UCHAR, 1),
                    ("DurationLimitDescriptor1", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "WRITE16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x8A - SCSIOP_WRITE16
                    ("DurationLimitDescriptor2", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("WriteProtect", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 8),
                    ("TransferLength", UCHAR * 4),
                    ("Group", UCHAR, 6),
                    ("DurationLimitDescriptor0", UCHAR, 1),
                    ("DurationLimitDescriptor1", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "VERIFY16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x8F - SCSIOP_VERIFY16
                    ("Reserved1", UCHAR, 1),
                    ("ByteCheck", UCHAR, 1),
                    ("BlockVerify", UCHAR, 1),
                    ("Reserved2", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("VerifyProtect", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 8),
                    ("VerificationLength", UCHAR * 4),
                    ("Reserved3", UCHAR, 7),
                    ("Streaming", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "SYNCHRONIZE_CACHE16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x91 - SCSIOP_SYNCHRONIZE_CACHE16
                    ("Reserved1", UCHAR, 1),
                    ("Immediate", UCHAR, 1),
                    ("Reserved2", UCHAR, 6),
                    ("LogicalBlock", UCHAR * 8),
                    ("BlockCount", UCHAR * 4),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "READ_CAPACITY16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x9E - SCSIOP_READ_CAPACITY16
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("LogicalBlock", UCHAR * 8),
                    ("AllocationLength", UCHAR * 4),
                    ("PMI", UCHAR, 1),
                    ("Reserved2", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "ATA_PASSTHROUGH16",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x85 - SCSIOP_ATA_PASSTHROUGH16
                    ("Extend", UCHAR, 1),
                    ("Protocol", UCHAR, 4),
                    ("MultipleCount", UCHAR, 3),
                    ("TLength", UCHAR, 2),
                    ("ByteBlock", UCHAR, 1),
                    ("TDir", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                    ("CkCond", UCHAR, 1),
                    ("Offline", UCHAR, 2),
                    ("Features15_8", UCHAR),
                    ("Features7_0", UCHAR),
                    ("SectorCount15_8", UCHAR),
                    ("SectorCount7_0", UCHAR),
                    ("LbaLow15_8", UCHAR),
                    ("LbaLow7_0", UCHAR),
                    ("LbaMid15_8", UCHAR),
                    ("LbaMid7_0", UCHAR),
                    ("LbaHigh15_8", UCHAR),
                    ("LbaHigh7_0", UCHAR),
                    ("Device", UCHAR),
                    ("Command", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "GET_LBA_STATUS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x9E SCSIOP_GET_LBA_STATUS
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("StartingLBA", UCHAR * 8),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "TOKEN_OPERATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x83 SCSIOP_POPULATE_TOKEN, SCSIOP_WRITE_USING_TOKEN
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("Reserved2", UCHAR * 4),
                    ("ListIdentifier", UCHAR * 4),
                    ("ParameterListLength", UCHAR * 4),
                    ("GroupNumber", UCHAR, 5),
                    ("Reserved3", UCHAR, 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "RECEIVE_TOKEN_INFORMATION",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x84 SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION
                    ("ServiceAction", UCHAR, 5),
                    ("Reserved1", UCHAR, 3),
                    ("ListIdentifier", UCHAR * 4),
                    ("Reserved2", UCHAR * 4),
                    ("AllocationLength", UCHAR * 4),
                    ("Reserved3", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "WRITE_BUFFER",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x3B SCSIOP_WRITE_DATA_BUFF
                    ("Mode", UCHAR, 5),
                    ("ModeSpecific", UCHAR, 3),
                    ("BufferID", UCHAR),
                    ("BufferOffset", UCHAR * 3),
                    ("ParameterListLength", UCHAR * 3),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "CLOSE_ZONE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x94 - SCSIOP_ZBC_OUT
                    ("ServiceAction", UCHAR, 5),  # 0x01 - SERVICE_ACTION_CLOSE_ZONE
                    ("Reserved1", UCHAR, 3),
                    ("ZoneId", UCHAR * 8),
                    ("Reserved2", UCHAR * 4),
                    ("All", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "FINISH_ZONE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x94 - SCSIOP_ZBC_OUT
                    ("ServiceAction", UCHAR, 5),  # 0x02 - SERVICE_ACTION_FINISH_ZONE
                    ("Reserved1", UCHAR, 3),
                    ("ZoneId", UCHAR * 8),
                    ("Reserved2", UCHAR * 4),
                    ("All", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "OPEN_ZONE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x94 - SCSIOP_ZBC_OUT
                    ("ServiceAction", UCHAR, 5),  # 0x03 - SERVICE_ACTION_OPEN_ZONE
                    ("Reserved1", UCHAR, 3),
                    ("ZoneId", UCHAR * 8),
                    ("Reserved2", UCHAR * 4),
                    ("All", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "RESET_WRITE_POINTER",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x94 - SCSIOP_ZBC_OUT
                    ("ServiceAction", UCHAR, 5),  # 0x04 - SERVICE_ACTION_RESET_WRITE_POINTER
                    ("Reserved1", UCHAR, 3),
                    ("ZoneId", UCHAR * 8),
                    ("Reserved2", UCHAR * 4),
                    ("All", UCHAR, 1),
                    ("Reserved3", UCHAR, 7),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REPORT_ZONES",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x95 - SCSIOP_ZBC_IN
                    ("ServiceAction", UCHAR, 5),  # 0x00 - SERVICE_ACTION_REPORT_ZONES
                    ("Reserved1", UCHAR, 3),
                    ("ZoneStartLBA", UCHAR * 8),
                    ("AllocationLength", UCHAR * 4),
                    ("ReportingOptions", UCHAR, 6),
                    ("Reserved3", UCHAR, 1),
                    ("Partial", UCHAR, 1),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "GET_PHYSICAL_ELEMENT_STATUS",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x9E - SCSIOP_GET_PHYSICAL_ELEMENT_STATUS
                    ("ServiceAction", UCHAR, 5),  # 0x17 - SERVICE_ACTION_GET_PHYSICAL_ELEMENT_STATUS
                    ("Reserved1", UCHAR, 3),
                    ("Reserved2", UCHAR * 4),
                    ("StartingElement", UCHAR * 4),
                    ("AllocationLength", UCHAR * 4),
                    ("ReportType", UCHAR, 4),
                    ("Reserved3", UCHAR, 2),
                    ("Filter", UCHAR, 2),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        (
            "REMOVE_ELEMENT_AND_TRUNCATE",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x9E - SCSIOP_REMOVE_ELEMENT_AND_TRUNCATE
                    ("ServiceAction", UCHAR, 5),  # 0x18 - SERVICE_ACTION_REMOVE_ELEMENT_AND_TRUNCATE
                    ("Reserved1", UCHAR, 3),
                    ("RequestedCapacity", UCHAR * 8),
                    ("ElementIdentifier", UCHAR * 4),
                    ("Reserved2", UCHAR),
                    ("Control", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG * 4),
        ("AsByte", UCHAR * 16),
    ]


PCDB = POINTER(CDB)


class CDB32(Union):
    _pack_ = _pack_
    _fields_ = [
        # Standard 32-byte CDB
        (
            "CDB32GENERIC",
            make_struct(
                [
                    ("OperationCode", UCHAR),
                    ("Control", UCHAR),
                    ("Reserved1", UCHAR * 4),
                    ("Group", UCHAR, 5),
                    ("Reserved2", UCHAR, 3),
                    ("AdditionalCDBLength", UCHAR),
                    ("ServiceAction", UCHAR * 2),
                    ("Reserved3", UCHAR),
                    ("DurationLimitDescriptor0", UCHAR, 1),
                    ("DurationLimitDescriptor1", UCHAR, 1),
                    ("DurationLimitDescriptor2", UCHAR, 1),
                    ("Reserved4", UCHAR, 5),
                    ("LogicalBlock", UCHAR * 8),
                    ("Reserved5", UCHAR * 8),
                    ("TransferLength", UCHAR * 4),
                ],
                _pack_,
            ),
        ),
        (
            "XDWRITEREAD32",
            make_struct(
                [
                    ("OperationCode", UCHAR),  # 0x7F - SCSIOP_OPERATION32
                    ("Control", UCHAR),
                    ("Reserved1", UCHAR * 4),
                    ("Group", UCHAR, 5),
                    ("Reserved2", UCHAR, 3),
                    ("AdditionalCDBLength", UCHAR),  # 0x18
                    ("ServiceAction", UCHAR * 2),  # 0x0007 - SERVICE_ACTION_XDWRITEREAD
                    ("XorProtectionInfo", UCHAR, 1),
                    ("Reservede", UCHAR, 1),
                    ("DisableWrite", UCHAR, 1),
                    ("ForceUnitAccess", UCHAR, 1),
                    ("DisablePageOut", UCHAR, 1),
                    ("WriteProtect", UCHAR, 1),
                    ("Reserved4", UCHAR),
                    ("LogicalBlock", UCHAR * 8),
                    ("Reserved5", UCHAR * 8),
                    ("TransferLength", UCHAR * 4),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG * 8),
        ("AsByte", UCHAR * 32),
    ]


PCDB32 = POINTER(CDB32)

_pack_ -= 1


#
# GET_EVENT_STATUS_NOTIFICATION


NOTIFICATION_OPERATIONAL_CHANGE_CLASS_MASK = 0x02
NOTIFICATION_POWER_MANAGEMENT_CLASS_MASK = 0x04
NOTIFICATION_EXTERNAL_REQUEST_CLASS_MASK = 0x08
NOTIFICATION_MEDIA_STATUS_CLASS_MASK = 0x10
NOTIFICATION_MULTI_HOST_CLASS_MASK = 0x20
NOTIFICATION_DEVICE_BUSY_CLASS_MASK = 0x40


NOTIFICATION_NO_CLASS_EVENTS = 0x0
NOTIFICATION_OPERATIONAL_CHANGE_CLASS_EVENTS = 0x1
NOTIFICATION_POWER_MANAGEMENT_CLASS_EVENTS = 0x2
NOTIFICATION_EXTERNAL_REQUEST_CLASS_EVENTS = 0x3
NOTIFICATION_MEDIA_STATUS_CLASS_EVENTS = 0x4
NOTIFICATION_MULTI_HOST_CLASS_EVENTS = 0x5
NOTIFICATION_DEVICE_BUSY_CLASS_EVENTS = 0x6

_pack_ += 1


class NOTIFICATION_EVENT_STATUS_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("EventDataLength", UCHAR * 2),
        ("NotificationClass", UCHAR, 3),
        ("Reserved", UCHAR, 4),
        ("NEA", UCHAR, 1),
        ("SupportedEventClasses", UCHAR),
        # if !defined(__midl)
        ("ClassEventData", UCHAR * 0),
        # endif
    ]


PNOTIFICATION_EVENT_STATUS_HEADER = POINTER(NOTIFICATION_EVENT_STATUS_HEADER)
_pack_ -= 1

NOTIFICATION_OPERATIONAL_EVENT_NO_CHANGE = 0x0
NOTIFICATION_OPERATIONAL_EVENT_CHANGE_REQUESTED = 0x1
NOTIFICATION_OPERATIONAL_EVENT_CHANGE_OCCURRED = 0x2

NOTIFICATION_OPERATIONAL_STATUS_AVAILABLE = 0x0
NOTIFICATION_OPERATIONAL_STATUS_TEMPORARY_BUSY = 0x1
NOTIFICATION_OPERATIONAL_STATUS_EXTENDED_BUSY = 0x2

NOTIFICATION_OPERATIONAL_OPCODE_NONE = 0x0
NOTIFICATION_OPERATIONAL_OPCODE_FEATURE_CHANGE = 0x1
NOTIFICATION_OPERATIONAL_OPCODE_FEATURE_ADDED = 0x2
NOTIFICATION_OPERATIONAL_OPCODE_UNIT_RESET = 0x3
NOTIFICATION_OPERATIONAL_OPCODE_FIRMWARE_CHANGED = 0x4
NOTIFICATION_OPERATIONAL_OPCODE_INQUIRY_CHANGED = 0x5

# Class event data may be one (or none) of the following:

_pack_ += 1


class NOTIFICATION_OPERATIONAL_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x1
        ("OperationalEvent", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("OperationalStatus", UCHAR, 4),
        ("Reserved2", UCHAR, 3),
        ("PersistentPrevented", UCHAR, 1),
        ("Operation", UCHAR * 2),
    ]


PNOTIFICATION_OPERATIONAL_STATUS = POINTER(NOTIFICATION_OPERATIONAL_STATUS)
_pack_ -= 1


NOTIFICATION_POWER_EVENT_NO_CHANGE = 0x0
NOTIFICATION_POWER_EVENT_CHANGE_SUCCEEDED = 0x1
NOTIFICATION_POWER_EVENT_CHANGE_FAILED = 0x2

NOTIFICATION_POWER_STATUS_ACTIVE = 0x1
NOTIFICATION_POWER_STATUS_IDLE = 0x2
NOTIFICATION_POWER_STATUS_STANDBY = 0x3
NOTIFICATION_POWER_STATUS_SLEEP = 0x4

_pack_ += 1


class NOTIFICATION_POWER_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x2
        ("PowerEvent", UCHAR, 4),
        ("Reserved", UCHAR, 4),
        ("PowerStatus", UCHAR),
        ("Reserved2", UCHAR * 2),
    ]


PNOTIFICATION_POWER_STATUS = POINTER(NOTIFICATION_POWER_STATUS)
_pack_ -= 1

NOTIFICATION_MEDIA_EVENT_NO_EVENT = 0x0
NOTIFICATION_EXTERNAL_EVENT_NO_CHANGE = 0x0
NOTIFICATION_EXTERNAL_EVENT_BUTTON_DOWN = 0x1
NOTIFICATION_EXTERNAL_EVENT_BUTTON_UP = 0x2
NOTIFICATION_EXTERNAL_EVENT_EXTERNAL = 0x3  # respond with GET_CONFIGURATION?

NOTIFICATION_EXTERNAL_STATUS_READY = 0x0
NOTIFICATION_EXTERNAL_STATUS_PREVENT = 0x1

NOTIFICATION_EXTERNAL_REQUEST_NONE = 0x0000
NOTIFICATION_EXTERNAL_REQUEST_QUEUE_OVERRUN = 0x0001
NOTIFICATION_EXTERNAL_REQUEST_PLAY = 0x0101
NOTIFICATION_EXTERNAL_REQUEST_REWIND_BACK = 0x0102
NOTIFICATION_EXTERNAL_REQUEST_FAST_FORWARD = 0x0103
NOTIFICATION_EXTERNAL_REQUEST_PAUSE = 0x0104
NOTIFICATION_EXTERNAL_REQUEST_STOP = 0x0106
NOTIFICATION_EXTERNAL_REQUEST_ASCII_LOW = 0x0200
NOTIFICATION_EXTERNAL_REQUEST_ASCII_HIGH = 0x02FF

_pack_ += 1


class NOTIFICATION_EXTERNAL_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x3
        ("ExternalEvent", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("ExternalStatus", UCHAR, 4),
        ("Reserved2", UCHAR, 3),
        ("PersistentPrevented", UCHAR, 1),
        ("Request", UCHAR * 2),
    ]


PNOTIFICATION_EXTERNAL_STATUS = POINTER(NOTIFICATION_EXTERNAL_STATUS)
_pack_ -= 1

NOTIFICATION_MEDIA_EVENT_NO_CHANGE = 0x0
NOTIFICATION_MEDIA_EVENT_EJECT_REQUEST = 0x1
NOTIFICATION_MEDIA_EVENT_NEW_MEDIA = 0x2
NOTIFICATION_MEDIA_EVENT_MEDIA_REMOVAL = 0x3
NOTIFICATION_MEDIA_EVENT_MEDIA_CHANGE = 0x4

_pack_ += 1


class NOTIFICATION_MEDIA_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x4
        ("MediaEvent", UCHAR, 4),
        ("Reserved", UCHAR, 4),
        (
            "_unnamed_union",
            make_union(
                [
                    ("PowerStatus", UCHAR),  # OBSOLETE -- was improperly named in NT5 headers
                    ("MediaStatus", UCHAR),  # Use this for currently reserved fields
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("DoorTrayOpen", UCHAR, 1),
                                ("MediaPresent", UCHAR, 1),
                                ("ReservedX", UCHAR, 6),  # do not reference this directly!
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        ("StartSlot", UCHAR),
        ("EndSlot", UCHAR),
    ]


PNOTIFICATION_MEDIA_STATUS = POINTER(NOTIFICATION_MEDIA_STATUS)
_pack_ -= 1

NOTIFICATION_BUSY_EVENT_NO_EVENT = 0x0
NOTIFICATION_MULTI_HOST_EVENT_NO_CHANGE = 0x0
NOTIFICATION_MULTI_HOST_EVENT_CONTROL_REQUEST = 0x1
NOTIFICATION_MULTI_HOST_EVENT_CONTROL_GRANT = 0x2
NOTIFICATION_MULTI_HOST_EVENT_CONTROL_RELEASE = 0x3

NOTIFICATION_MULTI_HOST_STATUS_READY = 0x0
NOTIFICATION_MULTI_HOST_STATUS_PREVENT = 0x1

NOTIFICATION_MULTI_HOST_PRIORITY_NO_REQUESTS = 0x0
NOTIFICATION_MULTI_HOST_PRIORITY_LOW = 0x1
NOTIFICATION_MULTI_HOST_PRIORITY_MEDIUM = 0x2
NOTIFICATION_MULTI_HOST_PRIORITY_HIGH = 0x3

_pack_ += 1


class NOTIFICATION_MULTI_HOST_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x5
        ("MultiHostEvent", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("MultiHostStatus", UCHAR, 4),
        ("Reserved2", UCHAR, 3),
        ("PersistentPrevented", UCHAR, 1),
        ("Priority", UCHAR * 2),
    ]


PNOTIFICATION_MULTI_HOST_STATUS = POINTER(NOTIFICATION_MULTI_HOST_STATUS)
_pack_ -= 1

NOTIFICATION_BUSY_EVENT_NO_EVENT = 0x0
NOTIFICATION_BUSY_EVENT_NO_CHANGE = 0x0
NOTIFICATION_BUSY_EVENT_BUSY = 0x1
NOTIFICATION_BUSY_EVENT_LO_CHANGE = 0x2

NOTIFICATION_BUSY_STATUS_NO_EVENT = 0x0
NOTIFICATION_BUSY_STATUS_POWER = 0x1
NOTIFICATION_BUSY_STATUS_IMMEDIATE = 0x2
NOTIFICATION_BUSY_STATUS_DEFERRED = 0x3

_pack_ += 1


class NOTIFICATION_BUSY_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [  # event class == 0x6
        ("DeviceBusyEvent", UCHAR, 4),
        ("Reserved", UCHAR, 4),
        ("DeviceBusyStatus", UCHAR),
        ("Time", UCHAR * 2),
    ]


PNOTIFICATION_BUSY_STATUS = POINTER(NOTIFICATION_BUSY_STATUS)
_pack_ -= 1

#
# SECURITY PROTOCOL IN/OUT definitions (SPC-4, 6.29/6.30)

_pack_ += 1


class SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 6),
        ("SupportedSecurityListLength", UCHAR * 2),
        ("SupportedSecurityProtocol", UCHAR * 0),
    ]


PSUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA = POINTER(SUPPORTED_SECURITY_PROTOCOLS_PARAMETER_DATA)
_pack_ -= 1

# Security protocols
SECURITY_PROTOCOL_IEEE1667 = 0xEE
TCG_SECURITY_PROTOCOL_ID_0 = 0x00
TCG_SECURITY_PROTOCOL_ID_1 = 0x01
TCG_SECURITY_PROTOCOL_ID_2 = 0x02

#
# Read DVD Structure Definitions and Constants

DVD_FORMAT_LEAD_IN = 0x00
DVD_FORMAT_COPYRIGHT = 0x01
DVD_FORMAT_DISK_KEY = 0x02
DVD_FORMAT_BCA = 0x03
DVD_FORMAT_MANUFACTURING = 0x04

_pack_ += 1


class READ_DVD_STRUCTURES_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("Reserved", UCHAR * 2),
        # if !defined(__midl)
        ("Data", UCHAR * 0),
        # endif
    ]


PREAD_DVD_STRUCTURES_HEADER = POINTER(READ_DVD_STRUCTURES_HEADER)
_pack_ -= 1

# DiskKey, BCA & Manufacturer information will provide byte arrays as their
# data.

# CDVD 0.9 Send & Report Key Definitions and Structures

DVD_REPORT_AGID = 0x00
DVD_CHALLENGE_KEY = 0x01
DVD_KEY_1 = 0x02
DVD_KEY_2 = 0x03
DVD_TITLE_KEY = 0x04
DVD_REPORT_ASF = 0x05
DVD_INVALIDATE_AGID = 0x3F

_pack_ += 1


class CDVD_KEY_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DataLength", UCHAR * 2),
        ("Reserved", UCHAR * 2),
        # if !defined(__midl)
        ("Data", UCHAR * 0),
        # endif
    ]


PCDVD_KEY_HEADER = POINTER(CDVD_KEY_HEADER)


class CDVD_REPORT_AGID_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 3),
        ("Reserved2", UCHAR, 6),
        ("AGID", UCHAR, 2),
    ]


PCDVD_REPORT_AGID_DATA = POINTER(CDVD_REPORT_AGID_DATA)


class CDVD_CHALLENGE_KEY_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ChallengeKeyValue", UCHAR * 10),
        ("Reserved", UCHAR * 2),
    ]


PCDVD_CHALLENGE_KEY_DATA = POINTER(CDVD_CHALLENGE_KEY_DATA)


class CDVD_KEY_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Key", UCHAR * 5),
        ("Reserved", UCHAR * 3),
    ]


PCDVD_KEY_DATA = POINTER(CDVD_KEY_DATA)


class CDVD_REPORT_ASF_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 3),
        ("Success", UCHAR, 1),
        ("Reserved2", UCHAR, 7),
    ]


PCDVD_REPORT_ASF_DATA = POINTER(CDVD_REPORT_ASF_DATA)


class CDVD_TITLE_KEY_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DataLength", UCHAR * 2),
        ("Reserved1", UCHAR * 1),
        ("Reserved2", UCHAR, 3),
        ("CGMS", UCHAR, 2),
        ("CP_SEC", UCHAR, 1),
        ("CPM", UCHAR, 1),
        ("Zero", UCHAR, 1),
        ("TitleKey", CDVD_KEY_DATA),
    ]


PCDVD_TITLE_KEY_HEADER = POINTER(CDVD_TITLE_KEY_HEADER)
_pack_ -= 1


# Format Unit Data definitions and structures

_pack_ += 1


class FORMAT_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfBlocks", UCHAR * 4),
        ("FormatSubType", UCHAR, 2),
        ("FormatType", UCHAR, 6),
        ("BlockLength", UCHAR * 3),
    ]


PFORMAT_DESCRIPTOR = POINTER(FORMAT_DESCRIPTOR)


class FORMAT_LIST_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", UCHAR),
        ("VendorSpecific", UCHAR, 1),
        ("Immediate", UCHAR, 1),
        ("TryOut", UCHAR, 1),
        ("IP", UCHAR, 1),
        ("STPF", UCHAR, 1),
        ("DCRT", UCHAR, 1),
        ("DPRY", UCHAR, 1),
        ("FOV", UCHAR, 1),
        ("FormatDescriptorLength", UCHAR * 2),
        # if !defined(__midl)
        ("Descriptors", FORMAT_DESCRIPTOR * 0),
        # endif
    ]


PFORMAT_LIST_HEADER = POINTER(FORMAT_LIST_HEADER)
_pack_ -= 1

# Read Formatted Capacity Data - returned in Big Endian Format


_pack_ += 1


class FORMATTED_CAPACITY_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfBlocks", UCHAR * 4),
        ("Maximum", UCHAR, 1),
        ("Valid", UCHAR, 1),
        ("FormatType", UCHAR, 6),
        ("BlockLength", UCHAR * 3),
    ]


PFORMATTED_CAPACITY_DESCRIPTOR = POINTER(FORMATTED_CAPACITY_DESCRIPTOR)


class FORMATTED_CAPACITY_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", UCHAR * 3),
        ("CapacityListLength", UCHAR),
        # if !defined(__midl)
        ("Descriptors", FORMATTED_CAPACITY_DESCRIPTOR * 0),
        # endif
    ]


PFORMATTED_CAPACITY_LIST = POINTER(FORMATTED_CAPACITY_LIST)
_pack_ -= 1

#      BLANK command blanking type codes

BLANK_FULL = 0x0
BLANK_MINIMAL = 0x1
BLANK_TRACK = 0x2
BLANK_UNRESERVE_TRACK = 0x3
BLANK_TAIL = 0x4
BLANK_UNCLOSE_SESSION = 0x5
BLANK_SESSION = 0x6

# PLAY_CD definitions and constants

CD_EXPECTED_SECTOR_ANY = 0x0
CD_EXPECTED_SECTOR_CDDA = 0x1
CD_EXPECTED_SECTOR_MODE1 = 0x2
CD_EXPECTED_SECTOR_MODE2 = 0x3
CD_EXPECTED_SECTOR_MODE2_FORM1 = 0x4
CD_EXPECTED_SECTOR_MODE2_FORM2 = 0x5

# Read Disk Information Definitions and Capabilities

DISK_STATUS_EMPTY = 0x00
DISK_STATUS_INCOMPLETE = 0x01
DISK_STATUS_COMPLETE = 0x02
DISK_STATUS_OTHERS = 0x03

LAST_SESSION_EMPTY = 0x00
LAST_SESSION_INCOMPLETE = 0x01
LAST_SESSION_RESERVED_DAMAGED = 0x02
LAST_SESSION_COMPLETE = 0x03

DISK_TYPE_CDDA = 0x00
DISK_TYPE_CDI = 0x10
DISK_TYPE_XA = 0x20
DISK_TYPE_UNDEFINED = 0xFF

#  Values for MrwStatus field.

DISC_BGFORMAT_STATE_NONE = 0x0
DISC_BGFORMAT_STATE_INCOMPLETE = 0x1
DISC_BGFORMAT_STATE_RUNNING = 0x2
DISC_BGFORMAT_STATE_COMPLETE = 0x3


_pack_ += 1


class OPC_TABLE_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Speed", UCHAR * 2),
        ("OPCValue", UCHAR * 6),
    ]


POPC_TABLE_ENTRY = POINTER(OPC_TABLE_ENTRY)


class DISC_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("DiscStatus", UCHAR, 2),
        ("LastSessionStatus", UCHAR, 2),
        ("Erasable", UCHAR, 1),
        ("Reserved1", UCHAR, 3),
        ("FirstTrackNumber", UCHAR),
        ("NumberOfSessionsLsb", UCHAR),
        ("LastSessionFirstTrackLsb", UCHAR),
        ("LastSessionLastTrackLsb", UCHAR),
        ("MrwStatus", UCHAR, 2),
        ("MrwDirtyBit", UCHAR, 1),
        ("Reserved2", UCHAR, 2),
        ("URU", UCHAR, 1),
        ("DBC_V", UCHAR, 1),
        ("DID_V", UCHAR, 1),
        ("DiscType", UCHAR),
        ("NumberOfSessionsMsb", UCHAR),
        ("LastSessionFirstTrackMsb", UCHAR),
        ("LastSessionLastTrackMsb", UCHAR),
        ("DiskIdentification", UCHAR * 4),
        ("LastSessionLeadIn", UCHAR * 4),  # HMSF
        ("LastPossibleLeadOutStartTime", UCHAR * 4),  # HMSF
        ("DiskBarCode", UCHAR * 8),
        ("Reserved4", UCHAR),
        ("NumberOPCEntries", UCHAR),
        ("OPCTable", OPC_TABLE_ENTRY * 1),  # can be many of these here....
    ]


PDISC_INFORMATION = POINTER(DISC_INFORMATION)

# TODO: Deprecate DISK_INFORMATION
##if PRAGMA_DEPRECATED_DDK
##pragma deprecated(_DISK_INFORMATION)  # Use DISC_INFORMATION, note size change
##pragma deprecated( DISK_INFORMATION)  # Use DISC_INFORMATION, note size change
##pragma deprecated(PDISK_INFORMATION)  # Use DISC_INFORMATION, note size change
##endif


class DISK_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("DiskStatus", UCHAR, 2),
        ("LastSessionStatus", UCHAR, 2),
        ("Erasable", UCHAR, 1),
        ("Reserved1", UCHAR, 3),
        ("FirstTrackNumber", UCHAR),
        ("NumberOfSessions", UCHAR),
        ("LastSessionFirstTrack", UCHAR),
        ("LastSessionLastTrack", UCHAR),
        ("Reserved2", UCHAR, 5),
        ("GEN", UCHAR, 1),
        ("DBC_V", UCHAR, 1),
        ("DID_V", UCHAR, 1),
        ("DiskType", UCHAR),
        ("Reserved3", UCHAR * 3),
        ("DiskIdentification", UCHAR * 4),
        ("LastSessionLeadIn", UCHAR * 4),  # MSF
        ("LastPossibleStartTime", UCHAR * 4),  # MSF
        ("DiskBarCode", UCHAR * 8),
        ("Reserved4", UCHAR),
        ("NumberOPCEntries", UCHAR),
        # if !defined(__midl)
        ("OPCTable", OPC_TABLE_ENTRY * 0),
        # endif
    ]


PDISK_INFORMATION = POINTER(DISK_INFORMATION)
_pack_ -= 1


# Read Header definitions and structures
_pack_ += 1


class DATA_BLOCK_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DataMode", UCHAR),
        ("Reserved", UCHAR * 4),
        (
            "_unnamed_union",
            make_union(
                [
                    ("LogicalBlockAddress", UCHAR * 4),
                    (
                        "MSF",
                        make_struct(
                            [
                                ("Reserved", UCHAR),
                                ("M", UCHAR),
                                ("S", UCHAR),
                                ("F", UCHAR),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
    ]


PDATA_BLOCK_HEADER = POINTER(DATA_BLOCK_HEADER)
_pack_ -= 1


DATA_BLOCK_MODE0 = 0x0
DATA_BLOCK_MODE1 = 0x1
DATA_BLOCK_MODE2 = 0x2

# Read TOC Format Codes

READ_TOC_FORMAT_TOC = 0x00
READ_TOC_FORMAT_SESSION = 0x01
READ_TOC_FORMAT_FULL_TOC = 0x02
READ_TOC_FORMAT_PMA = 0x03
READ_TOC_FORMAT_ATIP = 0x04

# TODO: Deprecate TRACK_INFORMATION structure, use TRACK_INFORMATION2 instead
_pack_ += 1


class TRACK_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("TrackNumber", UCHAR),
        ("SessionNumber", UCHAR),
        ("Reserved1", UCHAR),
        ("TrackMode", UCHAR, 4),
        ("Copy", UCHAR, 1),
        ("Damage", UCHAR, 1),
        ("Reserved2", UCHAR, 2),
        ("DataMode", UCHAR, 4),
        ("FP", UCHAR, 1),
        ("Packet", UCHAR, 1),
        ("Blank", UCHAR, 1),
        ("RT", UCHAR, 1),
        ("NWA_V", UCHAR, 1),
        ("Reserved3", UCHAR, 7),
        ("TrackStartAddress", UCHAR * 4),
        ("NextWritableAddress", UCHAR * 4),
        ("FreeBlocks", UCHAR * 4),
        ("FixedPacketSize", UCHAR * 4),
    ]


PTRACK_INFORMATION = POINTER(TRACK_INFORMATION)


# Second Revision Modifies:
# * Longer names for some fields
# * LSB to track/session number fields
# * LRA_V bit
# Second Revision Adds:
# * TrackSize
# * LastRecordedAddress
# * MSB to track/session
# * Two reserved bytes
# Total structure size increased by 12 (0x0C) bytes
class TRACK_INFORMATION2(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("TrackNumberLsb", UCHAR),
        ("SessionNumberLsb", UCHAR),
        ("Reserved4", UCHAR),
        ("TrackMode", UCHAR, 4),
        ("Copy", UCHAR, 1),
        ("Damage", UCHAR, 1),
        ("Reserved5", UCHAR, 2),
        ("DataMode", UCHAR, 4),
        ("FixedPacket", UCHAR, 1),
        ("Packet", UCHAR, 1),
        ("Blank", UCHAR, 1),
        ("ReservedTrack", UCHAR, 1),
        ("NWA_V", UCHAR, 1),
        ("LRA_V", UCHAR, 1),
        ("Reserved6", UCHAR, 6),
        ("TrackStartAddress", UCHAR * 4),
        ("NextWritableAddress", UCHAR * 4),
        ("FreeBlocks", UCHAR * 4),
        ("FixedPacketSize", UCHAR * 4),  # blocking factor
        ("TrackSize", UCHAR * 4),
        ("LastRecordedAddress", UCHAR * 4),
        ("TrackNumberMsb", UCHAR),
        ("SessionNumberMsb", UCHAR),
        ("Reserved7", UCHAR * 2),
    ]


PTRACK_INFORMATION2 = POINTER(TRACK_INFORMATION2)


# Third Revision Adds
# * ReadCompatibilityLBA
# Total structure size increased by 4 bytes
class TRACK_INFORMATION3(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("TrackNumberLsb", UCHAR),
        ("SessionNumberLsb", UCHAR),
        ("Reserved4", UCHAR),
        ("TrackMode", UCHAR, 4),
        ("Copy", UCHAR, 1),
        ("Damage", UCHAR, 1),
        ("Reserved5", UCHAR, 2),
        ("DataMode", UCHAR, 4),
        ("FixedPacket", UCHAR, 1),
        ("Packet", UCHAR, 1),
        ("Blank", UCHAR, 1),
        ("ReservedTrack", UCHAR, 1),
        ("NWA_V", UCHAR, 1),
        ("LRA_V", UCHAR, 1),
        ("Reserved6", UCHAR, 6),
        ("TrackStartAddress", UCHAR * 4),
        ("NextWritableAddress", UCHAR * 4),
        ("FreeBlocks", UCHAR * 4),
        ("FixedPacketSize", UCHAR * 4),  # blocking factor
        ("TrackSize", UCHAR * 4),
        ("LastRecordedAddress", UCHAR * 4),
        ("TrackNumberMsb", UCHAR),
        ("SessionNumberMsb", UCHAR),
        ("Reserved7", UCHAR * 2),
        ("ReadCompatibilityLba", UCHAR * 4),
    ]


PTRACK_INFORMATION3 = POINTER(TRACK_INFORMATION3)

_pack_ -= 1

_pack_ += 1


class PERFORMANCE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("RandomAccess", UCHAR, 1),
        ("Exact", UCHAR, 1),
        ("RestoreDefaults", UCHAR, 1),
        ("WriteRotationControl", UCHAR, 2),
        ("Reserved1", UCHAR, 3),
        ("Reserved", UCHAR * 3),
        ("StartLba", UCHAR * 4),
        ("EndLba", UCHAR * 4),
        ("ReadSize", UCHAR * 4),
        ("ReadTime", UCHAR * 4),
        ("WriteSize", UCHAR * 4),
        ("WriteTime", UCHAR * 4),
    ]


PPERFORMANCE_DESCRIPTOR = POINTER(PERFORMANCE_DESCRIPTOR)
_pack_ -= 1

# Command Descriptor Block constants.

CDB6GENERIC_LENGTH = 6
CDB10GENERIC_LENGTH = 10
CDB12GENERIC_LENGTH = 12

SETBITON = 1
SETBITOFF = 0

# Mode Sense/Select page constants.

MODE_PAGE_VENDOR_SPECIFIC = 0x00
MODE_PAGE_ERROR_RECOVERY = 0x01
MODE_PAGE_DISCONNECT = 0x02
MODE_PAGE_FORMAT_DEVICE = 0x03  # disk
MODE_PAGE_MRW = 0x03  # cdrom
MODE_PAGE_RIGID_GEOMETRY = 0x04
MODE_PAGE_FLEXIBILE = 0x05  # disk
MODE_PAGE_WRITE_PARAMETERS = 0x05  # cdrom
MODE_PAGE_VERIFY_ERROR = 0x07
MODE_PAGE_CACHING = 0x08
MODE_PAGE_PERIPHERAL = 0x09
MODE_PAGE_CONTROL = 0x0A
MODE_PAGE_MEDIUM_TYPES = 0x0B
MODE_PAGE_NOTCH_PARTITION = 0x0C
MODE_PAGE_CD_AUDIO_CONTROL = 0x0E
MODE_PAGE_DATA_COMPRESS = 0x0F
MODE_PAGE_DEVICE_CONFIG = 0x10
MODE_PAGE_XOR_CONTROL = 0x10  # disk
MODE_PAGE_MEDIUM_PARTITION = 0x11
MODE_PAGE_ENCLOSURE_SERVICES_MANAGEMENT = 0x14
MODE_PAGE_EXTENDED = 0x15
MODE_PAGE_EXTENDED_DEVICE_SPECIFIC = 0x16
MODE_PAGE_CDVD_FEATURE_SET = 0x18
MODE_PAGE_PROTOCOL_SPECIFIC_LUN = 0x18
MODE_PAGE_PROTOCOL_SPECIFIC_PORT = 0x19
MODE_PAGE_POWER_CONDITION = 0x1A
MODE_PAGE_LUN_MAPPING = 0x1B
MODE_PAGE_FAULT_REPORTING = 0x1C
MODE_PAGE_CDVD_INACTIVITY = 0x1D  # cdrom
MODE_PAGE_ELEMENT_ADDRESS = 0x1D
MODE_PAGE_TRANSPORT_GEOMETRY = 0x1E
MODE_PAGE_DEVICE_CAPABILITIES = 0x1F
MODE_PAGE_CAPABILITIES = 0x2A  # cdrom

MODE_SENSE_RETURN_ALL = 0x3F

MODE_SENSE_CURRENT_VALUES = 0x00
MODE_SENSE_CHANGEABLE_VALUES = 0x40
MODE_SENSE_DEFAULT_VAULES = 0x80
MODE_SENSE_SAVED_VALUES = 0xC0

# Page Control for MODE_SENSE/MODE_SENSE10
MODE_SENSE_CURRENT_VALUES_PAGE_CONTROL = 0
MODE_SENSE_CHANGEABLE_VALUES_PAGE_CONTROL = 1
MODE_SENSE_DEFAULT_VALUES_PAGE_CONTROL = 2
MODE_SENSE_SAVED_VALUES_PAGE_CONTROL = 3

MODE_SUBPAGE_COMMAND_DURATION_LIMIT_A_MODE = 0x03
MODE_SUBPAGE_COMMAND_DURATION_LIMIT_B_MODE = 0x04
MODE_SUBPAGE_COMMAND_DURATION_LIMIT_T2A_MODE = 0x07
MODE_SUBPAGE_COMMAND_DURATION_LIMIT_T2B_MODE = 0x08

# SCSI CDB operation codes

# 6-byte commands:
SCSIOP_TEST_UNIT_READY = 0x00
SCSIOP_REZERO_UNIT = 0x01
SCSIOP_REWIND = 0x01
SCSIOP_REQUEST_BLOCK_ADDR = 0x02
SCSIOP_REQUEST_SENSE = 0x03
SCSIOP_FORMAT_UNIT = 0x04
SCSIOP_READ_BLOCK_LIMITS = 0x05
SCSIOP_REASSIGN_BLOCKS = 0x07
SCSIOP_INIT_ELEMENT_STATUS = 0x07
SCSIOP_READ6 = 0x08
SCSIOP_RECEIVE = 0x08
SCSIOP_WRITE6 = 0x0A
SCSIOP_PRINT = 0x0A
SCSIOP_SEND = 0x0A
SCSIOP_SEEK6 = 0x0B
SCSIOP_TRACK_SELECT = 0x0B
SCSIOP_SLEW_PRINT = 0x0B
SCSIOP_SET_CAPACITY = 0x0B  # tape
SCSIOP_SEEK_BLOCK = 0x0C
SCSIOP_PARTITION = 0x0D
SCSIOP_READ_REVERSE = 0x0F
SCSIOP_WRITE_FILEMARKS = 0x10
SCSIOP_FLUSH_BUFFER = 0x10
SCSIOP_SPACE = 0x11
SCSIOP_INQUIRY = 0x12
SCSIOP_VERIFY6 = 0x13
SCSIOP_RECOVER_BUF_DATA = 0x14
SCSIOP_MODE_SELECT = 0x15
SCSIOP_RESERVE_UNIT = 0x16
SCSIOP_RELEASE_UNIT = 0x17
SCSIOP_COPY = 0x18
SCSIOP_ERASE = 0x19
SCSIOP_MODE_SENSE = 0x1A
SCSIOP_START_STOP_UNIT = 0x1B
SCSIOP_STOP_PRINT = 0x1B
SCSIOP_LOAD_UNLOAD = 0x1B
SCSIOP_RECEIVE_DIAGNOSTIC = 0x1C
SCSIOP_SEND_DIAGNOSTIC = 0x1D
SCSIOP_MEDIUM_REMOVAL = 0x1E

# 10-byte commands
SCSIOP_READ_FORMATTED_CAPACITY = 0x23
SCSIOP_READ_CAPACITY = 0x25
SCSIOP_READ = 0x28
SCSIOP_WRITE = 0x2A
SCSIOP_SEEK = 0x2B
SCSIOP_LOCATE = 0x2B
SCSIOP_POSITION_TO_ELEMENT = 0x2B
SCSIOP_WRITE_VERIFY = 0x2E
SCSIOP_VERIFY = 0x2F
SCSIOP_SEARCH_DATA_HIGH = 0x30
SCSIOP_SEARCH_DATA_EQUAL = 0x31
SCSIOP_SEARCH_DATA_LOW = 0x32
SCSIOP_SET_LIMITS = 0x33
SCSIOP_READ_POSITION = 0x34
SCSIOP_SYNCHRONIZE_CACHE = 0x35
SCSIOP_COMPARE = 0x39
SCSIOP_COPY_COMPARE = 0x3A
SCSIOP_WRITE_DATA_BUFF = 0x3B
SCSIOP_READ_DATA_BUFF = 0x3C
SCSIOP_WRITE_LONG = 0x3F
SCSIOP_CHANGE_DEFINITION = 0x40
SCSIOP_WRITE_SAME = 0x41
SCSIOP_READ_SUB_CHANNEL = 0x42
SCSIOP_UNMAP = 0x42  # block device
SCSIOP_READ_TOC = 0x43
SCSIOP_READ_HEADER = 0x44
SCSIOP_REPORT_DENSITY_SUPPORT = 0x44  # tape
SCSIOP_PLAY_AUDIO = 0x45
SCSIOP_GET_CONFIGURATION = 0x46
SCSIOP_PLAY_AUDIO_MSF = 0x47
SCSIOP_PLAY_TRACK_INDEX = 0x48
SCSIOP_SANITIZE = 0x48  # block device
SCSIOP_PLAY_TRACK_RELATIVE = 0x49
SCSIOP_GET_EVENT_STATUS = 0x4A
SCSIOP_PAUSE_RESUME = 0x4B
SCSIOP_LOG_SELECT = 0x4C
SCSIOP_LOG_SENSE = 0x4D
SCSIOP_STOP_PLAY_SCAN = 0x4E
SCSIOP_XDWRITE = 0x50
SCSIOP_XPWRITE = 0x51
SCSIOP_READ_DISK_INFORMATION = 0x51
SCSIOP_READ_DISC_INFORMATION = 0x51  # proper use of disc over disk
SCSIOP_READ_TRACK_INFORMATION = 0x52
SCSIOP_XDWRITE_READ = 0x53
SCSIOP_RESERVE_TRACK_RZONE = 0x53
SCSIOP_SEND_OPC_INFORMATION = 0x54  # optimum power calibration
SCSIOP_MODE_SELECT10 = 0x55
SCSIOP_RESERVE_UNIT10 = 0x56
SCSIOP_RESERVE_ELEMENT = 0x56
SCSIOP_RELEASE_UNIT10 = 0x57
SCSIOP_RELEASE_ELEMENT = 0x57
SCSIOP_REPAIR_TRACK = 0x58
SCSIOP_MODE_SENSE10 = 0x5A
SCSIOP_CLOSE_TRACK_SESSION = 0x5B
SCSIOP_READ_BUFFER_CAPACITY = 0x5C
SCSIOP_SEND_CUE_SHEET = 0x5D
SCSIOP_PERSISTENT_RESERVE_IN = 0x5E
SCSIOP_PERSISTENT_RESERVE_OUT = 0x5F

# 12-byte commands
SCSIOP_REPORT_LUNS = 0xA0
SCSIOP_BLANK = 0xA1
SCSIOP_ATA_PASSTHROUGH12 = 0xA1
SCSIOP_SEND_EVENT = 0xA2
SCSIOP_SECURITY_PROTOCOL_IN = 0xA2
SCSIOP_SEND_KEY = 0xA3
SCSIOP_MAINTENANCE_IN = 0xA3
SCSIOP_REPORT_KEY = 0xA4
SCSIOP_MAINTENANCE_OUT = 0xA4
SCSIOP_MOVE_MEDIUM = 0xA5
SCSIOP_LOAD_UNLOAD_SLOT = 0xA6
SCSIOP_EXCHANGE_MEDIUM = 0xA6
SCSIOP_SET_READ_AHEAD = 0xA7
SCSIOP_MOVE_MEDIUM_ATTACHED = 0xA7
SCSIOP_READ12 = 0xA8
SCSIOP_GET_MESSAGE = 0xA8
SCSIOP_SERVICE_ACTION_OUT12 = 0xA9
SCSIOP_WRITE12 = 0xAA
SCSIOP_SEND_MESSAGE = 0xAB
SCSIOP_SERVICE_ACTION_IN12 = 0xAB
SCSIOP_GET_PERFORMANCE = 0xAC
SCSIOP_READ_DVD_STRUCTURE = 0xAD
SCSIOP_WRITE_VERIFY12 = 0xAE
SCSIOP_VERIFY12 = 0xAF
SCSIOP_SEARCH_DATA_HIGH12 = 0xB0
SCSIOP_SEARCH_DATA_EQUAL12 = 0xB1
SCSIOP_SEARCH_DATA_LOW12 = 0xB2
SCSIOP_SET_LIMITS12 = 0xB3
SCSIOP_READ_ELEMENT_STATUS_ATTACHED = 0xB4
SCSIOP_REQUEST_VOL_ELEMENT = 0xB5
SCSIOP_SECURITY_PROTOCOL_OUT = 0xB5
SCSIOP_SEND_VOLUME_TAG = 0xB6
SCSIOP_SET_STREAMING = 0xB6  # C/DVD
SCSIOP_READ_DEFECT_DATA = 0xB7
SCSIOP_READ_ELEMENT_STATUS = 0xB8
SCSIOP_READ_CD_MSF = 0xB9
SCSIOP_SCAN_CD = 0xBA
SCSIOP_REDUNDANCY_GROUP_IN = 0xBA
SCSIOP_SET_CD_SPEED = 0xBB
SCSIOP_REDUNDANCY_GROUP_OUT = 0xBB
SCSIOP_PLAY_CD = 0xBC
SCSIOP_SPARE_IN = 0xBC
SCSIOP_MECHANISM_STATUS = 0xBD
SCSIOP_SPARE_OUT = 0xBD
SCSIOP_READ_CD = 0xBE
SCSIOP_VOLUME_SET_IN = 0xBE
SCSIOP_SEND_DVD_STRUCTURE = 0xBF
SCSIOP_VOLUME_SET_OUT = 0xBF
SCSIOP_INIT_ELEMENT_RANGE = 0xE7

# 16-byte commands
SCSIOP_XDWRITE_EXTENDED16 = 0x80  # disk
SCSIOP_WRITE_FILEMARKS16 = 0x80  # tape
SCSIOP_REBUILD16 = 0x81  # disk
SCSIOP_READ_REVERSE16 = 0x81  # tape
SCSIOP_REGENERATE16 = 0x82  # disk
SCSIOP_EXTENDED_COPY = 0x83
SCSIOP_POPULATE_TOKEN = 0x83  # disk
SCSIOP_WRITE_USING_TOKEN = 0x83  # disk
SCSIOP_RECEIVE_COPY_RESULTS = 0x84
SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION = 0x84  # disk
SCSIOP_ATA_PASSTHROUGH16 = 0x85
SCSIOP_ACCESS_CONTROL_IN = 0x86
SCSIOP_ACCESS_CONTROL_OUT = 0x87
SCSIOP_READ16 = 0x88
SCSIOP_COMPARE_AND_WRITE = 0x89
SCSIOP_WRITE16 = 0x8A
SCSIOP_READ_ATTRIBUTES = 0x8C
SCSIOP_WRITE_ATTRIBUTES = 0x8D
SCSIOP_WRITE_VERIFY16 = 0x8E
SCSIOP_VERIFY16 = 0x8F
SCSIOP_PREFETCH16 = 0x90
SCSIOP_SYNCHRONIZE_CACHE16 = 0x91
SCSIOP_SPACE16 = 0x91  # tape
SCSIOP_LOCK_UNLOCK_CACHE16 = 0x92
SCSIOP_LOCATE16 = 0x92  # tape
SCSIOP_WRITE_SAME16 = 0x93
SCSIOP_ERASE16 = 0x93  # tape
SCSIOP_ZBC_OUT = 0x94  # Close Zone, Finish Zone, Open Zone, Reset Write Pointer, etc.
SCSIOP_ZBC_IN = 0x95  # Report Zones, etc.
SCSIOP_READ_DATA_BUFF16 = 0x9B
SCSIOP_READ_CAPACITY16 = 0x9E
SCSIOP_GET_LBA_STATUS = 0x9E
SCSIOP_GET_PHYSICAL_ELEMENT_STATUS = 0x9E
SCSIOP_REMOVE_ELEMENT_AND_TRUNCATE = 0x9E
SCSIOP_SERVICE_ACTION_IN16 = 0x9E
SCSIOP_SERVICE_ACTION_OUT16 = 0x9F


# 32-byte commands
SCSIOP_OPERATION32 = 0x7F


# SCSIOP_SANITIZE - 0x48

SERVICE_ACTION_OVERWRITE = 0x01
SERVICE_ACTION_BLOCK_ERASE = 0x02
SERVICE_ACTION_CRYPTO_ERASE = 0x03
SERVICE_ACTION_EXIT_FAILURE = 0x1F


# SCSIOP_OPERATION32 - 0x7F

SERVICE_ACTION_XDWRITE = 0x0004
SERVICE_ACTION_XPWRITE = 0x0006
SERVICE_ACTION_XDWRITEREAD = 0x0007
SERVICE_ACTION_WRITE = 0x000B
SERVICE_ACTION_WRITE_VERIFY = 0x000C
SERVICE_ACTION_WRITE_SAME = 0x000D
SERVICE_ACTION_ORWRITE = 0x000E

# SCSIOP_POPULATE_TOKEN, SCSIOP_WRITE_USING_TOKEN - 0x83

SERVICE_ACTION_POPULATE_TOKEN = 0x10
SERVICE_ACTION_WRITE_USING_TOKEN = 0x11

# SCSIOP_RECEIVE_ROD_TOKEN_INFORMATION - 0x84

SERVICE_ACTION_RECEIVE_TOKEN_INFORMATION = 0x07

# SCSIOP_ZBC_OUT - 0x94

SERVICE_ACTION_CLOSE_ZONE = 0x01
SERVICE_ACTION_FINISH_ZONE = 0x02
SERVICE_ACTION_OPEN_ZONE = 0x03
SERVICE_ACTION_RESET_WRITE_POINTER = 0x04

# SCSIOP_ZBC_IN - 0x95

SERVICE_ACTION_REPORT_ZONES = 0x00

REPORT_ZONES_OPTION_LIST_ALL_ZONES = 0x00
REPORT_ZONES_OPTION_LIST_EMPTY_ZONES = 0x01
REPORT_ZONES_OPTION_LIST_IMPLICITLY_OPENED_ZONES = 0x02
REPORT_ZONES_OPTION_LIST_EXPLICITLY_OPENED_ZONES = 0x03
REPORT_ZONES_OPTION_LIST_CLOSED_ZONES = 0x04
REPORT_ZONES_OPTION_LIST_FULL_ZONES = 0x05
REPORT_ZONES_OPTION_LIST_READ_ONLY_ZONES = 0x06
REPORT_ZONES_OPTION_LIST_OFFLINE_ZONES = 0x07

REPORT_ZONES_OPTION_LIST_RWP_ZONES = 0x10
REPORT_ZONES_OPTION_LIST_NON_SEQUENTIAL_WRITE_RESOURCES_ACTIVE_ZONES = 0x11

REPORT_ZONES_OPTION_LIST_NOT_WRITE_POINTER_ZONES = 0x3F

# SCSIOP_SERVICE_ACTION_IN16 - 0x9E

SERVICE_ACTION_READ_CAPACITY16 = 0x10
SERVICE_ACTION_GET_LBA_STATUS = 0x12
SERVICE_ACTION_GET_PHYSICAL_ELEMENT_STATUS = 0x17
SERVICE_ACTION_REMOVE_ELEMENT_AND_TRUNCATE = 0x18

# SCSIOP_MAINTENANCE_IN - 0xA3

SERVICE_ACTION_REPORT_TIMESTAMP = 0x0F
SERVICE_ACTION_REPORT_SUPPORTED_OPERATION_CODES = 0x0C

# SCSIOP_MAINTENANCE_OUT - 0xA4

SERVICE_ACTION_SET_TIMESTAMP = 0x0F

# If the IMMED bit is 1, status is returned as soon
# as the operation is initiated. If the IMMED bit
# is 0, status is not returned until the operation
# is completed.

CDB_RETURN_ON_COMPLETION = 0
CDB_RETURN_IMMEDIATE = 1

# end_ntminitape

# CDB Force media access used in extended read and write commands.

CDB_FORCE_MEDIA_ACCESS = 0x08

# Denon CD ROM operation codes

SCSIOP_DENON_EJECT_DISC = 0xE6
SCSIOP_DENON_STOP_AUDIO = 0xE7
SCSIOP_DENON_PLAY_AUDIO = 0xE8
SCSIOP_DENON_READ_TOC = 0xE9
SCSIOP_DENON_READ_SUBCODE = 0xEB

# SCSI Bus Messages

SCSIMESS_ABORT = 0x06
SCSIMESS_ABORT_WITH_TAG = 0x0D
SCSIMESS_BUS_DEVICE_RESET = 0x0C
SCSIMESS_CLEAR_QUEUE = 0x0E
SCSIMESS_COMMAND_COMPLETE = 0x00
SCSIMESS_DISCONNECT = 0x04
SCSIMESS_EXTENDED_MESSAGE = 0x01
SCSIMESS_IDENTIFY = 0x80
SCSIMESS_IDENTIFY_WITH_DISCON = 0xC0
SCSIMESS_IGNORE_WIDE_RESIDUE = 0x23
SCSIMESS_INITIATE_RECOVERY = 0x0F
SCSIMESS_INIT_DETECTED_ERROR = 0x05
SCSIMESS_LINK_CMD_COMP = 0x0A
SCSIMESS_LINK_CMD_COMP_W_FLAG = 0x0B
SCSIMESS_MESS_PARITY_ERROR = 0x09
SCSIMESS_MESSAGE_REJECT = 0x07
SCSIMESS_NO_OPERATION = 0x08
SCSIMESS_HEAD_OF_QUEUE_TAG = 0x21
SCSIMESS_ORDERED_QUEUE_TAG = 0x22
SCSIMESS_SIMPLE_QUEUE_TAG = 0x20
SCSIMESS_RELEASE_RECOVERY = 0x10
SCSIMESS_RESTORE_POINTERS = 0x03
SCSIMESS_SAVE_DATA_POINTER = 0x02
SCSIMESS_TERMINATE_IO_PROCESS = 0x11

# SCSI Extended Message operation codes

SCSIMESS_MODIFY_DATA_POINTER = 0x00
SCSIMESS_SYNCHRONOUS_DATA_REQ = 0x01
SCSIMESS_WIDE_DATA_REQUEST = 0x03

# SCSI Extended Message Lengths

SCSIMESS_MODIFY_DATA_LENGTH = 5
SCSIMESS_SYNCH_DATA_LENGTH = 3
SCSIMESS_WIDE_DATA_LENGTH = 2

# SCSI extended message structure

_pack_ += 1


class SCSI_EXTENDED_MESSAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("InitialMessageCode", UCHAR),
        ("MessageLength", UCHAR),
        ("MessageType", UCHAR),
        (
            "ExtendedArguments",
            make_struct(
                [
                    (
                        "Modify",
                        make_struct(
                            [
                                ("Modifier", UCHAR * 4),
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Synchronous",
                        make_struct(
                            [
                                ("TransferPeriod", UCHAR),
                                ("ReqAckOffset", UCHAR),
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Wide",
                        make_struct(
                            [
                                ("Width", UCHAR),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),  # EXTENDED_ARGUMENTS
    ]


PSCSI_EXTENDED_MESSAGE = POINTER(SCSI_EXTENDED_MESSAGE)
_pack_ -= 1

# SCSI bus status codes.

SCSISTAT_GOOD = 0x00
SCSISTAT_CHECK_CONDITION = 0x02
SCSISTAT_CONDITION_MET = 0x04
SCSISTAT_BUSY = 0x08
SCSISTAT_INTERMEDIATE = 0x10
SCSISTAT_INTERMEDIATE_COND_MET = 0x14
SCSISTAT_RESERVATION_CONFLICT = 0x18
SCSISTAT_COMMAND_TERMINATED = 0x22
SCSISTAT_QUEUE_FULL = 0x28

# Enable Vital Product Data Flag (EVPD)
# used with INQUIRY command.

CDB_INQUIRY_EVPD = 0x01

# Defines for format CDB

LUN0_FORMAT_SAVING_DEFECT_LIST = 0
USE_DEFAULTMSB = 0
USE_DEFAULTLSB = 0

START_UNIT_CODE = 0x01
STOP_UNIT_CODE = 0x00

# begin_ntminitape

# Inquiry buffer structure. This is the data returned from the target
# after it receives an inquiry.
# This structure may be extended by the number of bytes specified
# in the field AdditionalLength. The defined size constant only
# includes fields through ProductRevisionLevel.
# The NT SCSI drivers are only interested in the first 36 bytes of data.

INQUIRYDATABUFFERSIZE = 36

VERSION_DESCRIPTOR = USHORT
PVERSION_DESCRIPTOR = POINTER(USHORT)


# if (NTDDI_VERSION < NTDDI_WINXP)
class INQUIRYDATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("DeviceTypeModifier", UCHAR, 7),
        ("RemovableMedia", UCHAR, 1),
        ("Versions", UCHAR),
        ("ResponseDataFormat", UCHAR, 4),
        ("HiSupport", UCHAR, 1),
        ("NormACA", UCHAR, 1),
        ("ReservedBit", UCHAR, 1),
        ("AERC", UCHAR, 1),
        ("AdditionalLength", UCHAR),
        ("Reserved", UCHAR * 2),
        ("SoftReset", UCHAR, 1),
        ("CommandQueue", UCHAR, 1),
        ("Reserved2", UCHAR, 1),
        ("LinkedCommands", UCHAR, 1),
        ("Synchronous", UCHAR, 1),
        ("Wide16Bit", UCHAR, 1),
        ("Wide32Bit", UCHAR, 1),
        ("RelativeAddressing", UCHAR, 1),
        ("VendorId", UCHAR * 8),
        ("ProductId", UCHAR * 16),
        ("ProductRevisionLevel", UCHAR * 4),
        ("VendorSpecific", UCHAR * 20),
        ("Reserved3", UCHAR * 2),
        ("VersionDescriptors", VERSION_DESCRIPTOR * 8),
        ("Reserved4", UCHAR * 30),
    ]


PINQUIRYDATA = POINTER(INQUIRYDATA)
# else
_pack_ += 1


class INQUIRYDATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("DeviceTypeModifier", UCHAR, 7),
        ("RemovableMedia", UCHAR, 1),
        (
            "_unnamed_union",
            make_union(
                [
                    ("Versions", UCHAR),
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("ANSIVersion", UCHAR, 3),
                                ("ECMAVersion", UCHAR, 3),
                                ("ISOVersion", UCHAR, 2),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        ("ResponseDataFormat", UCHAR, 4),
        ("HiSupport", UCHAR, 1),
        ("NormACA", UCHAR, 1),
        ("TerminateTask", UCHAR, 1),
        ("AERC", UCHAR, 1),
        ("AdditionalLength", UCHAR),
        (
            "_unnamed_union",
            make_union(
                [
                    ("Reserved", UCHAR),
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("PROTECT", UCHAR, 1),
                                ("Reserved_1", UCHAR, 2),
                                ("ThirdPartyCoppy", UCHAR, 1),
                                ("TPGS", UCHAR, 2),
                                ("ACC", UCHAR, 1),
                                ("SCCS", UCHAR, 1),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        ("Addr16", UCHAR, 1),  # defined only for SIP devices.
        ("Addr32", UCHAR, 1),  # defined only for SIP devices.
        ("AckReqQ", UCHAR, 1),  # defined only for SIP devices.
        ("MediumChanger", UCHAR, 1),
        ("MultiPort", UCHAR, 1),
        ("ReservedBit2", UCHAR, 1),
        ("EnclosureServices", UCHAR, 1),
        ("ReservedBit3", UCHAR, 1),
        ("SoftReset", UCHAR, 1),
        ("CommandQueue", UCHAR, 1),
        ("TransferDisable", UCHAR, 1),  # defined only for SIP devices.
        ("LinkedCommands", UCHAR, 1),
        ("Synchronous", UCHAR, 1),  # defined only for SIP devices.
        ("Wide16Bit", UCHAR, 1),  # defined only for SIP devices.
        ("Wide32Bit", UCHAR, 1),  # defined only for SIP devices.
        ("RelativeAddressing", UCHAR, 1),
        ("VendorId", UCHAR * 8),
        ("ProductId", UCHAR * 16),
        ("ProductRevisionLevel", UCHAR * 4),
        ("VendorSpecific", UCHAR * 20),
        ("Reserved3", UCHAR * 2),
        ("VersionDescriptors", VERSION_DESCRIPTOR * 8),
        ("Reserved4", UCHAR * 30),
    ]


PINQUIRYDATA = POINTER(INQUIRYDATA)
_pack_ -= 1
# endif

# define OFFSET_VER_DESCRIPTOR_ONE       (FIELD_OFFSET(INQUIRYDATA, VersionDescriptors[0]))
# define OFFSET_VER_DESCRIPTOR_EIGHT     (FIELD_OFFSET(INQUIRYDATA, VersionDescriptors[8]))

# Inquiry defines. Used to interpret data returned from target as result
# of inquiry command.
# DeviceType field

DIRECT_ACCESS_DEVICE = 0x00  # disks
SEQUENTIAL_ACCESS_DEVICE = 0x01  # tapes
PRINTER_DEVICE = 0x02  # printers
PROCESSOR_DEVICE = 0x03  # scanners, printers, etc
WRITE_ONCE_READ_MULTIPLE_DEVICE = 0x04  # worms
READ_ONLY_DIRECT_ACCESS_DEVICE = 0x05  # cdroms
SCANNER_DEVICE = 0x06  # scanners
OPTICAL_DEVICE = 0x07  # optical disks
MEDIUM_CHANGER = 0x08  # jukebox
COMMUNICATION_DEVICE = 0x09  # network
# 0xA and 0xB are obsolete
ARRAY_CONTROLLER_DEVICE = 0x0C
SCSI_ENCLOSURE_DEVICE = 0x0D
REDUCED_BLOCK_DEVICE = 0x0E  # e.g., 1394 disk
OPTICAL_CARD_READER_WRITER_DEVICE = 0x0F
BRIDGE_CONTROLLER_DEVICE = 0x10
OBJECT_BASED_STORAGE_DEVICE = 0x11  # OSD
HOST_MANAGED_ZONED_BLOCK_DEVICE = 0x14  # Host managed zoned block device
UNKNOWN_OR_NO_DEVICE = 0x1F  # Unknown or no device type
LOGICAL_UNIT_NOT_PRESENT_DEVICE = 0x7F
DEVICE_QUALIFIER_ACTIVE = 0x00
DEVICE_QUALIFIER_NOT_ACTIVE = 0x01
DEVICE_QUALIFIER_NOT_SUPPORTED = 0x03

# DeviceTypeQualifier field

DEVICE_CONNECTED = 0x00

# Vital Product Data Pages

# Unit Serial Number Page (page code 0x80)
# Provides a product serial number for the target or the logical unit.
_pack_ += 1


class VPD_MEDIA_SERIAL_NUMBER_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),
        ("Reserved", UCHAR),
        ("PageLength", UCHAR),
        # if !defined(__midl)
        ("SerialNumber", UCHAR * 0),
        # endif
    ]


PVPD_MEDIA_SERIAL_NUMBER_PAGE = POINTER(VPD_MEDIA_SERIAL_NUMBER_PAGE)
_pack_ -= 1

_pack_ += 1


class VPD_SERIAL_NUMBER_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),
        ("Reserved", UCHAR),
        ("PageLength", UCHAR),
        # if !defined(__midl)
        ("SerialNumber", UCHAR * 0),
        # endif
    ]


PVPD_SERIAL_NUMBER_PAGE = POINTER(VPD_SERIAL_NUMBER_PAGE)
_pack_ -= 1

# Device Identification Page (page code 0x83)
# Provides the means to retrieve zero or more identification descriptors
# applying to the logical unit.

_pack_ += 1


class VPD_CODE_SET(CEnum):
    VpdCodeSetReserved = 0
    VpdCodeSetBinary = 1
    VpdCodeSetAscii = 2
    VpdCodeSetUTF8 = 3


PVPD_CODE_SET = POINTER(VPD_CODE_SET)


class VPD_ASSOCIATION(CEnum):
    VpdAssocDevice = 0
    VpdAssocPort = 1
    VpdAssocTarget = 2
    VpdAssocReserved1 = 3
    VpdAssocReserved2 = 4  # bogus, only two bits


PVPD_ASSOCIATION = POINTER(VPD_ASSOCIATION)


class VPD_IDENTIFIER_TYPE(CEnum):
    VpdIdentifierTypeVendorSpecific = 0
    VpdIdentifierTypeVendorId = 1
    VpdIdentifierTypeEUI64 = 2
    VpdIdentifierTypeFCPHName = 3
    VpdIdentifierTypePortRelative = 4
    VpdIdentifierTypeTargetPortGroup = 5
    VpdIdentifierTypeLogicalUnitGroup = 6
    VpdIdentifierTypeMD5LogicalUnitId = 7
    VpdIdentifierTypeSCSINameString = 8


PVPD_IDENTIFIER_TYPE = POINTER(VPD_IDENTIFIER_TYPE)


class VPD_IDENTIFICATION_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CodeSet", UCHAR, 4),  # VPD_CODE_SET
        ("Reserved", UCHAR, 4),
        ("IdentifierType", UCHAR, 4),  # VPD_IDENTIFIER_TYPE
        ("Association", UCHAR, 2),
        ("Reserved2", UCHAR, 2),
        ("Reserved3", UCHAR),
        ("IdentifierLength", UCHAR),
        # if !defined(__midl)
        ("Identifier", UCHAR * 0),
        # endif
    ]


PVPD_IDENTIFICATION_DESCRIPTOR = POINTER(VPD_IDENTIFICATION_DESCRIPTOR)


class VPD_IDENTIFICATION_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),
        ("Reserved", UCHAR),
        ("PageLength", UCHAR),
        # The following field is actually a variable length array of identification
        # descriptors.  Unfortunately there's no C notation for an array of
        # variable length structures so we're forced to just pretend.
        # if !defined(__midl)
        # VPD_IDENTIFICATION_DESCRIPTOR Descriptors[0];
        ("Descriptors", UCHAR * 0),
        # endif
    ]


PVPD_IDENTIFICATION_PAGE = POINTER(VPD_IDENTIFICATION_PAGE)


# VPD Page 0x86, Extended INQUIRY Data
class VPD_EXTENDED_INQUIRY_DATA_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 86h
        ("PageLength", UCHAR * 2),  # [0] - 00h, [1] - 3Ch
        ("RefChk", UCHAR, 1),  # byte 4 bit 0
        ("AppChk", UCHAR, 1),
        ("GrdChk", UCHAR, 1),
        ("Spt", UCHAR, 3),
        ("ActivateMicrocode", UCHAR, 2),
        ("SimpSup", UCHAR, 1),  # byte 5 bit 0
        ("OrdSup", UCHAR, 1),
        ("HeadSup", UCHAR, 1),
        ("PriorSup", UCHAR, 1),
        ("GroupSup", UCHAR, 1),
        ("UaskSup", UCHAR, 1),
        ("Reserved0", UCHAR, 2),
        ("VSup", UCHAR, 1),  # byte 6 bit 0
        ("NvSup", UCHAR, 1),
        ("Obsolete0", UCHAR, 1),
        ("WuSup", UCHAR, 1),
        ("Reserved1", UCHAR, 4),
        ("LuiClr", UCHAR, 1),  # byte 7 bit 0
        ("Reserved2", UCHAR, 3),
        ("PiiSup", UCHAR, 1),
        ("NoPiChk", UCHAR, 1),
        ("Reserved3", UCHAR, 2),
        ("Obsolete1", UCHAR, 1),  # byte 8 bit 0
        ("HssRelef", UCHAR, 1),
        ("Reserved4", UCHAR, 1),
        ("RtdSup", UCHAR, 1),
        ("RSup", UCHAR, 1),
        ("LuCollectionType", UCHAR, 3),
        ("Multi_i_t_Nexus_Microcode_Download", UCHAR, 4),  # byte 9 bit 0
        ("Reserved5", UCHAR, 4),
        ("ExtendedSelfTestCompletionMinutes", UCHAR * 2),
        ("Reserved6", UCHAR, 5),  # byte 12 bit 0
        ("VsaSup", UCHAR, 1),
        ("HraSup", UCHAR, 1),
        ("PoaSup", UCHAR, 1),
        ("MaxSupportedSenseDataLength", UCHAR),
        ("Nrd0", UCHAR, 1),  # byte 14 bit 0
        ("Nrd1", UCHAR, 1),
        ("Sac", UCHAR, 1),
        ("Reserved7", UCHAR, 3),
        ("Ias", UCHAR, 1),
        ("Ibs", UCHAR, 1),
        ("MaxInquiryChangeLogs", UCHAR * 2),
        ("MaxModePageChangeLogs", UCHAR * 2),
        ("Reserved8", UCHAR * 45),
    ]


PVPD_EXTENDED_INQUIRY_DATA_PAGE = POINTER(VPD_EXTENDED_INQUIRY_DATA_PAGE)


# VPD Page 0x89, ATA Information
class VPD_ATA_INFORMATION_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0x89
        ("PageLength", UCHAR * 2),  # 0x238 fixed size
        ("Reserved0", UCHAR * 4),
        ("VendorId", UCHAR * 8),
        ("ProductId", UCHAR * 16),
        ("ProductRevisionLevel", UCHAR * 4),
        ("DeviceSignature", UCHAR * 20),
        ("CommandCode", UCHAR),
        ("Reserved1", UCHAR * 3),
        ("IdentifyDeviceData", UCHAR * 512),
    ]


PVPD_ATA_INFORMATION_PAGE = POINTER(VPD_ATA_INFORMATION_PAGE)


# if (NTDDI_VERSION >= NTDDI_WIN8)
# VPD Page 0x8F, Third Party Copy
class VPD_THIRD_PARTY_COPY_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0x8F
        ("PageLength", UCHAR * 2),  # at least 0x24 if target supports Windows Offload Data Transfers
        # if !defined(__midl)
        ("ThirdPartyCopyDescriptors", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


PVPD_THIRD_PARTY_COPY_PAGE = POINTER(VPD_THIRD_PARTY_COPY_PAGE)


class WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DescriptorType", UCHAR * 2),  # 0x00
        ("DescriptorLength", UCHAR * 2),  # 0x20
        ("VendorSpecific", UCHAR * 6),
        ("MaximumRangeDescriptors", UCHAR * 2),
        ("MaximumInactivityTimer", UCHAR * 4),
        ("DefaultInactivityTimer", UCHAR * 4),
        ("MaximumTokenTransferSize", UCHAR * 8),
        ("OptimalTransferCount", UCHAR * 8),
    ]


PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR = POINTER(WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR)

BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR_TYPE_WINDOWS = 0x00

# endif #(NTDDI_VERSION >= NTDDI_WIN8)


# VPD Page 0xB0, Block Limits
class VPD_BLOCK_LIMITS_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0xB0
        ("PageLength", UCHAR * 2),  # 0x3C
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("Reserved0", UCHAR),
                                ("MaximumCompareAndWriteLength", UCHAR),
                                ("OptimalTransferLengthGranularity", UCHAR * 2),
                                ("MaximumTransferLength", UCHAR * 4),
                                ("OptimalTransferLength", UCHAR * 4),
                                ("MaxPrefetchXDReadXDWriteTransferLength", UCHAR * 4),
                                ("MaximumUnmapLBACount", UCHAR * 4),
                                ("MaximumUnmapBlockDescriptorCount", UCHAR * 4),
                                ("OptimalUnmapGranularity", UCHAR * 4),
                                (
                                    "_unnamed_union",
                                    make_union(
                                        [
                                            (
                                                "_unnamed_struct",
                                                make_struct(
                                                    [
                                                        ("UnmapGranularityAlignmentByte3", UCHAR, 7),
                                                        ("UGAValid", UCHAR, 1),
                                                        ("UnmapGranularityAlignmentByte2", UCHAR),
                                                        ("UnmapGranularityAlignmentByte1", UCHAR),
                                                        ("UnmapGranularityAlignmentByte0", UCHAR),
                                                    ],
                                                    _pack_,
                                                ),
                                            ),
                                            ("UnmapGranularityAlignment", UCHAR * 4),
                                        ],
                                        _pack_,
                                    ),
                                ),
                                ("Reserved1", UCHAR * 28),
                            ],
                            _pack_,
                        ),
                    ),
                    # if !defined(__midl)
                    ("Descriptors", UCHAR * 0),
                    # endif
                ],
                _pack_,
            ),
        ),
    ]


PVPD_BLOCK_LIMITS_PAGE = POINTER(VPD_BLOCK_LIMITS_PAGE)

# VPD Page 0xB1, Block Device Characteristics
ZONED_CAPABILITIES_NOT_REPORTED = 0x0
ZONED_CAPABILITIES_HOST_AWARE = 0x1
ZONED_CAPABILITIES_DEVICE_MANAGED = 0x2


class VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0xB1
        ("Reserved0", UCHAR),
        ("PageLength", UCHAR),  # 0x3C
        ("MediumRotationRateMsb", UCHAR),
        ("MediumRotationRateLsb", UCHAR),
        ("MediumProductType", UCHAR),
        ("NominalFormFactor", UCHAR, 4),
        ("WACEREQ", UCHAR, 2),
        ("WABEREQ", UCHAR, 2),
        ("VBULS", UCHAR, 1),
        ("FUAB", UCHAR, 1),
        ("BOCS", UCHAR, 1),
        ("Reserved1", UCHAR, 1),
        ("ZONED", UCHAR, 2),
        ("Reserved2", UCHAR, 2),
        ("Reserved3", UCHAR * 3),
        ("DepopulationTime", UCHAR * 4),
        ("Reserved4", UCHAR * 48),
    ]


PVPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE = POINTER(VPD_BLOCK_DEVICE_CHARACTERISTICS_PAGE)

# VPD Page 0xB2, Logical Block Provisioning

PROVISIONING_TYPE_UNKNOWN = 0x0
PROVISIONING_TYPE_RESOURCE = 0x1
PROVISIONING_TYPE_THIN = 0x2


class VPD_LOGICAL_BLOCK_PROVISIONING_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0xB2
        ("PageLength", UCHAR * 2),
        ("ThresholdExponent", UCHAR),
        ("DP", UCHAR, 1),
        ("ANC_SUP", UCHAR, 1),
        ("LBPRZ", UCHAR, 1),
        ("Reserved0", UCHAR, 2),
        ("LBPWS10", UCHAR, 1),
        ("LBPWS", UCHAR, 1),
        ("LBPU", UCHAR, 1),
        ("ProvisioningType", UCHAR, 3),
        ("Reserved1", UCHAR, 5),
        ("Reserved2", UCHAR),
        # if !defined(__midl)
        ("ProvisioningGroupDescr", UCHAR * 0),
        # endif
    ]


PVPD_LOGICAL_BLOCK_PROVISIONING_PAGE = POINTER(VPD_LOGICAL_BLOCK_PROVISIONING_PAGE)

# VPD Page 0xB6, Zoned Block Device Characteristics


class VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),  # 0xB6
        ("PageLength", UCHAR * 2),  # 0x3C
        ("URSWRZ", UCHAR, 1),  # Unrestricted Read in Sequential Write Required Zone
        ("Reserved1", UCHAR, 7),
        ("Reserved2", UCHAR * 3),
        ("OptimalNumberOfOpenSequentialWritePreferredZone", UCHAR * 4),
        ("OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone", UCHAR * 4),
        ("MaxNumberOfOpenSequentialWriteRequiredZone", UCHAR * 4),
        ("Reserved3", UCHAR * 44),
    ]


PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE = POINTER(VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE)


# Supported Vital Product Data Pages Page (page code 0x00)
# Contains a list of the vital product data page cods supported by the target
# or logical unit.


class VPD_SUPPORTED_PAGES_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DeviceType", UCHAR, 5),
        ("DeviceTypeQualifier", UCHAR, 3),
        ("PageCode", UCHAR),
        ("Reserved", UCHAR),
        ("PageLength", UCHAR),
        # if !defined(__midl)
        ("SupportedPageList", UCHAR * 0),
        # endif
    ]


PVPD_SUPPORTED_PAGES_PAGE = POINTER(VPD_SUPPORTED_PAGES_PAGE)
_pack_ -= 1


VPD_MAX_BUFFER_SIZE = 0xFF

VPD_SUPPORTED_PAGES = 0x00
VPD_SERIAL_NUMBER = 0x80
VPD_DEVICE_IDENTIFIERS = 0x83
VPD_MEDIA_SERIAL_NUMBER = 0x84
VPD_SOFTWARE_INTERFACE_IDENTIFIERS = 0x84
VPD_NETWORK_MANAGEMENT_ADDRESSES = 0x85
VPD_EXTENDED_INQUIRY_DATA = 0x86
VPD_MODE_PAGE_POLICY = 0x87
VPD_SCSI_PORTS = 0x88
VPD_ATA_INFORMATION = 0x89

VPD_THIRD_PARTY_COPY = 0x8F
VPD_BLOCK_LIMITS = 0xB0
VPD_BLOCK_DEVICE_CHARACTERISTICS = 0xB1
VPD_LOGICAL_BLOCK_PROVISIONING = 0xB2
VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS = 0xB6


#
# Log page definitions

LOG_PAGE_CODE_SUPPORTED_LOG_PAGES = 0x00
LOG_PAGE_CODE_WRITE_ERROR_COUNTERS = 0x02
LOG_PAGE_CODE_READ_ERROR_COUNTERS = 0x03
LOG_PAGE_CODE_LOGICAL_BLOCK_PROVISIONING = 0x0C
LOG_PAGE_CODE_TEMPERATURE = 0x0D
LOG_PAGE_CODE_ENVIRONMENTAL_REPORTING = 0x0D
LOG_PAGE_CODE_STARTSTOP_CYCLE_COUNTERS = 0x0E
LOG_PAGE_CODE_UTILIZATION = 0x0E
LOG_PAGE_CODE_SELFTEST_RESULTS = 0x10
LOG_PAGE_CODE_SOLID_STATE_MEDIA = 0x11
LOG_PAGE_CODE_BACKGROUND_SCAN_RESULTS = 0x15
LOG_PAGE_CODE_PERFORMANCE_AND_STATISTICS = 0x19
LOG_PAGE_CODE_INFORMATIONAL_EXCEPTIONS = 0x2F

LOG_SUBPAGE_CODE_WRITE_ERROR_COUNTERS = 0x00
LOG_SUBPAGE_CODE_READ_ERROR_COUNTERS = 0x00
LOG_SUBPAGE_CODE_LOGICAL_BLOCK_PROVISIONING = 0x00
LOG_SUBPAGE_CODE_TEMPERATURE = 0x00
LOG_SUBPAGE_CODE_ENVIRONMENTAL_REPORTING = 0x01
LOG_SUBPAGE_CODE_STARTSTOP_CYCLE_COUNTERS = 0x00
LOG_SUBPAGE_CODE_UTILIZATION = 0x01
LOG_SUBPAGE_CODE_SELFTEST_RESULTS = 0x00
LOG_SUBPAGE_CODE_SOLID_STATE_MEDIA = 0x00
LOG_SUBPAGE_CODE_BACKGROUND_SCAN_RESULTS = 0x00
LOG_SUBPAGE_CODE_INFORMATIONAL_EXCEPTIONS = 0x00
LOG_SUBPAGE_CODE_COMMAND_DURATION_LIMIT_STATISTICS = 0x21
LOG_SUBPAGE_CODE_SUPPORTED_SUBPAGES = 0xFF

_pack_ += 1


class LOG_PARAMETER_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ParameterCode", UCHAR * 2),  # Bytes 0-1
        (
            "_unnamed_union",
            make_union(
                [
                    ("ControlByte", UCHAR),  # Byte  2
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("FormatAndLinking", UCHAR, 2),  # Byte  2, bit 0-1
                                ("TMC", UCHAR, 2),  # Byte  2, bit 2-3
                                ("ETC", UCHAR, 1),  # Byte  2, bit 4
                                ("TSD", UCHAR, 1),  # Byte  2, bit 5
                                ("Obsolete", UCHAR, 1),  # Byte  2, bit 6
                                ("DU", UCHAR, 1),  # Byte  2, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        ("ParameterLength", UCHAR),  # Byte  3
    ]


PLOG_PARAMETER_HEADER = POINTER(LOG_PARAMETER_HEADER)


class LOG_PARAMETER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", LOG_PARAMETER_HEADER),  # Bytes 0-3
        (
            "_unnamed_union",
            make_union(
                [
                    # if !defined(__midl)
                    ("AsByte", UCHAR * 0),  # Bytes 4-N
                    # endif
                    (
                        "THRESHOLD_RESOURCE_COUNT",
                        make_struct(
                            [
                                ("ResourceCount", UCHAR * 4),  # Bytes 4-7
                                ("Scope", UCHAR, 2),  # Byte  8, bit 0-1
                                ("Reserved1", UCHAR, 6),  # Byte  8, bit 2-7
                                ("Reserved2", UCHAR * 3),  # Byte  9
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "TEMPERATURE",
                        make_struct(
                            [
                                ("Reserved", UCHAR),  # Byte  4
                                ("Temperature", UCHAR),  # Byte  5
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "DATE_OF_MANUFACTURE",
                        make_struct(
                            [
                                ("Year", UCHAR * 4),  # Bytes 4-7
                                ("Week", UCHAR * 2),  # Bytes 8-9
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "WORKLOAD_UTILIZATION",
                        make_struct(
                            [
                                ("WorkloadUtilization", UCHAR * 2),  # Bytes 4-5
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "SELF_TEST_RESULTS",
                        make_struct(
                            [
                                ("SelfTestResults", UCHAR, 4),  # Byte  4, bit 0-3
                                ("Reserved1", UCHAR, 1),  # Byte  4, bit 4
                                ("SelfTestCode", UCHAR, 3),  # Byte  4, bit 5-7
                                ("SelfTestNumber", UCHAR),  # Byte  5
                                ("PowerOnHours", UCHAR * 2),  # Bytes 6-7
                                ("AddressOfFirstFailure", UCHAR * 8),  # Bytes 8-15
                                ("SenseKey", UCHAR, 4),  # Byte 16, bit 0-3
                                ("Reserved2", UCHAR, 4),  # Byte 16, bit 4-7
                                ("AdditionalSenseCode", UCHAR),  # Byte 17
                                ("AdditionalSenseCodeQualifier", UCHAR),  # Byte 18
                                ("VendorSpecific", UCHAR),  # Byte 19
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "SOLID_STATE_MEDIA",
                        make_struct(
                            [
                                ("Reserved", UCHAR * 3),  # Bytes 4-6
                                ("PercentageUsed", UCHAR),  # Byte  7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "BACKGROUND_SCAN_STATUS",
                        make_struct(
                            [
                                ("PowerOnMinutes", UCHAR * 4),  # Bytes 4-7
                                ("Reserved", UCHAR),  # Byte  8
                                ("ScanStatus", UCHAR),  # Byte  9
                                ("ScansPerformed", UCHAR * 2),  # Bytes 10-11
                                ("ScanProgress", UCHAR * 2),  # Bytes 12-13
                                ("MediumScansPerformed", UCHAR * 2),  # Bytes 14-15
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "INFORMATIONAL_EXCEPTIONS",
                        make_struct(
                            [
                                ("ASC", UCHAR),  # Byte  4
                                ("ASCQ", UCHAR),  # Byte  5
                                ("MostRecentTemperature", UCHAR),  # Byte  6
                                ("VendorSpecific", UCHAR * ANYSIZE_ARRAY),  # Bytes 7-N
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
    ]


PLOG_PARAMETER = POINTER(LOG_PARAMETER)


class LOG_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # Byte  0, bit 0-5
        ("SPF", UCHAR, 1),  # Byte  0, bit 6
        ("DS", UCHAR, 1),  # Byte  0, bit 7
        ("SubPageCode", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        # if !defined(__midl)
        ("Parameters", LOG_PARAMETER * 0),
        # endif
    ]


PLOG_PAGE = POINTER(LOG_PAGE)

_pack_ -= 1


# Logical Block Provisioning resource count parameter codes.
LOG_PAGE_LBP_PARAMETER_CODE_AVAILABLE = 0x1
LOG_PAGE_LBP_PARAMETER_CODE_USED = 0x2

# Logical Block Provisioning resource count scope codes.
LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED = 0x0
LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN = 0x1
LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN = 0x2


# Logical Block Provisioning threshold resource count log page parameter.
class LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", LOG_PARAMETER_HEADER),
        ("ResourceCount", UCHAR * 4),
        ("Scope", UCHAR, 2),
        ("Reserved0", UCHAR, 6),
        ("Reserved1", UCHAR * 3),
    ]


PLOG_PARAMETER_THRESHOLD_RESOURCE_COUNT = POINTER(LOG_PARAMETER_THRESHOLD_RESOURCE_COUNT)


# Logical Block Provisioning log page.
class LOG_PAGE_LOGICAL_BLOCK_PROVISIONING(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x0C
        ("SPF", UCHAR, 1),  # 0
        ("DS", UCHAR, 1),  # 1
        ("SubPageCode", UCHAR),  # 0x00
        ("PageLength", UCHAR * 2),
        # if !defined(__midl)
        ("Parameters", LOG_PARAMETER_HEADER * 0),
        # endif
    ]


PLOG_PAGE_LOGICAL_BLOCK_PROVISIONING = POINTER(LOG_PAGE_LOGICAL_BLOCK_PROVISIONING)


# Optional VERSION DESCRIPTOR fields provide the opportunity for SCSI targets to
# claim conformance with a number of standards. The INQUIRY response can contain
# any number of version descriptors between one and eight. Below values are
# excerpted from table 136 of SPC-4 specification available at http:#www.t10.org
# (backup copies maintained at http:#www.incits.org and # http:#www.ansi.org).

VER_DESCRIPTOR_SPC4_NOVERSION = 0x0460
VER_DESCRIPTOR_SPC4_T10_1731D_R16 = 0x0461
VER_DESCRIPTOR_SPC4_T10_1731D_R18 = 0x0462
VER_DESCRIPTOR_SPC4_T10_1731D_R23 = 0x0463
VER_DESCRIPTOR_SBC3 = 0x04C0

VER_DESCRIPTOR_1667_NOVERSION = 0xFFC0
VER_DESCRIPTOR_1667_2006 = 0xFFC1
VER_DESCRIPTOR_1667_2009 = 0xFFC2

# Persistent Reservation Definitions.

# PERSISTENT_RESERVE_* definitions

RESERVATION_ACTION_READ_KEYS = 0x00
RESERVATION_ACTION_READ_RESERVATIONS = 0x01
RESERVATION_ACTION_REPORT_CAPABILITIES = 0x02
RESERVATION_ACTION_READ_FULL_STATUS = 0x03

RESERVATION_ACTION_REGISTER = 0x00
RESERVATION_ACTION_RESERVE = 0x01
RESERVATION_ACTION_RELEASE = 0x02
RESERVATION_ACTION_CLEAR = 0x03
RESERVATION_ACTION_PREEMPT = 0x04
RESERVATION_ACTION_PREEMPT_ABORT = 0x05
RESERVATION_ACTION_REGISTER_IGNORE_EXISTING = 0x06
RESERVATION_ACTION_REGISTER_AND_MOVE = 0x07
RESERVATION_ACTION_REPLACE_LOST_RESERVATION = 0x08

RESERVATION_SCOPE_LU = 0x00
RESERVATION_SCOPE_ELEMENT = 0x02

RESERVATION_TYPE_WRITE_EXCLUSIVE = 0x01
RESERVATION_TYPE_EXCLUSIVE = 0x03
RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS = 0x05
RESERVATION_TYPE_EXCLUSIVE_REGISTRANTS = 0x06
RESERVATION_TYPE_WRITE_EXCLUSIVE_ALL_REGISTRANTS = 0x07
RESERVATION_TYPE_EXCLUSIVE_ALL_REGISTRANTS = 0x08

# Structures for reserve in command.

_pack_ += 1


class PRI_REGISTRATION_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Generation", UCHAR * 4),
        ("AdditionalLength", UCHAR * 4),
        # if !defined(__midl)
        ("ReservationKeyList", (UCHAR * 0) * 8),
        # endif
    ]


class PRI_RESERVATION_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ReservationKey", UCHAR * 8),
        ("ScopeSpecificAddress", UCHAR * 4),
        ("Reserved", UCHAR),
        ("Type", UCHAR, 4),
        ("Scope", UCHAR, 4),
        ("Obsolete", UCHAR * 2),
    ]


class PRI_RESERVATION_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Generation", UCHAR * 4),
        ("AdditionalLength", UCHAR * 4),
        # if !defined(__midl)
        ("Reservations", PRI_RESERVATION_DESCRIPTOR * 0),
        # endif
    ]


class PRI_FULL_STATUS_DESCRIPTOR_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ReservationKey", UCHAR * 8),
        ("Reserved", UCHAR * 4),
        ("ReservationHolder", UCHAR, 1),
        ("AllTargetPorts", UCHAR, 1),
        ("Reserved1", UCHAR, 6),
        ("Type", UCHAR, 4),
        ("Scope", UCHAR, 4),
        ("Reserved2", UCHAR * 4),
        ("RelativeTargetPortIdentifier", UCHAR * 2),
        ("AdditionalDescriptorLength", UCHAR * 4),
    ]


class PRI_FULL_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", PRI_FULL_STATUS_DESCRIPTOR_HEADER),
        ("TransportID", UCHAR * ANYSIZE_ARRAY),
    ]


class PRI_FULL_STATUS_LIST_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Generation", UCHAR * 4),
        ("AdditionalLength", UCHAR * 4),
    ]


class PRI_FULL_STATUS_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Generation", UCHAR * 4),
        ("AdditionalLength", UCHAR * 4),
        # Since TransportID could be different sizes,
        # we use PRI_FULL_STATUS_DESCRIPTOR_HEADER rather than PRI_FULL_STATUS_DESCRIPTOR
        # as a place holder here.
        ("FullStatusDescriptors", PRI_FULL_STATUS_DESCRIPTOR_HEADER * ANYSIZE_ARRAY),
    ]


class PRI_REPORT_CAPABILITIES(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Length", UCHAR * 2),
        ("PersistThroughPowerLossCapable", UCHAR, 1),
        ("Reserved", UCHAR, 1),
        ("AllTargetPortsCapable", UCHAR, 1),
        ("SpecifyInitiatorPortsCapable", UCHAR, 1),
        ("CompatibleReservationHandling", UCHAR, 1),
        ("Reserved1", UCHAR, 2),
        ("ReplaceLostReservationCapable", UCHAR, 1),
        ("PersistThroughPowerLossActivated", UCHAR, 1),
        ("Reserved2", UCHAR, 3),
        ("AllowCommands", UCHAR, 3),
        ("TypeMaskValid", UCHAR, 1),
        ("Reserved3", UCHAR, 1),
        ("WriteExclusive", UCHAR, 1),
        ("Reserved4", UCHAR, 1),
        ("ExclusiveAccess", UCHAR, 1),
        ("Reserved5", UCHAR, 1),
        ("WriteExclusiveRegistrantsOnly", UCHAR, 1),
        ("ExclusiveAccessRegistrantsOnly", UCHAR, 1),
        ("WriteExclusiveAllRegistrants", UCHAR, 1),
        ("ExclusiveAccessAllRegistrants", UCHAR, 1),
        ("Reserved6", UCHAR, 7),
        ("Reserved7", UCHAR * 2),
    ]


_pack_ -= 1

# Structures for reserve out command.

_pack_ += 1


class PRO_PARAMETER_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ReservationKey", UCHAR * 8),
        ("ServiceActionReservationKey", UCHAR * 8),
        ("ScopeSpecificAddress", UCHAR * 4),
        ("ActivatePersistThroughPowerLoss", UCHAR, 1),
        ("Reserved1", UCHAR, 1),
        ("AllTargetPorts", UCHAR, 1),
        ("SpecifyInitiatorPorts", UCHAR, 1),
        ("Reserved2", UCHAR, 4),
        ("Reserved3", UCHAR),
        ("Obsolete", UCHAR * 2),
    ]


_pack_ -= 1

# Structure for report timestamp command.

_pack_ += 1


class RT_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ParameterDataLength", UCHAR * 2),  # Byte  0-1
        ("Origin", UCHAR, 3),  # Byte  2, bit 0-2
        ("Reserved1", UCHAR, 5),  # Byte  2, bit 3-7
        ("Reserved2", UCHAR),  # Byte  3
        ("Timestamp", UCHAR * 6),  # Byte  4-9
        ("Reserved3", UCHAR * 2),  # Byte 10-11
    ]


_pack_ -= 1

# Structure for set timestamp command.

_pack_ += 1


class ST_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 4),  # Byte  0-3
        ("Timestamp", UCHAR * 6),  # Byte  4-9
        ("Reserved2", UCHAR * 2),  # Byte 10-11
    ]


_pack_ -= 1

# Report supported operation codes Definitions.

REPORT_SUPPORTED_OPERATION_CODES_REPORTING_OPTIONS_ALL = 0x0
REPORT_SUPPORTED_OPERATION_CODES_REPORTING_OPTIONS_OP = 0x1
REPORT_SUPPORTED_OPERATION_CODES_REPORTING_OPTIONS_OP_SA = 0x2
REPORT_SUPPORTED_OPERATION_CODES_REPORTING_OPTIONS_OP_SA_OVERWRITE = 0x3

REPORT_SUPPORTED_OPERATION_CODES_SUPPORT_NOT_AVAILABLE = 0x0
REPORT_SUPPORTED_OPERATION_CODES_SUPPORT_NONE = 0x1
REPORT_SUPPORTED_OPERATION_CODES_SUPPORT_SUPPORT_STANDARD = 0x3
REPORT_SUPPORTED_OPERATION_CODES_SUPPORT_SUPPORT_VENDOR = 0x5

# Structure for report supported operation codes.

_pack_ += 1


class RS_COMMAND_TIMEOUTS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DescriptorLength", UCHAR * 2),  # 0x0A
        ("Reserved", UCHAR),
        ("CommandSpecific", UCHAR),
        ("NominalCommandProcessingTimeoutInSec", UCHAR * 4),
        ("RecommendedCommandTimeoutInSec", UCHAR * 4),
    ]


class RS_ONE_COMMAND_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ReadWriteCommandDurationLimitsPage", UCHAR, 1),
        ("Reserved", UCHAR, 7),
        ("Support", UCHAR, 3),
        ("CommandDurationLimitPage", UCHAR, 2),
        ("MultipleLogicalUnits", UCHAR, 2),
        ("CommandTimeoutsDescriptorPresent", UCHAR, 1),
        ("CdbSize", UCHAR * 2),
        ("CdbUsageData", UCHAR * ANYSIZE_ARRAY),
        ##if !defined(__midl)
        #    RS_COMMAND_TIMEOUTS_DESCRIPTOR CommandTimeoutsDescriptor[0];
        ##endif
    ]


class RS_COMMAND_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("OperationCode", UCHAR),
        ("Reserved", UCHAR),
        ("ServiceAction", UCHAR * 2),
        ("Reserved1", UCHAR),
        ("ServiceActionValid", UCHAR, 1),
        ("CommandTimeoutsDescriptorPresent", UCHAR, 1),
        ("CommandDurationLimitPage", UCHAR, 2),
        ("MultipleLogicalUnits", UCHAR, 2),
        ("ReadWriteCommandDurationLimitsPage", UCHAR, 1),
        ("Reserved2", UCHAR, 1),
        ("CdbLength", UCHAR * 2),
        ##if !defined(__midl)
        #    RS_COMMAND_TIMEOUTS_DESCRIPTOR CommandTimeoutsDescriptor[0];
        ##endif
    ]


class RS_ALL_COMMANDS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CommandDataLength", UCHAR * 4),
        ("CommandDescriptor", RS_COMMAND_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


_pack_ -= 1

# if (NTDDI_VERSION >= NTDDI_WIN8)

BLOCK_DEVICE_TOKEN_SIZE = 512

# Stuctures for Token Operation and Receive Token Information commands

_pack_ += 1


class BLOCK_DEVICE_RANGE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogicalBlockAddress", UCHAR * 8),
        ("TransferLength", UCHAR * 4),
        ("Reserved", UCHAR * 4),
    ]


class POPULATE_TOKEN_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PopulateTokenDataLength", UCHAR * 2),
        ("Immediate", UCHAR, 1),
        ("Reserved1", UCHAR, 7),
        ("Reserved2", UCHAR),
        ("InactivityTimeout", UCHAR * 4),
        ("Reserved3", UCHAR * 6),
        ("BlockDeviceRangeDescriptorListLength", UCHAR * 2),
        # if !defined(__midl)
        ("BlockDeviceRangeDescriptor", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


class WRITE_USING_TOKEN_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("WriteUsingTokenDataLength", UCHAR * 2),
        ("Immediate", UCHAR, 1),
        ("Reserved1", UCHAR, 7),
        ("Reserved2", UCHAR * 5),
        ("BlockOffsetIntoToken", UCHAR * 8),
        ("Token", UCHAR * BLOCK_DEVICE_TOKEN_SIZE),
        ("Reserved3", UCHAR * 6),
        ("BlockDeviceRangeDescriptorListLength", UCHAR * 2),
        # if !defined(__midl)
        ("BlockDeviceRangeDescriptor", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


class RECEIVE_TOKEN_INFORMATION_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("AvailableData", UCHAR * 4),
        ("ResponseToServiceAction", UCHAR, 5),
        ("Reserved1", UCHAR, 3),
        ("OperationStatus", UCHAR, 7),
        ("Reserved2", UCHAR, 1),
        ("OperationCounter", UCHAR * 2),
        ("EstimatedStatusUpdateDelay", UCHAR * 4),
        ("CompletionStatus", UCHAR),
        ("SenseDataFieldLength", UCHAR),
        ("SenseDataLength", UCHAR),
        ("TransferCountUnits", UCHAR),
        ("TransferCount", UCHAR * 8),
        ("SegmentsProcessed", UCHAR * 2),
        ("Reserved3", UCHAR * 6),
        # if !defined(__midl)
        ("SenseData", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


class RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("TokenDescriptorsLength", UCHAR * 4),
        # if !defined(__midl)
        ("TokenDescriptor", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


class BLOCK_DEVICE_TOKEN_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("TokenIdentifier", UCHAR * 2),
        ("Token", UCHAR * BLOCK_DEVICE_TOKEN_SIZE),
    ]


class OPERATION_STATUS(CEnum):
    OPERATION_COMPLETED_WITH_SUCCESS = 0x01
    OPERATION_COMPLETED_WITH_ERROR = 0x02
    OPERATION_COMPLETED_WITH_RESIDUAL_DATA = 0x03
    OPERATION_IN_PROGRESS_IN_FOREGROUND = 0x11
    OPERATION_IN_PROGRESS_IN_BACKGROUND = 0x12
    OPERATION_TERMINATED = 0x60


POPERATION_STATUS = POINTER(OPERATION_STATUS)


class TRANSFER_COUNT_UNITS(CEnum):
    # Multiplier to convert a Transfer Count field to bytes
    TRANSFER_COUNT_UNITS_BYTES = 0  # 1
    TRANSFER_COUNT_UNITS_KIBIBYTES = 1  # 2^10 or 1024
    TRANSFER_COUNT_UNITS_MEBIBYTES = 2  # 2^20
    TRANSFER_COUNT_UNITS_GIBIBYTES = 3  # 2^30
    TRANSFER_COUNT_UNITS_TEBIBYTES = 4  # 2^40
    TRANSFER_COUNT_UNITS_PEBIBYTES = 5  # 2^50
    TRANSFER_COUNT_UNITS_EXBIBYTES = 6  # 2^60
    TRANSFER_COUNT_UNITS_NUMBER_BLOCKS = 0xF1  # Logical Block Length In Bytes (from ReadCapacity)


PTRANSFER_COUNT_UNITS = POINTER(TRANSFER_COUNT_UNITS)
_pack_ -= 1

# endif #(NTDDI_VERSION >= NTDDI_WIN8)

# SANITIZE related definition
_pack_ += 1


class OVERWRITE_PARAMETER_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("OverWriteCount", UCHAR, 5),
        ("Test", UCHAR, 2),
        ("Invert", UCHAR, 1),
        ("Reserved1", UCHAR),
        ("InitializationPatternLength", UCHAR * 2),
        # if !defined(__midl)
        ("InitializationPattern", UCHAR * ANYSIZE_ARRAY),
        # endif
    ]


POVERWRITE_PARAMETER_LIST = POINTER(OVERWRITE_PARAMETER_LIST)
_pack_ -= 1

# SCSIOP_WRITE_DATA_BUFF related definition
SCSI_WRITE_BUFFER_MODE_DOWNLOAD_MICROCODE_WITH_OFFSETS_SAVE_DEFER_ACTIVATE = 0x0E
SCSI_WRITE_BUFFER_MODE_ACTIVATE_DEFERRED_MICROCODE = 0x0F

SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_VSE_ACT = 0x01
SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_HR_ACT = 0x02
SCSI_WRITE_BUFFER_MODE_0D_MODE_SPECIFIC_PO_ACT = 0x04

# Sense Data Format

_pack_ += 1


class SENSE_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ErrorCode", UCHAR, 7),
        ("Valid", UCHAR, 1),
        ("SegmentNumber", UCHAR),
        ("SenseKey", UCHAR, 4),
        ("Reserved", UCHAR, 1),
        ("IncorrectLength", UCHAR, 1),
        ("EndOfMedia", UCHAR, 1),
        ("FileMark", UCHAR, 1),
        ("Information", UCHAR * 4),
        ("AdditionalSenseLength", UCHAR),
        ("CommandSpecificInformation", UCHAR * 4),
        ("AdditionalSenseCode", UCHAR),
        ("AdditionalSenseCodeQualifier", UCHAR),
        ("FieldReplaceableUnitCode", UCHAR),
        ("SenseKeySpecific", UCHAR * 3),
    ]


PSENSE_DATA = POINTER(SENSE_DATA)
_pack_ -= 1

_pack_ += 1

# NOTE: Sense Data Descriptor Format is supported only in Windows 8 and later


class SCSI_SENSE_DESCRIPTOR_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DescriptorType", UCHAR),
        ("AdditionalLength", UCHAR),
    ]


PSCSI_SENSE_DESCRIPTOR_HEADER = POINTER(SCSI_SENSE_DESCRIPTOR_HEADER)


# Information Sense Data Descriptor Format
class SCSI_SENSE_DESCRIPTOR_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", SCSI_SENSE_DESCRIPTOR_HEADER),
        ("Valid", UCHAR, 1),
        ("Reserved1", UCHAR, 7),
        ("Reserved2", UCHAR),
        ("Information", UCHAR * 8),
    ]


PSCSI_SENSE_DESCRIPTOR_INFORMATION = POINTER(SCSI_SENSE_DESCRIPTOR_INFORMATION)


# Block Command Sense Data Descriptor Format
class SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", SCSI_SENSE_DESCRIPTOR_HEADER),
        ("Reserved1", UCHAR),
        ("Reserved2", UCHAR, 5),
        ("IncorrectLength", UCHAR, 1),
        ("Reserved3", UCHAR, 2),
    ]


PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND = POINTER(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)


# ATA Status Return Descriptor Format
class SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", SCSI_SENSE_DESCRIPTOR_HEADER),
        ("Extend", UCHAR, 1),
        ("Reserved1", UCHAR, 7),
        ("Error", UCHAR),
        ("SectorCount15_8", UCHAR),
        ("SectorCount7_0", UCHAR),
        ("LbaLow15_8", UCHAR),
        ("LbaLow7_0", UCHAR),
        ("LbaMid15_8", UCHAR),
        ("LbaMid7_0", UCHAR),
        ("LbaHigh15_8", UCHAR),
        ("LbaHigh7_0", UCHAR),
        ("Device", UCHAR),
        ("Status", UCHAR),
    ]


PSCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN = POINTER(SCSI_SENSE_DESCRIPTOR_ATA_STATUS_RETURN)

# Fixed Sense Data Format
FIXED_SENSE_DATA = SENSE_DATA
PFIXED_SENSE_DATA = POINTER(SENSE_DATA)


# Descriptor Sense Data Format
class DESCRIPTOR_SENSE_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ErrorCode", UCHAR, 7),
        ("Reserved1", UCHAR, 1),
        ("SenseKey", UCHAR, 4),
        ("Reserved2", UCHAR, 4),
        ("AdditionalSenseCode", UCHAR),
        ("AdditionalSenseCodeQualifier", UCHAR),
        ("Reserved3", UCHAR * 3),
        ("AdditionalSenseLength", UCHAR),
        ("DescriptorBuffer", UCHAR * ANYSIZE_ARRAY),
    ]


PDESCRIPTOR_SENSE_DATA = POINTER(DESCRIPTOR_SENSE_DATA)


class SENSE_DATA_EX(Union):
    _pack_ = _pack_
    _fields_ = [
        # Sense data in fixed format
        ("FixedData", FIXED_SENSE_DATA),
        # Sense data in descriptor format
        ("DescriptorData", DESCRIPTOR_SENSE_DATA),
    ]


PSENSE_DATA_EX = POINTER(SENSE_DATA_EX)

_pack_ -= 1

# Default request sense buffer size

SENSE_BUFFER_SIZE = sizeof(SENSE_DATA)

SENSE_BUFFER_SIZE_EX = sizeof(SENSE_DATA_EX)

# Maximum request sense buffer size

MAX_SENSE_BUFFER_SIZE = 255

# Maximum number of additional sense bytes.

# define MAX_ADDITIONAL_SENSE_BYTES (MAX_SENSE_BUFFER_SIZE - SENSE_BUFFER_SIZE)

# define MAX_ADDITIONAL_SENSE_BYTES_EX (MAX_SENSE_BUFFER_SIZE - SENSE_BUFFER_SIZE_EX)

# Sense Data Error Codes

SCSI_SENSE_ERRORCODE_FIXED_CURRENT = 0x70
SCSI_SENSE_ERRORCODE_FIXED_DEFERRED = 0x71
SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT = 0x72
SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED = 0x73

# Sense Data Descriptor Types

SCSI_SENSE_DESCRIPTOR_TYPE_INFORMATION = 0x00
SCSI_SENSE_DESCRIPTOR_TYPE_COMMAND_SPECIFIC = 0x01
SCSI_SENSE_DESCRIPTOR_TYPE_SENSE_KEY_SPECIFIC = 0x02
SCSI_SENSE_DESCRIPTOR_TYPE_FIELD_REPLACEABLE_UNIT = 0x03
SCSI_SENSE_DESCRIPTOR_TYPE_STREAM_COMMAND = 0x04
SCSI_SENSE_DESCRIPTOR_TYPE_BLOCK_COMMAND = 0x05
SCSI_SENSE_DESCRIPTOR_TYPE_OSD_OBJECT_IDENTIFICATION = 0x06
SCSI_SENSE_DESCRIPTOR_TYPE_OSD_RESPONSE_INTEGRITY_CHECK = 0x07
SCSI_SENSE_DESCRIPTOR_TYPE_OSD_ATTRIBUTE_IDENTIFICATION = 0x08
SCSI_SENSE_DESCRIPTOR_TYPE_ATA_STATUS_RETURN = 0x09
SCSI_SENSE_DESCRIPTOR_TYPE_PROGRESS_INDICATION = 0x0A
SCSI_SENSE_DESCRIPTOR_TYPE_USER_DATA_SEGMENT_REFERRAL = 0x0B
SCSI_SENSE_DESCRIPTOR_TYPE_FORWARDED_SENSE_DATA = 0x0C

# Sense Keys

SCSI_SENSE_NO_SENSE = 0x00
SCSI_SENSE_RECOVERED_ERROR = 0x01
SCSI_SENSE_NOT_READY = 0x02
SCSI_SENSE_MEDIUM_ERROR = 0x03
SCSI_SENSE_HARDWARE_ERROR = 0x04
SCSI_SENSE_ILLEGAL_REQUEST = 0x05
SCSI_SENSE_UNIT_ATTENTION = 0x06
SCSI_SENSE_DATA_PROTECT = 0x07
SCSI_SENSE_BLANK_CHECK = 0x08
SCSI_SENSE_UNIQUE = 0x09
SCSI_SENSE_COPY_ABORTED = 0x0A
SCSI_SENSE_ABORTED_COMMAND = 0x0B
SCSI_SENSE_EQUAL = 0x0C
SCSI_SENSE_VOL_OVERFLOW = 0x0D
SCSI_SENSE_MISCOMPARE = 0x0E
SCSI_SENSE_RESERVED = 0x0F

# Additional tape bit

SCSI_ILLEGAL_LENGTH = 0x20
SCSI_EOM = 0x40
SCSI_FILE_MARK = 0x80

# Additional Sense codes

SCSI_ADSENSE_NO_SENSE = 0x00
SCSI_ADSENSE_NO_SEEK_COMPLETE = 0x02
SCSI_ADSENSE_WRITE = 0x03
SCSI_ADSENSE_LUN_NOT_READY = 0x04
SCSI_ADSENSE_LUN_COMMUNICATION = 0x08
SCSI_ADSENSE_SERVO_ERROR = 0x09
SCSI_ADSENSE_WARNING = 0x0B
SCSI_ADSENSE_WRITE_ERROR = 0x0C
SCSI_ADSENSE_COPY_TARGET_DEVICE_ERROR = 0x0D
SCSI_ADSENSE_UNRECOVERED_ERROR = 0x11
SCSI_ADSENSE_TRACK_ERROR = 0x14
SCSI_ADSENSE_SEEK_ERROR = 0x15
SCSI_ADSENSE_REC_DATA_NOECC = 0x17
SCSI_ADSENSE_REC_DATA_ECC = 0x18
SCSI_ADSENSE_DEFECT_LIST_ERROR = 0x19
SCSI_ADSENSE_PARAMETER_LIST_LENGTH = 0x1A
SCSI_ADSENSE_MISCOMPARE_DURING_VERIFY_OPERATION = 0x1D
SCSI_ADSENSE_ILLEGAL_COMMAND = 0x20
SCSI_ADSENSE_ACCESS_DENIED = 0x20
SCSI_ADSENSE_ILLEGAL_BLOCK = 0x21
SCSI_ADSENSE_INVALID_TOKEN = 0x23
SCSI_ADSENSE_INVALID_CDB = 0x24
SCSI_ADSENSE_INVALID_LUN = 0x25
SCSI_ADSENSE_INVALID_FIELD_PARAMETER_LIST = 0x26
SCSI_ADSENSE_WRITE_PROTECT = 0x27
SCSI_ADSENSE_MEDIUM_CHANGED = 0x28
SCSI_ADSENSE_BUS_RESET = 0x29
SCSI_ADSENSE_PARAMETERS_CHANGED = 0x2A
SCSI_ADSENSE_INSUFFICIENT_TIME_FOR_OPERATION = 0x2E
SCSI_ADSENSE_INVALID_MEDIA = 0x30
SCSI_ADSENSE_DEFECT_LIST = 0x32
SCSI_ADSENSE_LB_PROVISIONING = 0x38
SCSI_ADSENSE_NO_MEDIA_IN_DEVICE = 0x3A
SCSI_ADSENSE_POSITION_ERROR = 0x3B
SCSI_ADSENSE_LOGICAL_UNIT_ERROR = 0x3E
SCSI_ADSENSE_OPERATING_CONDITIONS_CHANGED = 0x3F
SCSI_ADSENSE_DATA_PATH_FAILURE = 0x41
SCSI_ADSENSE_POWER_ON_SELF_TEST_FAILURE = 0x42
SCSI_ADSENSE_INTERNAL_TARGET_FAILURE = 0x44
SCSI_ADSENSE_DATA_TRANSFER_ERROR = 0x4B
SCSI_ADSENSE_LUN_FAILED_SELF_CONFIGURATION = 0x4C
SCSI_ADSENSE_RESOURCE_FAILURE = 0x55
SCSI_ADSENSE_OPERATOR_REQUEST = 0x5A  # see below
SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x5D
SCSI_ADSENSE_ILLEGAL_MODE_FOR_THIS_TRACK = 0x64
SCSI_ADSENSE_COPY_PROTECTION_FAILURE = 0x6F
SCSI_ADSENSE_POWER_CALIBRATION_ERROR = 0x73
SCSI_ADSENSE_VENDOR_UNIQUE = 0x80  # and higher
SCSI_ADSENSE_MUSIC_AREA = 0xA0
SCSI_ADSENSE_DATA_AREA = 0xA1
SCSI_ADSENSE_VOLUME_OVERFLOW = 0xA7

# for legacy apps:
SCSI_ADWRITE_PROTECT = SCSI_ADSENSE_WRITE_PROTECT
SCSI_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED


# SCSI_ADSENSE_NO_SENSE (0x00) qualifiers

SCSI_SENSEQ_OPERATION_IS_IN_PROGRESS = 0x16

# SCSI_ADSENSE_WRITE (0x03) qualifiers
SCSI_SENSEQ_PERIPHERAL_DEVICE_WRITE_FAULT = 0x00
SCSI_SENSEQ_NO_WRITE_CURRENT = 0x01
SCSI_SENSEQ_EXCESSIVE_WRITE_ERRORS = 0x02

# SCSI_ADSENSE_LUN_NOT_READY (0x04) qualifiers

SCSI_SENSEQ_CAUSE_NOT_REPORTABLE = 0x00
SCSI_SENSEQ_BECOMING_READY = 0x01
SCSI_SENSEQ_INIT_COMMAND_REQUIRED = 0x02
SCSI_SENSEQ_MANUAL_INTERVENTION_REQUIRED = 0x03
SCSI_SENSEQ_FORMAT_IN_PROGRESS = 0x04
SCSI_SENSEQ_REBUILD_IN_PROGRESS = 0x05
SCSI_SENSEQ_RECALCULATION_IN_PROGRESS = 0x06
SCSI_SENSEQ_OPERATION_IN_PROGRESS = 0x07
SCSI_SENSEQ_LONG_WRITE_IN_PROGRESS = 0x08
SCSI_SENSEQ_SPACE_ALLOC_IN_PROGRESS = 0x14

# SCSI_ADSENSE_LUN_COMMUNICATION (0x08) qualifiers

SCSI_SENSEQ_COMM_FAILURE = 0x00
SCSI_SENSEQ_COMM_TIMEOUT = 0x01
SCSI_SENSEQ_COMM_PARITY_ERROR = 0x02
SCSI_SESNEQ_COMM_CRC_ERROR = 0x03
SCSI_SENSEQ_UNREACHABLE_TARGET = 0x04

# SCSI_ADSENSE_SERVO_ERROR (0x09) qualifiers
#
SCSI_SENSEQ_TRACK_FOLLOWING_ERROR = 0x00
SCSI_SENSEQ_TRACKING_SERVO_FAILURE = 0x01
SCSI_SENSEQ_FOCUS_SERVO_FAILURE = 0x02
SCSI_SENSEQ_SPINDLE_SERVO_FAILURE = 0x03
SCSI_SENSEQ_HEAD_SELECT_FAULT = 0x04

# SCSI_ADSENSE_WARNING (0x0B) qualifiers
SCSI_SENSEQ_POWER_LOSS_EXPECTED = 0x08

# SCSI_ADSENSE_WRITE_ERROR (0x0C) qualifiers
SCSI_SENSEQ_LOSS_OF_STREAMING = 0x09
SCSI_SENSEQ_PADDING_BLOCKS_ADDED = 0x0A

# SCSI_ADSENSE_COPY_TARGET_DEVICE_ERROR (0x0D) qualifiers

SCSI_SENSEQ_NOT_REACHABLE = 0x02
SCSI_SENSEQ_DATA_UNDERRUN = 0x04

# SCSI_ADSENSE_UNRECOVERED_ERROR (0x11) qualifiers

SCSI_SENSEQ_UNRECOVERED_READ_ERROR = 0x00

# SCSI_ADSENSE_SEEK_ERROR (0x15) qualifiers
SCSI_SENSEQ_RANDOM_POSITIONING_ERROR = 0x00
SCSI_SENSEQ_MECHANICAL_POSITIONING_ERROR = 0x01
SCSI_SENSEQ_POSITIONING_ERROR_DETECTED_BY_READ_OF_MEDIUM = 0x02

# SCSI_ADSENSE_DEFECT_LIST_ERROR (0x19) qualifiers
SCSI_SENSEQ_DEFECT_LIST_ERROR = 0x00
SCSI_SENSEQ_DEFECT_LIST_NOT_AVAILABLE = 0x01
SCSI_SENSEQ_DEFECT_LIST_ERROR_IN_PRIMARY_LIST = 0x02
SCSI_SENSEQ_DEFECT_LIST_ERROR_IN_GROWN_LIST = 0x03

# SCSI_ADSENSE_NO_SENSE (0x00) qualifiers

SCSI_SENSEQ_FILEMARK_DETECTED = 0x01
SCSI_SENSEQ_END_OF_MEDIA_DETECTED = 0x02
SCSI_SENSEQ_SETMARK_DETECTED = 0x03
SCSI_SENSEQ_BEGINNING_OF_MEDIA_DETECTED = 0x04

# SCSI_ADSENSE_ACCESS_DENIED (0x20) qualifiers

SCSI_SENSEQ_NO_ACCESS_RIGHTS = 0x02

# SCSI_ADSENSE_ILLEGAL_BLOCK (0x21) qualifiers

SCSI_SENSEQ_LOGICAL_ADDRESS_OUT_OF_RANGE = 0x00
SCSI_SENSEQ_ILLEGAL_ELEMENT_ADDR = 0x01
SCSI_SENSEQ_INVALID_WRITE_ADDRESS = 0x02
SCSI_SENSEQ_INVALID_WRITE_CROSSING_LAYER_JUMP = 0x03
SCSI_SENSEQ_UNALIGNED_WRITE = 0x04
SCSI_SENSEQ_WRITE_BOUNDARY_VIOLATION = 0x05
SCSI_SENSEQ_READ_INVALID_DATA = 0x06
SCSI_SENSEQ_READ_BOUNDARY_VIOLATION = 0x07
SCSI_SENSEQ_MISALIGNED_WRITE = 0x08

# SCSI_ADSENSE_INVALID_FIELD_PARAMETER_LIST (0x26) qualifiers

SCSI_SENSEQ_INVALID_RELEASE_OF_PERSISTENT_RESERVATION = 0x04
SCSI_SENSEQ_TOO_MANY_SEGMENT_DESCRIPTORS = 0x08

# SCSI_ADSENSE_WRITE_PROTECT (0x27) qualifiers

SCSI_SENSEQ_SPACE_ALLOC_FAILED_WRITE_PROTECT = 0x07

# SCSI_ADSENSE_PARAMETERS_CHANGED (0x2A) qualifiers

SCSI_SENSEQ_CAPACITY_DATA_CHANGED = 0x09

# SCSI_ADSENSE_POSITION_ERROR (0x3b) qualifiers

SCSI_SENSEQ_DESTINATION_FULL = 0x0D
SCSI_SENSEQ_SOURCE_EMPTY = 0x0E

# SCSI_ADSENSE_INVALID_MEDIA (0x30) qualifiers

SCSI_SENSEQ_INCOMPATIBLE_MEDIA_INSTALLED = 0x00
SCSI_SENSEQ_UNKNOWN_FORMAT = 0x01
SCSI_SENSEQ_INCOMPATIBLE_FORMAT = 0x02
SCSI_SENSEQ_CLEANING_CARTRIDGE_INSTALLED = 0x03

# SCSI_ADSENSE_DEFECT_LIST (0x32) qualifiers
SCSI_SENSEQ_NO_DEFECT_SPARE_LOCATION_AVAILABLE = 0x00
SCSI_SENSEQ_DEFECT_LIST_UPDATE_FAILURE = 0x01

# SCSI_ADSENSE_LB_PROVISIONING (0x38) qualifiers
SCSI_SENSEQ_SOFT_THRESHOLD_REACHED = 0x07

# SCSI_ADSENSE_LOGICAL_UNIT_ERROR (0x3e) qualifiers

SCSI_SENSEQ_LOGICAL_UNIT_HAS_NOT_SELF_CONFIGURED_YET = 0x00
SCSI_SENSEQ_LOGICAL_UNIT_FAILURE = 0x01
SCSI_SENSEQ_TIMEOUT_ON_LOGICAL_UNIT = 0x02
SCSI_SENSEQ_LOGICAL_UNIT_FAILED_SELF_TEST = 0x03
SCSI_SENSEQ_LOGICAL_UNIT_FAILED_TO_UPDATE_SELF_TEST_LOG = 0x04

# SCSI_ADSENSE_OPERATING_CONDITIONS_CHANGED (0x3f) qualifiers

SCSI_SENSEQ_TARGET_OPERATING_CONDITIONS_CHANGED = 0x00
SCSI_SENSEQ_MICROCODE_CHANGED = 0x01
SCSI_SENSEQ_OPERATING_DEFINITION_CHANGED = 0x02
SCSI_SENSEQ_INQUIRY_DATA_CHANGED = 0x03
SCSI_SENSEQ_COMPONENT_DEVICE_ATTACHED = 0x04
SCSI_SENSEQ_DEVICE_IDENTIFIER_CHANGED = 0x05
SCSI_SENSEQ_REDUNDANCY_GROUP_MODIFIED = 0x06
SCSI_SENSEQ_REDUNDANCY_GROUP_DELETED = 0x07
SCSI_SENSEQ_SPARE_MODIFIED = 0x08
SCSI_SENSEQ_SPARE_DELETED = 0x09
SCSI_SENSEQ_VOLUME_SET_MODIFIED = 0x0A
SCSI_SENSEQ_VOLUME_SET_DELETED = 0x0B
SCSI_SENSEQ_VOLUME_SET_DEASSIGNED = 0x0C
SCSI_SENSEQ_VOLUME_SET_REASSIGNED = 0x0D
SCSI_SENSEQ_REPORTED_LUNS_DATA_CHANGED = 0x0E
SCSI_SENSEQ_ECHO_BUFFER_OVERWRITTEN = 0x0F
SCSI_SENSEQ_MEDIUM_LOADABLE = 0x10
SCSI_SENSEQ_MEDIUM_AUXILIARY_MEMORY_ACCESSIBLE = 0x11

# SCSI_ADSENSE_INTERNAL_TARGET_FAILURE (0x44) qualifiers
SCSI_SENSEQ_INTERNAL_TARGET_FAILURE = 0x00
SCSI_SENSEQ_PRESISTENT_RESERVATION_INFORMATION_LOST = 0x01
SCSI_SENSEQ_ATA_DEVICE_FAILED_SET_FEATURES = 0x71

# SCSI_ADSENSE_DATA_TRANSFER_ERROR (0x4b) qualifiers

SCSI_SENSEQ_INITIATOR_RESPONSE_TIMEOUT = 0x06

# SCSI_ADSENSE_RESOURCE_FAILURE (0x55) qualifiers
SCSI_SENSEQ_SYSTEM_RESOURCE_FAILURE = 0x00
SCSI_SENSEQ_SYSTEM_BUFFER_FULL = 0x01
SCSI_SENSEQ_INSUFFICIENT_RESERVATION_RESOURCES = 0x02
SCSI_SENSEQ_INSUFFICIENT_RESOURCES = 0x03

# SCSI_ADSENSE_OPERATOR_REQUEST (0x5a) qualifiers

SCSI_SENSEQ_STATE_CHANGE_INPUT = 0x00  # generic request
SCSI_SENSEQ_MEDIUM_REMOVAL = 0x01
SCSI_SENSEQ_WRITE_PROTECT_ENABLE = 0x02
SCSI_SENSEQ_WRITE_PROTECT_DISABLE = 0x03

# SCSI_ADSENSE_FAILURE_PREDICTION_THRESHOLD_EXCEEDED (0x5d) qualifiers
SCSI_SENSEQ_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x00
SCSI_SENSEQ_MEDIA_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x01
SCSI_SENSEQ_LUN_FAILURE_PREDICTION_THRESHOLD_EXCEEDED = 0x02
SCSI_SENSEQ_SPARE_AREA_EXHAUSTION_PREDICTION_THRESHOLD_EXCEEDED = 0x03
SCSI_SENSEQ_GENERAL_HARD_DRIVE_FAILURE = 0x10
SCSI_SENSEQ_DRIVE_ERROR_RATE_TOO_HIGH = 0x11
SCSI_SENSEQ_DATA_ERROR_RATE_TOO_HIGH = 0x12
SCSI_SENSEQ_SEEK_ERROR_RATE_TOO_HIGH = 0x13
SCSI_SENSEQ_TOO_MANY_BLOCK_REASSIGNS = 0x14
SCSI_SENSEQ_ACCESS_TIMES_TOO_HIGH = 0x15
SCSI_SENSEQ_START_UNIT_TIMES_TOO_HIGH = 0x16
SCSI_SENSEQ_CHANNEL_PARAMETRICS = 0x17
SCSI_SENSEQ_CONTROLLER_DETECTED = 0x18
SCSI_SENSEQ_THROUGHPUT_PERFORMANCE = 0x19
SCSI_SENSEQ_SEEK_TIME_PERFORMANCE = 0x1A
SCSI_SENSEQ_SPIN_UP_RETRY_COUNT = 0x1B
SCSI_SENSEQ_DRIVE_CALIBRATION_RETRY_COUNT = 0x1C
SCSI_SENSEQ_DATA_CHANNEL_DATA_ERROR_RATE_TOO_HIGH = 0x32
SCSI_SENSEQ_SERVO_DATA_ERROR_RATE_TOO_HIGH = 0x42
SCSI_SENSEQ_SERVER_SEEK_ERROR_RATE_TOO_HIGH = 0x43
SCSI_SENSEQ_FAILURE_PREDICTION_THRESHOLD_EXCEEDED_FALSE = 0xFF

# SCSI_ADSENSE_COPY_PROTECTION_FAILURE (0x6f) qualifiers
SCSI_SENSEQ_AUTHENTICATION_FAILURE = 0x00
SCSI_SENSEQ_KEY_NOT_PRESENT = 0x01
SCSI_SENSEQ_KEY_NOT_ESTABLISHED = 0x02
SCSI_SENSEQ_READ_OF_SCRAMBLED_SECTOR_WITHOUT_AUTHENTICATION = 0x03
SCSI_SENSEQ_MEDIA_CODE_MISMATCHED_TO_LOGICAL_UNIT = 0x04
SCSI_SENSEQ_LOGICAL_UNIT_RESET_COUNT_ERROR = 0x05

# SCSI_ADSENSE_POWER_CALIBRATION_ERROR (0x73) qualifiers

SCSI_SENSEQ_POWER_CALIBRATION_AREA_ALMOST_FULL = 0x01
SCSI_SENSEQ_POWER_CALIBRATION_AREA_FULL = 0x02
SCSI_SENSEQ_POWER_CALIBRATION_AREA_ERROR = 0x03
SCSI_SENSEQ_PMA_RMA_UPDATE_FAILURE = 0x04
SCSI_SENSEQ_PMA_RMA_IS_FULL = 0x05
SCSI_SENSEQ_PMA_RMA_ALMOST_FULL = 0x06


# end_ntminitape

# SCSI IO Device Control Codes

FILE_DEVICE_SCSI = 0x0000001B

IOCTL_SCSI_EXECUTE_IN = (FILE_DEVICE_SCSI << 16) + 0x0011
IOCTL_SCSI_EXECUTE_OUT = (FILE_DEVICE_SCSI << 16) + 0x0012
IOCTL_SCSI_EXECUTE_NONE = (FILE_DEVICE_SCSI << 16) + 0x0013

# SMART support in atapi

IOCTL_SCSI_MINIPORT_SMART_VERSION = (FILE_DEVICE_SCSI << 16) + 0x0500
IOCTL_SCSI_MINIPORT_IDENTIFY = (FILE_DEVICE_SCSI << 16) + 0x0501
IOCTL_SCSI_MINIPORT_READ_SMART_ATTRIBS = (FILE_DEVICE_SCSI << 16) + 0x0502
IOCTL_SCSI_MINIPORT_READ_SMART_THRESHOLDS = (FILE_DEVICE_SCSI << 16) + 0x0503
IOCTL_SCSI_MINIPORT_ENABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0504
IOCTL_SCSI_MINIPORT_DISABLE_SMART = (FILE_DEVICE_SCSI << 16) + 0x0505
IOCTL_SCSI_MINIPORT_RETURN_STATUS = (FILE_DEVICE_SCSI << 16) + 0x0506
IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTOSAVE = (FILE_DEVICE_SCSI << 16) + 0x0507
IOCTL_SCSI_MINIPORT_SAVE_ATTRIBUTE_VALUES = (FILE_DEVICE_SCSI << 16) + 0x0508
IOCTL_SCSI_MINIPORT_EXECUTE_OFFLINE_DIAGS = (FILE_DEVICE_SCSI << 16) + 0x0509
IOCTL_SCSI_MINIPORT_ENABLE_DISABLE_AUTO_OFFLINE = (FILE_DEVICE_SCSI << 16) + 0x050A
IOCTL_SCSI_MINIPORT_READ_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050B
IOCTL_SCSI_MINIPORT_WRITE_SMART_LOG = (FILE_DEVICE_SCSI << 16) + 0x050C


# Data set management IOCTL to match DSM notifications. Lba Ranges carried by this IOCTL belong to the same file.
# This IOCTL carries SRB_IO_CONTROL and DSM_NOTIFICATION_REQUEST_BLOCK as part of input parameters.
IOCTL_SCSI_MINIPORT_DSM = (FILE_DEVICE_SCSI << 16) + 0x0720

# Data set management IOCTL sent to miniport driver. Lba Ranges carried by this IOCTL may cross different files or do not belong to file.
# This IOCTL carries SRB_IO_CONTROL and DEVICE_MANAGE_DATA_SET_ATTRIBUTES as part of input parameters.
# NOTE that when construct input buffer, padding place may be needed between SRB_IO_CONTROL and DEVICE_MANAGE_DATA_SET_ATTRIBUTES to make sure
# DEVICE_MANAGE_DATA_SET_ATTRIBUTES is pointer safe.
# e.g. input buffer layout should be: ALIGN_UP(sizeof(SRB_IO_CONTROL), PVOID) + DEVICE_MANAGE_DATA_SET_ATTRIBUTES.
#      (Parameter Block and DataSet Ranges will be indicated by fields in DEVICE_MANAGE_DATA_SET_ATTRIBUTES)
IOCTL_SCSI_MINIPORT_DSM_GENERAL = (FILE_DEVICE_SCSI << 16) + 0x0721

# CLUSTER support
# deliberately skipped some values to allow for expansion above.
IOCTL_SCSI_MINIPORT_NOT_QUORUM_CAPABLE = (FILE_DEVICE_SCSI << 16) + 0x0520
IOCTL_SCSI_MINIPORT_NOT_CLUSTER_CAPABLE = (FILE_DEVICE_SCSI << 16) + 0x0521


# begin_ntminitape

# Read Capacity Data - returned in Big Endian format

_pack_ += 1


class READ_CAPACITY_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogicalBlockAddress", ULONG),
        ("BytesPerBlock", ULONG),
    ]


PREAD_CAPACITY_DATA = POINTER(READ_CAPACITY_DATA)
_pack_ -= 1


_pack_ += 1


class READ_CAPACITY_DATA_EX(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogicalBlockAddress", LARGE_INTEGER),
        ("BytesPerBlock", ULONG),
    ]


PREAD_CAPACITY_DATA_EX = POINTER(READ_CAPACITY_DATA_EX)
_pack_ -= 1


RC_BASIS_LAST_LBA_NOT_SEQUENTIAL_WRITE_REQUIRED_ZONES = 0x0
RC_BASIS_LAST_LBA_ON_LOGICAL_UNIT = 0x1

_pack_ += 1


class READ_CAPACITY16_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogicalBlockAddress", LARGE_INTEGER),
        ("BytesPerBlock", ULONG),
        ("ProtectionEnable", UCHAR, 1),
        ("ProtectionType", UCHAR, 3),
        ("RcBasis", UCHAR, 2),
        ("Reserved", UCHAR, 2),
        ("LogicalPerPhysicalExponent", UCHAR, 4),
        ("ProtectionInfoExponent", UCHAR, 4),
        ("LowestAlignedBlock_MSB", UCHAR, 6),
        ("LBPRZ", UCHAR, 1),
        ("LBPME", UCHAR, 1),
        ("LowestAlignedBlock_LSB", UCHAR),
        ("Reserved3", UCHAR * 16),
    ]


PREAD_CAPACITY16_DATA = POINTER(READ_CAPACITY16_DATA)
_pack_ -= 1


# Get LBA Status structures, returned in Big Endian format.
_pack_ += 1


class LBA_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("StartingLBA", ULONGLONG),
        ("LogicalBlockCount", ULONG),
        ("ProvisioningStatus", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("Reserved2", UCHAR * 3),
    ]


PLBA_STATUS_DESCRIPTOR = POINTER(LBA_STATUS_DESCRIPTOR)


class LBA_STATUS_LIST_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ParameterLength", ULONG),
        ("Reserved", ULONG),
        # if !defined(__midl)
        ("Descriptors", LBA_STATUS_DESCRIPTOR * 0),
        # endif
    ]


PLBA_STATUS_LIST_HEADER = POINTER(LBA_STATUS_LIST_HEADER)
_pack_ -= 1

LBA_STATUS_MAPPED = 0x0
LBA_STATUS_DEALLOCATED = 0x1
LBA_STATUS_ANCHORED = 0x2

# Read Block Limits Data - returned in Big Endian format
# This structure returns the maximum and minimum block
# size for a TAPE device.

_pack_ += 1


class READ_BLOCK_LIMITS_DATA(Structure):  # READ_BLOCK_LIMITS
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", UCHAR),
        ("BlockMaximumSize", UCHAR * 3),
        ("BlockMinimumSize", UCHAR * 2),
    ]


PREAD_BLOCK_LIMITS_DATA = POINTER(READ_BLOCK_LIMITS_DATA)
_pack_ -= 1

_pack_ += 1


class READ_BUFFER_CAPACITY_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DataLength", UCHAR * 2),
        ("Reserved1", UCHAR),
        ("BlockDataReturned", UCHAR, 1),
        ("Reserved4", UCHAR, 7),
        ("TotalBufferSize", UCHAR * 4),
        ("AvailableBufferSize", UCHAR * 4),
    ]


PREAD_BUFFER_CAPACITY_DATA = POINTER(READ_BUFFER_CAPACITY_DATA)
_pack_ -= 1

# Report Zones data structures.
# Returned data contains REPORT_ZONES_DATA as header,
# and ZONE_DESCRIPTIOR(s)

ZONE_TYPE_CONVENTIONAL = 0x1
ZONE_TYPE_SEQUENTIAL_WRITE_REQUIRED = 0x2
ZONE_TYPE_SEQUENTIAL_WRITE_PREFERRED = 0x3

ZONE_CONDITION_NOT_WRITE_POINTER = 0x0
ZONE_CONDITION_EMPTY = 0x1
ZONE_CONDITION_IMPLICITLY_OPENED = 0x2
ZONE_CONDITION_EXPLICITLY_OPENED = 0x3
ZONE_CONDITION_CLOSED = 0x4
ZONE_CONDITION_READ_ONLY = 0xD
ZONE_CONDITION_FULL = 0xE
ZONE_CONDITION_OFFLINE = 0xF


_pack_ += 1


class ZONE_DESCRIPTIOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneType", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("Reset", UCHAR, 1),
        ("Non_Seq", UCHAR, 1),
        ("Reserved2", UCHAR, 2),
        ("ZoneCondition", UCHAR, 4),
        ("Reserved3", UCHAR * 6),
        ("ZoneLength", UCHAR * 8),
        ("ZoneStartLBA", UCHAR * 8),
        ("WritePointerLBA", UCHAR * 8),
        ("Reserved4", UCHAR * 32),
    ]


PZONE_DESCRIPTIOR = POINTER(ZONE_DESCRIPTIOR)
_pack_ -= 1

ZONES_TYPE_AND_LENGTH_MAY_DIFFERENT = 0x0
ZONES_TYPE_SAME_LENGTH_SAME = 0x1
ZONES_TYPE_SAME_LAST_ZONE_LENGTH_DIFFERENT = 0x2
ZONES_TYPE_MAY_DIFFERENT_LENGTH_SAME = 0x3

_pack_ += 1


class REPORT_ZONES_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneListLength", UCHAR * 4),
        ("Same", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("Reserved2", UCHAR * 3),
        ("MaxLBA", UCHAR * 8),
        ("Reserved3", UCHAR * 48),
        # if !defined(__midl)
        ("ZoneDescriptors", ZONE_DESCRIPTIOR * ANYSIZE_ARRAY),
        # endif
    ]


PREPORT_ZONES_DATA = POINTER(REPORT_ZONES_DATA)
_pack_ -= 1


# Mode data structures.

# Define Mode parameter header.

_pack_ += 1


class MODE_PARAMETER_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ModeDataLength", UCHAR),
        ("MediumType", UCHAR),
        ("DeviceSpecificParameter", UCHAR),
        ("BlockDescriptorLength", UCHAR),
    ]


PMODE_PARAMETER_HEADER = POINTER(MODE_PARAMETER_HEADER)


class MODE_PARAMETER_HEADER10(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ModeDataLength", UCHAR * 2),
        ("MediumType", UCHAR),
        ("DeviceSpecificParameter", UCHAR),
        ("Reserved", UCHAR * 2),
        ("BlockDescriptorLength", UCHAR * 2),
    ]


PMODE_PARAMETER_HEADER10 = POINTER(MODE_PARAMETER_HEADER10)
_pack_ -= 1

MODE_FD_SINGLE_SIDE = 0x01
MODE_FD_DOUBLE_SIDE = 0x02
MODE_FD_MAXIMUM_TYPE = 0x1E
MODE_DSP_FUA_SUPPORTED = 0x10
MODE_DSP_WRITE_PROTECT = 0x80

# Define the mode parameter block.

_pack_ += 1


class MODE_PARAMETER_BLOCK(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DensityCode", UCHAR),
        ("NumberOfBlocks", UCHAR * 3),
        ("Reserved", UCHAR),
        ("BlockLength", UCHAR * 3),
    ]


PMODE_PARAMETER_BLOCK = POINTER(MODE_PARAMETER_BLOCK)

_pack_ -= 1


# Define Disconnect-Reconnect page.

_pack_ += 1


class MODE_DISCONNECT_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("BufferFullRatio", UCHAR),
        ("BufferEmptyRatio", UCHAR),
        ("BusInactivityLimit", UCHAR * 2),
        ("BusDisconnectTime", UCHAR * 2),
        ("BusConnectTime", UCHAR * 2),
        ("MaximumBurstSize", UCHAR * 2),
        ("DataTransferDisconnect", UCHAR, 2),
        ("Reserved2", UCHAR * 3),
    ]


PMODE_DISCONNECT_PAGE = POINTER(MODE_DISCONNECT_PAGE)
_pack_ -= 1

# Define mode caching page.

_pack_ += 1


class MODE_CACHING_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("ReadDisableCache", UCHAR, 1),
        ("MultiplicationFactor", UCHAR, 1),
        ("WriteCacheEnable", UCHAR, 1),
        ("Reserved2", UCHAR, 5),
        ("WriteRetensionPriority", UCHAR, 4),
        ("ReadRetensionPriority", UCHAR, 4),
        ("DisablePrefetchTransfer", UCHAR * 2),
        ("MinimumPrefetch", UCHAR * 2),
        ("MaximumPrefetch", UCHAR * 2),
        ("MaximumPrefetchCeiling", UCHAR * 2),
    ]


PMODE_CACHING_PAGE = POINTER(MODE_CACHING_PAGE)
_pack_ -= 1

_pack_ += 1


class MODE_CACHING_PAGE_EX(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x08
        ("SubPageFormat", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("ReadDisableCache", UCHAR, 1),
        ("MultiplicationFactor", UCHAR, 1),
        ("WriteCacheEnable", UCHAR, 1),
        ("SizeEnable", UCHAR, 1),
        ("Discontinuity", UCHAR, 1),
        ("CachingAnalysisPermitted", UCHAR, 1),
        ("AbortPreFetch", UCHAR, 1),
        ("InitiatorControl", UCHAR, 1),
        ("WriteRetensionPriority", UCHAR, 4),
        ("ReadRetensionPriority", UCHAR, 4),
        ("DisablePrefetchTransfer", UCHAR * 2),
        ("MinimumPrefetch", UCHAR * 2),
        ("MaximumPrefetch", UCHAR * 2),
        ("MaximumPrefetchCeiling", UCHAR * 2),
        ("NvCacheDisable", UCHAR, 1),
        ("SyncCacheProgress", UCHAR, 2),
        ("VendorSpecific", UCHAR, 2),
        ("DisableReadAhead", UCHAR, 1),
        ("LogicalBlockCacheSegmentSize", UCHAR, 1),
        ("ForceSequentialWrite", UCHAR, 1),
        ("NumberOfCacheSegments", UCHAR),
        ("CacheSegmentSize", UCHAR * 2),
        ("Reserved", UCHAR * 4),
    ]


PMODE_CACHING_PAGE_EX = POINTER(MODE_CACHING_PAGE_EX)
_pack_ -= 1

_pack_ += 1


class MODE_CONTROL_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x0A
        ("Reserved1", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("RLEC", UCHAR, 1),
        ("GLTSD", UCHAR, 1),
        ("D_SENSE", UCHAR, 1),
        ("DPICZ", UCHAR, 1),
        ("TMF_ONLY", UCHAR, 1),
        ("TST", UCHAR, 3),
        ("Obsolete1", UCHAR, 1),
        ("QERR", UCHAR, 2),
        ("NUAR", UCHAR, 1),
        ("QueueAlgorithmModifier", UCHAR, 4),
        ("Obsolete2", UCHAR, 3),
        ("SWP", UCHAR, 1),
        ("UA_INTLCK_CTRL", UCHAR, 2),
        ("RAC", UCHAR, 1),
        ("VS", UCHAR, 1),
        ("AutoloadMode", UCHAR, 3),
        ("Reserved2", UCHAR, 1),
        ("RWWP", UCHAR, 1),
        ("ATMPE", UCHAR, 1),
        ("TAS", UCHAR, 1),
        ("ATO", UCHAR, 1),
        ("Obsolete3", UCHAR * 2),
        ("BusyTimeoutPeriod", UCHAR * 2),
        ("ExtendeSelfTestCompletionTime", UCHAR * 2),
    ]


PMODE_CONTROL_PAGE = POINTER(MODE_CONTROL_PAGE)
_pack_ -= 1


# Define write parameters cdrom page
_pack_ += 1


class MODE_CDROM_WRITE_PARAMETERS_PAGE2(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x05
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x32 ??
        ("WriteType", UCHAR, 4),
        ("TestWrite", UCHAR, 1),
        ("LinkSizeValid", UCHAR, 1),
        ("BufferUnderrunFreeEnabled", UCHAR, 1),
        ("Reserved2", UCHAR, 1),
        ("TrackMode", UCHAR, 4),
        ("Copy", UCHAR, 1),
        ("FixedPacket", UCHAR, 1),
        ("MultiSession", UCHAR, 2),
        ("DataBlockType", UCHAR, 4),
        ("Reserved3", UCHAR, 4),
        ("LinkSize", UCHAR),
        ("Reserved4", UCHAR),
        ("HostApplicationCode", UCHAR, 6),
        ("Reserved5", UCHAR, 2),
        ("SessionFormat", UCHAR),
        ("Reserved6", UCHAR),
        ("PacketSize", UCHAR * 4),
        ("AudioPauseLength", UCHAR * 2),
        ("MediaCatalogNumber", UCHAR * 16),
        ("ISRC", UCHAR * 16),
        ("SubHeaderData", UCHAR * 4),
    ]


PMODE_CDROM_WRITE_PARAMETERS_PAGE2 = POINTER(MODE_CDROM_WRITE_PARAMETERS_PAGE2)
_pack_ -= 1

# ifndef DEPRECATE_DDK_FUNCTIONS
# this structure is being retired due to missing fields and overly
# complex data definitions for the MCN and ISRC.
_pack_ += 1


class MODE_CDROM_WRITE_PARAMETERS_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageLength", UCHAR),  # 0x32 ??
        ("WriteType", UCHAR, 4),
        ("TestWrite", UCHAR, 1),
        ("LinkSizeValid", UCHAR, 1),
        ("BufferUnderrunFreeEnabled", UCHAR, 1),
        ("Reserved2", UCHAR, 1),
        ("TrackMode", UCHAR, 4),
        ("Copy", UCHAR, 1),
        ("FixedPacket", UCHAR, 1),
        ("MultiSession", UCHAR, 2),
        ("DataBlockType", UCHAR, 4),
        ("Reserved3", UCHAR, 4),
        ("LinkSize", UCHAR),
        ("Reserved4", UCHAR),
        ("HostApplicationCode", UCHAR, 6),
        ("Reserved5", UCHAR, 2),
        ("SessionFormat", UCHAR),
        ("Reserved6", UCHAR),
        ("PacketSize", UCHAR * 4),
        ("AudioPauseLength", UCHAR * 2),
        ("Reserved7", UCHAR, 7),
        ("MediaCatalogNumberValid", UCHAR, 1),
        ("MediaCatalogNumber", UCHAR * 13),
        ("MediaCatalogNumberZero", UCHAR),
        ("MediaCatalogNumberAFrame", UCHAR),
        ("Reserved8", UCHAR, 7),
        ("ISRCValid", UCHAR, 1),
        ("ISRCCountry", UCHAR * 2),
        ("ISRCOwner", UCHAR * 3),
        ("ISRCRecordingYear", UCHAR * 2),
        ("ISRCSerialNumber", UCHAR * 5),
        ("ISRCZero", UCHAR),
        ("ISRCAFrame", UCHAR),
        ("ISRCReserved", UCHAR),
        ("SubHeaderData", UCHAR * 4),
    ]


PMODE_CDROM_WRITE_PARAMETERS_PAGE = POINTER(MODE_CDROM_WRITE_PARAMETERS_PAGE)
_pack_ -= 1
# endif #ifndef DEPRECATE_DDK_FUNCTIONS

# Define the MRW mode page for CDROM device types
_pack_ += 1


class MODE_MRW_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x03
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x06
        ("Reserved1", UCHAR),
        ("LbaSpace", UCHAR, 1),
        ("Reserved2", UCHAR, 7),
        ("Reserved3", UCHAR * 4),
    ]


PMODE_MRW_PAGE = POINTER(MODE_MRW_PAGE)
_pack_ -= 1

# Define mode flexible disk page.

_pack_ += 1


class MODE_FLEXIBLE_DISK_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("TransferRate", UCHAR * 2),
        ("NumberOfHeads", UCHAR),
        ("SectorsPerTrack", UCHAR),
        ("BytesPerSector", UCHAR * 2),
        ("NumberOfCylinders", UCHAR * 2),
        ("StartWritePrecom", UCHAR * 2),
        ("StartReducedCurrent", UCHAR * 2),
        ("StepRate", UCHAR * 2),
        ("StepPluseWidth", UCHAR),
        ("HeadSettleDelay", UCHAR * 2),
        ("MotorOnDelay", UCHAR),
        ("MotorOffDelay", UCHAR),
        ("Reserved2", UCHAR, 5),
        ("MotorOnAsserted", UCHAR, 1),
        ("StartSectorNumber", UCHAR, 1),
        ("TrueReadySignal", UCHAR, 1),
        ("StepPlusePerCyclynder", UCHAR, 4),
        ("Reserved3", UCHAR, 4),
        ("WriteCompenstation", UCHAR),
        ("HeadLoadDelay", UCHAR),
        ("HeadUnloadDelay", UCHAR),
        ("Pin2Usage", UCHAR, 4),
        ("Pin34Usage", UCHAR, 4),
        ("Pin1Usage", UCHAR, 4),
        ("Pin4Usage", UCHAR, 4),
        ("MediumRotationRate", UCHAR * 2),
        ("Reserved4", UCHAR * 2),
    ]


PMODE_FLEXIBLE_DISK_PAGE = POINTER(MODE_FLEXIBLE_DISK_PAGE)
_pack_ -= 1

# Define mode format page.

_pack_ += 1


class MODE_FORMAT_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("TracksPerZone", UCHAR * 2),
        ("AlternateSectorsPerZone", UCHAR * 2),
        ("AlternateTracksPerZone", UCHAR * 2),
        ("AlternateTracksPerLogicalUnit", UCHAR * 2),
        ("SectorsPerTrack", UCHAR * 2),
        ("BytesPerPhysicalSector", UCHAR * 2),
        ("Interleave", UCHAR * 2),
        ("TrackSkewFactor", UCHAR * 2),
        ("CylinderSkewFactor", UCHAR * 2),
        ("Reserved2", UCHAR, 4),
        ("SurfaceFirst", UCHAR, 1),
        ("RemovableMedia", UCHAR, 1),
        ("HardSectorFormating", UCHAR, 1),
        ("SoftSectorFormating", UCHAR, 1),
        ("Reserved3", UCHAR * 3),
    ]


PMODE_FORMAT_PAGE = POINTER(MODE_FORMAT_PAGE)
_pack_ -= 1

# Define rigid disk driver geometry page.

_pack_ += 1


class MODE_RIGID_GEOMETRY_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("PageLength", UCHAR),
        ("NumberOfCylinders", UCHAR * 3),
        ("NumberOfHeads", UCHAR),
        ("StartWritePrecom", UCHAR * 3),
        ("StartReducedCurrent", UCHAR * 3),
        ("DriveStepRate", UCHAR * 2),
        ("LandZoneCyclinder", UCHAR * 3),
        ("RotationalPositionLock", UCHAR, 2),
        ("Reserved2", UCHAR, 6),
        ("RotationOffset", UCHAR),
        ("Reserved3", UCHAR),
        ("RoataionRate", UCHAR * 2),
        ("Reserved4", UCHAR * 2),
    ]


PMODE_RIGID_GEOMETRY_PAGE = POINTER(MODE_RIGID_GEOMETRY_PAGE)
_pack_ -= 1

# Define read write recovery page

_pack_ += 1


class MODE_READ_WRITE_RECOVERY_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved1", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),
        ("DCRBit", UCHAR, 1),
        ("DTEBit", UCHAR, 1),
        ("PERBit", UCHAR, 1),
        ("EERBit", UCHAR, 1),
        ("RCBit", UCHAR, 1),
        ("TBBit", UCHAR, 1),
        ("ARRE", UCHAR, 1),
        ("AWRE", UCHAR, 1),
        ("ReadRetryCount", UCHAR),
        ("Reserved4", UCHAR * 4),
        ("WriteRetryCount", UCHAR),
        ("Reserved5", UCHAR * 3),
    ]


PMODE_READ_WRITE_RECOVERY_PAGE = POINTER(MODE_READ_WRITE_RECOVERY_PAGE)
_pack_ -= 1

# Define read recovery page - cdrom

_pack_ += 1


class MODE_READ_RECOVERY_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved1", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),
        ("DCRBit", UCHAR, 1),
        ("DTEBit", UCHAR, 1),
        ("PERBit", UCHAR, 1),
        ("Reserved2", UCHAR, 1),
        ("RCBit", UCHAR, 1),
        ("TBBit", UCHAR, 1),
        ("Reserved3", UCHAR, 2),
        ("ReadRetryCount", UCHAR),
        ("Reserved4", UCHAR * 4),
    ]


PMODE_READ_RECOVERY_PAGE = POINTER(MODE_READ_RECOVERY_PAGE)
_pack_ -= 1


# Define Informational Exception Control Page. Used for failure prediction

_pack_ += 1


class MODE_INFO_EXCEPTIONS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("Reserved1", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),
        (
            "_unnamed_union",
            make_union(
                [
                    ("Flags", UCHAR),
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("LogErr", UCHAR, 1),
                                ("Reserved2", UCHAR, 1),
                                ("Test", UCHAR, 1),
                                ("Dexcpt", UCHAR, 1),
                                ("Reserved3", UCHAR, 3),
                                ("Perf", UCHAR, 1),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
        ("ReportMethod", UCHAR, 4),
        ("Reserved4", UCHAR, 4),
        ("IntervalTimer", UCHAR * 4),
        ("ReportCount", UCHAR * 4),
    ]


PMODE_INFO_EXCEPTIONS = POINTER(MODE_INFO_EXCEPTIONS)
_pack_ -= 1

# Begin C/DVD 0.9 definitions

# Power Condition Mode Page Format

_pack_ += 1


class POWER_CONDITION_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x1A
        ("Reserved", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x0A
        ("Reserved2", UCHAR),
        ("Standby", UCHAR, 1),
        ("Idle", UCHAR, 1),
        ("Reserved3", UCHAR, 6),
        ("IdleTimer", UCHAR * 4),
        ("StandbyTimer", UCHAR * 4),
    ]


PPOWER_CONDITION_PAGE = POINTER(POWER_CONDITION_PAGE)
_pack_ -= 1

# CD-Audio Control Mode Page Format

_pack_ += 1


class CDDA_OUTPUT_PORT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ChannelSelection", UCHAR, 4),
        ("Reserved", UCHAR, 4),
        ("Volume", UCHAR),
    ]


PCDDA_OUTPUT_PORT = POINTER(CDDA_OUTPUT_PORT)


class CDAUDIO_CONTROL_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x0E
        ("Reserved", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x0E
        ("Reserved2", UCHAR, 1),
        ("StopOnTrackCrossing", UCHAR, 1),  # Default 0
        ("Immediate", UCHAR, 1),  # Always 1
        ("Reserved3", UCHAR, 5),
        ("Reserved4", UCHAR * 3),
        ("Obsolete", UCHAR * 2),
        ("CDDAOutputPorts", CDDA_OUTPUT_PORT * 4),
    ]


PCDAUDIO_CONTROL_PAGE = POINTER(CDAUDIO_CONTROL_PAGE)
_pack_ -= 1

CDDA_CHANNEL_MUTED = 0x0
CDDA_CHANNEL_ZERO = 0x1
CDDA_CHANNEL_ONE = 0x2
CDDA_CHANNEL_TWO = 0x4
CDDA_CHANNEL_THREE = 0x8

# C/DVD Feature Set Support & Version Page

_pack_ += 1


class CDVD_FEATURE_SET_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x18
        ("Reserved", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x16
        ("CDAudio", UCHAR * 2),
        ("EmbeddedChanger", UCHAR * 2),
        ("PacketSMART", UCHAR * 2),
        ("PersistantPrevent", UCHAR * 2),
        ("EventStatusNotification", UCHAR * 2),
        ("DigitalOutput", UCHAR * 2),
        ("CDSequentialRecordable", UCHAR * 2),
        ("DVDSequentialRecordable", UCHAR * 2),
        ("RandomRecordable", UCHAR * 2),
        ("KeyExchange", UCHAR * 2),
        ("Reserved2", UCHAR * 2),
    ]


PCDVD_FEATURE_SET_PAGE = POINTER(CDVD_FEATURE_SET_PAGE)
_pack_ -= 1

# CDVD Inactivity Time-out Page Format

_pack_ += 1


class CDVD_INACTIVITY_TIMEOUT_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x1D
        ("Reserved", UCHAR, 1),
        ("PSBit", UCHAR, 1),
        ("PageLength", UCHAR),  # 0x08
        ("Reserved2", UCHAR * 2),
        ("SWPP", UCHAR, 1),
        ("DISP", UCHAR, 1),
        ("Reserved3", UCHAR, 6),
        ("Reserved4", UCHAR),
        ("GroupOneMinimumTimeout", UCHAR * 2),
        ("GroupTwoMinimumTimeout", UCHAR * 2),
    ]


PCDVD_INACTIVITY_TIMEOUT_PAGE = POINTER(CDVD_INACTIVITY_TIMEOUT_PAGE)
_pack_ -= 1

# CDVD Capabilities & Mechanism Status Page

CDVD_LMT_CADDY = 0
CDVD_LMT_TRAY = 1
CDVD_LMT_POPUP = 2
CDVD_LMT_RESERVED1 = 3
CDVD_LMT_CHANGER_INDIVIDUAL = 4
CDVD_LMT_CHANGER_CARTRIDGE = 5
CDVD_LMT_RESERVED2 = 6
CDVD_LMT_RESERVED3 = 7


_pack_ += 1


class CDVD_CAPABILITIES_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x2A
        ("Reserved", UCHAR, 1),
        ("PSBit", UCHAR, 1),  # offset 0
        ("PageLength", UCHAR),  # >= 0x18      # offset 1
        ("CDRRead", UCHAR, 1),
        ("CDERead", UCHAR, 1),
        ("Method2", UCHAR, 1),
        ("DVDROMRead", UCHAR, 1),
        ("DVDRRead", UCHAR, 1),
        ("DVDRAMRead", UCHAR, 1),
        ("Reserved2", UCHAR, 2),  # offset 2
        ("CDRWrite", UCHAR, 1),
        ("CDEWrite", UCHAR, 1),
        ("TestWrite", UCHAR, 1),
        ("Reserved3", UCHAR, 1),
        ("DVDRWrite", UCHAR, 1),
        ("DVDRAMWrite", UCHAR, 1),
        ("Reserved4", UCHAR, 2),  # offset 3
        ("AudioPlay", UCHAR, 1),
        ("Composite", UCHAR, 1),
        ("DigitalPortOne", UCHAR, 1),
        ("DigitalPortTwo", UCHAR, 1),
        ("Mode2Form1", UCHAR, 1),
        ("Mode2Form2", UCHAR, 1),
        ("MultiSession", UCHAR, 1),
        ("BufferUnderrunFree", UCHAR, 1),  # offset 4
        ("CDDA", UCHAR, 1),
        ("CDDAAccurate", UCHAR, 1),
        ("RWSupported", UCHAR, 1),
        ("RWDeinterleaved", UCHAR, 1),
        ("C2Pointers", UCHAR, 1),
        ("ISRC", UCHAR, 1),
        ("UPC", UCHAR, 1),
        ("ReadBarCodeCapable", UCHAR, 1),  # offset 5
        ("Lock", UCHAR, 1),
        ("LockState", UCHAR, 1),
        ("PreventJumper", UCHAR, 1),
        ("Eject", UCHAR, 1),
        ("Reserved6", UCHAR, 1),
        ("LoadingMechanismType", UCHAR, 3),  # offset 6
        ("SeparateVolume", UCHAR, 1),
        ("SeperateChannelMute", UCHAR, 1),
        ("SupportsDiskPresent", UCHAR, 1),
        ("SWSlotSelection", UCHAR, 1),
        ("SideChangeCapable", UCHAR, 1),
        ("RWInLeadInReadable", UCHAR, 1),
        ("Reserved7", UCHAR, 2),  # offset 7
        (
            "_unnamed_union",
            make_union(
                [
                    ("ReadSpeedMaximum", UCHAR * 2),
                    ("ObsoleteReserved", UCHAR * 2),  # offset 8
                ],
                _pack_,
            ),
        ),
        ("NumberVolumeLevels", UCHAR * 2),  # offset 10
        ("BufferSize", UCHAR * 2),  # offset 12
        (
            "_unnamed_union",
            make_union(
                [
                    ("ReadSpeedCurrent", UCHAR * 2),
                    ("ObsoleteReserved2", UCHAR * 2),  # offset 14
                ],
                _pack_,
            ),
        ),
        ("ObsoleteReserved3", UCHAR),  # offset 16
        ("Reserved8", UCHAR, 1),
        ("BCK", UCHAR, 1),
        ("RCK", UCHAR, 1),
        ("LSBF", UCHAR, 1),
        ("Length", UCHAR, 2),
        ("Reserved9", UCHAR, 2),  # offset 17
        (
            "_unnamed_union",
            make_union(
                [
                    ("WriteSpeedMaximum", UCHAR * 2),
                    ("ObsoleteReserved4", UCHAR * 2),  # offset 18
                ],
                _pack_,
            ),
        ),
        (
            "_unnamed_union",
            make_union(
                [
                    ("WriteSpeedCurrent", UCHAR * 2),
                    ("ObsoleteReserved11", UCHAR * 2),  # offset 20
                ],
                _pack_,
            ),
        ),
        # NOTE: This mode page is two bytes too small in the release
        #       version of the Windows2000 DDK.  it also incorrectly
        #       put the CopyManagementRevision at offset 20 instead
        #       of offset 22, so fix that with a nameless union (for
        #       backwards-compatibility with those who "fixed" it on
        #       their own by looking at Reserved10[]).
        (
            "_unnamed_union",
            make_union(
                [
                    ("CopyManagementRevision", UCHAR * 2),  # offset 22
                    ("Reserved10", UCHAR * 2),
                ],
                _pack_,
            ),
        ),
        # UCHAR Reserved12[2];                    # offset 24
    ]


PCDVD_CAPABILITIES_PAGE = POINTER(CDVD_CAPABILITIES_PAGE)
_pack_ -= 1

_pack_ += 1


class LUN_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LunListLength", UCHAR * 4),  # sizeof LunSize * 8
        ("Reserved", UCHAR * 4),
        # if !defined(__midl)
        ("Lun", (UCHAR * 0) * 8),  # 4 level of addressing.  2 bytes each.
        # endif
    ]


PLUN_LIST = POINTER(LUN_LIST)
_pack_ -= 1


LOADING_MECHANISM_CADDY = 0x00
LOADING_MECHANISM_TRAY = 0x01
LOADING_MECHANISM_POPUP = 0x02
LOADING_MECHANISM_INDIVIDUAL_CHANGER = 0x04
LOADING_MECHANISM_CARTRIDGE_CHANGER = 0x05

# end C/DVD 0.9 mode page definitions

# Define Mode Subpage header.
_pack_ += 1


class MODE_PAGE_SUBPAGE_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),
        ("SubPageFormat", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("SubPageCode", UCHAR),
        ("PageLength", UCHAR * 2),
    ]


PMODE_PAGE_SUBPAGE_HEADER = POINTER(MODE_PAGE_SUBPAGE_HEADER)
_pack_ -= 1

# Define Command Duration Limit Mode Subpages.

COMMAND_DURATION_LIMIT_T2_UNIT_NONE = 0
COMMAND_DURATION_LIMIT_T2_UNIT_500NS = 0x06
COMMAND_DURATION_LIMIT_T2_UNIT_1US = 0x08
COMMAND_DURATION_LIMIT_T2_UNIT_10MS = 0x0A
COMMAND_DURATION_LIMIT_T2_UNIT_500MS = 0x0E

DURATION_LIMIT_T2_DESCRIPTOR_COUNT = 7

COMMAND_DURATION_LIMIT_T2_POLICY_DO_NOTHING = 0
COMMAND_DURATION_LIMIT_T2_POLICY_CONTINUE_WITH_NEXT = 0x01
COMMAND_DURATION_LIMIT_T2_POLICY_CONTINUE = 0x02
COMMAND_DURATION_LIMIT_T2_POLICY_COMPLETE_DATA_UNAVAILABLE = 0x0D
COMMAND_DURATION_LIMIT_T2_POLICY_ABORT_TIMEOUT_PARTIAL_TRANSFER = 0x0E
COMMAND_DURATION_LIMIT_T2_POLICY_AOBRT_TIMEOUT = 0x0F

_pack_ += 1


class T2_COMMAND_DURATION_LIMIT_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("T2CDLUNITS", UCHAR, 4),
        ("Reserved", UCHAR, 4),
        ("Reserved1", UCHAR),
        ("MAX_INACTIVE_TIME", UCHAR * 2),
        ("MAX_ACTIVE_TIME", UCHAR * 2),
        ("MAX_ACTIVE_TIME_POLICY", UCHAR, 4),
        ("MAX_INACTIVE_TIME_POLICY", UCHAR, 4),
        ("Reserved2", UCHAR * 3),
        ("COMMAND_DURATION_GUIDELINE", UCHAR * 2),
        ("Reserved3", UCHAR * 2),
        ("COMMAND_DURATION_GUIDELINE_POLICY", UCHAR, 4),
        ("Reserved4", UCHAR, 4),
        ("BypassSequestration", UCHAR, 1),
        ("Reserved5", UCHAR, 7),
        ("Reserved6", UCHAR * 16),
    ]


PT2_COMMAND_DURATION_LIMIT_DESCRIPTOR = POINTER(T2_COMMAND_DURATION_LIMIT_DESCRIPTOR)


class MODE_COMMAND_DURATION_LIMIT_PAGE_T2A_SUBPAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x0A
        ("SubPageFormat", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("SubPageCode", UCHAR),  # 0x07
        ("PageLength", UCHAR * 2),  # Page length is 0x00E4 for T2A subpage
        ("Reserved", UCHAR * 3),
        ("Reserved1", UCHAR, 4),
        ("PerfvsCommandDurationGuidelines", UCHAR, 4),
        (
            "T2CommandDurationLimitDescriptors",
            T2_COMMAND_DURATION_LIMIT_DESCRIPTOR * DURATION_LIMIT_T2_DESCRIPTOR_COUNT,
        ),
    ]


PMODE_COMMAND_DURATION_LIMIT_PAGE_T2A_SUBPAGE = POINTER(MODE_COMMAND_DURATION_LIMIT_PAGE_T2A_SUBPAGE)

assert sizeof(MODE_COMMAND_DURATION_LIMIT_PAGE_T2A_SUBPAGE) == (0xE4 + sizeof(MODE_PAGE_SUBPAGE_HEADER))


class MODE_COMMAND_DURATION_LIMIT_PAGE_T2B_SUBPAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR, 6),  # 0x0A
        ("SubPageFormat", UCHAR, 1),
        ("PageSavable", UCHAR, 1),
        ("SubPageCode", UCHAR),  # 0x08
        ("PageLength", UCHAR * 2),  # Page length is 0x00E4 for T2B subpage
        ("Reserved", UCHAR * 3),
        ("Reserved1", UCHAR, 4),
        ("PerfvsLatencyControls", UCHAR, 4),
        (
            "T2CommandDurationLimitDescriptors",
            T2_COMMAND_DURATION_LIMIT_DESCRIPTOR * DURATION_LIMIT_T2_DESCRIPTOR_COUNT,
        ),
    ]


PMODE_COMMAND_DURATION_LIMIT_PAGE_T2B_SUBPAGE = POINTER(MODE_COMMAND_DURATION_LIMIT_PAGE_T2B_SUBPAGE)

assert sizeof(MODE_COMMAND_DURATION_LIMIT_PAGE_T2B_SUBPAGE) == (0xE4 + sizeof(MODE_PAGE_SUBPAGE_HEADER))
_pack_ -= 1

# Mode parameter list block descriptor -
# set the block length for reading/writing

MODE_BLOCK_DESC_LENGTH = 8
MODE_HEADER_LENGTH = 4
MODE_HEADER_LENGTH10 = 8

_pack_ += 1


class MODE_PARM_READ_WRITE_DATA(Structure):  # MODE_PARM_READ_WRITE
    _pack_ = _pack_
    _fields_ = [
        ("ParameterListHeader", MODE_PARAMETER_HEADER),  # List Header Format
        ("ParameterListBlock", MODE_PARAMETER_BLOCK),  # List Block Descriptor
    ]


PMODE_PARM_READ_WRITE_DATA = POINTER(MODE_PARM_READ_WRITE_DATA)
_pack_ -= 1

# end_ntminitape

# CDROM audio control (0x0E)

CDB_AUDIO_PAUSE = 0
CDB_AUDIO_RESUME = 1

CDB_DEVICE_START = 0x11
CDB_DEVICE_STOP = 0x10

CDB_EJECT_MEDIA = 0x10
CDB_LOAD_MEDIA = 0x01

CDB_SUBCHANNEL_HEADER = 0x00
CDB_SUBCHANNEL_BLOCK = 0x01

CDROM_AUDIO_CONTROL_PAGE = 0x0E
MODE_SELECT_IMMEDIATE = 0x04
MODE_SELECT_PFBIT = 0x10

CDB_USE_MSF = 0x01

_pack_ += 1


class PORT_OUTPUT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ChannelSelection", UCHAR),
        ("Volume", UCHAR),
    ]


PPORT_OUTPUT = POINTER(PORT_OUTPUT)


class AUDIO_OUTPUT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CodePage", UCHAR),
        ("ParameterLength", UCHAR),
        ("Immediate", UCHAR),
        ("Reserved", UCHAR * 2),
        ("LbaFormat", UCHAR),
        ("LogicalBlocksPerSecond", UCHAR * 2),
        ("PortOutput", PORT_OUTPUT * 4),
    ]


PAUDIO_OUTPUT = POINTER(AUDIO_OUTPUT)
_pack_ -= 1

# Multisession CDROM

GET_LAST_SESSION = 0x01
# define GET_SESSION_DATA 0x02;

# Atapi 2.5 changer

_pack_ += 1


class MECHANICAL_STATUS_INFORMATION_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CurrentSlot", UCHAR, 5),
        ("ChangerState", UCHAR, 2),
        ("Fault", UCHAR, 1),
        ("Reserved", UCHAR, 5),
        ("MechanismState", UCHAR, 3),
        ("CurrentLogicalBlockAddress", UCHAR * 3),
        ("NumberAvailableSlots", UCHAR),
        ("SlotTableLength", UCHAR * 2),
    ]


PMECHANICAL_STATUS_INFORMATION_HEADER = POINTER(MECHANICAL_STATUS_INFORMATION_HEADER)


class SLOT_TABLE_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DiscChanged", UCHAR, 1),
        ("Reserved", UCHAR, 6),
        ("DiscPresent", UCHAR, 1),
        ("Reserved2", UCHAR * 3),
    ]


PSLOT_TABLE_INFORMATION = POINTER(SLOT_TABLE_INFORMATION)


class MECHANICAL_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("MechanicalStatusHeader", MECHANICAL_STATUS_INFORMATION_HEADER),
        ("SlotTableInfo", SLOT_TABLE_INFORMATION * 1),
    ]


PMECHANICAL_STATUS = POINTER(MECHANICAL_STATUS)
_pack_ -= 1

# Structure related to 0x42 - SCSIOP_UNMAP

_pack_ += 1


class UNMAP_BLOCK_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("StartingLba", UCHAR * 8),
        ("LbaCount", UCHAR * 4),
        ("Reserved", UCHAR * 4),
    ]


PUNMAP_BLOCK_DESCRIPTOR = POINTER(UNMAP_BLOCK_DESCRIPTOR)


class UNMAP_LIST_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DataLength", UCHAR * 2),
        ("BlockDescrDataLength", UCHAR * 2),
        ("Reserved", UCHAR * 4),
        # if !defined(__midl)
        ("Descriptors", UNMAP_BLOCK_DESCRIPTOR * 0),
        # endif
    ]


PUNMAP_LIST_HEADER = POINTER(UNMAP_LIST_HEADER)
_pack_ -= 1


# begin_ntminitape

# Tape definitions

_pack_ += 1


class TAPE_POSITION_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR, 2),
        ("BlockPositionUnsupported", UCHAR, 1),
        ("Reserved2", UCHAR, 3),
        ("EndOfPartition", UCHAR, 1),
        ("BeginningOfPartition", UCHAR, 1),
        ("PartitionNumber", UCHAR),
        ("Reserved3", USHORT),
        ("FirstBlock", UCHAR * 4),
        ("LastBlock", UCHAR * 4),
        ("Reserved4", UCHAR),
        ("NumberOfBlocks", UCHAR * 3),
        ("NumberOfBytes", UCHAR * 4),
    ]


PTAPE_POSITION_DATA = POINTER(TAPE_POSITION_DATA)
_pack_ -= 1

# This structure is used to convert little endian
# ULONGs to SCSI CDB big endians values.

_pack_ += 1


class EIGHT_BYTE(Union):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_struct",
            make_struct(
                [
                    ("Byte0", UCHAR),
                    ("Byte1", UCHAR),
                    ("Byte2", UCHAR),
                    ("Byte3", UCHAR),
                    ("Byte4", UCHAR),
                    ("Byte5", UCHAR),
                    ("Byte6", UCHAR),
                    ("Byte7", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("AsULongLong", ULONGLONG),
    ]


PEIGHT_BYTE = POINTER(EIGHT_BYTE)


class FOUR_BYTE(Union):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_struct",
            make_struct(
                [
                    ("Byte0", UCHAR),
                    ("Byte1", UCHAR),
                    ("Byte2", UCHAR),
                    ("Byte3", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("AsULong", ULONG),
    ]


PFOUR_BYTE = POINTER(FOUR_BYTE)


class TWO_BYTE(Union):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_struct",
            make_struct(
                [
                    ("Byte0", UCHAR),
                    ("Byte1", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("AsUShort", USHORT),
    ]


PTWO_BYTE = POINTER(TWO_BYTE)
_pack_ -= 1


# Define alignment requirements for variable length components in extended SRB.
# For Win64, need to ensure all variable length components are 8 bytes align
# so the pointer fields within the variable length components are 8 bytes align.
# if defined(_WIN64) || defined(_M_ALPHA)
STOR_ADDRESS_ALIGN = DECLSPEC_ALIGN(8)
# else
# define STOR_ADDRESS_ALIGN
# endif


# Generic structure definition for accessing any STOR_ADDRESS. All
# STOR_ADDRESS must begin with a Type, Port and AddressLength field.
class STOR_ADDRESS(Structure):
    _pack_ = 8
    _fields_ = [
        ("Type", USHORT),
        ("Port", USHORT),
        ("AddressLength", ULONG),
        ("AddressData", UCHAR * ANYSIZE_ARRAY),
    ]


PSTOR_ADDRESS = POINTER(STOR_ADDRESS)

# Define different storage address types
STOR_ADDRESS_TYPE_UNKNOWN = 0x0
STOR_ADDRESS_TYPE_BTL8 = 0x1
STOR_ADDRESS_TYPE_MAX = 0xFFFF

# Define 8 bit bus, target and LUN address scheme
STOR_ADDR_BTL8_ADDRESS_LENGTH = 4


class STOR_ADDR_BTL8(Structure):
    _pack_ = 8
    _fields_ = [
        ("Type", USHORT),
        ("Port", USHORT),
        ("AddressLength", ULONG),
        ("Path", UCHAR),
        ("Target", UCHAR),
        ("Lun", UCHAR),
        ("Reserved", UCHAR),
    ]


PSTOR_ADDR_BTL8 = POINTER(STOR_ADDR_BTL8)

# if (NTDDI_VERSION >= NTDDI_WIN8)


#
# Ses definitions

SES_DIAGNOSTIC_PAGE_CONFIGURATION = 0x01
SES_DIAGNOSTIC_PAGE_CONTROL = 0x02
SES_DIAGNOSTIC_PAGE_STATUS = 0x02
SES_DIAGNOSTIC_PAGE_STRING_IN = 0x04
SES_DIAGNOSTIC_PAGE_ADDITIONAL_ELEMENT_STATUS = 0x0A
SES_DIAGNOSTIC_PAGE_DOWNLOAD_MICROCODE = 0x0E

SES_SAS_PROTOCOL_IDENTIFIER = 6


class SES_ELEMENT_TYPE(CEnum):
    SesElementTypeUnknown = 0
    SesElementTypeDeviceSlot = 1
    SesElementTypePowerSupply = 2
    SesElementTypeCooling = 3
    SesElementTypeTemperatureSensor = 4
    SesElementTypeDoor = 5
    SesElementTypeAudibleAlarm = 6
    SesElementTypeController = 7
    SesElementTypeScsiController = 8
    SesElementTypeNonVolatileCache = 9
    SesElementTypeInvalidOperationReason = 10
    SesElementTypeUps = 11
    SesElementTypeDisplay = 12
    SesElementTypeKeypad = 13
    SesElementTypeEnclosure = 14
    SesElementTypeScsiPort = 15
    SesElementTypeLanguage = 16
    SesElementTypeCommunicationPort = 17
    SesElementTypeVoltageSensor = 18
    SesElementTypeCurrentSensor = 19
    SesElementTypeScsiTargetPort = 20
    SesElementTypeScsiInitiatorPort = 21
    SesElementTypeSubEnclosure = 22
    SesElementTypeArrayDeviceSlot = 23
    SesElementTypeSasExpander = 24
    SesElementTypeSasConnector = 25
    SesElementTypeMax = 26


PSES_ELEMENT_TYPE = POINTER(SES_ELEMENT_TYPE)


class SES_ELEMENT_STATE(CEnum):
    SesElementStateNotReported = 0  # Unknown
    SesElementStateOkay = 1  # Healthy
    SesElementStateCritical = 2  # Unhealthy
    SesElementStateNonCritical = 3  # Warning
    SesElementStateUnrecoverable = 4  # Unhealthy
    SesElementStateNotInstalled = 5  # Unknown
    SesElementStateUnknown = 6  # Unhealthy
    SesElementStateNotAvailable = 7  # Warning
    SesElementStateNoAccessAllowed = 8  # Warning
    SesElementStateMax = 9


PSES_ELEMENT_STATE = POINTER(SES_ELEMENT_STATE)


class SES_DOWNLOAD_MICROCODE_STATE(CEnum):
    SesDownloadMcStateNoneInProgress = 0x00
    SesDownloadMcStateInProgress = 0x01
    SesDownloadMcStateCompletedPendingReset = 0x11
    SesDownloadMcStateCompletedPendingPowerOn = 0x12
    SesDownloadMcStateCompletedPendingActivation = 0x13


PSES_DOWNLOAD_MICROCODE_STATE = POINTER(SES_DOWNLOAD_MICROCODE_STATE)

_pack_ += 1


class SES_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("Reserved", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("PageData", UCHAR * ANYSIZE_ARRAY),
    ]


PSES_DIAGNOSTIC_PAGE = POINTER(SES_DIAGNOSTIC_PAGE)


class SES_TYPE_DESCRIPTOR_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ElementType", UCHAR),  # Byte  0
        ("NumberOfPossibleElements", UCHAR),  # Byte  1
        ("SubEnclosureId", UCHAR),  # Byte  2
        ("TypeDescriptorTextLength", UCHAR),  # Byte  3
    ]


PSES_TYPE_DESCRIPTOR_HEADER = POINTER(SES_TYPE_DESCRIPTOR_HEADER)


class SES_ENCLOSURE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfEnclosureServices", UCHAR, 3),  # Byte  0, bit 0-2
        ("Reserved1", UCHAR, 1),  # Byte  0, bit 3
        ("RelativeEnclosureServicesId", UCHAR, 3),  # Byte  0, bit 4-6
        ("Reserved2", UCHAR, 1),  # Byte  0, bit 7
        ("SubEnclosureId", UCHAR),  # Byte  1
        ("NumberOfTypeDescriptorHeaders", UCHAR),  # Byte  2
        ("EnclosureDescriptorLength", UCHAR),  # Byte  3
        ("Identifier", UCHAR * 8),  # Byte  4-11
        ("VendorId", UCHAR * 8),  # Byte 12-19
        ("ProductId", UCHAR * 16),  # Byte 20-35
        ("ProductRevisionLevel", UCHAR * 4),  # Byte 36-39
        ("VendorSpecific", UCHAR * ANYSIZE_ARRAY),
    ]


PSES_ENCLOSURE_DESCRIPTOR = POINTER(SES_ENCLOSURE_DESCRIPTOR)


class SES_CONFIGURATION_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("NumberOfSecondarySubEnclosures", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("GenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Descriptors", SES_ENCLOSURE_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_CONFIGURATION_DIAGNOSTIC_PAGE = POINTER(SES_CONFIGURATION_DIAGNOSTIC_PAGE)


class SES_CONTROL_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", UCHAR, 4),  # Byte  0, bit 0-3
        ("ResetSwap", UCHAR, 1),  # Byte  0, bit 4
        ("Disable", UCHAR, 1),  # Byte  0, bit 5
        ("PredictFailure", UCHAR, 1),  # Byte  0, bit 6
        ("Select", UCHAR, 1),  # Byte  0, bit 7
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "DeviceSlot",
                        make_struct(
                            [
                                ("Reserved1", UCHAR),  # Byte  1
                                ("Reserved2", UCHAR, 1),  # Byte  2, bit 0
                                ("RequestIdentify", UCHAR, 1),  # Byte  2, bit 1
                                ("RequestRemove", UCHAR, 1),  # Byte  2, bit 2
                                ("RequestInsert", UCHAR, 1),  # Byte  2, bit 3
                                ("RequestMissing", UCHAR, 1),  # Byte  2, bit 4
                                ("Reserved3", UCHAR, 1),  # Byte  2, bit 5
                                ("DoNotRemove", UCHAR, 1),  # Byte  2, bit 6
                                ("RequestActive", UCHAR, 1),  # Byte  2, bit 7
                                ("Reserved4", UCHAR, 2),  # Byte  3, bit 0-1
                                ("EnableBypassB", UCHAR, 1),  # Byte  3, bit 2
                                ("EnableBypassA", UCHAR, 1),  # Byte  3, bit 3
                                ("DeviceOff", UCHAR, 1),  # Byte  3, bit 4
                                ("RequestFault", UCHAR, 1),  # Byte  3, bit 5
                                ("Reserved5", UCHAR, 2),  # Byte  3, bit 6-7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "PowerSupply",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 7),  # Byte  1, bit 0-6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR),  # Byte  2
                                ("Reserved3", UCHAR, 5),  # Byte  3, bit 0-4
                                ("RequestOn", UCHAR, 1),  # Byte  3, bit 5
                                ("RequestFail", UCHAR, 1),  # Byte  3, bit 6
                                ("Reserved4", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Cooling",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 7),  # Byte  1, bit 0-6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR),  # Byte  2
                                ("RequestSpeedCode", UCHAR, 3),  # Byte  3, bit 0-2
                                ("Reserved3", UCHAR, 2),  # Byte  3, bit 3-4
                                ("RequestOn", UCHAR, 1),  # Byte  3, bit 5
                                ("RequestFail", UCHAR, 1),  # Byte  3, bit 6
                                ("Reserved4", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "TemperatureSensor",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 6),  # Byte  1, bit 0-5
                                ("RequestFail", UCHAR, 1),  # Byte  1, bit 6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR),  # Byte  2
                                ("Reserved3", UCHAR),  # Byte  3
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "VoltageSensor",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 6),  # Byte  1, bit 0-5
                                ("RequestFail", UCHAR, 1),  # Byte  1, bit 6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR),  # Byte  2
                                ("Reserved3", UCHAR),  # Byte  3
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "CurrentSensor",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 6),  # Byte  1, bit 0-5
                                ("RequestFail", UCHAR, 1),  # Byte  1, bit 6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR),  # Byte  2
                                ("Reserved3", UCHAR),  # Byte  3
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Enclosure",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 7),  # Byte  1, bit 0-6
                                ("RequestIdentify", UCHAR, 1),  # Byte  1, bit 7
                                ("PowerCycleDelay", UCHAR, 6),  # Byte  2, bit 0-5
                                ("PowerCycleRequest", UCHAR, 2),  # Byte  2, bit 6-7
                                ("RequestWarning", UCHAR, 1),  # Byte  3, bit 0
                                ("RequestFailure", UCHAR, 1),  # Byte  3, bit 1
                                ("PowerOffDuration", UCHAR, 6),  # Byte  3, bit 2-7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "ArrayDeviceSlot",
                        make_struct(
                            [
                                ("RequestRebuildAbort", UCHAR, 1),  # Byte  1, bit 0
                                ("RequestRebuild", UCHAR, 1),  # Byte  1, bit 1
                                ("RequestInFailedArray", UCHAR, 1),  # Byte  1, bit 2
                                ("RequestInCriticalArray", UCHAR, 1),  # Byte  1, bit 3
                                ("RequestConsistencyArray", UCHAR, 1),  # Byte  1, bit 4
                                ("RequestHotSpare", UCHAR, 1),  # Byte  1, bit 5
                                ("RequestReservedDevice", UCHAR, 1),  # Byte  1, bit 6
                                ("RequestOK", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved1", UCHAR, 1),  # Byte  2, bit 0
                                ("RequestIdentify", UCHAR, 1),  # Byte  2, bit 1
                                ("RequestRemove", UCHAR, 1),  # Byte  2, bit 2
                                ("RequestInsert", UCHAR, 1),  # Byte  2, bit 3
                                ("RequestMissing", UCHAR, 1),  # Byte  2, bit 4
                                ("Reserved2", UCHAR, 1),  # Byte  2, bit 5
                                ("DoNotRemove", UCHAR, 1),  # Byte  2, bit 6
                                ("RequestActive", UCHAR, 1),  # Byte  2, bit 7
                                ("Reserved3", UCHAR, 2),  # Byte  3, bit 0-1
                                ("EnableBypassB", UCHAR, 1),  # Byte  3, bit 2
                                ("EnableBypassA", UCHAR, 1),  # Byte  3, bit 3
                                ("DeviceOff", UCHAR, 1),  # Byte  3, bit 4
                                ("RequestFault", UCHAR, 1),  # Byte  3, bit 5
                                ("Reserved4", UCHAR, 2),  # Byte  3, bit 6-7
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
    ]


PSES_CONTROL_DESCRIPTOR = POINTER(SES_CONTROL_DESCRIPTOR)


class SES_CONTROL_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("Unrecoverable", UCHAR, 1),  # Byte  1, bit 0
        ("Critical", UCHAR, 1),  # Byte  1, bit 1
        ("NonCritical", UCHAR, 1),  # Byte  1, bit 2
        ("Informational", UCHAR, 1),  # Byte  1, bit 3
        ("Reserved", UCHAR, 4),  # Byte  1, bit 4-7
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("ExpectedGenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Descriptors", SES_CONTROL_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_CONTROL_DIAGNOSTIC_PAGE = POINTER(SES_CONTROL_DIAGNOSTIC_PAGE)


class SES_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ElementStatus", UCHAR, 4),  # Byte  0, bit 0-3
        ("Swap", UCHAR, 1),  # Byte  0, bit 4
        ("Disabled", UCHAR, 1),  # Byte  0, bit 5
        ("PredictedFailure", UCHAR, 1),  # Byte  0, bit 6
        ("Reserved1", UCHAR, 1),  # Byte  0, bit 7
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "DeviceSlot",
                        make_struct(
                            [
                                ("SlotAddress", UCHAR),  # Byte  1
                                ("Report", UCHAR, 1),  # Byte  2, bit 0
                                ("Identify", UCHAR, 1),  # Byte  2, bit 1
                                ("Remove", UCHAR, 1),  # Byte  2, bit 2
                                ("ReadyToInsert", UCHAR, 1),  # Byte  2, bit 3
                                ("EnclosureBypassedB", UCHAR, 1),  # Byte  2, bit 4
                                ("EnclosureBypassedA", UCHAR, 1),  # Byte  2, bit 5
                                ("DoNotRemove", UCHAR, 1),  # Byte  2, bit 6
                                ("AppBypassedA", UCHAR, 1),  # Byte  2, bit 7
                                ("DeviceBypassedB", UCHAR, 1),  # Byte  3, bit 0
                                ("DeviceBypassedA", UCHAR, 1),  # Byte  3, bit 1
                                ("BypassedB", UCHAR, 1),  # Byte  3, bit 2
                                ("BypassedA", UCHAR, 1),  # Byte  3, bit 3
                                ("DeviceOff", UCHAR, 1),  # Byte  3, bit 4
                                ("FaultRequested", UCHAR, 1),  # Byte  3, bit 5
                                ("FaultSensed", UCHAR, 1),  # Byte  3, bit 6
                                ("AppBypassedB", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "PowerSupply",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 7),  # Byte  1, bit 0-6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("Reserved2", UCHAR, 1),  # Byte  2, bit 0
                                ("DCOverCurrent", UCHAR, 1),  # Byte  2, bit 1
                                ("DCUnderVoltage", UCHAR, 1),  # Byte  2, bit 2
                                ("DCOverVoltage", UCHAR, 1),  # Byte  2, bit 3
                                ("Reserved3", UCHAR, 4),  # Byte  2, bit 4-7
                                ("DCFail", UCHAR, 1),  # Byte  3, bit 0
                                ("ACFail", UCHAR, 1),  # Byte  3, bit 1
                                ("TemperatureWarning", UCHAR, 1),  # Byte  3, bit 2
                                ("OverTemperatureFail", UCHAR, 1),  # Byte  3, bit 3
                                ("Off", UCHAR, 1),  # Byte  3, bit 4
                                ("RequestedOn", UCHAR, 1),  # Byte  3, bit 5
                                ("Fail", UCHAR, 1),  # Byte  3, bit 6
                                ("HotSwap", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Cooling",
                        make_struct(
                            [
                                ("ActualFanSpeedMSB", UCHAR, 3),  # Byte  1, bit 0-2
                                ("Reserved1", UCHAR, 4),  # Byte  1, bit 3-6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("ActualFanSpeedLSB", UCHAR),  # Byte  2
                                ("ActualSpeedCode", UCHAR, 3),  # Byte  3, bit 0-2
                                ("Reserved2", UCHAR, 1),  # Byte  3, bit 3
                                ("Off", UCHAR, 1),  # Byte  3, bit 4
                                ("RequestedOn", UCHAR, 1),  # Byte  3, bit 5
                                ("Fail", UCHAR, 1),  # Byte  3, bit 6
                                ("HotSwap", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "TemperatureSensor",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 6),  # Byte  1, bit 0-5
                                ("Fail", UCHAR, 1),  # Byte  1, bit 6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("Temperature", UCHAR),  # Byte  2
                                ("UnderTemperatureWarning", UCHAR, 1),  # Byte  3, bit 0
                                ("UnderTemperatureFailure", UCHAR, 1),  # Byte  3, bit 1
                                ("OverTemperatureWarning", UCHAR, 1),  # Byte  3, bit 2
                                ("OverTemperatureFailure", UCHAR, 1),  # Byte  3, bit 3
                                ("Reserved2", UCHAR, 4),  # Byte  3, bit 4-7
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "VoltageSensor",
                        make_struct(
                            [
                                ("CritUnder", UCHAR, 1),  # Byte  1, bit 0
                                ("CritOver", UCHAR, 1),  # Byte  1, bit 1
                                ("WarnUnder", UCHAR, 1),  # Byte  1, bit 2
                                ("WarnOver", UCHAR, 1),  # Byte  1, bit 3
                                ("Reserved1", UCHAR, 2),  # Byte  1, bit 4-5
                                ("Fail", UCHAR, 1),  # Byte  1, bit 6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("VoltageMSB", UCHAR),  # Byte  2
                                ("VoltageLSB", UCHAR),  # Byte  3
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "CurrentSensor",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 1),  # Byte  1, bit 0
                                ("CritOver", UCHAR, 1),  # Byte  1, bit 1
                                ("Reserved2", UCHAR, 1),  # Byte  1, bit 2
                                ("WarnOver", UCHAR, 1),  # Byte  1, bit 3
                                ("Reserved3", UCHAR, 2),  # Byte  1, bit 4-5
                                ("Fail", UCHAR, 1),  # Byte  1, bit 6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("CurrentMSB", UCHAR),  # Byte  2
                                ("CurrentLSB", UCHAR),  # Byte  3
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "Enclosure",
                        make_struct(
                            [
                                ("Reserved1", UCHAR, 7),  # Byte  1, bit 0-6
                                ("Identify", UCHAR, 1),  # Byte  1, bit 7
                                ("WarningIndication", UCHAR, 1),  # Byte  2, bit 0
                                ("FailureIndication", UCHAR, 1),  # Byte  2, bit 1
                                ("TimeUntilPowerCycle", UCHAR, 6),  # Byte  2, bit 6
                                ("WarningRequested", UCHAR, 1),  # Byte  3, bit 0
                                ("FailureRequested", UCHAR, 1),  # Byte  3, bit 1
                                ("RequestedPowerOffTime", UCHAR, 6),  # Byte  3, bit 6
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "ArrayDeviceSlot",
                        make_struct(
                            [
                                ("RebuildAbort", UCHAR, 1),  # Byte  1, bit 0
                                ("Rebuild", UCHAR, 1),  # Byte  1, bit 1
                                ("InFailedArray", UCHAR, 1),  # Byte  1, bit 2
                                ("InCriticalArray", UCHAR, 1),  # Byte  1, bit 3
                                ("ConsistencyCheck", UCHAR, 1),  # Byte  1, bit 4
                                ("HotSpare", UCHAR, 1),  # Byte  1, bit 5
                                ("ReservedDevice", UCHAR, 1),  # Byte  1, bit 6
                                ("OK", UCHAR, 1),  # Byte  1, bit 7
                                ("Report", UCHAR, 1),  # Byte  2, bit 0
                                ("Identify", UCHAR, 1),  # Byte  2, bit 1
                                ("Remove", UCHAR, 1),  # Byte  2, bit 2
                                ("ReadyToInsert", UCHAR, 1),  # Byte  2, bit 3
                                ("EnclosureBypassedB", UCHAR, 1),  # Byte  2, bit 4
                                ("EnclosureBypassedA", UCHAR, 1),  # Byte  2, bit 5
                                ("DoNotRemove", UCHAR, 1),  # Byte  2, bit 6
                                ("AppBypassedA", UCHAR, 1),  # Byte  2, bit 7
                                ("DeviceBypassedB", UCHAR, 1),  # Byte  3, bit 0
                                ("DeviceBypassedA", UCHAR, 1),  # Byte  3, bit 1
                                ("BypassedB", UCHAR, 1),  # Byte  3, bit 2
                                ("BypassedA", UCHAR, 1),  # Byte  3, bit 3
                                ("DeviceOff", UCHAR, 1),  # Byte  3, bit 4
                                ("FaultRequested", UCHAR, 1),  # Byte  3, bit 5
                                ("FaultSensed", UCHAR, 1),  # Byte  3, bit 6
                                ("AppBypassedB", UCHAR, 1),  # Byte  3, bit 7
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
    ]


PSES_STATUS_DESCRIPTOR = POINTER(SES_STATUS_DESCRIPTOR)


class SES_STATUS_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("Unrecoverable", UCHAR, 1),  # Byte  1, bit 0
        ("Critical", UCHAR, 1),  # Byte  1, bit 1
        ("NonCritical", UCHAR, 1),  # Byte  1, bit 2
        ("Informational", UCHAR, 1),  # Byte  1, bit 3
        ("InvalidOperation", UCHAR, 1),  # Byte  1, bit 4
        ("Reserved", UCHAR, 3),  # Byte  1, bit 5-7
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("GenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Descriptors", SES_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_STATUS_DIAGNOSTIC_PAGE = POINTER(SES_STATUS_DIAGNOSTIC_PAGE)


class SES_PHY_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR, 4),  # Byte  0, bit 0-3
        ("DeviceType", UCHAR, 3),  # Byte  0, bit 4-6
        ("Reserved3", UCHAR, 1),  # Byte  0, bit 7
        ("Reserved4", UCHAR),  # Byte  1
        ("Reserved5", UCHAR, 1),  # Byte  2, bit 0
        ("SmpInitiatorPort", UCHAR, 1),  # Byte  2, bit 1
        ("StpInitiatorPort", UCHAR, 1),  # Byte  2, bit 2
        ("SspInitiatorPort", UCHAR, 1),  # Byte  2, bit 3
        ("Reserved6", UCHAR, 4),  # Byte  2, bit 4-7
        ("SataDevice", UCHAR, 1),  # Byte  3, bit 0
        ("SmpTargetPort", UCHAR, 1),  # Byte  3, bit 1
        ("StpTargetPort", UCHAR, 1),  # Byte  3, bit 2
        ("SspTargetPort", UCHAR, 1),  # Byte  3, bit 3
        ("Reserved7", UCHAR, 3),  # Byte  3, bit 4-6
        ("SataPortSelector", UCHAR, 1),  # Byte  3, bit 7
        ("AttachedSASAddress", UCHAR * 8),  # Bytes 4-11
        ("SASAddress", UCHAR * 8),  # Bytes 12-19
        ("PhyIdentifier", UCHAR),  # Byte  20
        ("Reserved2", UCHAR * 7),  # Bytes 21-27
    ]


PSES_PHY_DESCRIPTOR = POINTER(SES_PHY_DESCRIPTOR)


class SES_SAS_SLOT_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfPhyDescriptors", UCHAR),  # Byte  0
        ("NotAllPhys", UCHAR, 1),  # Byte  1, bit 0
        ("Reserved1", UCHAR, 5),  # Byte  1, bit 1-5
        ("Type", UCHAR, 2),  # Byte  1, bit 6-7
        ("Reserved2", UCHAR),  # Byte  2
        ("DeviceSlotNumber", UCHAR),  # Byte  3
        ("PhyDescriptors", SES_PHY_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_SAS_SLOT_INFORMATION = POINTER(SES_SAS_SLOT_INFORMATION)


class SES_PROTOCOL_INFORMATION(Union):
    _pack_ = _pack_
    _fields_ = [
        # Add additional protocol infos
        # as needed
        ("SasSlot", SES_SAS_SLOT_INFORMATION),
    ]


PSES_PROTOCOL_INFORMATION = POINTER(SES_PROTOCOL_INFORMATION)


class SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        # We expect EIP to be set to 1
        ("ProtocolIdentifier", UCHAR, 4),  # Byte  0, bit 0-3
        ("EIP", UCHAR, 1),  # Byte  0, bit 4
        ("Reserved1", UCHAR, 2),  # Byte  0, bit 5-6
        ("Invalid", UCHAR, 1),  # Byte  0, bit 7
        ("Length", UCHAR),  # Byte  1
        ("Reserved2", UCHAR),  # Byte  2
        ("ElementIndex", UCHAR),  # Byte  3
        ("ProtocolInfo", SES_PROTOCOL_INFORMATION),
    ]


PSES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR = POINTER(SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR)


class SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("Reserved", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("GenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Descriptors", SES_ADDITIONAL_ELEMENT_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE = POINTER(SES_ADDITIONAL_ELEMENT_STATUS_DIAGNOSTIC_PAGE)


class SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR),  # Byte  0
        ("SubEnclosureId", UCHAR),  # Byte  1
        ("Status", UCHAR),  # Byte  2
        ("AdditionalStatus", UCHAR),  # Byte  3
        ("MaximumImageSize", UCHAR * 4),  # Bytes 4-7
        ("Reserved2", UCHAR * 3),  # Bytes 8-10
        ("ExpectedBufferId", UCHAR),  # Byte  11
        ("ExpectedBufferOffset", UCHAR),  # Bytes 12-15
    ]


PSES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR = POINTER(SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR)


class SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("NumberOfSecondarySubEnclosures", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("GenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Descriptors", SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PSES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE = POINTER(SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE)


class SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PageCode", UCHAR),  # Byte  0
        ("SubEnclosureId", UCHAR),  # Byte  1
        ("PageLength", UCHAR * 2),  # Bytes 2-3
        ("ExpectedGenerationCode", UCHAR * 4),  # Bytes 4-7
        ("Mode", UCHAR),  # Byte  8
        ("Reserved", UCHAR * 2),  # Bytes 9-10
        ("BufferID", UCHAR),  # Byte  11
        ("BufferOffset", UCHAR * 4),  # Bytes 12-15
        ("ImageLength", UCHAR * 4),  # Bytes 16-19
        ("DataLength", UCHAR * 4),  # Bytes 20-23
        ("Data", UCHAR * ANYSIZE_ARRAY),
    ]


PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE = POINTER(SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE)

_pack_ -= 1


# endif

# Definitions related to 0x9E - SCSIOP_GET_PHYSICAL_ELEMENT_STATUS

# Input: Report type
GET_PHYSICAL_ELEMENT_STATUS_REPORT_TYPE_PHYSICAL_ELEMENT = 0x0
GET_PHYSICAL_ELEMENT_STATUS_REPORT_TYPE_STORAGE_ELEMENT = 0x1

# Input: Filter
GET_PHYSICAL_ELEMENT_STATUS_ALL = 0x0
GET_PHYSICAL_ELEMENT_STATUS_FILTER_NEED_ATTENTION = 0x1

# Output: Physical element type
PHYSICAL_ELEMENT_TYPE_STORAGE_ELEMENT = 0x01

# Output: Physical element health
PHYSICAL_ELEMENT_HEALTH_NOT_REPORTED = 0x00
PHYSICAL_ELEMENT_HEALTH_MANUFACTURER_SPECIFICATION_LIMIT = 0x64
PHYSICAL_ELEMENT_HEALTH_RESERVED_LOWER_BOUNDARY = 0xD0
PHYSICAL_ELEMENT_HEALTH_RESERVED_UPPER_BOUNDARY = 0xFC
PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_COMPLETED_WITH_ERROR = 0xFD
PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_IN_PROGRESS = 0xFE
PHYSICAL_ELEMENT_HEALTH_DEPOPULATION_COMPLETED_SUCCESS = 0xFF

_pack_ += 1


class PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 4),
        ("ElementIdentifier", UCHAR * 4),
        ("Reserved2", UCHAR * 6),
        ("PhysicalElementType", UCHAR),
        ("PhysicalElementHealth", UCHAR),
        ("AssociatedCapacity", UCHAR * 8),
        ("Reserved3", UCHAR * 8),
    ]


PPHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR = POINTER(PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR)


class PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DescriptorCount", UCHAR * 4),
        ("ReturnedDescriptorCount", UCHAR * 4),
        ("ElementIdentifierBeingDepoped", UCHAR * 4),
        ("Reserved", UCHAR * 20),
        ("Descriptors", PHYSICAL_ELEMENT_STATUS_DATA_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PPHYSICAL_ELEMENT_STATUS_PARAMETER_DATA = POINTER(PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA)

_pack_ -= 1

# Definitions related to 0x9B - SCSIOP_READ_DATA_BUFF16(Mode 0x1C: Error History)

# Input: Mode field for Read buffer command

READ_BUFFER_MODE_ERROR_HISTORY = 0x1C

# Input: Mode specific field for Read buffer command

MODE_SPECIFIC_CREATE_VENDOR_SPECIFIC_DATA = 0x0
MODE_SPECIFIC_CREATE_CURRENT_INTERNAL_STATUS_DATA = 0x1

# Input: Buffer ID field for Read buffer command

# Return error history directory.
BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY = 0x0

# Return error history directory and create new error history snapshot.
BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_CREATE_NEW_ERROR_HISTORY_SNAPSHOT = 0x1

# Return error history directory and establish new error history I_T nexus.
BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_ESTABLISH_NEW_NEXUS = 0x2

# Return error history directory, establish new error history I_T nexus,
# and create new error history snapshot.
BUFFER_ID_RETURN_ERROR_HISTORY_DIRECTORY_ESTABLISH_NEW_NEXUS_AND_SNAPSHOT = 0x3

# 0x04h - 0x0Fh    Reserved.

# 0x10h - 0xEFh    Return error history.
BUFFER_ID_RETURN_ERROR_HISTORY_MINIMUM_THRESHOLD = 0x10

BUFFER_ID_RETURN_ERROR_HISTORY_MAXIMUM_THRESHOLD = 0xEF

# 0xF0h - 0xFDh    Reserved.

# Clear error history I_T nexus.
BUFFER_ID_CLEAR_ERROR_HISTORY_NEXUS = 0xFE

# Clear error history I_T nexus and release any error history snapshots.
BUFFER_ID_CLEAR_ERROR_HISTORY_AND_RELEASE_ANY_SNAPSHOT = 0xFF

# Output: Error history source field

ERROR_HISTORY_SOURCE_CREATED_BY_DEVICE_SERVER = 0x0
ERROR_HISTORY_SOURCE_CREATED_DUE_TO_CURRENT_READ_BUFFER_COMMAND = 0x1
ERROR_HISTORY_SOURCE_CREATED_DUE_TO_PREVIOUS_READ_BUFFER_COMMAND = 0x2
ERROR_HISTORY_SOURCE_INDICATED_IN_BUFFER_SOURCE_FIELD = 0x3

# Output: Error history retrieved field

ERROR_HISTORY_RETRIEVED_NO_INFORMATION = 0x0

# The error history I_T nexus has requested buffer ID FEh (i.e., clear error history I_T nexus) or buffer ID FFh
# (i.e., clear error history I_T nexus and release snapshot) for the current error history snapshot.
ERROR_HISTORY_RETRIEVED_BUFFER_ID_FE_OR_FF = 0x1

# An error history I_T nexus has not requested buffer ID FEh (i.e., clear error history I_T nexus) or buffer ID FFh
# (i.e., clear error history I_T nexus and release snapshot) for the current error history snapshot.
ERROR_HISTORY_RETRIEVED_NOT_BUFFER_ID_FE_OR_FF = 0x2
ERROR_HISTORY_RETRIEVED_RESERVED = 0x3

# Output: Buffer format

BUFFER_FORMAT_VENDOR_SPECIFIC = 0x0
BUFFER_FORMAT_CURRENT_INTERNAL_STATUS_DATA = 0x1
BUFFER_FORMAT_SAVED_INTERNAL_STATUS_DATA = 0x2

# Output: Buffer source

BUFFER_SOURCE_INDICATED_IN_EHS_SOURCE_FIELD = 0x0
BUFFER_SOURCE_UNKNOWN = 0x1
BUFFER_SOURCE_CREATED_BY_DEVICE_SERVER = 0x2
BUFFER_SOURCE_CREATED_DUE_TO_CURRENT_COMMAND = 0x3
BUFFER_SOURCE_CREATED_DUE_TO_PREVIOUS_COMMAND = 0x4

STATUS_DATA_SET_SIZE_INCREMENT_IN_BYTES = 0x200

_pack_ += 1


class ERROR_HISTORY_DIRECTORY_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("SupportedBufferId", UCHAR),
        ("BufferFormat", UCHAR),
        ("BufferSource", UCHAR, 4),
        ("Reserved0", UCHAR, 4),
        ("Reserved1", UCHAR),
        ("MaxAvailableLength", UCHAR * 4),
    ]


PERROR_HISTORY_DIRECTORY_ENTRY = POINTER(ERROR_HISTORY_DIRECTORY_ENTRY)


class ERROR_HISTORY_DIRECTORY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("T10VendorId", UCHAR * 8),
        ("ErrorHistoryVersion", UCHAR),
        ("ClearSupport", UCHAR, 1),
        ("ErrorHistorySource", UCHAR, 2),
        ("ErrorHistoryRetrieved", UCHAR, 2),
        ("Reserved0", UCHAR, 3),
        ("Reserved1", UCHAR * 20),
        ("DirectoryLength", UCHAR * 2),
        ("ErrorHistoryDirectoryList", ERROR_HISTORY_DIRECTORY_ENTRY * ANYSIZE_ARRAY),
    ]


PERROR_HISTORY_DIRECTORY = POINTER(ERROR_HISTORY_DIRECTORY)


class CURRENT_INTERNAL_STATUS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved0", UCHAR * 4),
        ("IEEECompanyId", UCHAR * 4),
        ("CurrentInternalStatusDataSetOneLength", UCHAR * 2),
        ("CurrentInternalStatusDataSetTwoLength", UCHAR * 2),
        ("CurrentInternalStatusDataSetThreeLength", UCHAR * 2),
        ("CurrentInternalStatusDataSetFourLength", UCHAR * 4),
        ("Reserved1", UCHAR * 364),
        ("NewSavedDataAvailable", UCHAR),
        ("SavedDataGenerationNumber", UCHAR),
        ("CurrentReasonIdentifier", UCHAR * 128),
        ("CurrentInternalStatusData", UCHAR * ANYSIZE_ARRAY),
    ]


PCURRENT_INTERNAL_STATUS_PARAMETER_DATA = POINTER(CURRENT_INTERNAL_STATUS_PARAMETER_DATA)


class SAVED_INTERNAL_STATUS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved0", UCHAR * 4),
        ("IEEECompanyId", UCHAR * 4),
        ("SavedInternalStatusDataSetOneLength", UCHAR * 2),
        ("SavedInternalStatusDataSetTwoLength", UCHAR * 2),
        ("SavedInternalStatusDataSetThreeLength", UCHAR * 2),
        ("SavedInternalStatusDataSetFourLength", UCHAR * 4),
        ("Reserved1", UCHAR * 364),
        ("NewSavedDataAvailable", UCHAR),
        ("SavedDataGenerationNumber", UCHAR),
        ("SavedReasonIdentifier", UCHAR * 128),
        ("SavedInternalStatusData", UCHAR * ANYSIZE_ARRAY),
    ]


PSAVED_INTERNAL_STATUS_PARAMETER_DATA = POINTER(SAVED_INTERNAL_STATUS_PARAMETER_DATA)

_pack_ -= 1

# Collections of SCSI utility functions

# SCSI sense data related functions

# NOTE: Sense Data Descriptor Format is supported only in Windows 8 and later

# Obtain Error Code from the sense info buffer.
# Note: Error Code is same as "Response Code" defined in SPC Specification.
# define ScsiGetSenseErrorCode(SenseInfoBuffer) (((PUCHAR)(SenseInfoBuffer))[0] & 0x7f)

# Determine the buffer length of a descriptor
# define ScsiGetSenseDescriptorLength(DescriptorBuffer)             (sizeof(SCSI_SENSE_DESCRIPTOR_HEADER) + ((PSCSI_SENSE_DESCRIPTOR_HEADER)(DescriptorBuffer))->AdditionalLength)

# Determine if sense data is in Fixed format
# define IsFixedSenseDataFormat(SenseInfoBuffer)             ((ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_FIXED_CURRENT ||              (ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_FIXED_DEFERRED)

# Determine if sense data is in Descriptor format
# define IsDescriptorSenseDataFormat(SenseInfoBuffer)             ((ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT ||              (ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED)

# Determine if sense data is Current error type
# define IsSenseDataCurrentError(SenseInfoBuffer)             ((ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_FIXED_CURRENT ||              (ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_DESCRIPTOR_CURRENT)

# Determine if sense data is Deferred error type
# define IsSenseDataDeferredError(SenseInfoBuffer)             ((ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_FIXED_DEFERRED ||              (ScsiGetSenseErrorCode(SenseInfoBuffer)) == SCSI_SENSE_ERRORCODE_DESCRIPTOR_DEFERRED)

# Determine if sense data format indicated in sense data payload is a valid value
# define IsSenseDataFormatValueValid(SenseInfoBuffer)             (IsFixedSenseDataFormat(SenseInfoBuffer) || IsDescriptorSenseDataFormat(SenseInfoBuffer))

# _Success_(return != FALSE)
"""FORCEINLINE BOOLEAN
ScsiGetTotalSenseByteCountIndicated (
   _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
   _In_  UCHAR SenseInfoBufferLength,
   _Out_ UCHAR *TotalByteCountIndicated
   )
'''++

Description:

    This function returns size of available sense data. This is based on
    AdditionalSenseLength field in the sense data payload as indicated
    by the device.

    This function handles both Fixed and Desciptor format.

Arguments:

    SenseInfoBuffer
      - A pointer to sense info buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    TotalByteCountIndicated
      - On output, it contains total byte counts of available sense data

Returns:

    TRUE if the function is able to determine size of available sense data

    Otherwise, FALSE

    Note: The routine returns FALSE when available sense data amount is
          greater than MAX_SENSE_BUFFER_SIZE

--'''
{
    BOOLEAN succeed = FALSE;
    UCHAR byteCount = 0;
    PFIXED_SENSE_DATA senseInfoBuffer = NULL;

    if (SenseInfoBuffer == NULL ||
        SenseInfoBufferLength == 0 ||
        TotalByteCountIndicated == NULL) {

        ("FALSE", return),
    }


    # Offset to AdditionalSenseLength field is same between
    # Fixed and Descriptor format.
    senseInfoBuffer = (PFIXED_SENSE_DATA)SenseInfoBuffer;

    if (RTL_CONTAINS_FIELD(senseInfoBuffer,
                           SenseInfoBufferLength
                           AdditionalSenseLength)) {

        if (senseInfoBuffer->AdditionalSenseLength <=
            (MAX_SENSE_BUFFER_SIZE - RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength))) {

            byteCount = senseInfoBuffer->AdditionalSenseLength
                        + RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);

            *TotalByteCountIndicated = byteCount;

            succeed = TRUE;
        }
    }

    ("succeed", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiGetFixedSenseKeyAndCodes (
   _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
   _In_ UCHAR SenseInfoBufferLength,
   _Out_opt_ PUCHAR SenseKey,
   _Out_opt_ PUCHAR AdditionalSenseCode,
   _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
   )
'''++

Description:

    This function retrieves the following information from sense data
    in Fixed format:

        1. Sense key
        2. Additional Sense Code
        3. Additional Sense Code Qualifier

    If Additional Sense Code or Additional Sense Code Qualifer is not available,
    it is set to 0 when the function returns.

Arguments:

    SenseInfoBuffer
      - A pointer to sense info buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    SenseKey
      - On output, buffer contains the sense key.
        If null is specified, the function will not retrieve the sense key

    AdditionalSenseCode
      - On output, buffer contains the additional sense code.
        If null is specified, the function will not retrieve the additional sense code.

    AdditionalSenseCodeQualifier
      - On output, buffer contains the additional sense code qualifier.
        If null is specified, the function will not retrieve the additional sense code qualifier.

Returns:

    TRUE if the function is able to retrieve the requested information.

    Otherwise, FALSE

--'''
{
    PFIXED_SENSE_DATA fixedSenseData = (PFIXED_SENSE_DATA)SenseInfoBuffer;
    BOOLEAN succeed = FALSE;
    ULONG dataLength = 0;

    if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        ("FALSE", return),
    }

    if (RTL_CONTAINS_FIELD(fixedSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {

        dataLength = fixedSenseData->AdditionalSenseLength + RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);

        if (dataLength > SenseInfoBufferLength) {
            dataLength = SenseInfoBufferLength;
        }

        if (SenseKey != NULL) {
           *SenseKey = fixedSenseData->SenseKey;
        }

        if (AdditionalSenseCode != NULL) {
           *AdditionalSenseCode = RTL_CONTAINS_FIELD(fixedSenseData, dataLength, AdditionalSenseCode) ?
                                  fixedSenseData->AdditionalSenseCode : 0;
        }

        if (AdditionalSenseCodeQualifier != NULL) {
           *AdditionalSenseCodeQualifier = RTL_CONTAINS_FIELD(fixedSenseData, dataLength, AdditionalSenseCodeQualifier) ?
                                           fixedSenseData->AdditionalSenseCodeQualifier : 0;
        }

        succeed = TRUE;
    }

    ("succeed", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiGetDescriptorSenseKeyAndCodes (
   _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
   _In_ UCHAR SenseInfoBufferLength,
   _Out_opt_ PUCHAR SenseKey,
   _Out_opt_ PUCHAR AdditionalSenseCode,
   _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
   )
'''++

Description:

    This function retrieves the following information from sense data
    in Descriptor format:

        1. Sense key
        2. Additional Sense Code
        3. Additional Sense Code Qualifier

Arguments:

    SenseInfoBuffer
      - A pointer to sense info buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    SenseKey
      - On output, buffer contains the sense key.
        Note: If null is specified, the function will not retrieve the sense key

    AdditionalSenseCode
      - On output, buffer contains the additional sense code.
        Note: If null is specified, the function will not retrieve the additional sense code.

    AdditionalSenseCodeQualifier
      - On output, buffer contains the additional sense code qualifier.
        Note: If null is specified, the function will not retrieve the additional sense code qualifier.

Returns:

    TRUE if the function is able to retrieve the requested information.

    Otherwise, FALSE

--'''
{
    PDESCRIPTOR_SENSE_DATA descriptorSenseData = (PDESCRIPTOR_SENSE_DATA)SenseInfoBuffer;
    BOOLEAN succeed = FALSE;

    if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        ("FALSE", return),
    }
    if (RTL_CONTAINS_FIELD(descriptorSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {

        if (SenseKey) {
            *SenseKey = descriptorSenseData->SenseKey;
        }

        if (AdditionalSenseCode != NULL) {
            *AdditionalSenseCode = descriptorSenseData->AdditionalSenseCode;
        }

        if (AdditionalSenseCodeQualifier != NULL) {
            *AdditionalSenseCodeQualifier = descriptorSenseData->AdditionalSenseCodeQualifier;
        }

        succeed = TRUE;
    }

    ("succeed", return),
}

# SCSI_SENSE_OPTIONS

SCSI_SENSE_OPTIONS = ULONG

# No options is specified
SCSI_SENSE_OPTIONS_NONE = ((SCSI_SENSE_OPTIONS)0x00000000)

# If no known format is indicated in the sense buffer, interpret
# the sense buffer as Fixed format.
SCSI_SENSE_OPTIONS_FIXED_FORMAT_IF_UNKNOWN_FORMAT_INDICATED = ((SCSI_SENSE_OPTIONS)0x00000001)

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiGetSenseKeyAndCodes (
   _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
   _In_ UCHAR SenseInfoBufferLength,
   _In_ SCSI_SENSE_OPTIONS Options,
   _Out_opt_ PUCHAR SenseKey,
   _Out_opt_ PUCHAR AdditionalSenseCode,
   _Out_opt_ PUCHAR AdditionalSenseCodeQualifier
   )
'''++

Description:

    This function retrieves the following information from sense data

        1. Sense key
        2. Additional Sense Code
        3. Additional Sense Code Qualifier

    This function handles both Fixed and Descriptor format.

Arguments:

    SenseInfoBuffer
      - A pointer to sense info buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    Options
      - Options used by this routine. It is a bit-field value. See defintions
        of list of #define SCSI_SENSE_OPTIONS above in this file.

    SenseKey
      - On output, buffer contains the sense key.
        Note: If null is specified, the function will not retrieve the sense key

    AdditionalSenseCode
      - On output, buffer contains the additional sense code.
        Note: If null is specified, the function will not retrieve the additional sense code.

    AdditionalSenseCodeQualifier
      - On output, buffer contains the additional sense code qualifier.
        Note: If null is specified, the function will not retrieve the additional sense code qualifier.

Returns:

    TRUE if the function is able to retrieve the requested information.

    Otherwise, FALSE

--'''
{
    BOOLEAN succeed = FALSE;

    if (SenseInfoBuffer == NULL || SenseInfoBufferLength == 0) {
        ("FALSE", return),
    }

    if (IsDescriptorSenseDataFormat(SenseInfoBuffer)) {

        succeed = ScsiGetDescriptorSenseKeyAndCodes( SenseInfoBuffer,
                                                     SenseInfoBufferLength
                                                     SenseKey
                                                     AdditionalSenseCode
                                                     AdditionalSenseCodeQualifier );
    } else {

        if ((Options & SCSI_SENSE_OPTIONS_FIXED_FORMAT_IF_UNKNOWN_FORMAT_INDICATED) ||
            IsFixedSenseDataFormat(SenseInfoBuffer)) {

            succeed = ScsiGetFixedSenseKeyAndCodes( SenseInfoBuffer,
                                                    SenseInfoBufferLength
                                                    SenseKey
                                                    AdditionalSenseCode
                                                    AdditionalSenseCodeQualifier );
        }
    }

    ("succeed", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiGetSenseDescriptor(
   _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
   _In_ UCHAR SenseInfoBufferLength,
   _Outptr_result_bytebuffer_(*DescriptorBufferLength) PVOID *DescriptorBuffer,
   _Out_ UCHAR *DescriptorBufferLength
   )
'''++

Description:

    This function calculates available amount of descriptors information
    within sense data in Descriptor format.  Then, it returns the starting
    address of descriptors and amount of descriptor data available.

Arguments:

    SenseInfoBuffer
      - A pointer to sense info buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    DescriptorBuffer
      - On output, it contains pointer to the starting address of descriptor

    DescriptorBufferLength
      - On output, it contains number of bytes of available descriptor data

Returns:

    TRUE if the function succeeds

    Otherwise, FALSE

    Note: FALSE if no descriptor data are available.

--'''
{
    ("descriptorSenseData", PDESCRIPTOR_SENSE_DATA),
    BOOLEAN succeed = FALSE;
    UCHAR dataLength = 0;

    if (SenseInfoBuffer == NULL    ||
        SenseInfoBufferLength == 0 ||
        DescriptorBuffer == NULL   ||
        DescriptorBufferLength == NULL) {
        ("FALSE", return),
    }

    *DescriptorBuffer = NULL;
    *DescriptorBufferLength = 0;

    if (!IsDescriptorSenseDataFormat(SenseInfoBuffer)) {
        ("FALSE", return),
    }

    descriptorSenseData = (PDESCRIPTOR_SENSE_DATA)SenseInfoBuffer;

    if (RTL_CONTAINS_FIELD(descriptorSenseData, SenseInfoBufferLength, AdditionalSenseLength)) {

        if (descriptorSenseData->AdditionalSenseLength <= (MAX_SENSE_BUFFER_SIZE - RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength))) {

            dataLength = descriptorSenseData->AdditionalSenseLength + RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength);

            if (dataLength > SenseInfoBufferLength) {
                dataLength = SenseInfoBufferLength;
            }

            *DescriptorBufferLength = dataLength - RTL_SIZEOF_THROUGH_FIELD(DESCRIPTOR_SENSE_DATA, AdditionalSenseLength);

            if (*DescriptorBufferLength > 0) {
                *DescriptorBuffer = (PVOID)(descriptorSenseData->DescriptorBuffer);
                succeed = TRUE;
            }
        }
    }

    ("succeed", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiValidateInformationSenseDescriptor(
    _In_reads_bytes_(DescriptorBufferLength) PVOID DescriptorBuffer,
    _In_ UCHAR DescriptorBufferLength
    )
'''++

Description:

    This function validates if buffer contains a valid payload for descriptor of Information type

Arguments:

    DescriptorBuffer
      - Pointer to the starting address of descriptor payload

    DescriptorBufferLength
      - Size of the buffer that DescriptorBuffer points to.

Returns:

    TRUE if DescriptorBuffer contains valid payload for Information type descriptor.

    Otherwise, FALSE

--'''
{
    ("descriptor", PSCSI_SENSE_DESCRIPTOR_INFORMATION),
    ("additionalLength", UCHAR),

    if (DescriptorBuffer == NULL || DescriptorBufferLength < sizeof(SCSI_SENSE_DESCRIPTOR_INFORMATION)) {
        ("FALSE", return),
    }

    descriptor = (PSCSI_SENSE_DESCRIPTOR_INFORMATION)DescriptorBuffer;

    if (descriptor->Header.DescriptorType != SCSI_SENSE_DESCRIPTOR_TYPE_INFORMATION) {
        ("FALSE", return),
    }

    additionalLength = sizeof(SCSI_SENSE_DESCRIPTOR_INFORMATION) - RTL_SIZEOF_THROUGH_FIELD(SCSI_SENSE_DESCRIPTOR_INFORMATION, Header);

    if (descriptor->Header.AdditionalLength != additionalLength) {
        ("FALSE", return),
    }

    if (descriptor->Valid == 0) {
        ("FALSE", return),
    }

   ("TRUE", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiValidateBlockCommandSenseDescriptor(
    _In_reads_bytes_(DescriptorBufferLength) PVOID DescriptorBuffer,
    _In_ UCHAR DescriptorBufferLength
    )
'''++

Description:

    This function validates if buffer contains a valid payload for Block Command type descriptor

Arguments:

    DescriptorBuffer
      - Pointer to the starting address of descriptor payload

    DescriptorBufferLength
      - Size of the buffer that DescriptorBuffer points to

Returns:

    TRUE if DescriptorBuffer contains a valid payload for descriptor of Block Command type

    Otherwise, FALSE

--'''
{
    ("descriptor", PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND),
    ("additionalLength", UCHAR),

    if (DescriptorBuffer == NULL || DescriptorBufferLength < sizeof(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)) {
        ("FALSE", return),
    }

    descriptor = (PSCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND)DescriptorBuffer;

    if (descriptor->Header.DescriptorType != SCSI_SENSE_DESCRIPTOR_TYPE_BLOCK_COMMAND) {
        ("FALSE", return),
    }

    additionalLength = sizeof(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND) - RTL_SIZEOF_THROUGH_FIELD(SCSI_SENSE_DESCRIPTOR_BLOCK_COMMAND, Header);

    if (descriptor->Header.AdditionalLength != additionalLength) {
        ("FALSE", return),
    }

   ("TRUE", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiConvertToFixedSenseFormat(
    _In_reads_bytes_(SenseInfoBufferLength) PVOID SenseInfoBuffer,
    _In_ UCHAR SenseInfoBufferLength,
    _Out_writes_bytes_(OutBufferLength) PVOID OutBuffer,
    _In_ UCHAR OutBufferLength
    )
'''++

Description:

    This routine converts descriptor format sense data to fixed format sense data.

    Due to differences between two formats, the conversion is only based on Sense Key,
    Additional Sense Code, and Additional Sense Code Qualififer.

Arguments:

    SenseInfoBuffer
      - A pointer to sense data buffer

    SenseInfoBufferLength
      - Size of the buffer SenseInfoBuffer points to.

    OutBuffer
      - On output, OutBuffer contains the fixed sense data as result of conversion.

    OutBufferLength
      - Size of the buffer that OutBuffer points to.

Returns:

    TRUE if conversion to Fixed format is successful.

    Otherwise, FALSE.

--'''
{
    BOOLEAN succeed = FALSE;
    BOOLEAN validSense  = FALSE;
    UCHAR senseKey = 0;
    UCHAR additionalSenseCode = 0;
    UCHAR additionalSenseCodeQualifier = 0;
    PFIXED_SENSE_DATA outBuffer = (PFIXED_SENSE_DATA)OutBuffer;

    if (SenseInfoBuffer == NULL ||
        SenseInfoBufferLength == 0 ||
        OutBuffer == NULL ||
        OutBufferLength < sizeof(FIXED_SENSE_DATA)) {
        ("FALSE", return),
    }

    if (IsDescriptorSenseDataFormat(SenseInfoBuffer)) {

        RtlZeroMemory(OutBuffer, OutBufferLength);

        validSense = ScsiGetSenseKeyAndCodes(SenseInfoBuffer,
                                             SenseInfoBufferLength
                                             SCSI_SENSE_OPTIONS_NONE
                                             &senseKey,
                                             &additionalSenseCode,
                                             &additionalSenseCodeQualifier);
        if (validSense) {

            if (IsSenseDataCurrentError(SenseInfoBuffer)) {
                outBuffer->ErrorCode = SCSI_SENSE_ERRORCODE_FIXED_CURRENT;
            } else {
                outBuffer->ErrorCode = SCSI_SENSE_ERRORCODE_FIXED_DEFERRED;
            }
            outBuffer->AdditionalSenseLength = sizeof(FIXED_SENSE_DATA) - RTL_SIZEOF_THROUGH_FIELD(FIXED_SENSE_DATA, AdditionalSenseLength);
            outBuffer->SenseKey = senseKey;
            outBuffer->AdditionalSenseCode = additionalSenseCode;
            outBuffer->AdditionalSenseCodeQualifier = additionalSenseCodeQualifier;

            succeed = TRUE;
        }
    }

    ("succeed", return),
}

# _Success_(return != FALSE)
FORCEINLINE BOOLEAN
ScsiGetNextSenseDescriptorByType (
    _In_reads_bytes_(BufferLength) PVOID Buffer,
    _In_ UCHAR BufferLength,
    _In_reads_(TypeListCount) PUCHAR TypeList,
    _In_ ULONG TypeListCount,
    _Out_ PUCHAR OutType,
    _Outptr_result_bytebuffer_(*OutBufferLength) PVOID *OutBuffer,
    _Out_ UCHAR *OutBufferLength
)
'''++

Description:

    This routine locates the next descriptor with type equals to one of the
    types specified by caller.

Arguments:

    Buffer - pointer to buffer to be searched.

    BufferLength - Size of the buffer that Buffer points to.

    TypeList - Pointer to array of descriptor types to be searched

    TypeListCount - Number of element in TypeList array

    OutType - Upon return, if a descriptor is found,
              it contains the type of the descriptor.

    OutBuffer - Upon return, if a descriptor is found,
                it points to start address of the descriptor buffer

    OutBufferLength - Upon return, if a descriptor is found,
                      it contains the number of bytes available starting at
                      OutBuffer. i.e. This is the buffer available between
                      OutBuffer pointer and end of Buffer.

Returns:

    TRUE if descriptor of specified type is found.

    Otherwise, FALSE.

--'''
{
    ("remainingBuffer", PUCHAR),
    ("remainingBufferLength", UCHAR),
    ("type", UCHAR),
    ("i", ULONG),
    ("descriptorLength", UCHAR),

    if (Buffer          == NULL ||
        BufferLength    == 0    ||
        TypeList        == NULL ||
        TypeListCount   == 0    ||
        OutType         == NULL ||
        OutBuffer       == NULL ||
        OutBufferLength == NULL) {

        ("FALSE", return),
    }

    *OutBuffer = NULL;
    *OutBufferLength = 0;
    *OutType = 0;

    remainingBuffer = (PUCHAR)Buffer;
    remainingBufferLength = BufferLength;

    while (remainingBufferLength >= sizeof(SCSI_SENSE_DESCRIPTOR_HEADER)) {

        for (i = 0; i < TypeListCount; i++) {

            type = TypeList[i];

            if (((PSCSI_SENSE_DESCRIPTOR_HEADER)remainingBuffer)->DescriptorType == type) {
                *OutBuffer = (PVOID)remainingBuffer;
                *OutBufferLength = remainingBufferLength;
                *OutType = type;
                ("TRUE", return),
            }
        }

        descriptorLength = ScsiGetSenseDescriptorLength(remainingBuffer);

        if (remainingBufferLength > descriptorLength) {

            # Advance to start address of next descriptor
            remainingBuffer += descriptorLength;
            remainingBufferLength -= descriptorLength;

        } else {

            # Search is completed.
            break;
        }

    }

    ("FALSE", return),
}"""

# [END] Collections of SCSI utiltiy functions

# end_storport end_storportp

# end_ntminitape

# pragma pack(pop, _scsi_) # restore original packing level

# pragma warning(pop) # un-sets any local warning changes

# endif ''' WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE) '''
# pragma endregion

# endif # !defined _NTSCSI_
