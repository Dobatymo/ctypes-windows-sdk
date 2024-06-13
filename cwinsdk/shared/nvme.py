from ctypes import POINTER, Structure, Union, sizeof
from ctypes.wintypes import CHAR, ULONG, USHORT

from cwinsdk import CEnum, make_struct, make_union
from cwinsdk.shared.guiddef import GUID
from cwinsdk.shared.ntdef import ANYSIZE_ARRAY, UCHAR, ULONGLONG

_pack_ = 0
"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    nvme.h

Abstract:

    NVMe command protocol related definitions

Revision:

    Aug. 2018 - Align to NVMe spec version 1.3.

--"""

# ifndef NVME_INCLUDED
# define NVME_INCLUDED

# include <winapifamily.h>

# pragma region Desktop Family or Storage Package
# if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE)

# if _MSC_VER >= 1200
# pragma once
# pragma warning(push)
# endif

# pragma warning(disable:4214)   # bit field types other than int
# pragma warning(disable:4201)   # nameless struct/union
# pragma warning(disable:4200)   # zero-sized array in struct/union


# 3.1.1  Offset 00h: CAP (Controller Capabilities)
class NVME_AMS_OPTION(CEnum):
    NVME_AMS_ROUND_ROBIN = 0
    NVME_AMS_WEIGHTED_ROUND_ROBIN_URGENT = 1


class NVME_CONTROLLER_CAPABILITIES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("MQES", ULONGLONG, 16),  # RO - Maximum Queue Entries Supported (MQES)
                    ("CQR", ULONGLONG, 1),  # RO - Contiguous Queues Required (CQR)
                    # Bit 17, 18 - AMS; RO - Arbitration Mechanism Supported (AMS)
                    ("AMS_WeightedRoundRobinWithUrgent", ULONGLONG, 1),  # Bit 17: Weighted Round Robin with Urgent;
                    ("AMS_VendorSpecific", ULONGLONG, 1),  # Bit 18: Vendor Specific.
                    ("Reserved0", ULONGLONG, 5),  # RO - bit 19 ~ 23
                    ("TO", ULONGLONG, 8),  # RO - Timeout (TO)
                    ("DSTRD", ULONGLONG, 4),  # RO - Doorbell Stride (DSTRD)
                    ("NSSRS", ULONGLONG, 1),  # RO - NVM Subsystem Reset Supported (NSSRS)
                    # Bit 37 ~ 44 - CSS; RO - Command Sets Supported (CSS)
                    ("CSS_NVM", ULONGLONG, 1),  # Bit 37: NVM command set
                    ("CSS_Reserved0", ULONGLONG, 1),  # Bit 38: Reserved
                    ("CSS_Reserved1", ULONGLONG, 1),  # Bit 39: Reserved
                    ("CSS_Reserved2", ULONGLONG, 1),  # Bit 40: Reserved
                    ("CSS_Reserved3", ULONGLONG, 1),  # Bit 41: Reserved
                    ("CSS_Reserved4", ULONGLONG, 1),  # Bit 42: Reserved
                    ("CSS_MultipleIo", ULONGLONG, 1),  # Bit 43: One or more IO command sets
                    ("CSS_AdminOnly", ULONGLONG, 1),  # Bit 44: Only Admin command set (no IO command set)
                    ("Reserved2", ULONGLONG, 3),  # RO - bit 45 ~ 47
                    ("MPSMIN", ULONGLONG, 4),  # RO - Memory Page Size Minimum (MPSMIN)
                    ("MPSMAX", ULONGLONG, 4),  # RO - Memory Page Size Maximum (MPSMAX)
                    ("Reserved3", ULONGLONG, 8),  # RO - bit 56 ~ 63
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlonglong", ULONGLONG),
    ]


# 3.1.2  Offset 08h: VS (Version)
class NVME_VERSION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("TER", ULONG, 8),  # Tertiary Version Number (TER)
                    ("MNR", ULONG, 8),  # Minor Version Number (MNR)
                    ("MJR", ULONG, 16),  # Major Version Number (MJR)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.5  Offset 14h: CC (Controller Configuration)
class NVME_CC_SHN_SHUTDOWN_NOTIFICATIONS(CEnum):
    NVME_CC_SHN_NO_NOTIFICATION = 0
    NVME_CC_SHN_NORMAL_SHUTDOWN = 1
    NVME_CC_SHN_ABRUPT_SHUTDOWN = 2


class NVME_CSS_COMMAND_SETS(CEnum):
    NVME_CSS_NVM_COMMAND_SET = 0
    NVME_CSS_ALL_SUPPORTED_IO_COMMAND_SET = 6
    NVME_CSS_ADMIN_COMMAND_SET_ONLY = 7


class NVME_CONTROLLER_CONFIGURATION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("EN", ULONG, 1),  # RW - Enable (EN)
                    ("Reserved0", ULONG, 3),  # RO
                    ("CSS", ULONG, 3),  # RW - I/O  Command Set Selected (CSS)
                    ("MPS", ULONG, 4),  # RW - Memory Page Size (MPS)
                    ("AMS", ULONG, 3),  # RW - Arbitration Mechanism Selected (AMS)
                    ("SHN", ULONG, 2),  # RW - Shutdown Notification (SHN)
                    ("IOSQES", ULONG, 4),  # RW - I/O  Submission Queue Entry Size (IOSQES)
                    ("IOCQES", ULONG, 4),  # RW - I/O  Completion Queue Entry Size (IOCQES)
                    ("Reserved1", ULONG, 8),  # RO
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.6  Offset 1Ch: CSTS (Controller Status)
class NVME_CSTS_SHST_SHUTDOWN_STATUS(CEnum):
    NVME_CSTS_SHST_NO_SHUTDOWN = 0
    NVME_CSTS_SHST_SHUTDOWN_IN_PROCESS = 1
    NVME_CSTS_SHST_SHUTDOWN_COMPLETED = 2


class NVME_CONTROLLER_STATUS(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("RDY", ULONG, 1),  # RO - Ready (RDY)
                    ("CFS", ULONG, 1),  # RO - Controller Fatal Status (CFS)
                    ("SHST", ULONG, 2),  # RO - Shutdown Status (SHST)
                    ("NSSRO", ULONG, 1),  # RW1C - NVM Subsystem Reset Occurred (NSSRO)
                    ("PP", ULONG, 1),  # RO - Processing Paused (PP)
                    ("Reserved0", ULONG, 26),  # RO
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.7  Offset 20h: NSSR (NVM Subsystem Reset)
class NVME_NVM_SUBSYSTEM_RESET(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NSSRC", ULONG),  # RW - NVM Subsystem Reset Control (NSSRC)
    ]


PNVME_NVM_SUBSYSTEM_RESET = POINTER(NVME_NVM_SUBSYSTEM_RESET)


# 3.1.8  Offset 24h: AQA (Admin Queue Attributes)
class NVME_ADMIN_QUEUE_ATTRIBUTES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("ASQS", ULONG, 12),  # RW - Admin  Submission Queue Size (ASQS)
                    ("Reserved0", ULONG, 4),  # RO
                    ("ACQS", ULONG, 12),  # RW - Admin  Completion Queue Size (ACQS)
                    ("Reserved1", ULONG, 4),  # RO
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.9  Offset 28h: ASQ (Admin Submission Queue Base Address)
class NVME_ADMIN_SUBMISSION_QUEUE_BASE_ADDRESS(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("Reserved0", ULONGLONG, 12),  # RO
                    ("ASQB", ULONGLONG, 52),  # RW - Admin Submission Queue Base (ASQB)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlonglong", ULONGLONG),
    ]


# 3.1.10  Offset 30h: ACQ (Admin Completion Queue Base Address)
class NVME_ADMIN_COMPLETION_QUEUE_BASE_ADDRESS(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("Reserved0", ULONGLONG, 12),  # RO
                    ("ACQB", ULONGLONG, 52),  # RW - Admin Completion Queue Base (ACQB)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlonglong", ULONGLONG),
    ]


# 3.1.11 Offset 38h: CMBLOC (Controller Memory Buffer Location)
class NVME_CONTROLLER_MEMORY_BUFFER_LOCATION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("BIR", ULONG, 3),  # RO - Base Indicator Register (BIR)
                    ("Reserved", ULONG, 9),  # RO
                    ("OFST", ULONG, 20),  # RO - Offset (OFST)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.12 Offset 3Ch: CMBSZ (Controller Memory Buffer Size)
class NVME_CMBSZ_SIZE_UNITS(CEnum):
    NVME_CMBSZ_SIZE_UNITS_4KB = 0
    NVME_CMBSZ_SIZE_UNITS_64KB = 1
    NVME_CMBSZ_SIZE_UNITS_1MB = 2
    NVME_CMBSZ_SIZE_UNITS_16MB = 3
    NVME_CMBSZ_SIZE_UNITS_256MB = 4
    NVME_CMBSZ_SIZE_UNITS_4GB = 5
    NVME_CMBSZ_SIZE_UNITS_64GB = 6


class NVME_CONTROLLER_MEMORY_BUFFER_SIZE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("SQS", ULONG, 1),  # RO - Submission Queue Support (SQS)
                    ("CQS", ULONG, 1),  # RO - Completion Queue Support (CQS)
                    ("LISTS", ULONG, 1),  # RO - PRP SGL List Support (LISTS)
                    ("RDS", ULONG, 1),  # RO - Read Data Support (RDS)
                    ("WDS", ULONG, 1),  # RO - Write Data Support (WDS)
                    ("Reserved", ULONG, 3),  # RO
                    ("SZU", ULONG, 4),  # RO - Size Units (SZU)
                    ("SZ", ULONG, 20),  # RO - Size (SZ)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.13  Offset (1000h + ((2y) * (4 << CAP.DSTRD))): SQyTDBL (Submission Queue y Tail Doorbell)
class NVME_SUBMISSION_QUEUE_TAIL_DOORBELL(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("SQT", ULONG, 16),  # RW - Submission Queue Tail (SQT)
                    ("Reserved0", ULONG, 16),  # RO
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# 3.1.14  Offset  (1000h + ((2y + 1) * (4 << CAP.DSTRD))): CQyHDBL (Completion Queue y Head Doorbell)
class NVME_COMPLETION_QUEUE_HEAD_DOORBELL(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("CQH", ULONG, 16),  # RW - Completion Queue Head (CQH)
                    ("Reserved0", ULONG, 16),  # RO
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CONTROLLER_REGISTERS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CAP", NVME_CONTROLLER_CAPABILITIES),  # Controller Capabilities; 8 bytes
        ("VS", NVME_VERSION),  # Version
        ("INTMS", ULONG),  # Interrupt Mask Set
        ("INTMC", ULONG),  # Interrupt Mask Clear
        ("CC", NVME_CONTROLLER_CONFIGURATION),  # Controller Configuration
        ("Reserved0", ULONG),
        ("CSTS", NVME_CONTROLLER_STATUS),  # Controller Status
        ("NSSR", NVME_NVM_SUBSYSTEM_RESET),  # NVM Subsystem Reset (Optional)
        ("AQA", NVME_ADMIN_QUEUE_ATTRIBUTES),  # Admin Queue Attributes
        ("ASQ", NVME_ADMIN_SUBMISSION_QUEUE_BASE_ADDRESS),  # Admin Submission Queue Base Address; 8 bytes
        ("ACQ", NVME_ADMIN_COMPLETION_QUEUE_BASE_ADDRESS),  # Admin Completion Queue Base Address; 8 bytes
        ("CMBLOC", NVME_CONTROLLER_MEMORY_BUFFER_LOCATION),  # Controller Memory Buffer Location (Optional)
        ("CMBSZ", NVME_CONTROLLER_MEMORY_BUFFER_SIZE),  # Controller Memory Buffer Size (Optional)
        ("Reserved2", ULONG * 944),  # 40h ~ EFFh
        ("Reserved3", ULONG * 64),  # F00h ~ FFFh, Command Set Specific
        ("Doorbells", ULONG * 0),  # Start of the first Doorbell register. (Admin SQ Tail Doorbell)
    ]


# Command completion status
# The "Phase Tag" field and "Status Field" are separated in spec. We define them in the same data structure to ease the memory access from software.
class NVME_COMMAND_STATUS(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("P", USHORT, 1),  # Phase Tag (P)
                    ("SC", USHORT, 8),  # Status Code (SC)
                    ("SCT", USHORT, 3),  # Status Code Type (SCT)
                    ("Reserved", USHORT, 2),
                    ("M", USHORT, 1),  # More (M)
                    ("DNR", USHORT, 1),  # Do Not Retry (DNR)
                ],
                _pack_,
            ),
        ),
        ("AsUshort", USHORT),
    ]


# Command completion entry
class NVME_COMPLETION_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DW0", ULONG),
        ("DW1", ULONG),
        (
            "DW2",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("SQHD", USHORT),  # SQ Head Pointer (SQHD)
                                ("SQID", USHORT),  # SQ Identifier (SQID)
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUlong", ULONG),
                ],
                _pack_,
            ),
        ),
        (
            "DW3",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("CID", USHORT),  # Command Identifier (CID)
                                ("Status", NVME_COMMAND_STATUS),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUlong", ULONG),
                ],
                _pack_,
            ),
        ),
    ]


# Completion entry DW0 for NVME_ADMIN_COMMAND_ASYNC_EVENT_REQUEST


class NVME_ASYNC_EVENT_TYPES(CEnum):
    NVME_ASYNC_EVENT_TYPE_ERROR_STATUS = 0
    NVME_ASYNC_EVENT_TYPE_HEALTH_STATUS = 1
    NVME_ASYNC_EVENT_TYPE_NOTICE = 2
    NVME_ASYNC_EVENT_TYPE_IO_COMMAND_SET_STATUS = 6
    NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC = 7


# Error Status: NVME_ASYNC_EVENT_TYPE_ERROR_STATUS
class NVME_ASYNC_EVENT_ERROR_STATUS_CODES(CEnum):
    NVME_ASYNC_ERROR_INVALID_SUBMISSION_QUEUE = 0
    NVME_ASYNC_ERROR_INVALID_DOORBELL_WRITE_VALUE = 1
    NVME_ASYNC_ERROR_DIAG_FAILURE = 2
    NVME_ASYNC_ERROR_PERSISTENT_INTERNAL_DEVICE_ERROR = 3
    NVME_ASYNC_ERROR_TRANSIENT_INTERNAL_DEVICE_ERROR = 4
    NVME_ASYNC_ERROR_FIRMWARE_IMAGE_LOAD_ERROR = 5


# SMART/Health Status: NVME_ASYNC_EVENT_TYPE_HEALTH_STATUS
class NVME_ASYNC_EVENT_HEALTH_STATUS_CODES(CEnum):
    NVME_ASYNC_HEALTH_NVM_SUBSYSTEM_RELIABILITY = 0
    NVME_ASYNC_HEALTH_TEMPERATURE_THRESHOLD = 1
    NVME_ASYNC_HEALTH_SPARE_BELOW_THRESHOLD = 2


# Notice Status: NVME_ASYNC_EVENT_TYPE_NOTICE
class NVME_ASYNC_EVENT_NOTICE_CODES(CEnum):
    NVME_ASYNC_NOTICE_NAMESPACE_ATTRIBUTE_CHANGED = 0
    NVME_ASYNC_NOTICE_FIRMWARE_ACTIVATION_STARTING = 1
    NVME_ASYNC_NOTICE_TELEMETRY_LOG_CHANGED = 2
    NVME_ASYNC_NOTICE_ASYMMETRIC_ACCESS_CHANGE = 3
    NVME_ASYNC_NOTICE_PREDICTABLE_LATENCY_EVENT_AGGREGATE_LOG_CHANGE = 4
    NVME_ASYNC_NOTICE_LBA_STATUS_INFORMATION_ALERT = 5
    NVME_ASYNC_NOTICE_ENDURANCE_GROUP_EVENT_AGGREGATE_LOG_CHANGE = 6

    NVME_ASYNC_NOTICE_ZONE_DESCRIPTOR_CHANGED = 0xEF


# NVM Command Set Status: NVME_ASYNC_EVENT_TYPE_IO_COMMAND_SET_STATUS
class NVME_ASYNC_EVENT_IO_COMMAND_SET_STATUS_CODES(CEnum):
    NVME_ASYNC_IO_CMD_SET_RESERVATION_LOG_PAGE_AVAILABLE = 0
    NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED = 1
    NVME_ASYNC_IO_CMD_SANITIZE_OPERATION_COMPLETED_WITH_UNEXPECTED_DEALLOCATION = 2


class NVME_COMPLETION_DW0_ASYNC_EVENT_REQUEST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("AsyncEventType", ULONG, 3),
        ("Reserved0", ULONG, 5),
        ("AsyncEventInfo", ULONG, 8),
        ("LogPage", ULONG, 8),
        ("Reserved1", ULONG, 8),
    ]


#  Status Code Type (SCT)
class NVME_STATUS_TYPES(CEnum):
    NVME_STATUS_TYPE_GENERIC_COMMAND = 0
    NVME_STATUS_TYPE_COMMAND_SPECIFIC = 1
    NVME_STATUS_TYPE_MEDIA_ERROR = 2
    NVME_STATUS_TYPE_VENDOR_SPECIFIC = 7


#  Status Code (SC) of NVME_STATUS_TYPE_GENERIC_COMMAND
class NVME_STATUS_GENERIC_COMMAND_CODES(CEnum):
    NVME_STATUS_SUCCESS_COMPLETION = 0x00
    NVME_STATUS_INVALID_COMMAND_OPCODE = 0x01
    NVME_STATUS_INVALID_FIELD_IN_COMMAND = 0x02
    NVME_STATUS_COMMAND_ID_CONFLICT = 0x03
    NVME_STATUS_DATA_TRANSFER_ERROR = 0x04
    NVME_STATUS_COMMAND_ABORTED_DUE_TO_POWER_LOSS_NOTIFICATION = 0x05
    NVME_STATUS_INTERNAL_DEVICE_ERROR = 0x06
    NVME_STATUS_COMMAND_ABORT_REQUESTED = 0x07
    NVME_STATUS_COMMAND_ABORTED_DUE_TO_SQ_DELETION = 0x08
    NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_FUSED_COMMAND = 0x09
    NVME_STATUS_COMMAND_ABORTED_DUE_TO_FAILED_MISSING_COMMAND = 0x0A
    NVME_STATUS_INVALID_NAMESPACE_OR_FORMAT = 0x0B
    NVME_STATUS_COMMAND_SEQUENCE_ERROR = 0x0C
    NVME_STATUS_INVALID_SGL_LAST_SEGMENT_DESCR = 0x0D
    NVME_STATUS_INVALID_NUMBER_OF_SGL_DESCR = 0x0E
    NVME_STATUS_DATA_SGL_LENGTH_INVALID = 0x0F
    NVME_STATUS_METADATA_SGL_LENGTH_INVALID = 0x10
    NVME_STATUS_SGL_DESCR_TYPE_INVALID = 0x11
    NVME_STATUS_INVALID_USE_OF_CONTROLLER_MEMORY_BUFFER = 0x12
    NVME_STATUS_PRP_OFFSET_INVALID = 0x13
    NVME_STATUS_ATOMIC_WRITE_UNIT_EXCEEDED = 0x14
    NVME_STATUS_OPERATION_DENIED = 0x15
    NVME_STATUS_SGL_OFFSET_INVALID = 0x16
    NVME_STATUS_RESERVED = 0x17
    NVME_STATUS_HOST_IDENTIFIER_INCONSISTENT_FORMAT = 0x18
    NVME_STATUS_KEEP_ALIVE_TIMEOUT_EXPIRED = 0x19
    NVME_STATUS_KEEP_ALIVE_TIMEOUT_INVALID = 0x1A
    NVME_STATUS_COMMAND_ABORTED_DUE_TO_PREEMPT_ABORT = 0x1B
    NVME_STATUS_SANITIZE_FAILED = 0x1C
    NVME_STATUS_SANITIZE_IN_PROGRESS = 0x1D
    NVME_STATUS_SGL_DATA_BLOCK_GRANULARITY_INVALID = 0x1E

    NVME_STATUS_DIRECTIVE_TYPE_INVALID = 0x70
    NVME_STATUS_DIRECTIVE_ID_INVALID = 0x71

    NVME_STATUS_NVM_LBA_OUT_OF_RANGE = 0x80
    NVME_STATUS_NVM_CAPACITY_EXCEEDED = 0x81
    NVME_STATUS_NVM_NAMESPACE_NOT_READY = 0x82
    NVME_STATUS_NVM_RESERVATION_CONFLICT = 0x83
    NVME_STATUS_FORMAT_IN_PROGRESS = 0x84


#  Status Code (SC) of NVME_STATUS_TYPE_COMMAND_SPECIFIC
class NVME_STATUS_COMMAND_SPECIFIC_CODES(CEnum):
    NVME_STATUS_COMPLETION_QUEUE_INVALID = 0x00  # Create I/O Submission Queue
    NVME_STATUS_INVALID_QUEUE_IDENTIFIER = 0x01  # Create I/O Submission Queue, Create I/O Completion Queue, Delete I/O Completion Queue, Delete I/O Submission Queue
    NVME_STATUS_MAX_QUEUE_SIZE_EXCEEDED = 0x02  # Create I/O Submission Queue, Create I/O Completion Queue
    NVME_STATUS_ABORT_COMMAND_LIMIT_EXCEEDED = 0x03  # Abort
    NVME_STATUS_ASYNC_EVENT_REQUEST_LIMIT_EXCEEDED = 0x05  # Asynchronous Event Request
    NVME_STATUS_INVALID_FIRMWARE_SLOT = 0x06  # Firmware Commit
    NVME_STATUS_INVALID_FIRMWARE_IMAGE = 0x07  # Firmware Commit
    NVME_STATUS_INVALID_INTERRUPT_VECTOR = 0x08  # Create I/O Completion Queue
    NVME_STATUS_INVALID_LOG_PAGE = 0x09  # Get Log Page
    NVME_STATUS_INVALID_FORMAT = 0x0A  # Format NVM
    NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_CONVENTIONAL_RESET = 0x0B  # Firmware Commit
    NVME_STATUS_INVALID_QUEUE_DELETION = 0x0C  # Delete I/O Completion Queue
    NVME_STATUS_FEATURE_ID_NOT_SAVEABLE = 0x0D  # Set Features
    NVME_STATUS_FEATURE_NOT_CHANGEABLE = 0x0E  # Set Features
    NVME_STATUS_FEATURE_NOT_NAMESPACE_SPECIFIC = 0x0F  # Set Features
    NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_NVM_SUBSYSTEM_RESET = 0x10  # Firmware Commit
    NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_RESET = 0x11  # Firmware Commit
    NVME_STATUS_FIRMWARE_ACTIVATION_REQUIRES_MAX_TIME_VIOLATION = 0x12  # Firmware Commit
    NVME_STATUS_FIRMWARE_ACTIVATION_PROHIBITED = 0x13  # Firmware Commit
    NVME_STATUS_OVERLAPPING_RANGE = 0x14  # Firmware Commit, Firmware Image Download, Set Features

    NVME_STATUS_NAMESPACE_INSUFFICIENT_CAPACITY = 0x15  # Namespace Management
    NVME_STATUS_NAMESPACE_IDENTIFIER_UNAVAILABLE = 0x16  # Namespace Management
    NVME_STATUS_NAMESPACE_ALREADY_ATTACHED = 0x18  # Namespace Attachment
    NVME_STATUS_NAMESPACE_IS_PRIVATE = 0x19  # Namespace Attachment
    NVME_STATUS_NAMESPACE_NOT_ATTACHED = 0x1A  # Namespace Attachment
    NVME_STATUS_NAMESPACE_THIN_PROVISIONING_NOT_SUPPORTED = 0x1B  # Namespace Management
    NVME_STATUS_CONTROLLER_LIST_INVALID = 0x1C  # Namespace Attachment

    NVME_STATUS_DEVICE_SELF_TEST_IN_PROGRESS = 0x1D  # Device Self-test

    NVME_STATUS_BOOT_PARTITION_WRITE_PROHIBITED = 0x1E  # Firmware Commit

    NVME_STATUS_INVALID_CONTROLLER_IDENTIFIER = 0x1F  # Virtualization Management
    NVME_STATUS_INVALID_SECONDARY_CONTROLLER_STATE = 0x20  # Virtualization Management
    NVME_STATUS_INVALID_NUMBER_OF_CONTROLLER_RESOURCES = 0x21  # Virtualization Management
    NVME_STATUS_INVALID_RESOURCE_IDENTIFIER = 0x22  # Virtualization Management

    NVME_STATUS_SANITIZE_PROHIBITED_ON_PERSISTENT_MEMORY = 0x23  # Sanitize

    NVME_STATUS_INVALID_ANA_GROUP_IDENTIFIER = 0x24  # Namespace Management
    NVME_STATUS_ANA_ATTACH_FAILED = 0x25  # Namespace Attachment

    NVME_IO_COMMAND_SET_NOT_SUPPORTED = 0x29  # Namespace Attachment/Management
    NVME_IO_COMMAND_SET_NOT_ENABLED = 0x2A  # Namespace Attachment
    NVME_IO_COMMAND_SET_COMBINATION_REJECTED = 0x2B  # Set Features
    NVME_IO_COMMAND_SET_INVALID = 0x2C  # Identify

    NVME_STATUS_STREAM_RESOURCE_ALLOCATION_FAILED = 0x7F  # Streams Directive
    NVME_STATUS_ZONE_INVALID_FORMAT = 0x7F  # Namespace Management

    NVME_STATUS_NVM_CONFLICTING_ATTRIBUTES = 0x80  # Dataset Management, Read, Write
    NVME_STATUS_NVM_INVALID_PROTECTION_INFORMATION = 0x81  # Compare, Read, Write, Write Zeroes
    NVME_STATUS_NVM_ATTEMPTED_WRITE_TO_READ_ONLY_RANGE = (
        0x82  # Dataset Management, Write, Write Uncorrectable, Write Zeroes
    )
    NVME_STATUS_NVM_COMMAND_SIZE_LIMIT_EXCEEDED = 0x83  # Dataset Management

    NVME_STATUS_ZONE_BOUNDARY_ERROR = (
        0xB8  # Compare, Read, Verify, Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append
    )
    NVME_STATUS_ZONE_FULL = 0xB9  # Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append
    NVME_STATUS_ZONE_READ_ONLY = 0xBA  # Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append
    NVME_STATUS_ZONE_OFFLINE = (
        0xBB  # Compare, Read, Verify, Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append
    )
    NVME_STATUS_ZONE_INVALID_WRITE = 0xBC  # Write, Write Uncorrectable, Write Zeroes, Copy
    NVME_STATUS_ZONE_TOO_MANY_ACTIVE = (
        0xBD  # Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append, Zone Management Send
    )
    NVME_STATUS_ZONE_TOO_MANY_OPEN = (
        0xBE  # Write, Write Uncorrectable, Write Zeroes, Copy, Zone Append, Zone Management Send
    )
    NVME_STATUS_ZONE_INVALID_STATE_TRANSITION = 0xBF  # Zone Management Send


#  Status Code (SC) of NVME_STATUS_TYPE_MEDIA_ERROR
class NVME_STATUS_MEDIA_ERROR_CODES(CEnum):
    NVME_STATUS_NVM_WRITE_FAULT = 0x80
    NVME_STATUS_NVM_UNRECOVERED_READ_ERROR = 0x81
    NVME_STATUS_NVM_END_TO_END_GUARD_CHECK_ERROR = 0x82
    NVME_STATUS_NVM_END_TO_END_APPLICATION_TAG_CHECK_ERROR = 0x83
    NVME_STATUS_NVM_END_TO_END_REFERENCE_TAG_CHECK_ERROR = 0x84
    NVME_STATUS_NVM_COMPARE_FAILURE = 0x85
    NVME_STATUS_NVM_ACCESS_DENIED = 0x86
    NVME_STATUS_NVM_DEALLOCATED_OR_UNWRITTEN_LOGICAL_BLOCK = 0x87


# Admin Command Set
class NVME_ADMIN_COMMANDS(CEnum):
    NVME_ADMIN_COMMAND_DELETE_IO_SQ = 0x00
    NVME_ADMIN_COMMAND_CREATE_IO_SQ = 0x01
    NVME_ADMIN_COMMAND_GET_LOG_PAGE = 0x02
    NVME_ADMIN_COMMAND_DELETE_IO_CQ = 0x04
    NVME_ADMIN_COMMAND_CREATE_IO_CQ = 0x05
    NVME_ADMIN_COMMAND_IDENTIFY = 0x06
    NVME_ADMIN_COMMAND_ABORT = 0x08
    NVME_ADMIN_COMMAND_SET_FEATURES = 0x09
    NVME_ADMIN_COMMAND_GET_FEATURES = 0x0A
    NVME_ADMIN_COMMAND_ASYNC_EVENT_REQUEST = 0x0C
    NVME_ADMIN_COMMAND_NAMESPACE_MANAGEMENT = 0x0D

    NVME_ADMIN_COMMAND_FIRMWARE_ACTIVATE = 0x10
    NVME_ADMIN_COMMAND_FIRMWARE_COMMIT = (
        0x10  # "Firmware Activate" command has been renamed to "Firmware Commit" command in spec v1.2
    )
    NVME_ADMIN_COMMAND_FIRMWARE_IMAGE_DOWNLOAD = 0x11
    NVME_ADMIN_COMMAND_DEVICE_SELF_TEST = 0x14
    NVME_ADMIN_COMMAND_NAMESPACE_ATTACHMENT = 0x15

    NVME_ADMIN_COMMAND_DIRECTIVE_SEND = 0x19
    NVME_ADMIN_COMMAND_DIRECTIVE_RECEIVE = 0x1A
    NVME_ADMIN_COMMAND_VIRTUALIZATION_MANAGEMENT = 0x1C
    NVME_ADMIN_COMMAND_NVME_MI_SEND = 0x1D
    NVME_ADMIN_COMMAND_NVME_MI_RECEIVE = 0x1E

    NVME_ADMIN_COMMAND_DOORBELL_BUFFER_CONFIG = 0x7C

    NVME_ADMIN_COMMAND_FORMAT_NVM = 0x80
    NVME_ADMIN_COMMAND_SECURITY_SEND = 0x81
    NVME_ADMIN_COMMAND_SECURITY_RECEIVE = 0x82
    NVME_ADMIN_COMMAND_SANITIZE = 0x84
    NVME_ADMIN_COMMAND_GET_LBA_STATUS = 0x86


# Features for Get/Set Features command
class NVME_FEATURES(CEnum):
    NVME_FEATURE_ARBITRATION = 0x01
    NVME_FEATURE_POWER_MANAGEMENT = 0x02
    NVME_FEATURE_LBA_RANGE_TYPE = 0x03
    NVME_FEATURE_TEMPERATURE_THRESHOLD = 0x04
    NVME_FEATURE_ERROR_RECOVERY = 0x05
    NVME_FEATURE_VOLATILE_WRITE_CACHE = 0x06
    NVME_FEATURE_NUMBER_OF_QUEUES = 0x07
    NVME_FEATURE_INTERRUPT_COALESCING = 0x08
    NVME_FEATURE_INTERRUPT_VECTOR_CONFIG = 0x09
    NVME_FEATURE_WRITE_ATOMICITY = 0x0A
    NVME_FEATURE_ASYNC_EVENT_CONFIG = 0x0B
    NVME_FEATURE_AUTONOMOUS_POWER_STATE_TRANSITION = 0x0C
    NVME_FEATURE_HOST_MEMORY_BUFFER = 0x0D
    NVME_FEATURE_TIMESTAMP = 0x0E
    NVME_FEATURE_KEEP_ALIVE = 0x0F
    NVME_FEATURE_HOST_CONTROLLED_THERMAL_MANAGEMENT = 0x10
    NVME_FEATURE_NONOPERATIONAL_POWER_STATE = 0x11
    NVME_FEATURE_READ_RECOVERY_LEVEL_CONFIG = 0x12
    NVME_FEATURE_PREDICTABLE_LATENCY_MODE_CONFIG = 0x13
    NVME_FEATURE_PREDICTABLE_LATENCY_MODE_WINDOW = 0x14
    NVME_FEATURE_LBA_STATUS_INFORMATION_REPORT_INTERVAL = 0x15
    NVME_FEATURE_HOST_BEHAVIOR_SUPPORT = 0x16
    NVME_FEATURE_SANITIZE_CONFIG = 0x17
    NVME_FEATURE_ENDURANCE_GROUP_EVENT_CONFIG = 0x18
    NVME_FEATURE_IO_COMMAND_SET_PROFILE = 0x19

    NVME_FEATURE_ENHANCED_CONTROLLER_METADATA = 0x7D
    NVME_FEATURE_CONTROLLER_METADATA = 0x7E
    NVME_FEATURE_NAMESPACE_METADATA = 0x7F

    NVME_FEATURE_NVM_SOFTWARE_PROGRESS_MARKER = 0x80
    NVME_FEATURE_NVM_HOST_IDENTIFIER = 0x81
    NVME_FEATURE_NVM_RESERVATION_NOTIFICATION_MASK = 0x82
    NVME_FEATURE_NVM_RESERVATION_PERSISTANCE = 0x83
    NVME_FEATURE_NVM_NAMESPACE_WRITE_PROTECTION_CONFIG = 0x84

    NVME_FEATURE_ERROR_INJECTION = 0xC0  # This is from OCP NVMe Cloud SSD spec.
    NVME_FEATURE_CLEAR_FW_UPDATE_HISTORY = 0xC1  # This is from OCP NVMe Cloud SSD spec.
    NVME_FEATURE_READONLY_WRITETHROUGH_MODE = 0xC2  # This is from OCP NVMe Cloud SSD spec.
    NVME_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS = 0xC3  # This is from OCP NVMe Cloud SSD spec.
    NVME_FEATURE_ENABLE_IEEE1667_SILO = 0xC4  # This is from OCP NVMe Cloud SSD spec.
    NVME_FEATURE_PLP_HEALTH_MONITOR = 0xC5  # This is from OCP NVMe Cloud SSD spec.


# Abort command: parameter
class NVME_CDW10_ABORT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("SQID", ULONG, 8),  # Submission Queue Identifier (SQID)
                    ("CID", ULONG, 16),  # Command Identifier (CID)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Identify Command of Controller or Namespace Structure (CNS)
class NVME_IDENTIFY_CNS_CODES(CEnum):
    NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE = 0x0
    NVME_IDENTIFY_CNS_CONTROLLER = 0x1
    NVME_IDENTIFY_CNS_ACTIVE_NAMESPACES = 0x2  # A list of up to 1024 active namespace IDs is returned to the host containing active namespaces with a namespace identifier greater than the value specified in the Namespace Identifier (CDW1.NSID) field.
    NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE = 0x3
    NVME_IDENTIFY_CNS_NVM_SET = 0x4

    NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE_IO_COMMAND_SET = 0x5
    NVME_IDENTIFY_CNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET = 0x6
    NVME_IDENTIFY_CNS_ACTIVE_NAMESPACE_LIST_IO_COMMAND_SET = 0x7

    NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_LIST = 0x10
    NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE = 0x11
    NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NSID = 0x12
    NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NVM_SUBSYSTEM = 0x13
    NVME_IDENTIFY_CNS_PRIMARY_CONTROLLER_CAPABILITIES = 0x14
    NVME_IDENTIFY_CNS_SECONDARY_CONTROLLER_LIST = 0x15
    NVME_IDENTIFY_CNS_NAMESPACE_GRANULARITY_LIST = 0x16
    NVME_IDENTIFY_CNS_UUID_LIST = 0x17
    NVME_IDENTIFY_CNS_DOMAIN_LIST = 0x18
    NVME_IDENTIFY_CNS_ENDURANCE_GROUP_LIST = 0x19

    NVME_IDENTIFY_CNS_ALLOCATED_NAMSPACE_LIST_IO_COMMAND_SET = 0x1A
    NVME_IDENTIFY_CNS_ALLOCATED_NAMESPACE_IO_COMMAND_SET = 0x1B
    NVME_IDENTIFY_CNS_IO_COMMAND_SET = 0x1C


# Identify Command Set Identifiers (CSI)
class NVME_COMMAND_SET_IDENTIFIERS(CEnum):
    NVME_COMMAND_SET_NVM = 0x0
    NVME_COMMAND_SET_KEY_VALUE = 0x1
    NVME_COMMAND_SET_ZONED_NAMESPACE = 0x2


class NVME_CDW10_IDENTIFY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("CNS", ULONG, 8),  # Controller or Namespace Structure (CNS, Defined in NVME_IDENTIFY_CNS_CODES)
                    ("Reserved", ULONG, 8),
                    ("CNTID", ULONG, 16),  # Controller Identifier (CNTID)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_IDENTIFY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NVMSETID", USHORT),  # NVM Set Identifier
                    ("Reserved", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "DUMMYSTRUCTNAME2",
            make_struct(
                [
                    ("CNSID", ULONG, 16),  # CNS Specific Identifier (NVM Set ID/Domain ID/Endurance Group ID)
                    ("Reserved2", ULONG, 8),
                    ("CSI", ULONG, 8),  # Command Set Identifier (CSI, Defined in NVME_COMMAND_SET_IDENTIFIERS)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Output of NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE (0x0)
class NVME_LBA_FORMAT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("MS", USHORT),  # bit 0:15     Metadata Size (MS)
                    ("LBADS", UCHAR),  # bit 16:23    LBA  Data  Size (LBADS)
                    ("RP", UCHAR, 2),  # bit 24:25    Relative Performance (RP)
                    ("Reserved0", UCHAR, 6),  # bit 26:31
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVM_RESERVATION_CAPABILITIES(Union):  # fixme: *PNVME_RESERVATION_CAPABILITIES
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("PersistThroughPowerLoss", UCHAR, 1),
                    ("WriteExclusiveReservation", UCHAR, 1),
                    ("ExclusiveAccessReservation", UCHAR, 1),
                    ("WriteExclusiveRegistrantsOnlyReservation", UCHAR, 1),
                    ("ExclusiveAccessRegistrantsOnlyReservation", UCHAR, 1),
                    ("WriteExclusiveAllRegistrantsReservation", UCHAR, 1),
                    ("ExclusiveAccessAllRegistrantsReservation", UCHAR, 1),
                    ("Reserved", UCHAR, 1),
                ],
                _pack_,
            ),
        ),
        ("AsUchar", UCHAR),
    ]


class NVME_IDENTIFY_NAMESPACE_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NSZE", ULONGLONG),  # byte 0:7.    M - Namespace Size (NSZE)
        ("NCAP", ULONGLONG),  # byte 8:15    M - Namespace Capacity (NCAP)
        ("NUSE", ULONGLONG),  # byte 16:23   M - Namespace Utilization (NUSE)
        (
            "NSFEAT",
            make_struct(
                [
                    ("ThinProvisioning", UCHAR, 1),
                    ("NameSpaceAtomicWriteUnit", UCHAR, 1),
                    ("DeallocatedOrUnwrittenError", UCHAR, 1),
                    ("SkipReuseUI", UCHAR, 1),
                    ("NameSpaceIoOptimization", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                ],
                _pack_,
            ),
        ),  # byte 24      M - Namespace Features (NSFEAT)
        ("NLBAF", UCHAR),  # byte 25      M - Number of LBA Formats (NLBAF)
        (
            "FLBAS",
            make_struct(
                [
                    ("LbaFormatIndex", UCHAR, 4),
                    ("MetadataInExtendedDataLBA", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                ],
                _pack_,
            ),
        ),  # byte 26      M - Formatted LBA Size (FLBAS)
        (
            "MC",
            make_struct(
                [
                    ("MetadataInExtendedDataLBA", UCHAR, 1),
                    ("MetadataInSeparateBuffer", UCHAR, 1),
                    ("Reserved", UCHAR, 6),
                ],
                _pack_,
            ),
        ),  # byte 27      M - Metadata Capabilities (MC)
        (
            "DPC",
            make_struct(
                [
                    ("ProtectionInfoType1", UCHAR, 1),
                    ("ProtectionInfoType2", UCHAR, 1),
                    ("ProtectionInfoType3", UCHAR, 1),
                    ("InfoAtBeginningOfMetadata", UCHAR, 1),
                    ("InfoAtEndOfMetadata", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                ],
                _pack_,
            ),
        ),  # byte 28      M - End-to-end Data Protection Capabilities (DPC)
        (
            "DPS",
            make_struct(
                [
                    ("ProtectionInfoTypeEnabled", UCHAR, 3),  # 0 - not enabled; 1 ~ 3: enabled type; 4 ~ 7: reserved
                    ("InfoAtBeginningOfMetadata", UCHAR, 1),
                    ("Reserved", UCHAR, 4),
                ],
                _pack_,
            ),
        ),  # byte 29      M - End-to-end Data Protection Type Settings (DPS)
        (
            "NMIC",
            make_struct(
                [
                    ("SharedNameSpace", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # byte 30      O - Namespace Multi-path I/O and Namespace Sharing Capabilities (NMIC)
        ("RESCAP", NVM_RESERVATION_CAPABILITIES),  # byte 31      O - Reservation Capabilities (RESCAP)
        (
            "FPI",
            make_struct(
                [
                    (
                        "PercentageRemained",
                        UCHAR,
                        7,
                    ),  # Bits 6:0: indicate the percentage of the namespace that remains to be formatted
                    (
                        "Supported",
                        UCHAR,
                        1,
                    ),  # Bit 7: if set to 1 indicates that the namespace supports the Format Progress Indicator.
                ],
                _pack_,
            ),
        ),  # byte 32      O - Format Progress Indicator (FPI)
        (
            "DLFEAT",
            make_struct(
                [
                    ("ReadBehavior", UCHAR, 3),  # Bits 2:0: indicate deallocated logical block read behavior
                    ("WriteZeroes", UCHAR, 1),  # Bit 3: indicate controller supports the deallocate bit in Write Zeroes
                    (
                        "GuardFieldWithCRC",
                        UCHAR,
                        1,
                    ),  # Bit 4: indicate guard field for deallocated logical blocks is set to CRC
                    ("Reserved", UCHAR, 3),
                ],
                _pack_,
            ),
        ),  # byte 33
        ("NAWUN", USHORT),  # byte 34:35 O - Namespace Atomic Write Unit Normal (NAWUN)
        ("NAWUPF", USHORT),  # byte 36:37 O - Namespace Atomic Write Unit Power Fail (NAWUPF)
        ("NACWU", USHORT),  # byte 38:39 O - Namespace Atomic Compare & Write Unit (NACWU)
        ("NABSN", USHORT),  # byte 40:41 O - Namespace Atomic Boundary Size Normal (NABSN)
        ("NABO", USHORT),  # byte 42:43 O - Namespace Atomic Boundary Offset (NABO)
        ("NABSPF", USHORT),  # byte 44:45 O - Namespace Atomic Boundary Size Power Fail (NABSPF)
        ("NOIOB", USHORT),  # byte 46:47 O - Namespace Optimal IO Boundary (NOIOB)
        ("NVMCAP", UCHAR * 16),  # byte 48:63 O - NVM Capacity (NVMCAP)
        ("NPWG", USHORT),  # byte 64:65 O - Namespace Preferred Write Granularity (NPWG)
        ("NPWA", USHORT),  # byte 66:67 O - Namespace Preferred Write Alignment (NPWA)
        ("NPDG", USHORT),  # byte 68:69 O - Namespace Preferred Deallocate Granularity (NPDG)
        ("NPDA", USHORT),  # byte 70:71 O - Namespace Preferred Deallocate Alignment (NPDA)
        ("NOWS", USHORT),  # byte 72:73 O - Namespace Optimal Write Size (NOWS)
        ("MSSRL", USHORT),  # byte 74:75 O - Maximum Single Source Range Length(MSSRL)
        ("MCL", ULONG),  # byte 76:79 O - Maximum Copy Length(MCL)
        ("MSRC", UCHAR),  # byte 80 O - Maximum Source Range Count(MSRC)
        ("Reserved2", UCHAR * 11),  # byte 81:91
        ("ANAGRPID", ULONG),  # byte 92:95 O - ANA Group Identifier (ANAGRPID)
        ("Reserved3", UCHAR * 3),  # byte 96:98
        (
            "NSATTR",
            make_struct(
                [
                    ("WriteProtected", UCHAR, 1),  # Write Protected
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # byte 99 O - Namespace Attributes
        ("NVMSETID", USHORT),  # byte 100:101 O - Associated NVM Set Identifier
        ("ENDGID", USHORT),  # byte 102:103 O - Associated Endurance Group Identier
        ("NGUID", UCHAR * 16),  # byte 104:119 O - Namespace Globally Unique Identifier (NGUID)
        ("EUI64", UCHAR * 8),  # byte 120:127 M - IEEE Extended Unique Identifier (EUI64)
        ("LBAF", NVME_LBA_FORMAT * 16),  # byte 128:131 M - LBA Format 0 Support (LBAF0)
        # byte 132:135 O - LBA Format 1 Support (LBAF1)
        # byte 136:139 O - LBA Format 2 Support (LBAF2)
        # byte 140:143 O - LBA Format 3 Support (LBAF3)
        # byte 144:147 O - LBA Format 4 Support (LBAF4)
        # byte 148:151 O - LBA Format 5 Support (LBAF5)
        # byte 152:155 O - LBA Format 6 Support (LBAF6)
        # byte 156:159 O - LBA Format 7 Support (LBAF7)
        # byte 160:163 O - LBA Format 8 Support (LBAF8)
        # byte 164:167 O - LBA Format 9 Support (LBAF9)
        # byte 168:171 O - LBA Format 10 Support (LBAF10)
        # byte 172:175 O - LBA Format 11 Support (LBAF11)
        # byte 176:179 O - LBA Format 12 Support (LBAF12)
        # byte 180:183 O - LBA Format 13 Support (LBAF13)
        # byte 184:187 O - LBA Format 14 Support (LBAF14)
        # byte 188:191 O - LBA Format 15 Support (LBAF15)
        ("Reserved4", UCHAR * 192),  # byte 192:383
        (
            "VS",
            UCHAR * 3712,
        ),  # byte 384:4095 O - Vendor Specific (VS): This range of bytes is allocated for vendor specific usage.
    ]


# Output of NVME_IDENTIFY_CNS_CONTROLLER (0x01)
class NVME_POWER_STATE_DESC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("MP", USHORT),  # bit 0:15.    Maximum  Power (MP)
        ("Reserved0", UCHAR),  # bit 16:23
        ("MPS", UCHAR, 1),  # bit 24: Max Power Scale (MPS)
        ("NOPS", UCHAR, 1),  # bit 25: Non-Operational State (NOPS)
        ("Reserved1", UCHAR, 6),  # bit 26:31
        ("ENLAT", ULONG),  # bit 32:63.   Entry Latency (ENLAT)
        ("EXLAT", ULONG),  # bit 64:95.   Exit Latency (EXLAT)
        ("RRT", UCHAR, 5),  # bit 96:100.  Relative Read Throughput (RRT)
        ("Reserved2", UCHAR, 3),  # bit 101:103
        ("RRL", UCHAR, 5),  # bit 104:108  Relative Read Latency (RRL)
        ("Reserved3", UCHAR, 3),  # bit 109:111
        ("RWT", UCHAR, 5),  # bit 112:116  Relative Write Throughput (RWT)
        ("Reserved4", UCHAR, 3),  # bit 117:119
        ("RWL", UCHAR, 5),  # bit 120:124  Relative Write Latency (RWL)
        ("Reserved5", UCHAR, 3),  # bit 125:127
        ("IDLP", USHORT),  # bit 128:143  Idle Power (IDLP)
        ("Reserved6", UCHAR, 6),  # bit 144:149
        ("IPS", UCHAR, 2),  # bit 150:151  Idle Power Scale (IPS)
        ("Reserved7", UCHAR),  # bit 152:159
        ("ACTP", USHORT),  # bit 160:175  Active Power (ACTP)
        ("APW", UCHAR, 3),  # bit 176:178  Active Power Workload (APW)
        ("Reserved8", UCHAR, 3),  # bit 179:181
        ("APS", UCHAR, 2),  # bit 182:183  Active Power Scale (APS)
        ("Reserved9", UCHAR * 9),  # bit 184:255.
    ]


class NVME_IDENTIFY_CONTROLLER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        # byte 0 : 255, Controller Capabilities and Features
        ("VID", USHORT),  # byte 0:1.    M - PCI Vendor ID (VID)
        ("SSVID", USHORT),  # byte 2:3.    M - PCI Subsystem Vendor ID (SSVID)
        ("SN", UCHAR * 20),  # byte 4: 23.  M - Serial Number (SN)
        ("MN", UCHAR * 40),  # byte 24:63.  M - Model Number (MN)
        ("FR", UCHAR * 8),  # byte 64:71.  M - Firmware Revision (FR)
        ("RAB", UCHAR),  # byte 72.     M - Recommended Arbitration Burst (RAB)
        ("IEEE", UCHAR * 3),  # byte 73:75.  M - IEEE OUI Identifier (IEEE). Controller Vendor code.
        (
            "CMIC",
            make_struct(
                [
                    ("MultiPCIePorts", UCHAR, 1),
                    ("MultiControllers", UCHAR, 1),
                    ("SRIOV", UCHAR, 1),
                    ("ANAR", UCHAR, 1),
                    ("Reserved", UCHAR, 4),
                ],
                _pack_,
            ),
        ),  # byte 76.     O - Controller Multi-Path I/O and Namespace Sharing Capabilities (CMIC)
        ("MDTS", UCHAR),  # byte 77.     M - Maximum Data Transfer Size (MDTS)
        ("CNTLID", USHORT),  # byte 78:79.   M - Controller ID (CNTLID)
        ("VER", ULONG),  # byte 80:83.   M - Version (VER)
        ("RTD3R", ULONG),  # byte 84:87.   M - RTD3 Resume Latency (RTD3R)
        ("RTD3E", ULONG),  # byte 88:91.   M - RTD3 Entry Latency (RTD3E)
        (
            "OAES",
            make_struct(
                [
                    ("Reserved0", ULONG, 8),
                    ("NamespaceAttributeChanged", ULONG, 1),
                    ("FirmwareActivation", ULONG, 1),
                    ("Reserved1", ULONG, 1),
                    ("AsymmetricAccessChanged", ULONG, 1),
                    ("PredictableLatencyAggregateLogChanged", ULONG, 1),
                    ("LbaStatusChanged", ULONG, 1),
                    ("EnduranceGroupAggregateLogChanged", ULONG, 1),
                    ("Reserved2", ULONG, 12),
                    ("ZoneInformation", ULONG, 1),
                    ("Reserved3", ULONG, 4),
                ],
                _pack_,
            ),
        ),  # byte 92:95.   M - Optional Asynchronous Events Supported (OAES)
        (
            "CTRATT",
            make_struct(
                [
                    ("HostIdentifier128Bit", ULONG, 1),
                    ("NOPSPMode", ULONG, 1),
                    ("NVMSets", ULONG, 1),
                    ("ReadRecoveryLevels", ULONG, 1),
                    ("EnduranceGroups", ULONG, 1),
                    ("PredictableLatencyMode", ULONG, 1),
                    ("TBKAS", ULONG, 1),  # Traffic Based Keep Alive Support
                    ("NamespaceGranularity", ULONG, 1),
                    ("SQAssociations", ULONG, 1),
                    ("UUIDList", ULONG, 1),
                    ("Reserved0", ULONG, 22),
                ],
                _pack_,
            ),
        ),  # byte 96:99.   M - Controller Attributes (CTRATT)
        (
            "RRLS",
            make_struct(
                [
                    ("ReadRecoveryLevel0", USHORT, 1),
                    ("ReadRecoveryLevel1", USHORT, 1),
                    ("ReadRecoveryLevel2", USHORT, 1),
                    ("ReadRecoveryLevel3", USHORT, 1),
                    ("ReadRecoveryLevel4", USHORT, 1),
                    ("ReadRecoveryLevel5", USHORT, 1),
                    ("ReadRecoveryLevel6", USHORT, 1),
                    ("ReadRecoveryLevel7", USHORT, 1),
                    ("ReadRecoveryLevel8", USHORT, 1),
                    ("ReadRecoveryLevel9", USHORT, 1),
                    ("ReadRecoveryLevel10", USHORT, 1),
                    ("ReadRecoveryLevel11", USHORT, 1),
                    ("ReadRecoveryLevel12", USHORT, 1),
                    ("ReadRecoveryLevel13", USHORT, 1),
                    ("ReadRecoveryLevel14", USHORT, 1),
                    ("ReadRecoveryLevel15", USHORT, 1),
                ],
                _pack_,
            ),
        ),  # byte 100:101. O - Read Recovery Levels Supported (RRLS)
        ("Reserved0", UCHAR * 9),  # byte 102:110.
        ("CNTRLTYPE", UCHAR),  # byte 111.     M - Controller Type
        ("FGUID", UCHAR * 16),  # byte 112:127. O - FRU Globally Unique Identifier (FGUID)
        ("CRDT1", USHORT),  # byte 128:129. O - Command Retry Delay Time 1
        ("CRDT2", USHORT),  # byte 130:131. O - Command Retry Delay Time 1
        ("CRDT3", USHORT),  # byte 132:133. O - Command Retry Delay Time 1
        ("Reserved0_1", UCHAR * 106),  # byte 134:239.
        (
            "ReservedForManagement",
            UCHAR * 16,
        ),  # byte 240:255.  Refer to the NVMe Management Interface Specification for definition.
        # byte 256 : 511, Admin Command Set Attributes
        (
            "OACS",
            make_struct(
                [
                    ("SecurityCommands", USHORT, 1),
                    ("FormatNVM", USHORT, 1),
                    ("FirmwareCommands", USHORT, 1),
                    ("NamespaceCommands", USHORT, 1),
                    ("DeviceSelfTest", USHORT, 1),
                    ("Directives", USHORT, 1),
                    ("NVMeMICommands", USHORT, 1),
                    ("VirtualizationMgmt", USHORT, 1),
                    ("DoorBellBufferConfig", USHORT, 1),
                    ("GetLBAStatus", USHORT, 1),
                    ("Reserved", USHORT, 6),
                ],
                _pack_,
            ),
        ),  # byte 256:257. M - Optional Admin Command Support (OACS)
        ("ACL", UCHAR),  # byte 258.    M - Abort Command Limit (ACL)
        ("AERL", UCHAR),  # byte 259.    M - Asynchronous Event Request Limit (AERL)
        (
            "FRMW",
            make_struct(
                [
                    ("Slot1ReadOnly", UCHAR, 1),
                    ("SlotCount", UCHAR, 3),
                    ("ActivationWithoutReset", UCHAR, 1),
                    ("Reserved", UCHAR, 3),
                ],
                _pack_,
            ),
        ),  # byte 260.    M - Firmware Updates (FRMW)
        (
            "LPA",
            make_struct(
                [
                    ("SmartPagePerNamespace", UCHAR, 1),
                    ("CommandEffectsLog", UCHAR, 1),
                    ("LogPageExtendedData", UCHAR, 1),
                    ("TelemetrySupport", UCHAR, 1),
                    ("PersistentEventLog", UCHAR, 1),
                    ("Reserved0", UCHAR, 1),
                    ("TelemetryDataArea4", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),
                ],
                _pack_,
            ),
        ),  # byte 261.    M - Log Page Attributes (LPA)
        ("ELPE", UCHAR),  # byte 262.    M - Error Log Page Entries (ELPE)
        ("NPSS", UCHAR),  # byte 263.    M - Number of Power States Support (NPSS)
        (
            "AVSCC",
            make_struct(
                [
                    ("CommandFormatInSpec", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # byte 264.    M - Admin Vendor Specific Command Configuration (AVSCC)
        (
            "APSTA",
            make_struct(
                [
                    ("Supported", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # byte 265.     O - Autonomous Power State Transition Attributes (APSTA)
        ("WCTEMP", USHORT),  # byte 266:267. M - Warning Composite Temperature Threshold (WCTEMP)
        ("CCTEMP", USHORT),  # byte 268:269. M - Critical Composite Temperature Threshold (CCTEMP)
        ("MTFA", USHORT),  # byte 270:271. O - Maximum Time for Firmware Activation (MTFA)
        ("HMPRE", ULONG),  # byte 272:275. O - Host Memory Buffer Preferred Size (HMPRE)
        ("HMMIN", ULONG),  # byte 276:279. O - Host Memory Buffer Minimum Size (HMMIN)
        ("TNVMCAP", UCHAR * 16),  # byte 280:295. O - Total NVM Capacity (TNVMCAP)
        ("UNVMCAP", UCHAR * 16),  # byte 296:311. O - Unallocated NVM Capacity (UNVMCAP)
        (
            "RPMBS",
            make_struct(
                [
                    ("RPMBUnitCount", ULONG, 3),  # Number of RPMB Units
                    ("AuthenticationMethod", ULONG, 3),  # Authentication Method
                    ("Reserved0", ULONG, 10),
                    ("TotalSize", ULONG, 8),  # Total Size: in 128KB units.
                    ("AccessSize", ULONG, 8),  # Access Size: in 512B units.
                ],
                _pack_,
            ),
        ),  # byte 312:315. O - Replay Protected Memory Block Support (RPMBS)
        ("EDSTT", USHORT),  # byte 316:317. O - Extended Device Self-test Time (EDSTT)
        ("DSTO", UCHAR),  # byte 318.     O - Device Self-test Options (DSTO)
        ("FWUG", UCHAR),  # byte 319.     M - Firmware Update Granularity (FWUG)
        ("KAS", USHORT),  # byte 320:321  M - Keep Alive Support (KAS)
        (
            "HCTMA",
            make_struct(
                [
                    ("Supported", USHORT, 1),
                    ("Reserved", USHORT, 15),
                ],
                _pack_,
            ),
        ),  # byte 322:323  O - Host Controlled Thermal Management Attributes (HCTMA)
        ("MNTMT", USHORT),  # byte 324:325  O - Minimum Thermal Management Temperature (MNTMT)
        ("MXTMT", USHORT),  # byte 326:327  O - Maximum Thermal Management Temperature (MXTMT)
        (
            "SANICAP",
            make_struct(
                [
                    ("CryptoErase", ULONG, 1),  # Controller supports Crypto Erase Sanitize
                    ("BlockErase", ULONG, 1),  # Controller supports Block Erase Sanitize
                    ("Overwrite", ULONG, 1),  # Controller supports Overwrite Santize
                    ("Reserved", ULONG, 26),
                    ("NDI", ULONG, 1),  # No-Deallocate Inhibited (NDI)
                    ("NODMMAS", ULONG, 2),  # No-Deallocate Modifies Media After Sanitize (NODMMAS)
                ],
                _pack_,
            ),
        ),  # byte 328:331  O - Sanitize Capabilities (SANICAP)
        ("HMMINDS", ULONG),  # byte 332:335  O - Host Memory Buffer Minimum Descriptor Entry Size (HMMINDS)
        ("HMMAXD", USHORT),  # byte 336:337  O - Host Memory Maxiumum Descriptors Entries (HMMAXD)
        ("NSETIDMAX", USHORT),  # byte 338:339  O - NVM Set Identifier Maximum
        ("ENDGIDMAX", USHORT),  # byte 340:341  O - Endurance Group Identifier Maximum (ENDGIDMAX)
        ("ANATT", UCHAR),  # byte 342      O - ANA Transition Time (ANATT)
        (
            "ANACAP",
            make_struct(
                [
                    ("OptimizedState", UCHAR, 1),  # Report ANA Optimized State
                    ("NonOptimizedState", UCHAR, 1),  # Report ANA Non-Optimized State
                    ("InaccessibleState", UCHAR, 1),  # Report ANA Inaccessible State
                    ("PersistentLossState", UCHAR, 1),  # Report ANA Persistent Loss State
                    ("ChangeState", UCHAR, 1),  # Report ANA Change State
                    ("Reserved", UCHAR, 1),
                    ("StaticANAGRPID", UCHAR, 1),  # If set, ANAGRPID in Identify Namespace doesn't change
                    (
                        "SupportNonZeroANAGRPID",
                        UCHAR,
                        1,
                    ),  # If set, Controller supports a non-zero value in ANAGRPID field of Namespace Mgmt Command
                ],
                _pack_,
            ),
        ),  # byte 343      O - Asymmetric Namespace Access Capabilities (ANACAP)
        ("ANAGRPMAX", ULONG),  # byte 344:347  O - ANA Group Identifier Maximum (ANAGRPMAX)
        ("NANAGRPID", ULONG),  # byte 348:351  O - Number of ANA Group Identifiers (NANAGRPID)
        ("PELS", ULONG),  # byte 352:355  O - Persistent Event Log Size (PELS)
        ("Reserved1", UCHAR * 156),  # byte 356:511.
        # byte 512 : 703, NVM Command Set Attributes
        (
            "SQES",
            make_struct(
                [
                    ("RequiredEntrySize", UCHAR, 4),  # The value is in bytes and is reported as a power of two (2^n).
                    (
                        "MaxEntrySize",
                        UCHAR,
                        4,
                    ),  # This value is larger than or equal to the required SQ entry size.  The value is in bytes and is reported as a power of two (2^n).
                ],
                _pack_,
            ),
        ),  # byte 512.    M - Submission Queue Entry Size (SQES)
        (
            "CQES",
            make_struct(
                [
                    ("RequiredEntrySize", UCHAR, 4),  # The value is in bytes and is reported as a power of two (2^n).
                    (
                        "MaxEntrySize",
                        UCHAR,
                        4,
                    ),  # This value is larger than or equal to the required CQ entry size. The value is in bytes and is reported as a power of two (2^n).
                ],
                _pack_,
            ),
        ),  # byte 513.    M - Completion Queue Entry Size (CQES)
        ("MAXCMD", USHORT),  # byte 514:515. M - Maximum Outstanding Commands (MAXCMD)
        ("NN", ULONG),  # byte 516:519. M - Number of Namespaces (NN)
        (
            "ONCS",
            make_struct(
                [
                    ("Compare", USHORT, 1),
                    ("WriteUncorrectable", USHORT, 1),
                    ("DatasetManagement", USHORT, 1),
                    ("WriteZeroes", USHORT, 1),
                    ("FeatureField", USHORT, 1),
                    ("Reservations", USHORT, 1),
                    ("Timestamp", USHORT, 1),
                    ("Verify", USHORT, 1),
                    ("Reserved", USHORT, 8),
                ],
                _pack_,
            ),
        ),  # byte 520:521. M - Optional NVM Command Support (ONCS)
        (
            "FUSES",
            make_struct(
                [
                    ("CompareAndWrite", USHORT, 1),
                    ("Reserved", USHORT, 15),
                ],
                _pack_,
            ),
        ),  # byte 522:523. M - Fused Operation Support (FUSES)
        (
            "FNA",
            make_struct(
                [
                    ("FormatApplyToAll", UCHAR, 1),
                    ("SecureEraseApplyToAll", UCHAR, 1),
                    ("CryptographicEraseSupported", UCHAR, 1),
                    ("FormatSupportNSIDAllF", UCHAR, 1),
                    ("Reserved", UCHAR, 4),
                ],
                _pack_,
            ),
        ),  # byte 524.     M - Format NVM Attributes (FNA)
        (
            "VWC",
            make_struct(
                [
                    ("Present", UCHAR, 1),
                    ("FlushBehavior", UCHAR, 2),
                    ("Reserved", UCHAR, 5),
                ],
                _pack_,
            ),
        ),  # byte 525.     M - Volatile Write Cache (VWC)
        ("AWUN", USHORT),  # byte 526:527. M - Atomic Write Unit Normal (AWUN)
        ("AWUPF", USHORT),  # byte 528:529. M - Atomic Write Unit Power Fail (AWUPF)
        (
            "NVSCC",
            make_struct(
                [
                    ("CommandFormatInSpec", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # byte 530.     M - NVM Vendor Specific Command Configuration (NVSCC)
        (
            "NWPC",
            make_struct(
                [
                    ("WriteProtect", UCHAR, 1),
                    ("UntilPowerCycle", UCHAR, 1),
                    ("Permanent", UCHAR, 1),
                    ("Reserved", UCHAR, 5),
                ],
                _pack_,
            ),
        ),  # byte 531.     M - Namespace Write Protection Capabilities (NWPC)
        ("ACWU", USHORT),  # byte 532:533  O - Atomic Compare & Write Unit (ACWU)
        ("Reserved4", UCHAR * 2),  # byte 534:535.
        (
            "SGLS",
            make_struct(
                [
                    ("SGLSupported", ULONG, 2),
                    ("KeyedSGLData", ULONG, 1),
                    ("Reserved0", ULONG, 13),
                    ("BitBucketDescrSupported", ULONG, 1),
                    ("ByteAlignedContiguousPhysicalBuffer", ULONG, 1),
                    ("SGLLengthLargerThanDataLength", ULONG, 1),
                    ("MPTRSGLDescriptor", ULONG, 1),
                    ("AddressFieldSGLDataBlock", ULONG, 1),
                    ("TransportSGLData", ULONG, 1),
                    ("Reserved1", ULONG, 10),
                ],
                _pack_,
            ),
        ),  # byte 536:539. O - SGL Support (SGLS)
        ("MNAN", ULONG),  # byte 540:543. O - Maximum Number of Allowed Namespace (MNAN)
        ("Reserved6", UCHAR * 224),  # byte 544:767.
        ("SUBNQN", UCHAR * 256),  # byte 768:1023. M - NVM Subsystem NVMe Qualified Name (SUBNQN)
        ("Reserved7", UCHAR * 768),  # byte 1024:1791
        ("Reserved8", UCHAR * 256),  # byte 1792:2047. Refer to NVMe over Fabrics Specification
        # byte 2048 : 3071, Power State Descriptors
        (
            "PDS",
            NVME_POWER_STATE_DESC * 32,
        ),  # byte 2048:2079. M - Power State 0 Descriptor (PSD0):  This field indicates the characteristics of power state 0
        # byte 2080:2111. O - Power State 1 Descriptor (PSD1):  This field indicates the characteristics of power state 1
        # byte 2112:2143. O - Power State 2 Descriptor (PSD1):  This field indicates the characteristics of power state 2
        # byte 2144:2175. O - Power State 3 Descriptor (PSD1):  This field indicates the characteristics of power state 3
        # byte 2176:2207. O - Power State 4 Descriptor (PSD1):  This field indicates the characteristics of power state 4
        # byte 2208:2239. O - Power State 5 Descriptor (PSD1):  This field indicates the characteristics of power state 5
        # byte 2240:2271. O - Power State 6 Descriptor (PSD1):  This field indicates the characteristics of power state 6
        # byte 2272:2303. O - Power State 7 Descriptor (PSD1):  This field indicates the characteristics of power state 7
        # byte 2304:2335. O - Power State 8 Descriptor (PSD1):  This field indicates the characteristics of power state 8
        # byte 2336:2367. O - Power State 9 Descriptor (PSD1):  This field indicates the characteristics of power state 9
        # byte 2368:2399. O - Power State 10 Descriptor (PSD1):  This field indicates the characteristics of power state 10
        # byte 2400:2431. O - Power State 11 Descriptor (PSD1):  This field indicates the characteristics of power state 11
        # byte 2432:2463. O - Power State 12 Descriptor (PSD1):  This field indicates the characteristics of power state 12
        # byte 2464:2495. O - Power State 13 Descriptor (PSD1):  This field indicates the characteristics of power state 13
        # byte 2496:2527. O - Power State 14 Descriptor (PSD1):  This field indicates the characteristics of power state 14
        # byte 2528:2559. O - Power State 15 Descriptor (PSD1):  This field indicates the characteristics of power state 15
        # byte 2560:2591. O - Power State 16 Descriptor (PSD1):  This field indicates the characteristics of power state 16
        # byte 2592:2623. O - Power State 17 Descriptor (PSD1):  This field indicates the characteristics of power state 17
        # byte 2624:2655. O - Power State 18 Descriptor (PSD1):  This field indicates the characteristics of power state 18
        # byte 2656:2687. O - Power State 19 Descriptor (PSD1):  This field indicates the characteristics of power state 19
        # byte 2688:2719. O - Power State 20 Descriptor (PSD1):  This field indicates the characteristics of power state 20
        # byte 2720:2751. O - Power State 21 Descriptor (PSD1):  This field indicates the characteristics of power state 21
        # byte 2752:2783. O - Power State 22 Descriptor (PSD1):  This field indicates the characteristics of power state 22
        # byte 2784:2815. O - Power State 23 Descriptor (PSD1):  This field indicates the characteristics of power state 23
        # byte 2816:2847. O - Power State 24 Descriptor (PSD1):  This field indicates the characteristics of power state 24
        # byte 2848:2879. O - Power State 25 Descriptor (PSD1):  This field indicates the characteristics of power state 25
        # byte 2880:2911. O - Power State 26 Descriptor (PSD1):  This field indicates the characteristics of power state 26
        # byte 2912:2943. O - Power State 27 Descriptor (PSD1):  This field indicates the characteristics of power state 27
        # byte 2944:2975. O - Power State 28 Descriptor (PSD1):  This field indicates the characteristics of power state 28
        # byte 2976:3007. O - Power State 29 Descriptor (PSD1):  This field indicates the characteristics of power state 29
        # byte 3008:3039. O - Power State 30 Descriptor (PSD1):  This field indicates the characteristics of power state 30
        # byte 3040:3071. O - Power State 31 Descriptor (PSD1):  This field indicates the characteristics of power state 31
        # byte 3072 : 4095, Vendor Specific
        ("VS", UCHAR * 1024),  # byte 3072 : 4095.
    ]


# Namespace Identfier Type (NIDT)
class NVME_IDENTIFIER_TYPE(CEnum):
    NVME_IDENTIFIER_TYPE_EUI64 = 0x1
    NVME_IDENTIFIER_TYPE_NGUID = 0x2
    NVME_IDENTIFIER_TYPE_UUID = 0x3
    NVME_IDENTIFIER_TYPE_CSI = 0x4


# Namespace Identfier Length (NIDL) for a given type defined by NVME_IDENTIFIER_TYPE
class NVME_IDENTIFIER_TYPE_LENGTH(CEnum):
    NVME_IDENTIFIER_TYPE_EUI64_LENGTH = 0x8
    NVME_IDENTIFIER_TYPE_NGUID_LENGTH = 0x10
    NVME_IDENTIFIER_TYPE_UUID_LENGTH = 0x10
    NVME_IDENTIFIER_TYPE_CSI_LENGTH = 0x1


# Output of NVME_IDENTIFY_CNS_ACTIVE_NAMESPACES (0x02)


class NVME_ACTIVE_NAMESPACE_ID_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NSID", ULONG * 1024),  # List of Namespace ID upto 1024 entries
    ]


# Output of NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE (0x03)

NVME_IDENTIFY_CNS_DESCRIPTOR_NAMESPACE_SIZE = 0x1000


class NVME_IDENTIFY_NAMESPACE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NIDT", UCHAR),  # Namespace Identifier Type as defined in NVME_IDENTIFIER_TYPE
        ("NIDL", UCHAR),  # Namespace Identifier Length
        ("Reserved", UCHAR * 2),
        ("NID", UCHAR * ANYSIZE_ARRAY),  # Namespace Identifier (Based on NVME_IDENTIFIER_TYPE)
    ]


# Output of NVME_IDENTIFY_CNS_NVM_SET (0x04)
class NVME_SET_ATTRIBUTES_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Identifier", USHORT),
        ("ENDGID", USHORT),
        ("Reserved1", ULONG),
        ("Random4KBReadTypical", ULONG),
        ("OptimalWriteSize", ULONG),
        ("TotalCapacity", UCHAR * 16),
        ("UnallocatedCapacity", UCHAR * 16),
        ("Reserved2", UCHAR * 80),
    ]


class NVM_SET_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("IdentifierCount", UCHAR),
        ("Reserved", UCHAR * 127),
        ("Entry", NVME_SET_ATTRIBUTES_ENTRY * ANYSIZE_ARRAY),
    ]


# Output of NVME_IDENTIFY_CNS_SPECIFIC_NAMESPACE_IO_COMMAND_SET (0x05)
class NVME_LBA_ZONE_FORMAT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneSize", ULONGLONG),  # bit 0:63     Zone Size (MS)
        ("ZDES", UCHAR),  # bit 64:71    Zone Descriptor Extension Size (ZDES)
        ("Reserved", UCHAR * 7),
    ]


class NVME_IDENTIFY_SPECIFIC_NAMESPACE_IO_COMMAND_SET(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "ZOC",
            make_struct(
                [
                    ("VariableZoneCapacity", USHORT, 1),
                    ("ZoneExcursions", USHORT, 1),
                    ("Reserved", USHORT, 14),
                ],
                _pack_,
            ),
        ),  # Zone Operation Characteristics
        (
            "OZCS",
            make_struct(
                [
                    ("ReadAcrossZoneBoundaries", USHORT, 1),
                    ("Reserved", USHORT, 15),
                ],
                _pack_,
            ),
        ),  # Optional Zoned Command Support
        ("MAR", ULONG),  # Maximum Active Resources (MAR)
        ("MOR", ULONG),  # Maximum Open Resources (MOR)
        ("RRL", ULONG),  # Reset Recommended Limit (RRL)
        ("FRL", ULONG),  # Finish Recommended Limit (FRL)
        ("Reserved0", UCHAR * 2796),
        ("LBAEF", NVME_LBA_ZONE_FORMAT * 16),  # byte 2816:2831 M - LBA Format 0 Extension (LBAFE0)
        # byte 2832:2847 O - LBA Format 1 Extension (LBAFE1)
        # byte 2848:2863 O - LBA Format 2 Extension (LBAFE2)
        # byte 2864:2879 O - LBA Format 3 Extension (LBAFE3)
        # byte 2880:2895 O - LBA Format 4 Extension (LBAFE4)
        # byte 2896:2911 O - LBA Format 5 Extension (LBAFE5)
        # byte 2912:2927 O - LBA Format 6 Extension (LBAFE6)
        # byte 2928:2943 O - LBA Format 7 Extension (LBAFE7)
        # byte 2944:2959 O - LBA Format 8 Extension (LBAFE8)
        # byte 2960:2975 O - LBA Format 9 Extension (LBAFE9)
        # byte 2976:2991 O - LBA Format 10 Extension (LBAFE10)
        # byte 2992:3007 O - LBA Format 11 Extension (LBAFE11)
        # byte 3008:3023 O - LBA Format 12 Extension (LBAFE12)
        # byte 3024:3039 O - LBA Format 13 Extension (LBAFE13)
        # byte 3040:3055 O - LBA Format 14 Extension (LBAFE14)
        # byte 3056:3971 O - LBA Format 15 Extension (LBAFE15)
        ("Reserved1", UCHAR * 768),  # byte 3072:3839
        (
            "VS",
            UCHAR * 256,
        ),  # byte 3840:4095 O - Vendor Specific (VS): This range of bytes is allocated for vendor specific usage.
    ]


# Output of NVME_IDENTIFY_CNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET (0x06) with Command Set Identifier (0x00)
class NVME_IDENTIFY_NVM_SPECIFIC_CONTROLLER_IO_COMMAND_SET(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("VSL", UCHAR),  # byte 0       O - Verify Size Limit (VZL)
        ("WZSL", UCHAR),  # byte 1       O - Write Zeroes Size Limit (WZSL)
        ("WUSL", UCHAR),  # byte 2       O - Write Uncorrectable Size Limit (WUSL)
        ("DMRL", UCHAR),  # byte 3       O - Dataset Management Ranges Limit (DMRL)
        ("DMRSL", ULONG),  # byte 4:7     O - Dataset Management Range Size Limit (DMRSL)
        ("DMSL", ULONGLONG),  # byte 8:15    O - Dataset Management Size Limit (DMSL)
        ("Reserved", UCHAR * 4080),  # byte 16:4095
    ]


# Output of NVME_IDENTIFY_CNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET (0x06) with Command Set Identifier (0x02)
class NVME_IDENTIFY_ZNS_SPECIFIC_CONTROLLER_IO_COMMAND_SET(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZASL", UCHAR),  # byte 0.          O - Zone Append Size Limit (ZASL)
        ("Reserved", UCHAR * 4095),  # byte 1:4095
    ]


# Output of NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NSID (0x12)/NVME_IDENTIFY_CNS_CONTROLLER_LIST_OF_NVM_SUBSYSTEM (0x13)
class NVME_CONTROLLER_LIST(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfIdentifiers", USHORT),
        ("ControllerID", USHORT * 2047),
    ]


# Output of NVME_IDENTIFY_CNS_IO_COMMAND_SET (0x1C)
class NVME_IDENTIFY_IO_COMMAND_SET(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("IOCommandSetVector", ULONGLONG * 512),
    ]


# Data Structure of LBA Range Type entry
class NVME_LBA_RANGE_TYPES(CEnum):
    NVME_LBA_RANGE_TYPE_RESERVED = 0
    NVME_LBA_RANGE_TYPE_FILESYSTEM = 1
    NVME_LBA_RANGE_TYPE_RAID = 2
    NVME_LBA_RANGE_TYPE_CACHE = 3
    NVME_LBA_RANGE_TYPE_PAGE_SWAP_FILE = 4


class NVME_LBA_RANGET_TYPE_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Type", UCHAR),  # Type (Type): Specifies the Type of the LBA range.
        (
            "Attributes",
            make_struct(
                [
                    ("MayOverwritten", UCHAR, 1),
                    ("Hidden", UCHAR, 1),
                    ("Reserved", UCHAR, 6),
                ],
                _pack_,
            ),
        ),  # Attributes: Specifies attributes of the LBA range. Each bit defines an attribute.
        ("Reserved0", UCHAR * 14),
        (
            "SLBA",
            ULONGLONG,
        ),  # Starting LBA (SLBA): This field specifies the 64-bit address of the first logical block that is part of this LBA range.
        (
            "NLB",
            ULONGLONG,
        ),  # Number of Logical Blocks (NLB): This field specifies the number of logical blocks that are part of this LBA range. This is a 0s based value.
        (
            "GUID",
            UCHAR * 16,
        ),  # Unique Identifier (GUID): This field is a global unique identifier that uniquely specifies the type of this LBA range. Well known Types may be defined and are published on the NVM Express website.
        ("Reserved1", UCHAR * 16),
    ]


# Vendor defined log pages
class NVME_VENDOR_LOG_PAGES(CEnum):
    NVME_LOG_PAGE_OCP_DEVICE_SMART_INFORMATION = 0xC0  # OCP device SMART Information log page
    NVME_LOG_PAGE_OCP_DEVICE_ERROR_RECOVERY = 0xC1  # OCP device Error Recovery log page
    NVME_LOG_PAGE_OCP_FIRMWARE_ACTIVATION_HISTORY = 0xC2  # OCP device Firmware Activation History log page
    NVME_LOG_PAGE_OCP_LATENCY_MONITOR = 0xC3  # OCP device Latency Monitor log page
    NVME_LOG_PAGE_OCP_DEVICE_CAPABILITIES = 0xC4  # OCP device Device Capabilities log page
    NVME_LOG_PAGE_OCP_UNSUPPORTED_REQUIREMENTS = 0xC5  # OCP device Unsupported Requirements log page
    NVME_LOG_PAGE_OCP_TCG_CONFIGURATION = 0xC8  # OCP device TCG Configuration log page
    NVME_LOG_PAGE_OCP_TCG_HISTORY = 0xC9  # OCP device TCG History log page


NVME_LOG_PAGE_WCS_DEVICE_SMART_ATTRIBUTES = NVME_VENDOR_LOG_PAGES.NVME_LOG_PAGE_OCP_DEVICE_SMART_INFORMATION
NVME_LOG_PAGE_WCS_DEVICE_ERROR_RECOVERY = (
    NVME_VENDOR_LOG_PAGES.NVME_LOG_PAGE_OCP_DEVICE_ERROR_RECOVERY
)  # WCS device Error Recovery log page

# SMART Attributes Log Page GUID is defined in spec as byte stream: 0xAFD514C97C6F4F9CA4F2BFEA2810AFC5
# which is converted to GUID format as: {2810AFC5-BFEA-A4F2-9C4F-6F7CC914D5AF}
# define GUID_OCP_DEVICE_SMART_INFORMATIONGuid { 0x2810AFC5, 0xBFEA, 0xA4F2, { 0x9C, 0x4F, 0x6F, 0x7C, 0xC9, 0x14, 0xD5, 0xAF} }
GUID_OCP_DEVICE_SMART_INFORMATION = GUID(0x2810AFC5, 0xBFEA, 0xA4F2, (0x9C, 0x4F, 0x6F, 0x7C, 0xC9, 0x14, 0xD5, 0xAF))
# define GUID_WCS_DEVICE_SMART_ATTRIBUTESGuid { 0x2810AFC5, 0xBFEA, 0xA4F2, { 0x9C, 0x4F, 0x6F, 0x7C, 0xC9, 0x14, 0xD5, 0xAF} }
GUID_WCS_DEVICE_SMART_ATTRIBUTES = GUID(0x2810AFC5, 0xBFEA, 0xA4F2, (0x9C, 0x4F, 0x6F, 0x7C, 0xC9, 0x14, 0xD5, 0xAF))
# Error Recovery Log Page GUID is defined in spec as byte stream: 0x5A1983BA3DFD4DABAE3430FE2131D944
# which is converted to GUID format as: {2131D944-30FE-AE34-AB4D-FD3DBA83195A}
# define GUID_OCP_DEVICE_ERROR_RECOVERYGuid { 0x2131D944, 0x30FE, 0xAE34, {0xAB, 0x4D, 0xFD, 0x3D, 0xBA, 0x83, 0x19, 0x5A} }
GUID_OCP_DEVICE_ERROR_RECOVERY = GUID(0x2131D944, 0x30FE, 0xAE34, (0xAB, 0x4D, 0xFD, 0x3D, 0xBA, 0x83, 0x19, 0x5A))
# define GUID_WCS_DEVICE_ERROR_RECOVERYGuid { 0x2131D944, 0x30FE, 0xAE34, {0xAB, 0x4D, 0xFD, 0x3D, 0xBA, 0x83, 0x19, 0x5A} }
GUID_WCS_DEVICE_ERROR_RECOVERY = GUID(0x2131D944, 0x30FE, 0xAE34, (0xAB, 0x4D, 0xFD, 0x3D, 0xBA, 0x83, 0x19, 0x5A))
# Firmware Activation History Log Page GUID is defined in spec as byte stream: 0xD11CF3AC8AB24DE2A3F6DAB4769A796D
# which is converted to GUID format as: {769A796D-DAB4-A3F6-E24D-B28AACF31CD1}
# define GUID_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORYGuid { 0x769A796D, 0xDAB4, 0xA3F6, { 0xE2, 0x4D, 0xB2, 0x8A, 0xAC, 0xF3, 0x1C, 0xD1} }
GUID_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY = GUID(
    0x769A796D, 0xDAB4, 0xA3F6, (0xE2, 0x4D, 0xB2, 0x8A, 0xAC, 0xF3, 0x1C, 0xD1)
)
# Latency Monitor Log Page GUID is defined in spec as byte stream: 0x85D45E58D4E643709C6C84D08CC07A92
# which is converted to GUID format as: {8CC07A92-84D0-9C6C-7043-E6D4585ED485}
# define GUID_OCP_DEVICE_LATENCY_MONITORGuid { 0x8CC07A92, 0x84D0, 0x9C6C, { 0x70, 0x43, 0xE6, 0xD4, 0x58, 0x5E, 0xD4, 0x85} }
GUID_OCP_DEVICE_LATENCY_MONITOR = GUID(0x8CC07A92, 0x84D0, 0x9C6C, (0x70, 0x43, 0xE6, 0xD4, 0x58, 0x5E, 0xD4, 0x85))
# Device Capabilities Log Page GUID is defined in spec as byte stream: 0xB7053C914B58495D98C9E1D10D054297
# which is converted to GUID format as: {0D054297-E1D1-98C9-5D49-584B913C05B7}
# define GUID_OCP_DEVICE_DEVICE_CAPABILITIESGuid { 0x0D054297, 0xE1D1, 0x98C9, { 0x5D, 0x49, 0x58, 0x4B, 0x91, 0x3C, 0x05, 0xB7} }
GUID_OCP_DEVICE_DEVICE_CAPABILITIES = GUID(0x0D054297, 0xE1D1, 0x98C9, (0x5D, 0x49, 0x58, 0x4B, 0x91, 0x3C, 0x05, 0xB7))
# Unsupported Requirements Log Page GUID is defined in spec as byte stream: 0xC7BB98B7D0324863BB2C23990E9C722F
# which is converted to GUID format as: {0E9C722F-2399-BB2C-6348-32D0B798BBC7}
# define GUID_OCP_DEVICE_UNSUPPORTED_REQUIREMENTSGuid { 0x0E9C722F, 0x2399, 0xBB2C, { 0x63, 0x48, 0x32, 0xD0, 0xB7, 0x98, 0xBB, 0xC7} }
GUID_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS = GUID(
    0x0E9C722F, 0x2399, 0xBB2C, (0x63, 0x48, 0x32, 0xD0, 0xB7, 0x98, 0xBB, 0xC7)
)
# TCG Configuration Log Page GUID is defined in spec as byte stream: 0x54E02A9DFA5447C083E6E07EBD244006
# which is converted to GUID format as: {BD244006-E07E-83E6-C047-54FA9D2AE054}
# define GUID_OCP_DEVICE_TCG_CONFIGURATIONGuid { 0xBD244006, 0xE07E, 0x83E6, { 0xC0, 0x47, 0x54, 0xFA, 0x9D, 0x2A, 0xE0, 0x54} }
GUID_OCP_DEVICE_TCG_CONFIGURATION = GUID(0xBD244006, 0xE07E, 0x83E6, (0xC0, 0x47, 0x54, 0xFA, 0x9D, 0x2A, 0xE0, 0x54))
# TCG History Log Page GUID is defined in spec as byte stream: 0x88D7909696D04E27949009C6704b513E
# which is converted to GUID format as: {704B513E-09C6-9490-274E-D0969690D788}
# define GUID_OCP_DEVICE_TCG_HISTORYGuid { 0x704B513E, 0x09C6, 0x9490, { 0x27, 0x4E, 0xD0, 0x96, 0x96, 0x90, 0xD7, 0x88} }
GUID_OCP_DEVICE_TCG_HISTORY = GUID(0x704B513E, 0x09C6, 0x9490, (0x27, 0x4E, 0xD0, 0x96, 0x96, 0x90, 0xD7, 0x88))
# MFND child controller event Log Page GUID is defined in spec as byte stream: 0x9C669D257FD944A5BF35A5F098BCCE18
# which is converted to GUID format as: {98BCCE18-A5F0-BF35-A544-D97F259D669C}
# define GUID_MFND_CHILD_CONTROLLER_EVENT_LOG_PAGEGuid { 0x98BCCE18, 0xA5F0, 0xBF35, {0xA5, 0x44, 0xD9, 0x7F, 0x25, 0x9D, 0x66, 0x9C} }
GUID_MFND_CHILD_CONTROLLER_EVENT_LOG_PAGE = GUID(
    0x98BCCE18, 0xA5F0, 0xBF35, (0xA5, 0x44, 0xD9, 0x7F, 0x25, 0x9D, 0x66, 0x9C)
)


# Notice Status: NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC
class NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_CODES(CEnum):
    NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_RESERVED = 0
    NVME_ASYNC_EVENT_TYPE_VENDOR_SPECIFIC_DEVICE_PANIC = 1


# Device recommended reset action on firmware assert for Windows Cloud Server Devices
class NVME_WCS_DEVICE_RESET_ACTION(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("ControllerReset", UCHAR, 1),
                                ("NVMeSubsystemReset", UCHAR, 1),
                                ("PCIeFLR", UCHAR, 1),
                                ("PERST", UCHAR, 1),
                                ("PowerCycle", UCHAR, 1),
                                ("PCIeConventionalHotReset", UCHAR, 1),
                                ("Reserved", UCHAR, 2),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUCHAR", UCHAR),
                ],
                _pack_,
            ),
        ),
    ]


PNVME_WCS_DEVICE_RESET_ACTION = POINTER(NVME_WCS_DEVICE_RESET_ACTION)


# Windows Cloud Server device capabilities
class NVME_WCS_DEVICE_CAPABILITIES(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("PanicAEN", ULONG, 1),
                                ("PanicCFS", ULONG, 1),
                                ("Reserved", ULONG, 30),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsULONG", ULONG),
                ],
                _pack_,
            ),
        ),
    ]


PNVME_WCS_DEVICE_CAPABILITIES = POINTER(NVME_WCS_DEVICE_CAPABILITIES)


# Device recovery action on device panic
class NVME_WCS_DEVICE_RECOVERY_ACTION1(CEnum):
    NVMeDeviceRecoveryNoAction = 0  # Requires no action
    NVMeDeviceRecoveryFormatNVM = 1  # Requires Format NVM
    NVMeDeviceRecoveryVendorSpecificCommand = 2  # Requires Vendor Specific Command
    NVMeDeviceRecoveryVendorAnalysis = 3  # Requires Vendor Analysis
    NVMeDeviceRecoveryDeviceReplacement = 4  # Requires Device Replacement
    NVMeDeviceRecoverySanitize = 5  # Requires Sanitize
    NVMeDeviceRecovery1Max = 15  # Not an actual action, denotes max action.


PNVME_WCS_DEVICE_RECOVERY_ACTION1 = POINTER(NVME_WCS_DEVICE_RECOVERY_ACTION1)


class NVME_WCS_DEVICE_RECOVERY_ACTION2(CEnum):
    NVMeDeviceRecoveryControllerReset = 0  # Requires controller reset
    NVMeDeviceRecoverySubsystemReset = 1  # Requires NVM subsystem reset
    NVMeDeviceRecoveryPcieFunctionReset = 2  # Requires PCIe Function Level Reset
    NVMeDeviceRecoveryPERST = 3  # Requires PERST#
    NVMeDeviceRecoveryPowerCycle = 4  # Requires Main Power Cycle
    NVMeDeviceRecoveryPcieHotReset = 5  # Requires PCIe Conventional Hot Reset
    NVMeDeviceRecovery2Max = 15  # Not an actual action, denotes max action.


PNVME_WCS_DEVICE_RECOVERY_ACTION2 = POINTER(NVME_WCS_DEVICE_RECOVERY_ACTION2)

_pack_ += 1

# Log page definition of NVME_LOG_PAGE_WCS_DEVICE_SMART_ATTRIBUTES/NVME_LOG_PAGE_OCP_DEVICE_SMART_INFORMATION. Size 512 bytes

# Version independent structure to perform basic validation


class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("VersionSpecificData", UCHAR * 494),
        ("LogPageVersionNumber", USHORT),
        ("LogPageGUID", GUID),  # Shall be set to GUID_WCS_DEVICE_SMART_ATTRIBUTES / GUID_OCP_DEVICE_SMART_INFORMATION
    ]


PNVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG = POINTER(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG)

assert sizeof(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG) == 512
# Version 2

NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_VERSION_2 = 0x0002


class NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("MediaUnitsWritten", UCHAR * 16),
        ("MediaUnitsRead", UCHAR * 16),
        (
            "BadUserNANDBlockCount",
            make_struct(
                [
                    ("RawCount", UCHAR * 6),
                    ("Normalized", UCHAR * 2),
                ],
                _pack_,
            ),
        ),
        (
            "BadSystemNANDBlockCount",
            make_struct(
                [
                    ("RawCount", UCHAR * 6),
                    ("Normalized", UCHAR * 2),
                ],
                _pack_,
            ),
        ),
        ("XORRecoveryCount", ULONGLONG),
        ("UnrecoverableReadErrorCount", ULONGLONG),
        ("SoftECCErrorCount", ULONGLONG),
        (
            "EndToEndCorrectionCounts",
            make_struct(
                [
                    ("DetectedCounts", ULONG),
                    ("CorrectedCounts", ULONG),
                ],
                _pack_,
            ),
        ),
        ("PercentageSystemDataUsed", UCHAR),
        ("RefreshCount", UCHAR * 7),
        (
            "UserDataEraseCounts",
            make_struct(
                [
                    ("MaximumCount", ULONG),
                    ("MinimumCount", ULONG),
                ],
                _pack_,
            ),
        ),
        (
            "ThermalThrottling",
            make_struct(
                [
                    ("EventCount", UCHAR),
                    ("Status", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("Reserved0", UCHAR * 6),
        ("PCIeCorrectableErrorCount", ULONGLONG),
        ("IncompleteShutdownCount", ULONG),
        ("Reserved1", ULONG),
        ("PercentageFreeBlocks", UCHAR),
        ("Reserved2", UCHAR * 7),
        ("CapacitorHealth", USHORT),
        ("Reserved3", UCHAR * 6),
        ("UnalignedIOCount", ULONGLONG),
        ("SecurityVersionNumber", ULONGLONG),
        ("NUSE", ULONGLONG),
        ("PLPStartCount", UCHAR * 16),
        ("EnduranceEstimate", UCHAR * 16),
        ("Reserved4", UCHAR * 302),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_VERSION_2
        ("LogPageGUID", GUID),  # Shall be set to GUID_WCS_DEVICE_SMART_ATTRIBUTES
    ]


PNVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2 = POINTER(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2)

assert sizeof(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG_V2) == sizeof(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG)
# Version 3

NVME_OCP_DEVICE_SMART_INFORMATION_LOG_VERSION_3 = 0x0003


class NVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("MediaUnitsWritten", UCHAR * 16),
        ("MediaUnitsRead", UCHAR * 16),
        (
            "BadUserNANDBlockCount",
            make_struct(
                [
                    ("RawCount", UCHAR * 6),
                    ("Normalized", UCHAR * 2),
                ],
                _pack_,
            ),
        ),
        (
            "BadSystemNANDBlockCount",
            make_struct(
                [
                    ("RawCount", UCHAR * 6),
                    ("Normalized", UCHAR * 2),
                ],
                _pack_,
            ),
        ),
        ("XORRecoveryCount", ULONGLONG),
        ("UnrecoverableReadErrorCount", ULONGLONG),
        ("SoftECCErrorCount", ULONGLONG),
        (
            "EndToEndCorrectionCounts",
            make_struct(
                [
                    ("DetectedCounts", ULONG),
                    ("CorrectedCounts", ULONG),
                ],
                _pack_,
            ),
        ),
        ("PercentageSystemDataUsed", UCHAR),
        ("RefreshCount", UCHAR * 7),
        (
            "UserDataEraseCounts",
            make_struct(
                [
                    ("MaximumCount", ULONG),
                    ("MinimumCount", ULONG),
                ],
                _pack_,
            ),
        ),
        (
            "ThermalThrottling",
            make_struct(
                [
                    ("EventCount", UCHAR),
                    ("Status", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("DSSDSpecVersion", UCHAR * 6),
        ("PCIeCorrectableErrorCount", ULONGLONG),
        ("IncompleteShutdownCount", ULONG),
        ("Reserved1", ULONG),
        ("PercentageFreeBlocks", UCHAR),
        ("Reserved2", UCHAR * 7),
        ("CapacitorHealth", USHORT),
        ("NvmeErrata", UCHAR),
        ("Reserved3", UCHAR * 5),
        ("UnalignedIOCount", ULONGLONG),
        ("SecurityVersionNumber", ULONGLONG),
        ("NUSE", ULONGLONG),
        ("PLPStartCount", UCHAR * 16),
        ("EnduranceEstimate", UCHAR * 16),
        ("PCIeLinkRetrainingCount", ULONGLONG),
        ("PowerStateChangeCount", ULONGLONG),
        ("Reserved4", UCHAR * 286),
        ("LogPageVersionNumber", USHORT),
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_SMART_INFORMATION
    ]


PNVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3 = POINTER(NVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3)

assert sizeof(NVME_OCP_DEVICE_SMART_INFORMATION_LOG_V3) == sizeof(NVME_WCS_DEVICE_SMART_ATTRIBUTES_LOG)

# Log page definition of NVME_LOG_PAGE_WCS_DEVICE_ERROR_RECOVERY. Size 512 bytes

# Version independent structure to perform basic validation


class NVME_WCS_DEVICE_ERROR_RECOVERY_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        # Amount of time to wait for device panic workflow to complete in msec. Delay the reset accordingly
        ("PanicResetWaitTime", USHORT),
        # Reset actions on firmware assert, multiple options could be set
        ("PanicResetAction", NVME_WCS_DEVICE_RESET_ACTION),
        # Recovery action for device panic condition
        ("DriveRecoveryAction", UCHAR),
        # Id to identify the panic condition
        ("PanicId", ULONGLONG),
        # Device capabilities
        ("DeviceCapabilities", NVME_WCS_DEVICE_CAPABILITIES),
        # Vendor specific command opcode to recover device from panic condition
        ("VendorSpecificRecoveryCode", UCHAR),
        ("Reserved0", UCHAR * 3),
        # CDW12 value for the Vendor Specific command to recover device from panic condition
        ("VendorSpecificCommandCDW12", ULONG),
        # CDW13 value for the Vendor Specific command to recover device from panic condition
        ("VendorSpecificCommandCDW13", ULONG),
        ("Reserved1", UCHAR * 466),
        ("LogPageVersionNumber", USHORT),
        ("LogPageGUID", GUID),  # Shall be set to GUID_WCS_DEVICE_ERROR_RECOVERY / GUID_OCP_DEVICE_ERROR_RECOVERY
    ]


PNVME_WCS_DEVICE_ERROR_RECOVERY_LOG = POINTER(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG)

assert sizeof(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG) == 512
# Version 1

NVME_WCS_DEVICE_ERROR_RECOVERY_LOG_VERSION_1 = 0x0001

NVME_WCS_DEVICE_ERROR_RECOVERY_LOG_V1 = NVME_WCS_DEVICE_ERROR_RECOVERY_LOG
PNVME_WCS_DEVICE_ERROR_RECOVERY_LOG_V1 = POINTER(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG)

assert sizeof(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG_V1) == sizeof(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG)
# Version 2

NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_VERSION_2 = 0x0002


class NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2(Structure):
    _pack_ = _pack_
    _fields_ = [
        # Amount of time to wait for device panic workflow to complete in msec. Delay the reset accordingly
        ("PanicResetWaitTime", USHORT),
        # Reset actions on firmware assert, multiple options could be set
        ("PanicResetAction", NVME_WCS_DEVICE_RESET_ACTION),
        # Recovery action for device panic condition
        ("DeviceRecoveryAction1", UCHAR),
        # Id to identify the panic condition
        ("PanicId", ULONGLONG),
        # Device capabilities
        ("DeviceCapabilities", NVME_WCS_DEVICE_CAPABILITIES),
        # Vendor specific command opcode to recover device from panic condition
        ("VendorSpecificRecoveryCode", UCHAR),
        ("Reserved0", UCHAR * 3),
        # CDW12 value for the Vendor Specific command to recover device from panic condition
        ("VendorSpecificCommandCDW12", ULONG),
        # CDW13 value for the Vendor Specific command to recover device from panic condition
        ("VendorSpecificCommandCDW13", ULONG),
        ("VendorSpecificCommandTimeout", UCHAR),
        ("DeviceRecoveryAction2", UCHAR),
        ("DeviceRecoveryAction2Timeout", UCHAR),
        ("Reserved1", UCHAR * 463),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_VERSION_2
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_ERROR_RECOVERY
    ]


PNVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2 = POINTER(NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2)

assert sizeof(NVME_OCP_DEVICE_ERROR_RECOVERY_LOG_V2) == sizeof(NVME_WCS_DEVICE_ERROR_RECOVERY_LOG)
# Log page definition of NVME_LOG_PAGE_OCP_FIRMWARE_ACTIVATION_HISTORY. Size 4096 bytes

FIRMWARE_ACTIVATION_HISTORY_ENTRY_VERSION_1 = 0x01


class FIRMWARE_ACTIVATION_HISTORY_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("VersionNumber", UCHAR),
        ("Length", UCHAR),
        ("Reserved0", USHORT),
        ("ActivationCount", USHORT),
        ("Timestamp", ULONGLONG),
        ("Reserved1", ULONGLONG),
        ("PowerCycleCount", ULONGLONG),
        ("PreviousFirmware", ULONGLONG),
        ("NewFirmware", ULONGLONG),
        ("SlotNumber", UCHAR),
        ("CommitActionType", UCHAR),
        ("Result", USHORT),
        ("Reserved2", UCHAR * 14),
    ]


PFIRMWARE_ACTIVATION_HISTORY_ENTRY = POINTER(FIRMWARE_ACTIVATION_HISTORY_ENTRY)

assert sizeof(FIRMWARE_ACTIVATION_HISTORY_ENTRY) == 64
NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LID", UCHAR),  # Shall be set to NVME_LOG_PAGE_OCP_FIRMWARE_ACTIVATION_HISTORY
        ("Reserved0", UCHAR * 3),
        ("ValidNumberOfEntries", ULONG),
        ("Entries", FIRMWARE_ACTIVATION_HISTORY_ENTRY * 20),
        ("Reserved1", UCHAR * 2790),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY
    ]


PNVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG = POINTER(NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG)

assert sizeof(NVME_OCP_DEVICE_FIRMWARE_ACTIVATION_HISTORY_LOG) == 4096

# Log page definition of NVME_LOG_PAGE_OCP_LATENCY_MONITOR. Size 512 bytes


class LATENCY_MONITOR_FEATURE_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("FeatureEnabled", UCHAR, 1),
                                ("ActiveLatencyMode", UCHAR, 1),
                                ("ActiveMeasuredLatency", UCHAR, 1),
                                ("Reserved", UCHAR, 5),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUchar", UCHAR),
                ],
                _pack_,
            ),
        ),
    ]


PLATENCY_MONITOR_FEATURE_STATUS = POINTER(LATENCY_MONITOR_FEATURE_STATUS)


class ACTIVE_LATENCY_CONFIGURATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_union",
            make_union(
                [
                    (
                        "_unnamed_struct",
                        make_struct(
                            [
                                ("Read0", USHORT, 1),
                                ("Write0", USHORT, 1),
                                ("Trim0", USHORT, 1),
                                ("Read1", USHORT, 1),
                                ("Write1", USHORT, 1),
                                ("Trim1", USHORT, 1),
                                ("Read2", USHORT, 1),
                                ("Write2", USHORT, 1),
                                ("Trim2", USHORT, 1),
                                ("Read3", USHORT, 1),
                                ("Write3", USHORT, 1),
                                ("Trim3", USHORT, 1),
                                ("Reserved", USHORT, 4),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
    ]


PACTIVE_LATENCY_CONFIGURATION = POINTER(ACTIVE_LATENCY_CONFIGURATION)


class BUCKET_COUNTER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", ULONG),
        ("Trim", ULONG),
        ("Write", ULONG),
        ("Read", ULONG),
    ]


PBUCKET_COUNTER = POINTER(BUCKET_COUNTER)

assert sizeof(BUCKET_COUNTER) == 16


class LATENCY_STAMP(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Trim3", ULONGLONG),
        ("Write3", ULONGLONG),
        ("Read3", ULONGLONG),
        ("Trim2", ULONGLONG),
        ("Write2", ULONGLONG),
        ("Read2", ULONGLONG),
        ("Trim1", ULONGLONG),
        ("Write1", ULONGLONG),
        ("Read1", ULONGLONG),
        ("Trim0", ULONGLONG),
        ("Write0", ULONGLONG),
        ("Read0", ULONGLONG),
    ]


PLATENCY_STAMP = POINTER(LATENCY_STAMP)

assert sizeof(LATENCY_STAMP) == 96


class MEASURED_LATENCY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Trim3", USHORT),
        ("Write3", USHORT),
        ("Read3", USHORT),
        ("Trim2", USHORT),
        ("Write2", USHORT),
        ("Read2", USHORT),
        ("Trim1", USHORT),
        ("Write1", USHORT),
        ("Read1", USHORT),
        ("Trim0", USHORT),
        ("Write0", USHORT),
        ("Read0", USHORT),
    ]


PMEASURED_LATENCY = POINTER(MEASURED_LATENCY)

assert sizeof(MEASURED_LATENCY) == 24


class LATENCY_STAMP_UNITS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Read0", USHORT, 1),
        ("Write0", USHORT, 1),
        ("Trim0", USHORT, 1),
        ("Read1", USHORT, 1),
        ("Write1", USHORT, 1),
        ("Trim1", USHORT, 1),
        ("Read2", USHORT, 1),
        ("Write2", USHORT, 1),
        ("Trim2", USHORT, 1),
        ("Read3", USHORT, 1),
        ("Write3", USHORT, 1),
        ("Trim3", USHORT, 1),
        ("Reserved", USHORT, 4),
    ]


PLATENCY_STAMP_UNITS = POINTER(LATENCY_STAMP_UNITS)

assert sizeof(LATENCY_STAMP_UNITS) == 2


class DEBUG_BIT_FIELD(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Read0", USHORT, 1),
        ("Write0", USHORT, 1),
        ("Trim0", USHORT, 1),
        ("Read1", USHORT, 1),
        ("Write1", USHORT, 1),
        ("Trim1", USHORT, 1),
        ("Read2", USHORT, 1),
        ("Write2", USHORT, 1),
        ("Trim2", USHORT, 1),
        ("Read3", USHORT, 1),
        ("Write3", USHORT, 1),
        ("Trim3", USHORT, 1),
        ("Reserved", USHORT, 4),
    ]


PDEBUG_BIT_FIELD = POINTER(DEBUG_BIT_FIELD)

assert sizeof(DEBUG_BIT_FIELD) == 2
NVME_OCP_DEVICE_LATENCY_MONITOR_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_LATENCY_MONITOR_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("FeatureStatus", LATENCY_MONITOR_FEATURE_STATUS),
        ("Reserved0", UCHAR),
        ("ActiveBucketTimer", USHORT),
        ("ActiveBucketTimerThreshold", USHORT),
        ("ActiveThresholdA", UCHAR),
        ("ActiveThresholdB", UCHAR),
        ("ActiveThresholdC", UCHAR),
        ("ActiveThresholdD", UCHAR),
        ("ActiveLatencyConfig", ACTIVE_LATENCY_CONFIGURATION),
        ("ActiveLatencyMinimumWindow", UCHAR),
        ("Reserved1", UCHAR * 19),
        ("ActiveBucketCounter0", BUCKET_COUNTER),
        ("ActiveBucketCounter1", BUCKET_COUNTER),
        ("ActiveBucketCounter2", BUCKET_COUNTER),
        ("ActiveBucketCounter3", BUCKET_COUNTER),
        ("ActiveLatencyStamp", LATENCY_STAMP),
        ("ActiveMeasuredLatency", MEASURED_LATENCY),
        ("ActiveLatencyStampUnits", LATENCY_STAMP_UNITS),
        ("Reserved2", UCHAR * 22),
        ("StaticBucketCounter0", BUCKET_COUNTER),
        ("StaticBucketCounter1", BUCKET_COUNTER),
        ("StaticBucketCounter2", BUCKET_COUNTER),
        ("StaticBucketCounter3", BUCKET_COUNTER),
        ("StaticLatencyStamp", LATENCY_STAMP),
        ("StaticMeasuredLatency", MEASURED_LATENCY),
        ("StaticLatencyStampUnits", LATENCY_STAMP_UNITS),
        ("Reserved3", UCHAR * 22),
        ("DebugLogTriggerEnable", DEBUG_BIT_FIELD),
        ("DebugLogMeasuredLatency", USHORT),
        ("DebugLogLatencyStamp", ULONGLONG),
        ("DebugLogPointer", USHORT),
        ("DebugCounterTriggerSource", DEBUG_BIT_FIELD),
        (
            "DebugLogStampUnits",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("BasedOnTimestamp", UCHAR, 1),
                                ("Reserved", UCHAR, 7),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUchar", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("Reserved4", UCHAR * 29),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_LATENCY_MONITOR_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_LATENCY_MONITOR
    ]


PNVME_OCP_DEVICE_LATENCY_MONITOR_LOG = POINTER(NVME_OCP_DEVICE_LATENCY_MONITOR_LOG)

assert sizeof(NVME_OCP_DEVICE_LATENCY_MONITOR_LOG) == 512

# Log page definition of NVME_LOG_PAGE_OCP_DEVICE_CAPABILITIES. Size 4096 bytes


class DSSD_POWER_STATE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NvmePowerState", UCHAR, 5),
        ("Reserved", UCHAR, 2),
        ("ValidDSSDPowerState", UCHAR, 1),
    ]


PDSSD_POWER_STATE_DESCRIPTOR = POINTER(DSSD_POWER_STATE_DESCRIPTOR)

assert sizeof(DSSD_POWER_STATE_DESCRIPTOR) == 1
NVME_OCP_DEVICE_CAPABILITIES_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_CAPABILITIES_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PciePorts", USHORT),
        (
            "OobMgmtSupport",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("MctpOverSMBusSupported", USHORT, 1),
                                ("MctpOverPcieVDMSupported", USHORT, 1),
                                ("BasicMgmtCommandSupported", USHORT, 1),
                                ("Reserved", USHORT, 12),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "WriteZeroesCommand",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("Supported", USHORT, 1),
                                ("DEACBitSupported", USHORT, 1),
                                ("FUABitSupported", USHORT, 1),
                                ("NvmeIo5Met", USHORT, 1),
                                ("NvmeIo6Met", USHORT, 1),
                                ("Reserved", USHORT, 10),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "SanitizeCommand",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("Supported", USHORT, 1),
                                ("CryptoEraseSupported", USHORT, 1),
                                ("BlockEraseSupported", USHORT, 1),
                                ("OverwriteSupported", USHORT, 1),
                                ("DeallocateLbaSupported", USHORT, 1),
                                ("Reserved", USHORT, 10),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "DatasetMgmtCommand",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("Supported", USHORT, 1),
                                ("AttribDeallocateSupported", USHORT, 1),
                                ("Reserved", USHORT, 13),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "WriteUncorrectableCommand",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("Supported", USHORT, 1),
                                ("SingleLBASupported", USHORT, 1),
                                ("MaxLBASupported", USHORT, 1),
                                ("NvmeIo14Met", USHORT, 1),
                                ("Reserved", USHORT, 11),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        (
            "FusedCommand",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("CWFusedSupported", USHORT, 1),
                                ("Reserved", USHORT, 14),
                                ("CompliesWithSpec", USHORT, 1),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUshort", USHORT),
                ],
                _pack_,
            ),
        ),
        ("MinimumValidDSSDPowerState", USHORT),
        ("Reserved0", UCHAR),
        ("DssdDescriptors", DSSD_POWER_STATE_DESCRIPTOR * 127),
        ("Reserved1", UCHAR * 3934),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_CAPABILITIES_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_DEVICE_CAPABILITIES
    ]


PNVME_OCP_DEVICE_CAPABILITIES_LOG = POINTER(NVME_OCP_DEVICE_CAPABILITIES_LOG)

assert sizeof(NVME_OCP_DEVICE_CAPABILITIES_LOG) == 4096

# Log page definition of NVME_LOG_PAGE_OCP_UNSUPPORTED_REQUIREMENTS. Size 4096 bytes


class UNSUPPORTED_REQUIREMENT(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ReqId", UCHAR * 16),  # Zero padded ASCII string of the requirement id not supported
    ]


PUNSUPPORTED_REQUIREMENT = POINTER(UNSUPPORTED_REQUIREMENT)

NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("UnsupportedCount", USHORT),
        ("Reserved0", UCHAR * 14),
        ("UnsupportedReqList", UNSUPPORTED_REQUIREMENT * 253),
        ("Reserved1", UCHAR * 14),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS
    ]


PNVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG = POINTER(NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG)

assert sizeof(NVME_OCP_DEVICE_UNSUPPORTED_REQUIREMENTS_LOG) == 4096
# Log page definition of NVME_LOG_PAGE_OCP_TCG_CONFIGURATION. Size 512 bytes

NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "State",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                ("CPINSIDValue", UCHAR, 1),
                                ("CPINSIDBlocked", UCHAR, 1),
                                ("LockingEnabled", UCHAR, 1),
                                ("SUMOwner", UCHAR, 1),
                                ("Reserved", UCHAR, 4),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUchar", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("Reserved0", UCHAR * 3),
        # Locking SP Activation count
        ("LSPActivationCount", UCHAR),
        # TPer Revert count
        ("TPRevertCount", UCHAR),
        # Locking SP Revert count
        ("LSPRevertCount", UCHAR),
        # Locking Object Count in Locking Table
        ("LOCount", UCHAR),
        # Single User Mode Locking Object count
        ("SUMLOCount", UCHAR),
        # Range Provisioned Locking Object count
        ("RPLOCount", UCHAR),
        # Namespace Provisioned Locking Object count
        ("NPLOCount", UCHAR),
        # Read Locked Locking Object count
        ("RLLOCount", UCHAR),
        # Write Locked Locking Object count
        ("WLLOCount", UCHAR),
        # Read Unlocked Locking Object count
        ("RULOCount", UCHAR),
        # Write Unlocked Locking Object count
        ("WULOCount", UCHAR),
        ("Reserved1", UCHAR),
        # SID Authentication Try (failed) count
        ("SIDAuthTryCount", ULONG),
        # SID Authentication Try (failed) limit
        ("SIDAuthTryLimit", ULONG),
        # Programmatic TCG Reset count
        ("ResetCount", ULONG),
        # Count of Locking Objects transitioned to locked state
        # due to Programmatic TCG Reset
        ("ResetLockCount", ULONG),
        ("Reserved2", UCHAR * 462),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_TCG_CONFIGURATION
    ]


PNVME_OCP_DEVICE_TCG_CONFIGURATION_LOG = POINTER(NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG)

assert sizeof(NVME_OCP_DEVICE_TCG_CONFIGURATION_LOG) == 512
# Log page definition of NVME_LOG_PAGE_OCP_TCG_HISTORY. Size 4096 bytes

TCG_HISTORY_ENTRY_VERSION_1 = 0x01


class TCG_HISTORY_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("VersionNumber", UCHAR),
        ("EntryLength", UCHAR),
        ("PowerCycleCount", USHORT),
        ("TcgCommandCount", ULONG),
        ("TcgCommandCompletionTS", ULONGLONG),
        ("InvokingId", ULONGLONG),
        ("MethodId", ULONGLONG),
        ("ComId", USHORT),
        ("ProtocolId", UCHAR),
        ("TcgStatus", UCHAR),
        ("ProcessTime", USHORT),
        ("CommandSpecific", UCHAR * 10),
    ]


PTCG_HISTORY_ENTRY = POINTER(TCG_HISTORY_ENTRY)

assert sizeof(TCG_HISTORY_ENTRY) == 48


class TCG_AUTH_METHOD_SPECIFIC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("AuthorityId", ULONGLONG),
        ("TriesCount", UCHAR),
    ]


PTCG_AUTH_METHOD_SPECIFIC = POINTER(TCG_AUTH_METHOD_SPECIFIC)


class TCG_ACTIVATE_METHOD_SPECIFIC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("RangeStartLengthPolicy", UCHAR),
    ]


PTCG_ACTIVATE_METHOD_SPECIFIC = POINTER(TCG_ACTIVATE_METHOD_SPECIFIC)


class TCG_REACTIVATE_METHOD_SPECIFIC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("RangeStartLengthPolicy", UCHAR),
    ]


PTCG_REACTIVATE_METHOD_SPECIFIC = POINTER(TCG_REACTIVATE_METHOD_SPECIFIC)


class TCG_ASSIGN_METHOD_SPECIFIC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NamespaceId", ULONG),
    ]


PTCG_ASSIGN_METHOD_SPECIFIC = POINTER(TCG_ASSIGN_METHOD_SPECIFIC)


class TCG_BLOCKSID_METHOD_SPECIFIC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ClearEvents", UCHAR),
    ]


PTCG_BLOCKSID_METHOD_SPECIFIC = POINTER(TCG_BLOCKSID_METHOD_SPECIFIC)

NVME_OCP_DEVICE_TCG_HISTORY_LOG_VERSION_1 = 0x0001


class NVME_OCP_DEVICE_TCG_HISTORY_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LID", UCHAR),  # Shall be set to NVME_LOG_PAGE_OCP_TCG_HISTORY
        ("Reserved0", UCHAR * 3),
        ("HistoryEntryCount", ULONG),
        ("HistoryEntries", TCG_HISTORY_ENTRY * 84),
        ("Reserved1", UCHAR * 38),
        ("LogPageVersionNumber", USHORT),  # Shall be set to NVME_OCP_DEVICE_TCG_HISTORY_LOG_VERSION_1
        ("LogPageGUID", GUID),  # Shall be set to GUID_OCP_DEVICE_TCG_HISTORY
    ]


PNVME_OCP_DEVICE_TCG_HISTORY_LOG = POINTER(NVME_OCP_DEVICE_TCG_HISTORY_LOG)

assert sizeof(NVME_OCP_DEVICE_TCG_HISTORY_LOG) == 4096
_pack_ -= 1


# Parameters for NVME_ADMIN_COMMAND_CREATE_IO_CQ
class NVME_CDW10_CREATE_IO_QUEUE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("QID", ULONG, 16),  # Queue Identifier (QID)
                    ("QSIZE", ULONG, 16),  # Queue Size (QSIZE)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_CREATE_IO_CQ(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("PC", ULONG, 1),  # Physically Contiguous (PC)
                    ("IEN", ULONG, 1),  # Interrupts Enabled (IEN)
                    ("Reserved0", ULONG, 14),
                    ("IV", ULONG, 16),  # Interrupt Vector (IV)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for NVME_ADMIN_COMMAND_CREATE_IO_SQ
class NVME_NVM_QUEUE_PRIORITIES(CEnum):
    NVME_NVM_QUEUE_PRIORITY_URGENT = 0
    NVME_NVM_QUEUE_PRIORITY_HIGH = 1
    NVME_NVM_QUEUE_PRIORITY_MEDIUM = 2
    NVME_NVM_QUEUE_PRIORITY_LOW = 3


class NVME_CDW11_CREATE_IO_SQ(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("PC", ULONG, 1),  # Physically Contiguous (PC)
                    ("QPRIO", ULONG, 2),  # Queue Priority (QPRIO)
                    ("Reserved0", ULONG, 13),
                    ("CQID", ULONG, 16),  # Completion Queue Identifier (CQID)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Output and Parameters for NVME_ADMIN_COMMAND_GET_FEATURES or NVME_ADMIN_COMMAND_SET_FEATURES
class NVME_FEATURE_VALUE_CODES(CEnum):
    NVME_FEATURE_VALUE_CURRENT = 0
    NVME_FEATURE_VALUE_DEFAULT = 1
    NVME_FEATURE_VALUE_SAVED = 2
    NVME_FEATURE_VALUE_SUPPORTED_CAPABILITIES = 3


class NVME_CDW10_GET_FEATURES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("FID", ULONG, 8),  # Feature Identifier (FID)
                    (
                        "SEL",
                        ULONG,
                        3,
                    ),  # Select (SEL): This field specifies which value of the attributes to return in the provided data.
                    ("Reserved0", ULONG, 21),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW10_SET_FEATURES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("FID", ULONG, 8),  # Feature Identifier (FID)
                    ("Reserved0", ULONG, 23),
                    ("SV", ULONG, 1),  # Save (SV)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_NUMBER_OF_QUEUES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NSQ", ULONG, 16),  # Number of IO Submission Queues.
                    ("NCQ", ULONG, 16),  # Number of IO Completion Queues.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_INTERRUPT_COALESCING(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("THR", ULONG, 8),  # Aggregation Threshold (THR)
                    ("TIME", ULONG, 8),  # Aggregation Time (TIME)
                    ("Reserved0", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_INTERRUPT_VECTOR_CONFIG(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("IV", ULONG, 16),  # Interrupt Vector (IV)
                    ("CD", ULONG, 1),  # Coalescing Disabled (CD)
                    ("Reserved0", ULONG, 15),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_WRITE_ATOMICITY_NORMAL(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("DN", ULONG, 1),  # Disable Normal (DN)
                    ("Reserved0", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_NON_OPERATIONAL_POWER_STATE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NOPPME", ULONG, 1),  # Non-Operational Power State Permissive Mode Enable (NOPPME)
                    ("Reserved0", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_LBA_RANGE_TYPE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NUM", ULONG, 6),  # Number of LBA Ranges (NUM)
                    ("Reserved0", ULONG, 26),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_ARBITRATION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("AB", ULONG, 3),  # Arbitration Burst (AB)
                    ("Reserved0", ULONG, 5),
                    ("LPW", ULONG, 8),  # Low Priority Weight (LPW)
                    ("MPW", ULONG, 8),  # Medium Priority Weight (MPW)
                    ("HPW", ULONG, 8),  # High Priority Weight (HPW)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_VOLATILE_WRITE_CACHE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("WCE", ULONG, 1),  # Volatile Write Cache Enable (WCE)
                    ("Reserved0", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_SUPPORTED_CAPABILITY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("SAVE", ULONG, 1),  # Save supported
                    ("NSS", ULONG, 1),  # Namespace specific
                    ("MOD", ULONG, 1),  # Changeable
                    ("Reserved0", ULONG, 29),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_FEATURE_ASYNC_EVENT_CONFIG(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("CriticalWarnings", ULONG, 8),  # SMART / Health Critical Warnings
                    ("NsAttributeNotices", ULONG, 1),  # Namespace Attributes Notices
                    ("FwActivationNotices", ULONG, 1),  # Firmware Activation Notices
                    ("TelemetryLogNotices", ULONG, 1),  # Telemetry Log Notices
                    ("ANAChangeNotices", ULONG, 1),  # Asymmetric Namespace Access Change Notices
                    ("PredictableLogChangeNotices", ULONG, 1),  # Predictable Latency Event Aggregate Log Change Notices
                    ("LBAStatusNotices", ULONG, 1),  # LBA Status Information Notices
                    ("EnduranceEventNotices", ULONG, 1),  # Endurance Group Event Aggregate Log Change Notices
                    ("Reserved0", ULONG, 12),
                    ("ZoneDescriptorNotices", ULONG, 1),  # Zone Descriptor Changed Notices
                    ("Reserved1", ULONG, 4),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for NVME_FEATURE_POWER_MANAGEMENT
class NVME_CDW11_FEATURE_POWER_MANAGEMENT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("PS", ULONG, 5),  # Power State (PS)
                    ("Reserved0", ULONG, 27),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for NVME_FEATURE_AUTONOMOUS_POWER_STATE_TRANSITION
class NVME_CDW11_FEATURE_AUTO_POWER_STATE_TRANSITION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("APSTE", ULONG, 1),  # Autonomous Power State Transition Enable (APSTE)
                    ("Reserved0", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for NVME_FEATURE_AUTONOMOUS_POWER_STATE_TRANSITION
# There is an array of 32 of these (one for each power state) in the data buffer.
class NVME_AUTO_POWER_STATE_TRANSITION_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved0", ULONG, 3),  # Bits 0-2 are reserved.
        (
            "IdleTransitionPowerState",
            ULONG,
            5,
        ),  # Bits 3-7 - (ITPS) The non-operational power state for the controller to autonomously transition to after there is a continuous period of idle time in the current power state that exceeds time specified in the ITPT field.
        (
            "IdleTimePriorToTransition",
            ULONG,
            24,
        ),  # Bits 8-31 - (ITPT) The amount of idle time (in ms) that occurs in this power state prior to transitioning to the Idle Transition Power State.  A value of 0 disables APST for this power state.
        ("Reserved1", ULONG),  # Bits 32-63 are reserved.
    ]


# Parameter for NVME_FEATURE_TEMPERATURE_THRESHOLD


# Following definitions are used in "THSEL" field.
class NVME_TEMPERATURE_THRESHOLD_TYPES(CEnum):
    NVME_TEMPERATURE_OVER_THRESHOLD = 0
    NVME_TEMPERATURE_UNDER_THRESHOLD = 1


class NVME_CDW11_FEATURE_TEMPERATURE_THRESHOLD(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    (
                        "TMPTH",
                        ULONG,
                        16,
                    ),  # Temperature Threshold (TMPTH):  Indicates the threshold for the temperature of the overall device (controller and NVM included) in units of Kelvin.
                    ("TMPSEL", ULONG, 4),  # Threshold Temperature Select (TMPSEL)
                    ("THSEL", ULONG, 2),  # Threshold Type Select (THSEL)
                    ("Reserved0", ULONG, 10),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for NVME_FEATURE_ERROR_RECOVERY
class NVME_CDW11_FEATURE_ERROR_RECOVERY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("TLER", ULONG, 16),  # Time limited error recovery (TLER)
                    ("DULBE", ULONG, 1),  # Deallocated or unwritten logical block error enable (DULBE)
                    ("Reserved0", ULONG, 15),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for NVME_FEATURE_HOST_MEMORY_BUFFER
class NVME_CDW11_FEATURE_HOST_MEMORY_BUFFER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("EHM", ULONG, 1),  # Enable Host Memory (EHM) - Enables the host memory buffer.
                    (
                        "MR",
                        ULONG,
                        1,
                    ),  # Memory Return (MR) - Indicates if the host is returning previously allocated memory to the controller.
                    ("Reserved", ULONG, 30),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    (
                        "HSIZE",
                        ULONG,
                    ),  # Host Memory Buffer Size (HSIZE) - The size of the host memory buffer in memory page size (CC.MPS) units.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved", ULONG, 4),
                    (
                        "HMDLLA",
                        ULONG,
                        28,
                    ),  # Host Memory Descriptor List Lower Address (HMDLLA) - 16-byte aligned, lower 32 bits of the physical location of the Host Memory Descriptor List.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    (
                        "HMDLUA",
                        ULONG,
                    ),  # Host Memory Descriptor List Upper Address (HMDLLA) - Upper 32 bits of the physical location of the Host Memory Descriptor List.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    (
                        "HMDLEC",
                        ULONG,
                    ),  # Host Memory Descriptor List Entry Count (HMDLEC) - Number of entries in the Host Memory Descriptor List.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# This structure is a single entry in the host memory descriptor list.
class NVME_HOST_MEMORY_BUFFER_DESCRIPTOR_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "BADD",
            ULONGLONG,
        ),  # Buffer Address (BADD) - Physical host memory address aligned to the memory page size (CC.MPS)
        (
            "BSIZE",
            ULONG,
        ),  # Buffer Size (BSIZE) - The number of contiguous memory page size (CC.MPS) units for this entry.
        ("Reserved", ULONG),
    ]


# Parameters for NVME_FEATURE_IO_COMMAND_SET_PROFILE
class NVME_CDW11_FEATURE_IO_COMMAND_SET_PROFILE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("IOCSCI", ULONG, 8),  # I/O command Set Profile
                    ("Reserved", ULONG, 24),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for NVME_FEATURE_ENHANDED_CONTROLLER_METADATA, NVME_FEATURE_CONTROLLER_METADATA, NVME_FEATURE_NAMESPACE_METADATA
class NVME_CDW11_FEATURE_GET_HOST_METADATA(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("GDHM", ULONG, 1),  # Generate Default Host Metadata (GDHM)
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_HOST_METADATA_ELEMENT_ACTIONS(CEnum):
    NVME_HOST_METADATA_ADD_REPLACE_ENTRY = 0
    NVME_HOST_METADATA_DELETE_ENTRY_MULTIPLE = 1
    NVME_HOST_METADATA_ADD_ENTRY_MULTIPLE = 2


class NVME_CDW11_FEATURE_SET_HOST_METADATA(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 13),
                    ("EA", ULONG, 2),  # Element Action (EA), value defined in enum NVME_HOST_METADATA_ELEMENT_ACTIONS
                    ("Reserved1", ULONG, 17),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CONTROLLER_METADATA_ELEMENT_TYPES(CEnum):
    NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_CONTROLLER_NAME = 0x1
    NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_NAME = 0x2
    NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_VERSION = 0x3
    NVME_CONTROLLER_METADATA_PREBOOT_CONTROLLER_NAME = 0x4
    NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_NAME = 0x5
    NVME_CONTROLLER_METADATA_PREBOOT_DRIVER_VERSION = 0x6
    NVME_CONTROLLER_METADATA_SYSTEM_PROCESSOR_MODEL = 0x7
    NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_NAME = 0x8
    NVME_CONTROLLER_METADATA_CHIPSET_DRIVER_VERSION = 0x9
    NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_NAME_AND_BUILD = 0xA
    NVME_CONTROLLER_METADATA_SYSTEM_PRODUCT_NAME = 0xB
    NVME_CONTROLLER_METADATA_FIRMWARE_VERSION = 0xC
    NVME_CONTROLLER_METADATA_OPERATING_SYSTEM_DRIVER_FILENAME = 0xD
    NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_NAME = 0xE
    NVME_CONTROLLER_METADATA_DISPLAY_DRIVER_VERSION = 0xF
    NVME_CONTROLLER_METADATA_HOST_DETERMINED_FAILURE_RECORD = 0x10


class NVME_NAMESPACE_METADATA_ELEMENT_TYPES(CEnum):
    NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME = 0x1
    NVME_NAMESPACE_METADATA_PREBOOT_NAMESPACE_NAME = 0x2
    NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_1 = 0x3
    NVME_NAMESPACE_METADATA_OPERATING_SYSTEM_NAMESPACE_NAME_QUALIFIER_2 = 0x4


class NVME_HOST_METADATA_ELEMENT_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "ET",
            ULONG,
            6,
        ),  # Element Type (ET), value defined in enum NVME_CONTROLLER_METADATA_ELEMENT_TYPES, NVME_NAMESPACE_METADATA_ELEMENT_TYPES
        ("Reserved0", ULONG, 2),
        ("ER", ULONG, 4),  # Element Revision (ER)
        ("Reserved1", ULONG, 4),
        ("ELEN", ULONG, 16),  # Element Length (ELEN), element value length in bytes
        ("EVAL", UCHAR * ANYSIZE_ARRAY),  # Element Value (EVAL), UTF-8 string
    ]


class NVME_FEATURE_HOST_METADATA_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfMetadataElementDescriptors", UCHAR),
        ("Reserved0", UCHAR),
        ("MetadataElementDescriptors", UCHAR * 4094),  # Use NVME_HOST_METADATA_ELEMENT_DESCRIPTOR to access this list.
    ]


# Parameter for NVME_FEATURE_ERROR_INJECTION
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW11_FEATURE_ERROR_INJECTION(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NUM", ULONG, 7),  # Number of Error Injections.
                    ("Reserved0", ULONG, 25),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# DWORD 0 for get feature command (Error Injection) shares the same format with DWORD 11 for set feature command (Error Injection).
NVME_CDW0_FEATURE_ERROR_INJECTION = NVME_CDW11_FEATURE_ERROR_INJECTION
PNVME_CDW0_FEATURE_ERROR_INJECTION = POINTER(NVME_CDW11_FEATURE_ERROR_INJECTION)


class NVME_ERROR_INJECTION_ENTRY(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "Flags",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                (
                                    "Enable",
                                    UCHAR,
                                    1,
                                ),  # A value of 0 indicates error injection is not enabled. A value of 1 indicates error injection is enabled.
                                (
                                    "SingleInstance",
                                    UCHAR,
                                    1,
                                ),  # A value of 0 indicates error injection is enabled until disable.
                                # A value of 1 indicates a single instance error injection where a single error is injected.
                                # After a single instance error has been created, the value of the Enable field shall be 0 in the results from Get Features command.
                                ("Reserved0", UCHAR, 6),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUchar", UCHAR),
                ],
                _pack_,
            ),
        ),
        ("Reserved1", UCHAR),
        ("ErrorInjectionType", USHORT),  # Specifies the Type of Error Injection.
        ("ErrorInjectionTypeSpecific", UCHAR * 28),  # Error Injection Type specific definition.
    ]


# Definitions are used in "Error Injection Type" field.
class NVME_ERROR_INJECTION_TYPES(CEnum):
    NVME_ERROR_INJECTION_TYPE_RESERVED0 = 0
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_CPU_CONTROLLER_HANG = 1  # 0x1
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_HANG = 2  # 0x2
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_PLP_DEFECT = 3  # 0x3
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_LOGICAL_FW_ERROR = 4  # 0x4
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_CRITICAL = 5  # 0x5
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_DRAM_CORRUPTION_NONCRITICAL = 6  # 0x6
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_NAND_CORRUPTION = 7  # 0x7
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_SRAM_CORRUPTION = 8  # 0x8
    NVME_ERROR_INJECTION_TYPE_DEVICE_PANIC_HW_MALFUNCTION = 9  # 0x9

    NVME_ERROR_INJECTION_TYPE_RESERVED1 = 10  # 0xA

    NVME_ERROR_INJECTION_TYPE_MAX = 0xFFFF


# Parameter for set feature NVME_FEATURE_CLEAR_FW_UPDATE_HISTORY
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW11_FEATURE_CLEAR_FW_UPDATE_HISTORY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 31),
                    ("Clear", ULONG, 1),  # Clear Firmware Update History Log.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for set feature NVME_FEATURE_READONLY_WRITETHROUGH_MODE
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW11_FEATURE_READONLY_WRITETHROUGH_MODE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 30),
                    ("EOLBehavior", ULONG, 2),  # End of Life Behavior.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Output for get feature NVME_FEATURE_READONLY_WRITETHROUGH_MODE
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW0_FEATURE_READONLY_WRITETHROUGH_MODE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("EOLBehavior", ULONG, 3),  # End of Life Behavior.
                    ("Reserved0", ULONG, 29),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for set feature NVME_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW11_FEATURE_CLEAR_PCIE_CORRECTABLE_ERROR_COUNTERS(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 31),
                    ("Clear", ULONG, 1),  # Clear PCIe Error Counters.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameter for set feature NVME_FEATURE_ENABLE_IEEE1667_SILO
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW11_FEATURE_ENABLE_IEEE1667_SILO(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 31),
                    ("Enable", ULONG, 1),  # Enable IEEE1667 Silo.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Output for get feature NVME_FEATURE_ENABLE_IEEE1667_SILO
# This is from OCP NVMe Cloud SSD spec.
class NVME_CDW0_FEATURE_ENABLE_IEEE1667_SILO(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Enabled", ULONG, 3),  # IEEE1667 Silo Enabled.
                    ("Reserved0", ULONG, 29),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for NVME_FEATURE_NVM_HOST_IDENTIFIER
NVME_MAX_HOST_IDENTIFIER_SIZE = 16  # 16 Bytes, 128 Bits
NVME_HOST_IDENTIFIER_SIZE = 8  # 8 Bytes, 64 Bits
NVME_EXTENDED_HOST_IDENTIFIER_SIZE = 16  # 16 Bytes, 128 Bits


class NVME_CDW11_FEATURE_HOST_IDENTIFIER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("EXHID", ULONG, 1),  # Enable Extended Host Identifier (EXHID)
        ("Reserved", ULONG, 31),
    ]


class NVME_FEATURE_HOST_IDENTIFIER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("HOSTID", UCHAR * NVME_MAX_HOST_IDENTIFIER_SIZE),  # Host Identifier (HOSTID)
    ]


class NVME_CDW11_FEATURE_RESERVATION_PERSISTENCE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PTPL", ULONG, 1),  # Persist Through Power Loss (PTPL)
        ("Reserved", ULONG, 31),
    ]


class NVME_CDW11_FEATURE_RESERVATION_NOTIFICATION_MASK(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved", ULONG, 1),
        ("REGPRE", ULONG, 1),  # Mask Registration Preempted Notification (REGPRE)
        ("RESREL", ULONG, 1),  # Mask Reservation Released Notification (RESREL)
        ("RESPRE", ULONG, 1),  # Mast Reservation Preempted Notification (RESPRE)
        ("Reserved1", ULONG, 28),
    ]


class NVME_CDW11_FEATURES(Union):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfQueues", NVME_CDW11_FEATURE_NUMBER_OF_QUEUES),
        ("InterruptCoalescing", NVME_CDW11_FEATURE_INTERRUPT_COALESCING),
        ("InterruptVectorConfig", NVME_CDW11_FEATURE_INTERRUPT_VECTOR_CONFIG),
        ("LbaRangeType", NVME_CDW11_FEATURE_LBA_RANGE_TYPE),
        ("Arbitration", NVME_CDW11_FEATURE_ARBITRATION),
        ("VolatileWriteCache", NVME_CDW11_FEATURE_VOLATILE_WRITE_CACHE),
        ("AsyncEventConfig", NVME_CDW11_FEATURE_ASYNC_EVENT_CONFIG),
        ("PowerManagement", NVME_CDW11_FEATURE_POWER_MANAGEMENT),
        ("AutoPowerStateTransition", NVME_CDW11_FEATURE_AUTO_POWER_STATE_TRANSITION),
        ("TemperatureThreshold", NVME_CDW11_FEATURE_TEMPERATURE_THRESHOLD),
        ("ErrorRecovery", NVME_CDW11_FEATURE_ERROR_RECOVERY),
        ("HostMemoryBuffer", NVME_CDW11_FEATURE_HOST_MEMORY_BUFFER),
        ("WriteAtomicityNormal", NVME_CDW11_FEATURE_WRITE_ATOMICITY_NORMAL),
        ("NonOperationalPowerState", NVME_CDW11_FEATURE_NON_OPERATIONAL_POWER_STATE),
        ("IoCommandSetProfile", NVME_CDW11_FEATURE_IO_COMMAND_SET_PROFILE),
        ("ErrorInjection", NVME_CDW11_FEATURE_ERROR_INJECTION),
        ("HostIdentifier", NVME_CDW11_FEATURE_HOST_IDENTIFIER),
        ("ReservationPersistence", NVME_CDW11_FEATURE_RESERVATION_PERSISTENCE),
        ("ReservationNotificationMask", NVME_CDW11_FEATURE_RESERVATION_NOTIFICATION_MASK),
        ("GetHostMetadata", NVME_CDW11_FEATURE_GET_HOST_METADATA),
        ("SetHostMetadata", NVME_CDW11_FEATURE_SET_HOST_METADATA),
        ("AsUlong", ULONG),
    ]


class NVME_CDW12_FEATURES(Union):
    _pack_ = _pack_
    _fields_ = [
        ("HostMemoryBuffer", NVME_CDW12_FEATURE_HOST_MEMORY_BUFFER),
        ("AsUlong", ULONG),
    ]


class NVME_CDW13_FEATURES(Union):
    _pack_ = _pack_
    _fields_ = [
        ("HostMemoryBuffer", NVME_CDW13_FEATURE_HOST_MEMORY_BUFFER),
        ("AsUlong", ULONG),
    ]


class NVME_CDW14_FEATURES(Union):
    _pack_ = _pack_
    _fields_ = [
        ("HostMemoryBuffer", NVME_CDW14_FEATURE_HOST_MEMORY_BUFFER),
        ("AsUlong", ULONG),
    ]


class NVME_CDW15_FEATURES(Union):
    _pack_ = _pack_
    _fields_ = [
        ("HostMemoryBuffer", NVME_CDW15_FEATURE_HOST_MEMORY_BUFFER),
        ("AsUlong", ULONG),
    ]


# NVMe Maximum log size
NVME_MAX_LOG_SIZE = 0x1000


# Parameters for NVME_ADMIN_COMMAND_GET_LOG_PAGE Command
class NVME_LOG_PAGES(CEnum):
    NVME_LOG_PAGE_ERROR_INFO = 0x01
    NVME_LOG_PAGE_HEALTH_INFO = 0x02
    NVME_LOG_PAGE_FIRMWARE_SLOT_INFO = 0x03
    NVME_LOG_PAGE_CHANGED_NAMESPACE_LIST = 0x04
    NVME_LOG_PAGE_COMMAND_EFFECTS = 0x05
    NVME_LOG_PAGE_DEVICE_SELF_TEST = 0x06
    NVME_LOG_PAGE_TELEMETRY_HOST_INITIATED = 0x07
    NVME_LOG_PAGE_TELEMETRY_CTLR_INITIATED = 0x08
    NVME_LOG_PAGE_ENDURANCE_GROUP_INFORMATION = 0x09
    NVME_LOG_PAGE_PREDICTABLE_LATENCY_NVM_SET = 0x0A
    NVME_LOG_PAGE_PREDICTABLE_LATENCY_EVENT_AGGREGATE = 0x0B
    NVME_LOG_PAGE_ASYMMETRIC_NAMESPACE_ACCESS = 0x0C
    NVME_LOG_PAGE_PERSISTENT_EVENT_LOG = 0x0D
    NVME_LOG_PAGE_LBA_STATUS_INFORMATION = 0x0E
    NVME_LOG_PAGE_ENDURANCE_GROUP_EVENT_AGGREGATE = 0x0F

    NVME_LOG_PAGE_RESERVATION_NOTIFICATION = 0x80
    NVME_LOG_PAGE_SANITIZE_STATUS = 0x81

    NVME_LOG_PAGE_CHANGED_ZONE_LIST = 0xBF


# Get LOG PAGE format which confines to  < 1.3 NVMe Specification
#
class NVME_CDW10_GET_LOG_PAGE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("LID", ULONG, 8),  # Log Page Identifier (LID)
                    ("Reserved0", ULONG, 8),
                    ("NUMD", ULONG, 12),  # Number of Dwords (NUMD)
                    ("Reserved1", ULONG, 4),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Get LOG PAGE format which confines to  >= 1.3 NVMe Specification
#
class NVME_CDW10_GET_LOG_PAGE_V13(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("LID", ULONG, 8),  # Log Page Identifier (LID)
                    ("LSP", ULONG, 4),  # Log Specific Field (LSP)
                    ("Reserved0", ULONG, 3),
                    ("RAE", ULONG, 1),  # Retain Asynchronous Event (RAE)
                    ("NUMDL", ULONG, 16),  # Number of Lower Dwords (NUMDL)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_GET_LOG_PAGE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NUMDU", ULONG, 16),  # Number of Upper Dwords (NUMDU)
                    ("LogSpecificIdentifier", ULONG, 16),  # Log Specific Identifier
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW12_GET_LOG_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LPOL", ULONG),  # Log Page Offset Lower (LPOL)
    ]


class NVME_CDW13_GET_LOG_PAGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LPOU", ULONG),  # Log Page Offset Upper (LPOU)
    ]


class NVME_CDW14_GET_LOG_PAGE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("UUIDIndex", ULONG, 7),  # UUID Index
                    ("Reserved", ULONG, 17),
                    ("CommandSetIdentifier", ULONG, 8),  # Command Set Identifier
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Information of log: NVME_LOG_PAGE_ERROR_INFO. Size: 64 bytes
class NVME_ERROR_INFO_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ErrorCount", ULONGLONG),
        ("SQID", USHORT),  # Submission Queue ID
        ("CMDID", USHORT),  # Command ID
        (
            "Status",
            NVME_COMMAND_STATUS,
        ),  # Status Field: This field indicates the Status Field for the command  that completed.  The Status Field is located in bits 15:01, bit 00 corresponds to the Phase Tag posted for the command.
        (
            "ParameterErrorLocation",
            make_struct(
                [
                    ("Byte", USHORT, 8),  # Byte in command that contained the error.
                    ("Bit", USHORT, 3),  # Bit in command that contained the error.
                    ("Reserved", USHORT, 5),
                ],
                _pack_,
            ),
        ),
        (
            "Lba",
            ULONGLONG,
        ),  # LBA: This field indicates the first LBA that experienced the error condition, if applicable.
        (
            "NameSpace",
            ULONG,
        ),  # Namespace: This field indicates the namespace that the error is associated with, if applicable.
        ("VendorInfoAvailable", UCHAR),  # Vendor Specific Information Available
        ("Reserved0", UCHAR * 3),
        (
            "CommandSpecificInfo",
            ULONGLONG,
        ),  # This field contains command specific information. If used, the command definition specifies the information returned.
        ("Reserved1", UCHAR * 24),
    ]


# Information of log: NVME_LOG_PAGE_HEALTH_INFO. Size: 512 bytes
class NVME_HEALTH_INFO_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "CriticalWarning",
            make_union(
                [
                    (
                        "DUMMYSTRUCTNAME",
                        make_struct(
                            [
                                (
                                    "AvailableSpaceLow",
                                    UCHAR,
                                    1,
                                ),  # If set to 1, then the available spare space has fallen below the threshold.
                                (
                                    "TemperatureThreshold",
                                    UCHAR,
                                    1,
                                ),  # If set to 1, then a temperature is above an over temperature threshold or below an under temperature threshold.
                                (
                                    "ReliabilityDegraded",
                                    UCHAR,
                                    1,
                                ),  # If set to 1, then the device reliability has been degraded due to significant media related  errors or any internal error that degrades device reliability.
                                ("ReadOnly", UCHAR, 1),  # If set to 1, then the media has been placed in read only mode
                                (
                                    "VolatileMemoryBackupDeviceFailed",
                                    UCHAR,
                                    1,
                                ),  # If set to 1, then the volatile memory backup device has failed. This field is only valid if the controller has a volatile memory backup solution.
                                ("Reserved", UCHAR, 3),
                            ],
                            _pack_,
                        ),
                    ),
                    ("AsUchar", UCHAR),
                ],
                _pack_,
            ),
        ),  # This field indicates critical warnings for the state of the  controller. Each bit corresponds to a critical warning type; multiple bits may be set.
        (
            "Temperature",
            UCHAR * 2,
        ),  # Temperature: Contains the temperature of the overall device (controller and NVM included) in units of Kelvin. If the temperature exceeds the temperature threshold, refer to section 5.12.1.4, then an asynchronous event completion may occur
        (
            "AvailableSpare",
            UCHAR,
        ),  # Available Spare:  Contains a normalized percentage (0 to 100%) of the remaining spare capacity available
        (
            "AvailableSpareThreshold",
            UCHAR,
        ),  # Available Spare Threshold:  When the Available Spare falls below the threshold indicated in this field, an asynchronous event  completion may occur. The value is indicated as a normalized percentage (0 to 100%).
        ("PercentageUsed", UCHAR),  # Percentage Used
        ("Reserved0", UCHAR * 26),
        (
            "DataUnitRead",
            UCHAR * 16,
        ),  # Data Units Read:  Contains the number of 512 byte data units the host has read from the controller; this value does not include metadata. This value is reported in thousands (i.e., a value of 1 corresponds to 1000 units of 512 bytes read)  and is rounded up.  When the LBA size is a value other than 512 bytes, the controller shall convert the amount of data read to 512 byte units. For the NVM command set, logical blocks read as part of Compare and Read operations shall be included in this value
        (
            "DataUnitWritten",
            UCHAR * 16,
        ),  # Data Units Written: Contains the number of 512 byte data units the host has written to the controller; this value does not include metadata. This value is reported in thousands (i.e., a value of 1 corresponds to 1000 units of 512 bytes written)  and is rounded up.  When the LBA size is a value other than 512 bytes, the controller shall convert the amount of data written to 512 byte units. For the NVM command set, logical blocks written as part of Write operations shall be included in this value. Write Uncorrectable commands shall not impact this value.
        (
            "HostReadCommands",
            UCHAR * 16,
        ),  # Host Read Commands:  Contains the number of read commands  completed by  the controller. For the NVM command set, this is the number of Compare and Read commands.
        (
            "HostWrittenCommands",
            UCHAR * 16,
        ),  # Host Write Commands:  Contains the number of write commands  completed by  the controller. For the NVM command set, this is the number of Write commands.
        (
            "ControllerBusyTime",
            UCHAR * 16,
        ),  # Controller Busy Time:  Contains the amount of time the controller is busy with I/O commands. The controller is busy when there is a command outstanding to an I/O Queue (specifically, a command was issued via an I/O Submission Queue Tail doorbell write and the corresponding  completion queue entry  has not been posted yet to the associated I/O Completion Queue). This value is reported in minutes.
        ("PowerCycle", UCHAR * 16),  # Power Cycles: Contains the number of power cycles.
        (
            "PowerOnHours",
            UCHAR * 16,
        ),  # Power On Hours: Contains the number of power-on hours. This does not include time that the controller was powered and in a low power state condition.
        (
            "UnsafeShutdowns",
            UCHAR * 16,
        ),  # Unsafe Shutdowns: Contains the number of unsafe shutdowns. This count is incremented when a shutdown notification (CC.SHN) is not received prior to loss of power.
        (
            "MediaErrors",
            UCHAR * 16,
        ),  # Media Errors:  Contains the number of occurrences where the controller detected an unrecovered data integrity error. Errors such as uncorrectable ECC, CRC checksum failure, or LBA tag mismatch are included in this field.
        (
            "ErrorInfoLogEntryCount",
            UCHAR * 16,
        ),  # Number of Error Information Log Entries:  Contains the number of Error Information log entries over the life of the controller
        (
            "WarningCompositeTemperatureTime",
            ULONG,
        ),  # Warning Composite Temperature Time: Contains the amount of time in minutes that the controller is operational and the Composite Temperature is greater than or equal to the Warning Composite Temperature Threshold (WCTEMP) field and less than the Critical Composite Temperature Threshold (CCTEMP) field in the Identify Controller data structure
        (
            "CriticalCompositeTemperatureTime",
            ULONG,
        ),  # Critical Composite Temperature Time: Contains the amount of time in minutes that the controller is operational and the Composite Temperature is greater the Critical Composite Temperature Threshold (CCTEMP) field in the Identify Controller data structure
        ("TemperatureSensor1", USHORT),  # Contains the current temperature reported by temperature sensor 1.
        ("TemperatureSensor2", USHORT),  # Contains the current temperature reported by temperature sensor 2.
        ("TemperatureSensor3", USHORT),  # Contains the current temperature reported by temperature sensor 3.
        ("TemperatureSensor4", USHORT),  # Contains the current temperature reported by temperature sensor 4.
        ("TemperatureSensor5", USHORT),  # Contains the current temperature reported by temperature sensor 5.
        ("TemperatureSensor6", USHORT),  # Contains the current temperature reported by temperature sensor 6.
        ("TemperatureSensor7", USHORT),  # Contains the current temperature reported by temperature sensor 7.
        ("TemperatureSensor8", USHORT),  # Contains the current temperature reported by temperature sensor 8.
        ("Reserved1", UCHAR * 296),
    ]


# "Telemetry Host-Initiated Log" structure definition.

NVME_TELEMETRY_DATA_BLOCK_SIZE = 0x200  # All NVMe Telemetry Data Blocks are 512 bytes in size.


class NVME_TELEMETRY_HOST_INITIATED_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogIdentifier", UCHAR),  # Byte 0
        ("Reserved0", UCHAR * 4),  # Bytes 1-4
        ("OrganizationID", UCHAR * 3),  # Bytes 5-7 - IEEE OUI Identifier
        ("Area1LastBlock", USHORT),  # Bytes 8-9
        ("Area2LastBlock", USHORT),  # Bytes 10-11
        ("Area3LastBlock", USHORT),  # Bytes 12-13
        ("Reserved1", UCHAR * 2),  # Bytes 14-15
        ("Area4LastBlock", ULONG),  # Bytes 16-19
        ("Reserved2", UCHAR * 361),  # Bytes 20-380
        ("HostInitiatedDataGenerationNumber", UCHAR),  # Byte 381
        ("ControllerInitiatedDataAvailable", UCHAR),  # Byte 382
        ("ControllerInitiatedDataGenerationNumber", UCHAR),  # Byte 383
        ("ReasonIdentifier", UCHAR * 128),  # Bytes 384-511
    ]


PNVME_TELEMETRY_HOST_INITIATED_LOG = POINTER(NVME_TELEMETRY_HOST_INITIATED_LOG)


# "Telemetry Controller-Initiated Log" structure definition.
class NVME_TELEMETRY_CONTROLLER_INITIATED_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogIdentifier", UCHAR),  # Byte 0
        ("Reserved0", UCHAR * 4),  # Bytes 1-4
        ("OrganizationID", UCHAR * 3),  # Bytes 5-7 - IEEE OUI Identifier
        ("Area1LastBlock", USHORT),  # Bytes 8-9
        ("Area2LastBlock", USHORT),  # Bytes 10-11
        ("Area3LastBlock", USHORT),  # Bytes 12-13
        ("Reserved1", UCHAR * 2),  # Bytes 14-15
        ("Area4LastBlock", ULONG),  # Bytes 16-19
        ("Reserved2", UCHAR * 362),  # Bytes 20-381
        ("ControllerInitiatedDataAvailable", UCHAR),  # Byte 382
        ("ControllerInitiatedDataGenerationNumber", UCHAR),  # Byte 383
        ("ReasonIdentifier", UCHAR * 128),  # Bytes 384-511
    ]


PNVME_TELEMETRY_CONTROLLER_INITIATED_LOG = POINTER(NVME_TELEMETRY_CONTROLLER_INITIATED_LOG)


# Information of log: NVME_LOG_PAGE_FIRMWARE_SLOT_INFO. Size: 512 bytes
class NVME_FIRMWARE_SLOT_INFO_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "AFI",
            make_struct(
                [
                    (
                        "ActiveSlot",
                        UCHAR,
                        3,
                    ),  # Bits 2:0 indicates the firmware slot that contains the actively running firmware revision.
                    ("Reserved0", UCHAR, 1),
                    (
                        "PendingActivateSlot",
                        UCHAR,
                        3,
                    ),  # Bits 6:4 indicates the firmware slot that is going to be activated at the next controller reset.
                    ("Reserved1", UCHAR, 1),
                ],
                _pack_,
            ),
        ),  # Active Firmware Info (AFI)
        ("Reserved0", UCHAR * 7),
        (
            "FRS",
            ULONGLONG * 7,
        ),  # Firmware Revision for Slot 1 - 7(FRS1 - FRS7):  Contains the revision of the firmware downloaded to firmware slot 1 - 7.
        ("Reserved1", UCHAR * 448),
    ]


# Information of log: NVME_LOG_PAGE_CHANGED_NAMESPACE_LIST. Size: 4096 bytes
class NVME_CHANGED_NAMESPACE_LIST_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NSID", ULONG * 1024),  # List of Namespace ID upto 1024 entries
    ]


# Information of log: NVME_LOG_PAGE_CHANGED_ZONE_LIST. Size: 4096 bytes
class NVME_CHANGED_ZONE_LIST_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneIdentifiersCount", USHORT),  # Number of Zone Identifiers
        ("Reserved", UCHAR * 6),
        (
            "ZoneIdentifier",
            ULONGLONG * 511,
        ),  # List of Zone Identifiers upto 511 entries. Identifier contains Zone Start Logical Block Address(ZSLBA)
    ]


# Information of log: NVME_LOG_PAGE_COMMAND_EFFECTS. Size: 4096 bytes
class NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMITS(CEnum):
    NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_NONE = 0
    NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_NAMESPACE = 1
    NVME_COMMAND_EFFECT_SBUMISSION_EXECUTION_LIMIT_SINGLE_PER_CONTROLLER = 2


class NVME_COMMAND_EFFECTS_DATA(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("CSUPP", ULONG, 1),  # Command Supported (CSUPP)
                    ("LBCC", ULONG, 1),  # Logical Block Content Change (LBCC)
                    ("NCC", ULONG, 1),  # Namespace Capability Change (NCC)
                    ("NIC", ULONG, 1),  # Namespace Inventory Change (NIC)
                    ("CCC", ULONG, 1),  # Controller Capability Change (CCC)
                    ("Reserved0", ULONG, 11),
                    ("CSE", ULONG, 3),  # Command Submission and Execution (CSE)
                    ("Reserved1", ULONG, 13),
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_COMMAND_EFFECTS_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ACS", NVME_COMMAND_EFFECTS_DATA * 256),  # Admin Command Supported
        ("IOCS", NVME_COMMAND_EFFECTS_DATA * 256),  # I/O Command Supported
        ("Reserved", UCHAR * 2048),
    ]


_pack_ += 1


class NVME_DEVICE_SELF_TEST_RESULT_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "Status",
            make_struct(
                [
                    ("Result", UCHAR, 4),  # Result of Device Self-Test operation of this particular result data
                    ("CodeValue", UCHAR, 4),  # Self-Test code value that was specified in command
                ],
                _pack_,
            ),
        ),
        ("SegmentNumber", UCHAR),  # Indicates the first segment that failure occured
        (
            "ValidDiagnostics",
            make_struct(
                [
                    ("NSIDValid", UCHAR, 1),  # If set to 1, the contents of Namespace Identifier field is valid
                    ("FLBAValid", UCHAR, 1),  # If set to 1, the contents of Failing LBA field is valid
                    ("SCTValid", UCHAR, 1),  # If set to 1, the contents of Status Code Type field is valid
                    ("SCValid", UCHAR, 1),  # If set to 1, the contents of Status Code field is valid
                    ("Reserved", UCHAR, 4),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR),
        ("POH", ULONGLONG),  # Power On Hours, when test operation was completed/aborted
        ("NSID", ULONG),  # Namespace Identifier. Only valid if NSIDValid is set
        ("FailingLBA", ULONGLONG),  # Failed LBA which caused test to fail. Only valid if FLBAValid is set
        (
            "StatusCodeType",
            make_struct(
                [
                    (
                        "AdditionalInfo",
                        UCHAR,
                        3,
                    ),  # Additional information related to errors/conditions. Only valid if SCTValid is set
                    ("Reserved", UCHAR, 5),
                ],
                _pack_,
            ),
        ),
        ("StatusCode", UCHAR),  # Additional information related to errors/conditons. Only valid if SCValid is set
        ("VendorSpecific", USHORT),
    ]


# Information of log: NVME_LOG_PAGE_DEVICE_SELF_TEST. Size: 564 bytes
class NVME_DEVICE_SELF_TEST_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "CurrentOperation",
            make_struct(
                [
                    ("Status", UCHAR, 4),  # Status of current Device Self-Test operation
                    ("Reserved", UCHAR, 4),
                ],
                _pack_,
            ),
        ),
        (
            "CurrentCompletion",
            make_struct(
                [
                    (
                        "CompletePercent",
                        UCHAR,
                        7,
                    ),  # Percentage of completion of Device Self-Test operation. Valid if Status field is non-zero.
                    ("Reserved", UCHAR, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 2),
        (
            "ResultData",
            NVME_DEVICE_SELF_TEST_RESULT_DATA * 20,
        ),  # Last 20 Self-Test Result Data, latest to oldest available in sorted order
    ]


# Information of log: NVME_LOG_PAGE_ENDURANCE_GROUP_INFORMATION. Size: 512 bytes
class NVME_ENDURANCE_GROUP_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved0", ULONG),
        ("AvailableSpareThreshold", UCHAR),  # Available spare indicated as normalized percentage (0-100)
        (
            "PercentageUsed",
            UCHAR,
        ),  # Vendor specific estimate of percentage of life used for the NVM set(s) of Endurance Group (Billion Unit)
        ("Reserved1", UCHAR * 26),
        (
            "EnduranceEstimate",
            UCHAR * 16,
        ),  # Estimate of total number of data bytes written to NVM set(s) of Endurance Group (Billion Unit)
        (
            "DataUnitsRead",
            UCHAR * 16,
        ),  # Total number of data bytes read from NVM set(s) of Endurance Group (Billion Unit)
        (
            "DataUnitsWritten",
            UCHAR * 16,
        ),  # Total number of data bytes written to NVM sets(s) of Endurance Group (Billion Unit)
        # Includes only host writes
        (
            "MediaUnitsWritten",
            UCHAR * 16,
        ),  # Total number of data bytes written to NVM sets(s) of Endurance Group (Billion Unit)
        # Includes both host and controller writes.
        ("Reserved2", UCHAR * 416),
    ]


# Information of log: NVME_LOG_PAGE_PERSISTENT_EVENT_LOG. Header Size: 512 bytes
class NVME_PERSISTENT_EVENT_LOG_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogIdentifier", UCHAR),  # Byte 0      - Shall be set to 0x0D
        ("Reserved0", UCHAR * 3),  # Bytes 1-3
        ("TotalNumberOfEvents", ULONG),  # Bytes 4-7   - Contains the number of event entries in the log.
        (
            "TotalLogLength",
            ULONGLONG,
        ),  # Bytes 8-15  - Contains the total number of bytes of persistent event log page data available, including the header.
        (
            "LogRevision",
            UCHAR,
        ),  # Bytes 16    - Contains a number indicating the revision of the Get Log Page data structure that this log page data complies with.
        ("Reserved1", UCHAR),  # Bytes 17
        (
            "LogHeaderLength",
            USHORT,
        ),  # Bytes 18-19 - Contains the length in bytes of the log header information that follows. The total length of the log header in bytes is the value in this field plus 20.
        ("Timestamp", ULONGLONG),  # Bytes 20-27
        (
            "PowerOnHours",
            UCHAR * 16,
        ),  # Bytes 28-43 - Indicates the number of power-on hours at the time the Persistent Event log was retrieved.
        ("PowerCycleCount", ULONGLONG),  # Bytes 44-51 - Contains the number of power cycles for the controller.
        (
            "PciVendorId",
            USHORT,
        ),  # Bytes 52-53 - Same value as reported in the Identify Controller data PCI Vendor ID field.
        (
            "PciSubsystemVendorId",
            USHORT,
        ),  # Bytes 54-55 - Same value as reported in the Identify Controller data PCI Subsystem Vendor ID field.
        (
            "SerialNumber",
            UCHAR * 20,
        ),  # Bytes 56-75 - Same value as reported in the Identify Controller data Serial Number field.
        (
            "ModelNumber",
            UCHAR * 40,
        ),  # Bytes 76-115 - Same value as reported in the Identify Controller data Model Number field.
        (
            "NVMSubsystemNVMeQualifiedName",
            UCHAR * 256,
        ),  # Bytes 116-371 - Same value as reported in the Identify Controller data.
        ("Reserved", UCHAR * 108),  # Bytes 372-479
        (
            "SupportedEventsBitmap",
            UCHAR * 32,
        ),  # Bytes 480-511 - Contains a bitmap indicating support for the persistent event log events.
    ]


class NVME_PERSISTENT_EVENT_LOG_EVENT_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("EventType", UCHAR),  # Byte 0      - Indicates the event type for this entry.
        ("EventTypeRevision", UCHAR),  # Byte 1      - Contains a number indicating the revision of the event data.
        (
            "EventHeaderLength",
            UCHAR,
        ),  # Byte 2      - Contains the length in bytes of the event header information that follows.
        ("Reserved0", UCHAR),  # Byte 3
        (
            "ControllerIdentifier",
            USHORT,
        ),  # Bytes 4-5   - Contains the NVM subsystem unique controller identifier for the controller that created this event.
        ("EventTimestamp", ULONGLONG),  # Bytes 6-13
        ("Reserved1", UCHAR * 6),  # Bytes 14-19
        (
            "VendorSpecificInformationLength",
            USHORT,
        ),  # Bytes 20-21 - Indicates the length in bytes of the Vendor Specific Information.
        ("EventLength", USHORT),  # Bytes 22-23 - Indicates the length in bytes of the Vendor Specific Information.
    ]


class NVME_PERSISTENT_EVENT_LOG_EVENT_TYPES(CEnum):
    NVME_PERSISTENT_EVENT_TYPE_RESERVED0 = 0x00

    NVME_PERSISTENT_EVENT_TYPE_SMART_HEALTH_LOG_SNAPSHOT = 0x01
    NVME_PERSISTENT_EVENT_TYPE_FIRMWARE_COMMIT = 0x02
    NVME_PERSISTENT_EVENT_TYPE_TIMESTAMP_CHANGE = 0x03
    NVME_PERSISTENT_EVENT_TYPE_POWER_ON_OR_RESET = 0x04
    NVME_PERSISTENT_EVENT_TYPE_NVM_SUBSYSTEM_HARDWARE_ERROR = 0x05
    NVME_PERSISTENT_EVENT_TYPE_CHANGE_NAMESPACE = 0x06
    NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_START = 0x07
    NVME_PERSISTENT_EVENT_TYPE_FORMAT_NVM_COMPLETION = 0x08
    NVME_PERSISTENT_EVENT_TYPE_SANITIZE_START = 0x09
    NVME_PERSISTENT_EVENT_TYPE_SANITIZE_COMPLETION = 0x0A
    NVME_PERSISTENT_EVENT_TYPE_SET_FEATURE = 0x0B
    NVME_PERSISTENT_EVENT_TYPE_TELEMETRY_LOG_CREATED = 0x0C
    NVME_PERSISTENT_EVENT_TYPE_THERMAL_EXCURSION = 0x0D

    NVME_PERSISTENT_EVENT_TYPE_RESERVED1_BEGIN = 0x0E
    NVME_PERSISTENT_EVENT_TYPE_RESERVED1_END = 0xDD

    NVME_PERSISTENT_EVENT_TYPE_VENDOR_SPECIFIC_EVENT = 0xDE
    NVME_PERSISTENT_EVENT_TYPE_TCG_DEFINED = 0xDF

    NVME_PERSISTENT_EVENT_TYPE_RESERVED2_BEGIN = 0xE0
    NVME_PERSISTENT_EVENT_TYPE_RESERVED2_END = 0xFF

    NVME_PERSISTENT_EVENT_TYPE_MAX = 0xFF


_pack_ -= 1


# Information of log: NVME_LOG_PAGE_RESERVATION_NOTIFICATION. Size: 64 bytes
class NVME_RESERVATION_NOTIFICATION_TYPES(CEnum):
    NVME_RESERVATION_NOTIFICATION_TYPE_EMPTY_LOG_PAGE = 0
    NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_PREEMPTED = 1
    NVME_RESERVATION_NOTIFICATION_TYPE_REGISTRATION_RELEASED = 2
    NVME_RESERVATION_NOTIFICATION_TYPE_RESERVATION_PREEPMPTED = 3


class NVME_RESERVATION_NOTIFICATION_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogPageCount", ULONGLONG),  # Log Page Count
        ("LogPageType", UCHAR),  # Reservation Notification Log Page Type.
        ("AvailableLogPageCount", UCHAR),  # Number of Available Log Pages
        ("Reserved0", UCHAR * 2),
        ("NameSpaceId", ULONG),  # Namespace ID
        ("Reserved1", UCHAR * 48),
    ]


# Information of log: NVME_SANITIZE_STATUS_LOG. Size: 512 bytes
class NVME_SANITIZE_OPERATION_STATUS(CEnum):
    # The NVM subsystem has never been sanitized.
    NVME_SANITIZE_OPERATION_NONE = 0

    # The most recent sanitize operation completed successfully including
    # any additional media modification.
    NVME_SANITIZE_OPERATION_SUCCEEDED = 1

    # A sanitize operation is currently in progress.
    NVME_SANITIZE_OPERATION_IN_PROGRESS = 2

    # The most recent sanitize operation failed.
    NVME_SANITIZE_OPERATION_FAILED = 3

    # The most recent sanitize operation for which No-Deallocate After Sanitize was Requested
    # has completed successfully with deallocation of all LBAs.
    NVME_SANITIZE_OPERATION_SUCCEEDED_WITH_FORCED_DEALLOCATION = 4


PNVME_SANITIZE_OPERATION_STATUS = POINTER(NVME_SANITIZE_OPERATION_STATUS)


class NVME_SANITIZE_STATUS(Structure):
    _pack_ = _pack_
    _fields_ = [
        # This contains the status of the most recent sanitize operation.
        # The value of this field is defined in enum NVME_SANITIZE_OPERATION_STATUS.
        ("MostRecentSanitizeOperationStatus", USHORT, 3),
        # This contains the number of completed passes if the most recent sanitize operation
        # was an Overwrite.
        ("NumberCompletedPassesOfOverwrite", USHORT, 4),
        # If set to 1, then no namespace logical block in the NVM subsystem has been written to
        # and no Persistent Memory Region in the NVM subsystem has been enabled since manufactured
        # or most recent successfully sanitized operation.
        # If set to 0, then a namespace logical block in the NVM subsystem has been written to
        # or a Persistent Memory Region in the NVM subsystem has been enabled since manufactured
        # or most recent successfully sanitized operation.
        ("GlobalDataErased", USHORT, 1),
        ("Reserved", USHORT, 8),
    ]


class NVME_SANITIZE_STATUS_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        # Sanitize Progress (SPROG)
        # This field indicates the fraction complete of the sanitize operation. The value is a numerator
        # of the fraction complete that has 65536 (10000h) as its denominator. This value shall be set to
        # FFFFh if bits 2:0 of the SSTAT field are not set to 10b.
        ("SPROG", USHORT),
        # Sanitize Status (SSTAT)
        # This field indicates the status associated with the most recent sanitize operation.
        ("SSTAT", NVME_SANITIZE_STATUS),
        # Sanitize Command Dword 10 Information (SCDW10)
        # This field contains the value of the Command Dword 10 field of the Sanitize command that started
        # the sanitize operation whose status is reported in the SSTAT field.
        ("SCDW10", ULONG),
        # These fields below indicates the number of seconds required to complete the sanitize operation
        # of Overwrite/Block Erase/Crypto Erase methods when the No-Deallocate Modifies Media After Sanitize
        # field is not set to 10b. A value of 0 indicates that the sanitize operation is expected to be
        # completed in the background when the Sanitize command that started that operation is completed.
        # A value of FFFFFFFFh indicates that no time period is reported.
        ("EstimatedTimeForOverwrite", ULONG),
        ("EstimatedTimeForBlockErase", ULONG),
        ("EstimatedTimeForCryptoErase", ULONG),
        # These fields below indicates the number of seconds required to complete the sanitize operation
        # of Overwrite/Block Erase/CryptoErase methods and the associated additional media modification
        # after the sanitize operation. A value of 0 indicates that the sanitize operation is expected
        # to be completed in the background when the Sanitize command that started that operation is completed.
        # A value of FFFFFFFFh indicates that no time period is reported.
        ("EstimatedTimeForOverwriteWithNoDeallocateMediaModification", ULONG),
        ("EstimatedTimeForBlockEraseWithNoDeallocateMediaModification", ULONG),
        ("EstimatedTimeForCryptoEraseWithNoDeallocateMediaModification", ULONG),
        ("Reserved", UCHAR * 480),
    ]


# Parameters for FIRMWARE IMAGE DOWNLOAD Command
class NVME_CDW10_FIRMWARE_DOWNLOAD(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NUMD", ULONG),  # Number of Dwords (NUMD)
    ]


class NVME_CDW11_FIRMWARE_DOWNLOAD(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("OFST", ULONG),  # Offset (OFST)
    ]


# Parameters for FIRMWARE ACTIVATE/COMMIT Commands
class NVME_FIRMWARE_ACTIVATE_ACTIONS(CEnum):
    NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT = 0
    NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE = 1
    NVME_FIRMWARE_ACTIVATE_ACTION_ACTIVATE = 2
    NVME_FIRMWARE_ACTIVATE_ACTION_DOWNLOAD_TO_SLOT_AND_ACTIVATE_IMMEDIATE = 3


class NVME_CDW10_FIRMWARE_ACTIVATE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("FS", ULONG, 3),  # Firmware Slot (FS)
                    ("AA", ULONG, 2),  # Activate Action (AA)
                    ("Reserved", ULONG, 27),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for FORMAT NVM Commands
class NVME_PROTECTION_INFORMATION_TYPES(CEnum):
    NVME_PROTECTION_INFORMATION_NOT_ENABLED = 0
    NVME_PROTECTION_INFORMATION_TYPE1 = 1
    NVME_PROTECTION_INFORMATION_TYPE2 = 2
    NVME_PROTECTION_INFORMATION_TYPE3 = 3


class NVME_SECURE_ERASE_SETTINGS(CEnum):
    NVME_SECURE_ERASE_NONE = 0
    NVME_SECURE_ERASE_USER_DATA = 1
    NVME_SECURE_ERASE_CRYPTOGRAPHIC = 2


class NVME_CDW10_FORMAT_NVM(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("LBAF", ULONG, 4),  # LBA Format (LBAF)
                    ("MS", ULONG, 1),  # Metadata Settings (MS)
                    ("PI", ULONG, 3),  # Protection Information (PI)
                    ("PIL", ULONG, 1),  # Protection Information Location (PIL)
                    ("SES", ULONG, 3),  # Secure Erase Settings (SES)
                    ("ZF", ULONG, 2),  # Zone Format (ZF)
                    ("Reserved", ULONG, 18),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE(CEnum):
    # Additional media modification after sanitize is not defined.
    NVME_MEDIA_ADDITIONALLY_MODIFIED_AFTER_SANITIZE_NOT_DEFINED = 0

    # Media is not additionally modified after sanitize completes successfully.
    NVME_MEDIA_NOT_ADDITIONALLY_MODIFIED_AFTER_SANITIZE = 1

    # Media is additionally modified after sanitize completes sucessfully. The Sanitize Operation Completed event
    # does not occur until the additional media modification associated with this field has completed.
    NVME_MEDIA_ADDITIONALLY_MOFIDIED_AFTER_SANITIZE = 2


PNVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE = POINTER(NVME_NO_DEALLOCATE_MODIFIES_MEDIA_AFTER_SANITIZE)

# Parameters for Sanitize.


class NVME_SANITIZE_ACTION(CEnum):
    NVME_SANITIZE_ACTION_RESERVED = 0
    NVME_SANITIZE_ACTION_EXIT_FAILURE_MODE = 1
    NVME_SANITIZE_ACTION_START_BLOCK_ERASE_SANITIZE = 2
    NVME_SANITIZE_ACTION_START_OVERWRITE_SANITIZE = 3
    NVME_SANITIZE_ACTION_START_CRYPTO_ERASE_SANITIZE = 4


PNVME_SANITIZE_ACTION = POINTER(NVME_SANITIZE_ACTION)


class NVME_CDW10_SANITIZE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # Sanitize Action (SANACT)
                    # The value of this field is defined in enum NVME_SANTIZE_ACTION.
                    ("SANACT", ULONG, 3),  # Sanitize Action (SANACT)
                    # Allow Unrestricted Sanitize Exit (AUSE)
                    # This bit is ignored if Sanitize Action is in Exit Failure Mode (001b).
                    ("AUSE", ULONG, 1),  # Allow Unrestricted Sanitize Exit (AUSE)
                    # Overwrite Pass Count (OWPASS)
                    # This field specifies the number of overwrite passes using the data from Overwrite Pattern.
                    # A value of 0h specified 16 overwrite passes. This is ignored unless Sanitize Action is Overwrite (011b).
                    ("OWPASS", ULONG, 4),  # Overwrite Pass Count (OWPASS)
                    # Overwrite Invert Pattern Between Passes (OIPBP)
                    # This field indicates if Overwrite Pattern shall be inverted between passes.
                    # This is ignored unless Sanitize Action is Overwrite (011b).
                    ("OIPBP", ULONG, 1),  # Overwrite Invert Pattern Between Passes (OIPBP)
                    # No Deallocate After Sanitize
                    # If set to 1 and No-Deallocate Inhibited bit is 0,
                    #     controller shall not deallocate any logical blocks after sanitize completed successfully.
                    # If set to 1 and No-Deallocate Inhibited bit is 1, or if set to 0,
                    #     controller shall deallocate logical blocks after sanitize completed successfully.
                    # This bit is ignored if Sanitize Action is Exit Failure Mode (001b).
                    ("NDAS", ULONG, 1),  # No Deallocate After Sanitize
                    ("Reserved", ULONG, 22),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_SANITIZE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # Overwrite Pattern
                    # This field is ignored unless the Sanitize Action field in Command Dword 10 is set to 011b (Overwrite).
                    # This field specifies a 32-bit pattern that is used for the Overwrite sanitize operation.
                    ("OVRPAT", ULONG),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for RESERVATION Commands
class NVME_RESERVATION_TYPES(CEnum):
    NVME_RESERVATION_TYPE_RESERVED = 0
    NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE = 1
    NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS = 2
    NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS_ONLY = 3
    NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_REGISTRANTS_ONLY = 4
    NVME_RESERVATION_TYPE_WRITE_EXCLUSIVE_ALL_REGISTRANTS = 5
    NVME_RESERVATION_TYPE_EXCLUSIVE_ACCESS_ALL_REGISTRANTS = 6


# Parameters for RESERVATION ACQUIRE Commands
class NVME_RESERVATION_ACQUIRE_ACTIONS(CEnum):
    NVME_RESERVATION_ACQUIRE_ACTION_ACQUIRE = 0
    NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT = 1
    NVME_RESERVATION_ACQUIRE_ACTION_PREEMPT_AND_ABORT = 2


class NVME_CDW0_RESERVATION_PERSISTENCE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PTPL", ULONG, 1),  # Persist Through Power Loss (PTPL)
        ("Reserved", ULONG, 31),
    ]


class NVME_CDW10_RESERVATION_ACQUIRE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("RACQA", ULONG, 3),  # Reservation Acquire Action (RACQA)
                    ("IEKEY", ULONG, 1),  # Ignore Existing Key (IEKEY)
                    ("Reserved", ULONG, 4),
                    ("RTYPE", ULONG, 8),  # Reservation Type (RTYPE)
                    ("Reserved1", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Reservation Acquire Data Structure
class NVME_RESERVATION_ACQUIRE_DATA_STRUCTURE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CRKEY", ULONGLONG),  # Current Reservation Key (CRKEY)
        # If the Reseravation Acquire Action is set to 001b (Preempt) or 010b (Preempt and Abort),
        # then this field specifies the reservation key to be unregistered from the namespace.
        # For all other Reservation Acquire Action values, this field is reserved.
        ("PRKEY", ULONGLONG),  # Preempt Reservation Key (PRKEY)
    ]


# Parameters for RESERVATION REGISTER Commands
class NVME_RESERVATION_REGISTER_ACTIONS(CEnum):
    NVME_RESERVATION_REGISTER_ACTION_REGISTER = 0
    NVME_RESERVATION_REGISTER_ACTION_UNREGISTER = 1
    NVME_RESERVATION_REGISTER_ACTION_REPLACE = 2


class NVME_RESERVATION_REGISTER_PTPL_STATE_CHANGES(CEnum):
    NVME_RESERVATION_REGISTER_PTPL_STATE_NO_CHANGE = 0
    NVME_RESERVATION_REGISTER_PTPL_STATE_RESERVED = 1
    NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_0 = (
        2  # Reservations are released and registrants are cleared on a power on.
    )
    NVME_RESERVATION_REGISTER_PTPL_STATE_SET_TO_1 = 3  # Reservations and registrants persist across a power loss.


class NVME_CDW10_RESERVATION_REGISTER(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("RREGA", ULONG, 3),  # Reservation Register Action (RREGA)
                    ("IEKEY", ULONG, 1),  # Ignore Existing Key (IEKEY)
                    ("Reserved", ULONG, 26),
                    ("CPTPL", ULONG, 2),  # Change Persist Through Power Loss State (CPTPL)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Reservation Register Data Structure
class NVME_RESERVATION_REGISTER_DATA_STRUCTURE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CRKEY", ULONGLONG),  # Current Reservation Key (CRKEY)
        # If the Reseravation Acquire Action is set to 001b (Preempt) or 010b (Preempt and Abort),
        # then this field specifies the reservation key to be unregistered from the namespace.
        # For all other Reservation Acquire Action values, this field is reserved.
        ("NRKEY", ULONGLONG),  # New Reservation Key (NRKEY)
    ]


# Parameters for RESERVATION RELEASE Commands
class NVME_RESERVATION_RELEASE_ACTIONS(CEnum):
    NVME_RESERVATION_RELEASE_ACTION_RELEASE = 0
    NVME_RESERVATION_RELEASE_ACTION_CLEAR = 1


class NVME_CDW10_RESERVATION_RELEASE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("RRELA", ULONG, 3),  # Reservation Release Action (RRELA)
                    ("IEKEY", ULONG, 1),  # IgnoreExistingKey (IEKEY)
                    ("Reserved", ULONG, 4),
                    ("RTYPE", ULONG, 8),  # Reservation Type (RTYPE)
                    ("Reserved1", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Reservation Release Data Structure
class NVME_RESERVATION_RELEASE_DATA_STRUCTURE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CRKEY", ULONGLONG),  # Current Reservation Key (CRKEY)
    ]


# Parameters for RESERVATION REPORT Commands


class NVME_CDW10_RESERVATION_REPORT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NUMD", ULONG),  # Number of Dwords (NUMD), NOTE: 0's based value.
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_RESERVATION_REPORT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("EDS", ULONG, 1),  # Extended Data Structure (EDS)
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


_pack_ += 1


class NVME_RESERVATION_REPORT_STATUS_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        # This field is a counter that increments any time the below occurs:
        #      a. a Reservation Register command completes successfully on any controller associated with the namespace;
        #      b. a Reservation Release command with Reservation Release Action set to 001b (Clear) completes successfully
        #         on any controller associated with the name space;
        #      c. a Reservation Acquire command with Reservation Acquire Action set to 001b (Preempt) or 010b (Preempt and Abort)
        #         completes successfully on any controller associated with the namespace.
        # If the value of this field is FFFFFFFFh, then the field shall be cleared to 0b when incremented.
        ("GEN", ULONG),  # Generation (Gen)
        ("RTYPE", UCHAR),  # Reservation Type (RTYPE)
        ("REGCTL", USHORT),  # Number of Registered Controllers (REGCTL)
        ("Reserved", UCHAR * 2),
        ("PTPLS", UCHAR),  # Persist Through Power Loss State (PTPLS)
        ("Reserved1", UCHAR * 14),
    ]


_pack_ -= 1

assert sizeof(NVME_RESERVATION_REPORT_STATUS_HEADER) == 24


class NVME_REGISTERED_CONTROLLER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CNTLID", USHORT),  # Controller ID (CNTLID)
        (
            "RCSTS",
            make_struct(
                [
                    ("HoldReservation", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # Reservation Status (RCSTS)
        ("Reserved", UCHAR * 5),
        ("HOSTID", UCHAR * 8),  # Host Identifier (HOSTID)
        ("RKEY", ULONGLONG),  # Reservation Key (RKEY)
    ]


assert sizeof(NVME_REGISTERED_CONTROLLER_DATA) == 24


class NVME_RESERVATION_REPORT_STATUS_DATA_STRUCTURE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", NVME_RESERVATION_REPORT_STATUS_HEADER),
        ("RegisteredControllersData", NVME_REGISTERED_CONTROLLER_DATA * ANYSIZE_ARRAY),
    ]


class NVME_REGISTERED_CONTROLLER_EXTENDED_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("CNTLID", USHORT),  # Controller ID (CNTLID)
        (
            "RCSTS",
            make_struct(
                [
                    ("HoldReservation", UCHAR, 1),
                    ("Reserved", UCHAR, 7),
                ],
                _pack_,
            ),
        ),  # Reservation Status (RCSTS)
        ("Reserved", UCHAR * 5),
        ("RKEY", ULONGLONG),  # Reservation Key (RKEY)
        ("HOSTID", UCHAR * 16),  # 128-bit Host Identifier (HOSTID)
        ("Reserved1", UCHAR * 32),
    ]


assert sizeof(NVME_REGISTERED_CONTROLLER_EXTENDED_DATA) == 64


class NVME_RESERVATION_REPORT_STATUS_EXTENDED_DATA_STRUCTURE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", NVME_RESERVATION_REPORT_STATUS_HEADER),
        ("Reserved1", UCHAR * 40),
        ("RegisteredControllersExtendedData", NVME_REGISTERED_CONTROLLER_EXTENDED_DATA * ANYSIZE_ARRAY),
    ]


# Parameters for Directives.


class NVME_DIRECTIVE_TYPES(CEnum):
    NVME_DIRECTIVE_TYPE_IDENTIFY = 0x00
    NVME_DIRECTIVE_TYPE_STREAMS = 0x01


NVME_STREAMS_ID_MIN = 1
NVME_STREAMS_ID_MAX = 0xFFFF

# General parameters for Directive Receive.


class NVME_CDW10_DIRECTIVE_RECEIVE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NUMD", ULONG),  # Number of Dwords (NUMD)
    ]


class NVME_CDW11_DIRECTIVE_RECEIVE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("DOPER", ULONG, 8),  # Directive Operation
                    ("DTYPE", ULONG, 8),  # Directive Type
                    ("DSPEC", ULONG, 16),  # Directive Specific
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# General parameters for Directive Send.


class NVME_CDW10_DIRECTIVE_SEND(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NUMD", ULONG),  # Number of Dwords (NUMD)
    ]


class NVME_CDW11_DIRECTIVE_SEND(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("DOPER", ULONG, 8),  # Directive Operation
                    ("DTYPE", ULONG, 8),  # Directive Type
                    ("DSPEC", ULONG, 16),  # Directive Specific
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for the Identify Directive Type.


class NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATIONS(CEnum):
    NVME_DIRECTIVE_RECEIVE_IDENTIFY_OPERATION_RETURN_PARAMETERS = 1


class NVME_DIRECTIVE_SEND_IDENTIFY_OPERATIONS(CEnum):
    NVME_DIRECTIVE_SEND_IDENTIFY_OPERATION_ENABLE_DIRECTIVE = 1


class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Identify", UCHAR, 1),
        ("Streams", UCHAR, 1),
        ("Reserved0", UCHAR, 6),
        ("Reserved1", UCHAR * 31),
    ]


class NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("DirectivesSupported", NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR),
        ("DirectivesEnabled", NVME_DIRECTIVE_IDENTIFY_RETURN_PARAMETERS_DESCRIPTOR),
        # This data structure is 4KB in size.  The reserved space is commented out
        # so that this data structure can be safely allocated on the stack.
        # UCHAR   Reserved[4032]; # 4096 - 32 - 32 = 4032
    ]


class NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("ENDIR", ULONG, 1),  # Enable Directive
                    ("Reserved0", ULONG, 7),
                    ("DTYPE", ULONG, 8),  # Directive Type
                    ("Reserved1", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Parameters for the Streams Directive Type
class NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATIONS(CEnum):
    NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_RETURN_PARAMETERS = 1
    NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_GET_STATUS = 2
    NVME_DIRECTIVE_RECEIVE_STREAMS_OPERATION_ALLOCATE_RESOURCES = 3


class NVME_DIRECTIVE_SEND_STREAMS_OPERATIONS(CEnum):
    NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_IDENTIFIER = 1
    NVME_DIRECTIVE_SEND_STREAMS_OPERATION_RELEASE_RESOURCES = 2


class NVME_DIRECTIVE_STREAMS_RETURN_PARAMETERS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("MSL", USHORT),  # Max Streams Limit
        ("NSSA", USHORT),  # NVM Subsystem Streams Available
        ("NSSO", USHORT),  # NVM Subsystem Streams Open
        ("Reserved0", UCHAR * 10),
        ("SWS", ULONG),  # Stream Write Size
        ("SGS", USHORT),  # Stream Granularity Size
        ("NSA", USHORT),  # Namespace Streams Allocated
        ("NSO", USHORT),  # Namespace Streams Open
        ("Reserved1", UCHAR * 6),
    ]


NVME_STREAMS_GET_STATUS_MAX_IDS = 65535


class NVME_DIRECTIVE_STREAMS_GET_STATUS_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("OpenStreamCount", USHORT),  # Number of currently open streams.
        ("StreamIdentifiers", USHORT * NVME_STREAMS_GET_STATUS_MAX_IDS),  # Array of stream IDs that are currently open.
    ]


class NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NSR", ULONG, 16),  # Namespace Streams Requested
                    ("Reserved", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_COMPLETION_DW0_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES(Structure):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NSA", ULONG, 16),  # Namespace Streams Allocated
                    ("Reserved", ULONG, 16),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW12_DIRECTIVE_SEND(Union):
    _pack_ = _pack_
    _fields_ = [
        ("EnableDirective", NVME_CDW12_DIRECTIVE_SEND_IDENTIFY_ENABLE_DIRECTIVE),
        ("AsUlong", ULONG),
    ]


class NVME_CDW12_DIRECTIVE_RECEIVE(Union):
    _pack_ = _pack_
    _fields_ = [
        ("AllocateResources", NVME_CDW12_DIRECTIVE_RECEIVE_STREAMS_ALLOCATE_RESOURCES),
        ("AsUlong", ULONG),
    ]


# Parameters for SECURITY SEND / RECEIVE Commands
class NVME_CDW10_SECURITY_SEND_RECEIVE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved0", ULONG, 8),
                    ("SPSP", ULONG, 16),  # SP Specific (SPSP)
                    ("SECP", ULONG, 8),  # Security Protocol (SECP)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_SECURITY_SEND(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("TL", ULONG),  # Transfer Length  (TL):
    ]


class NVME_CDW11_SECURITY_RECEIVE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("AL", ULONG),  # Transfer Length  (AL)
    ]


# NVM Command Set
class NVME_NVM_COMMANDS(CEnum):
    NVME_NVM_COMMAND_FLUSH = 0x00
    NVME_NVM_COMMAND_WRITE = 0x01
    NVME_NVM_COMMAND_READ = 0x02

    NVME_NVM_COMMAND_WRITE_UNCORRECTABLE = 0x04
    NVME_NVM_COMMAND_COMPARE = 0x05
    NVME_NVM_COMMAND_WRITE_ZEROES = 0x08
    NVME_NVM_COMMAND_DATASET_MANAGEMENT = 0x09
    NVME_NVM_COMMAND_VERIFY = 0x0C
    NVME_NVM_COMMAND_RESERVATION_REGISTER = 0x0D
    NVME_NVM_COMMAND_RESERVATION_REPORT = 0x0E
    NVME_NVM_COMMAND_RESERVATION_ACQUIRE = 0x11
    NVME_NVM_COMMAND_RESERVATION_RELEASE = 0x15
    NVME_NVM_COMMAND_COPY = 0x19

    NVME_NVM_COMMAND_ZONE_MANAGEMENT_SEND = 0x79
    NVME_NVM_COMMAND_ZONE_MANAGEMENT_RECEIVE = 0x7A
    NVME_NVM_COMMAND_ZONE_APPEND = 0x7D


# Data structure of CDW12 for Read/Write command
class NVME_CDW12_READ_WRITE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NLB", ULONG, 16),  # Number of Logical Blocks (NLB)
                    ("Reserved0", ULONG, 4),
                    ("DTYPE", ULONG, 4),  # Directive Type (DTYPE)
                    ("Reserved1", ULONG, 2),
                    ("PRINFO", ULONG, 4),  # Protection Information Field (PRINFO)
                    ("FUA", ULONG, 1),  # Force Unit Access (FUA)
                    ("LR", ULONG, 1),  # Limited Retry (LR)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Data structure of CDW13 for Read/Write command
class NVME_ACCESS_FREQUENCIES(CEnum):
    NVME_ACCESS_FREQUENCY_NONE = 0  # No frequency information provided.
    NVME_ACCESS_FREQUENCY_TYPICAL = 1  # Typical number of reads and writes expected for this LBA range.
    NVME_ACCESS_FREQUENCY_INFR_WRITE_INFR_READ = 2  # Infrequent writes and infrequent reads to the LBA range indicated.
    NVME_ACCESS_FREQUENCY_INFR_WRITE_FR_READ = 3  # Infrequent writes and frequent reads to the LBA range indicated.
    NVME_ACCESS_FREQUENCY_FR_WRITE_INFR_READ = 4  # Frequent writes and infrequent reads to the LBA range indicated.
    NVME_ACCESS_FREQUENCY_FR_WRITE_FR_READ = 5  # Frequent writes and frequent reads to the LBA range indicated.
    NVME_ACCESS_FREQUENCY_ONE_TIME_READ = (
        6  # One time read. E.g. command is due to virus scan, backup, file copy, or archive.
    )
    NVME_ACCESS_FREQUENCY_SPECULATIVE_READ = 7  # Speculative read. The command is part of a prefetch operation.
    NVME_ACCESS_FREQUENCY_WILL_BE_OVERWRITTEN = 8  # The LBA range is going to be overwritten in the near future.


class NVME_ACCESS_LATENCIES(CEnum):
    NVME_ACCESS_LATENCY_NONE = 0  # None.  No latency information provided.
    NVME_ACCESS_LATENCY_IDLE = 1  # Idle. Longer latency acceptable
    NVME_ACCESS_LATENCY_NORMAL = 2  # Normal. Typical latency.
    NVME_ACCESS_LATENCY_LOW = 3  # Low. Smallest possible latency


class NVME_CDW13_READ_WRITE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    (
                        "DSM",
                        make_struct(
                            [
                                ("AccessFrequency", UCHAR, 4),
                                ("AccessLatency", UCHAR, 2),
                                ("SequentialRequest", UCHAR, 1),
                                ("Incompressible", UCHAR, 1),
                            ],
                            _pack_,
                        ),
                    ),  # Dataset Management (DSM)
                    ("Reserved", UCHAR),
                    ("DSPEC", USHORT),  # Directive Specific Value
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Data structure of CDW15 for Read/Write command
class NVME_CDW15_READ_WRITE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("ELBAT", ULONG, 16),  # Expected Logical Block Application Tag (ELBAT)
                    ("ELBATM", ULONG, 16),  # Expected Logical Block Application Tag Mask (ELBATM)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Dataset Management - Range Definition
class NVME_CONTEXT_ATTRIBUTES(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("AccessFrequency", ULONG, 4),
                    ("AccessLatency", ULONG, 2),
                    ("Reserved0", ULONG, 2),
                    ("SequentialReadRange", ULONG, 1),
                    ("SequentialWriteRange", ULONG, 1),
                    ("WritePrepare", ULONG, 1),
                    ("Reserved1", ULONG, 13),
                    ("CommandAccessSize", ULONG, 8),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_LBA_RANGE(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "Attributes",
            NVME_CONTEXT_ATTRIBUTES,
        ),  # The use of this information is optional and the controller is not required to perform any specific action.
        ("LogicalBlockCount", ULONG),
        ("StartingLBA", ULONGLONG),
    ]


class NVME_CDW10_DATASET_MANAGEMENT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NR", ULONG, 8),  # Number of Ranges (NR)
                    ("Reserved", ULONG, 24),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW11_DATASET_MANAGEMENT(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("IDR", ULONG, 1),  # Integral Dataset for Read (IDR)
                    ("IDW", ULONG, 1),  # Integral Dataset for Write (IDW)
                    ("AD", ULONG, 1),  # Deallocate (AD)
                    ("Reserved", ULONG, 29),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Zone Descriptor
class NVME_ZONE_DESCRIPTOR(Structure):
    _anonymous_ = ("DUMMYSTRUCTNAME", "DUMMYSTRUCTNAME")
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("ZT", UCHAR, 4),  # Zone Type
                    ("Reserved1", UCHAR, 4),
                ],
                _pack_,
            ),
        ),
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("Reserved2", UCHAR, 4),
                    ("ZS", UCHAR, 4),  # Zone State
                ],
                _pack_,
            ),
        ),
        (
            "ZA",
            make_struct(
                [
                    ("ZFC", UCHAR, 1),  # Zone Finished by Controller (ZFC)
                    ("FZR", UCHAR, 1),  # Finish Zone Recommended (FZR)
                    ("RZR", UCHAR, 1),  # Reset Zone Recommended (RZR)
                    ("Reserved", UCHAR, 4),
                    ("ZDEV", UCHAR, 1),  # Zone Descriptor Extension Valid (ZDEV)
                ],
                _pack_,
            ),
        ),  # Zone Attribute
        ("Reserved3", UCHAR * 5),
        ("ZCAP", ULONGLONG),  # Zone Capacity
        ("ZSLBA", ULONGLONG),  # Zone Start Logical Block Address
        ("WritePointer", ULONGLONG),  # Current Write pointer of the Zone
        ("Reserved4", UCHAR * 32),
    ]


# Zone States
class ZONE_STATE(CEnum):
    NVME_STATE_ZSE = 0x1  # Zone State Empty
    NVME_STATE_ZSIO = 0x2  # Zone State Implicitly Opened
    NVME_STATE_ZSEO = 0x3  # Zone State Explicitly Opened
    NVME_STATE_ZSC = 0x4  # Zone State Closed

    NVME_STATE_ZSRO = 0xD  # Zone State Read-Only
    NVME_STATE_ZSF = 0xE  # Zone State Full
    NVME_STATE_ZSO = 0xF  # Zone State Offline


# Data structure of CDW13 for Zone Management Send command
class NVME_ZONE_SEND_ACTION(CEnum):
    NVME_ZONE_SEND_CLOSE = 1  # Close one or more zones
    NVME_ZONE_SEND_FINISH = 2  # Finish one or more zones
    NVME_ZONE_SEND_OPEN = 3  # Open one or more zones
    NVME_ZONE_SEND_RESET = 4  # Reset one or more zones
    NVME_ZONE_SEND_OFFLINE = 5  # Offline one or more zones

    NVME_ZONE_SEND_SET_ZONE_DESCRIPTOR = 0x10  # Attach Zone Descriptor Extension data to a zone in the Empty state and
    # transition the zone to the Closed state


class NVME_CDW10_ZONE_MANAGEMENT_SEND(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("SLBA", ULONGLONG),  # Starting LBA (SLBA)
    ]


class NVME_CDW13_ZONE_MANAGEMENT_SEND(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("ZSA", ULONG, 8),  # Zone Send Action, as defined in NVME_ZONE_SEND_ACTION
                    ("SelectAll", ULONG, 1),  # Select all the zones. SLBA is ignored if set
                    ("Reserved", ULONG, 23),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Report Zone Data Structure
class NVME_REPORT_ZONE_INFO(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneCount", ULONGLONG),  # Number of Zones
        ("Reserved", ULONGLONG * 7),
        ("ZoneDescriptor", NVME_ZONE_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


# Extended Report Zone Data Structure and related defines
class NVME_ZONE_DESCRIPTOR_EXTENSION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneDescriptorExtensionInfo", UCHAR * 64),
    ]


class NVME_ZONE_EXTENDED_REPORT_ZONE_DESC(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneDescriptor", NVME_ZONE_DESCRIPTOR),
        ("ZoneDescriptorExtension", NVME_ZONE_DESCRIPTOR_EXTENSION * ANYSIZE_ARRAY),
    ]


class NVME_EXTENDED_REPORT_ZONE_INFO(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneCount", ULONGLONG),  # Number of Zones
        ("Reserved", ULONGLONG * 7),
        ("Desc", NVME_ZONE_EXTENDED_REPORT_ZONE_DESC * ANYSIZE_ARRAY),
    ]


# Data structure of CDW13 for Zone Management Receive command and related defines
class NVME_ZONE_RECEIVE_ACTION(CEnum):
    NVME_ZONE_RECEIVE_REPORT_ZONES = 0  # Returns report zone Descriptors
    NVME_ZONE_RECEIVE_EXTENDED_REPORT_ZONES = 1  # Returns report zone descriptors with extended report zone information


class NVME_ZONE_RECEIVE_ACTION_SPECIFIC(CEnum):
    NVME_ZRA_ALL_ZONES = 0  # List all zones
    NVME_ZRA_EMPTY_STATE_ZONES = 1  # List zones with state Zone State Empty
    NVME_ZRA_IO_STATE_ZONES = 2  # List zones with state Zone State Implicitly Opened
    NVME_ZRA_EO_STATE_ZONES = 3  # List zones with state Zone State Explicitly Opened
    NVME_ZRA_CLOSED_STATE_ZONES = 4  # List zones with state Zone State Closed
    NVME_ZRA_FULL_STATE_ZONES = 5  # List zones with state Zone State Full
    NVME_ZRA_RO_STATE_ZONES = 6  # List zones with state Zone State Read-Only
    NVME_ZRA_OFFLINE_STATE_ZONES = 7  # List zones with state Zone State Offline


class NVME_CDW10_ZONE_MANAGEMENT_RECEIVE(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("SLBA", ULONGLONG),  # Starting LBA (SLBA)
    ]


class NVME_CDW13_ZONE_MANAGEMENT_RECEIVE(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("ZRA", ULONG, 8),  # Zone Receive Action, as defined in NVME_ZONE_RECEIVE_ACTION
                    (
                        "ZRASpecific",
                        ULONG,
                        8,
                    ),  # Zone Receive Action Specific field, as defined in NVME_ZONE_RECEIVE_ACTION_SPECIFIC
                    ("Partial", ULONG, 1),  # Report Zones and Extended Report Zones: Partial Report
                    ("Reserved", ULONG, 15),
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW10_ZONE_APPEND(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("SLBA", ULONGLONG),  # Starting LBA (SLBA)
    ]


class NVME_CDW12_ZONE_APPEND(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("NLB", ULONG, 16),  # Number of Logical Blocks (NLB)
                    ("Reserved", ULONG, 9),
                    ("PIREMAP", ULONG, 1),  # Protection Information Remap (PIREMAP)
                    ("PRINFO", ULONG, 4),  # Protection Information Field (PRINFO)
                    ("FUA", ULONG, 1),  # Force Unit Access (FUA)
                    ("LR", ULONG, 1),  # Limited Retry(LR);
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


class NVME_CDW15_ZONE_APPEND(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    ("LBAT", ULONG, 16),  # Logical Bloack Application Tag
                    ("LBATM", ULONG, 16),  # Logical Block Application Tag Mask (LBATM)
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Command Dword 0
class NVME_COMMAND_DWORD0(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("OPC", ULONG, 8),  # Opcode (OPC)
                    ("FUSE", ULONG, 2),  # Fused Operation (FUSE)
                    ("Reserved0", ULONG, 5),
                    ("PSDT", ULONG, 1),  # PRP or SGL for Data Transfer (PSDT)
                    ("CID", ULONG, 16),  # Command Identifier (CID)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlong", ULONG),
    ]


# Fused Operation code
class NVME_FUSED_OPERATION_CODES(CEnum):
    NVME_FUSED_OPERATION_NORMAL = 0
    NVME_FUSED_OPERATION_FIRST_CMD = 1
    NVME_FUSED_OPERATION_SECOND_CMD = 2


class NVME_PRP_ENTRY(Union):
    _anonymous_ = ("DUMMYSTRUCTNAME",)
    _pack_ = _pack_
    _fields_ = [
        (
            "DUMMYSTRUCTNAME",
            make_struct(
                [
                    # LSB
                    ("Reserved0", ULONGLONG, 2),
                    ("PBAO", ULONGLONG, 62),  # Page Base Address and Offset (PBAO)
                    # MSB
                ],
                _pack_,
            ),
        ),
        ("AsUlonglong", ULONGLONG),
    ]


# If the namespace is not used for the command, then 'NSID' field shall be cleared to 0h.
# If a command shall be applied to all namespaces on the device, then 'NSID' field shall be set to FFFFFFFFh.
NVME_NAMESPACE_ALL = 0xFFFFFFFF


# NVMe command data structure
class NVME_COMMAND(Structure):
    _pack_ = _pack_
    _fields_ = [
        # Common fields for all commands
        ("CDW0", NVME_COMMAND_DWORD0),
        ("NSID", ULONG),
        ("Reserved0", ULONG * 2),
        ("MPTR", ULONGLONG),
        ("PRP1", ULONGLONG),
        ("PRP2", ULONGLONG),
        # Command independent fields from CDW10 to CDW15
        (
            "u",
            make_union(
                [
                    # General Command data fields
                    (
                        "GENERAL",
                        make_struct(
                            [
                                ("CDW10", ULONG),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Identify
                    (
                        "IDENTIFY",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_IDENTIFY),
                                ("CDW11", NVME_CDW11_IDENTIFY),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Abort
                    (
                        "ABORT",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_ABORT),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Get/Set Features
                    (
                        "GETFEATURES",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_GET_FEATURES),
                                ("CDW11", NVME_CDW11_FEATURES),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    (
                        "SETFEATURES",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_SET_FEATURES),
                                ("CDW11", NVME_CDW11_FEATURES),
                                ("CDW12", NVME_CDW12_FEATURES),
                                ("CDW13", NVME_CDW13_FEATURES),
                                ("CDW14", NVME_CDW14_FEATURES),
                                ("CDW15", NVME_CDW15_FEATURES),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Get Log Page
                    (
                        "GETLOGPAGE",
                        make_struct(
                            [
                                (
                                    "_unnamed_union",
                                    make_union(
                                        [
                                            ("CDW10", NVME_CDW10_GET_LOG_PAGE),
                                            ("CDW10_V13", NVME_CDW10_GET_LOG_PAGE_V13),
                                        ],
                                        _pack_,
                                    ),
                                ),
                                ("CDW11", NVME_CDW11_GET_LOG_PAGE),
                                ("CDW12", NVME_CDW12_GET_LOG_PAGE),
                                ("CDW13", NVME_CDW13_GET_LOG_PAGE),
                                ("CDW14", NVME_CDW14_GET_LOG_PAGE),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Create IO Completion Queue
                    (
                        "CREATEIOCQ",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_CREATE_IO_QUEUE),
                                ("CDW11", NVME_CDW11_CREATE_IO_CQ),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: Create IO Submission Queue
                    (
                        "CREATEIOSQ",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_CREATE_IO_QUEUE),
                                ("CDW11", NVME_CDW11_CREATE_IO_SQ),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: Dataset Management
                    (
                        "DATASETMANAGEMENT",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_DATASET_MANAGEMENT),
                                ("CDW11", NVME_CDW11_DATASET_MANAGEMENT),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: SECURITY SEND
                    (
                        "SECURITYSEND",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_SECURITY_SEND_RECEIVE),
                                ("CDW11", NVME_CDW11_SECURITY_SEND),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: SECURITY RECEIVE
                    (
                        "SECURITYRECEIVE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_SECURITY_SEND_RECEIVE),
                                ("CDW11", NVME_CDW11_SECURITY_RECEIVE),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: FIRMWARE IMAGE DOWNLOAD
                    (
                        "FIRMWAREDOWNLOAD",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_FIRMWARE_DOWNLOAD),
                                ("CDW11", NVME_CDW11_FIRMWARE_DOWNLOAD),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: FIRMWARE ACTIVATE
                    (
                        "FIRMWAREACTIVATE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_FIRMWARE_ACTIVATE),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: FORMAT NVM
                    (
                        "FORMATNVM",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_FORMAT_NVM),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: DIRECTIVE RECEIVE
                    (
                        "DIRECTIVERECEIVE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_DIRECTIVE_RECEIVE),
                                ("CDW11", NVME_CDW11_DIRECTIVE_RECEIVE),
                                ("CDW12", NVME_CDW12_DIRECTIVE_RECEIVE),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: DIRECTIVE SEND
                    (
                        "DIRECTIVESEND",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_DIRECTIVE_SEND),
                                ("CDW11", NVME_CDW11_DIRECTIVE_SEND),
                                ("CDW12", NVME_CDW12_DIRECTIVE_SEND),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # Admin Command: SANITIZE
                    (
                        "SANITIZE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_SANITIZE),
                                ("CDW11", NVME_CDW11_SANITIZE),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: Read/Write
                    (
                        "READWRITE",
                        make_struct(
                            [
                                ("LBALOW", ULONG),
                                ("LBAHIGH", ULONG),
                                ("CDW12", NVME_CDW12_READ_WRITE),
                                ("CDW13", NVME_CDW13_READ_WRITE),
                                ("CDW14", ULONG),
                                ("CDW15", NVME_CDW15_READ_WRITE),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: RESERVATION ACQUIRE
                    (
                        "RESERVATIONACQUIRE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_RESERVATION_ACQUIRE),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: RESERVATION REGISTER
                    (
                        "RESERVATIONREGISTER",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_RESERVATION_REGISTER),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: RESERVATION RELEASE
                    (
                        "RESERVATIONRELEASE",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_RESERVATION_RELEASE),
                                ("CDW11", ULONG),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: RESERVATION REPORT
                    (
                        "RESERVATIONREPORT",
                        make_struct(
                            [
                                ("CDW10", NVME_CDW10_RESERVATION_REPORT),
                                ("CDW11", NVME_CDW11_RESERVATION_REPORT),
                                ("CDW12", ULONG),
                                ("CDW13", ULONG),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: Zone Management Send
                    (
                        "ZONEMANAGEMENTSEND",
                        make_struct(
                            [
                                ("CDW1011", NVME_CDW10_ZONE_MANAGEMENT_SEND),
                                ("CDW12", ULONG),
                                ("CDW13", NVME_CDW13_ZONE_MANAGEMENT_SEND),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: Zone Management Receive
                    (
                        "ZONEMANAGEMENTRECEIVE",
                        make_struct(
                            [
                                ("CDW1011", NVME_CDW10_ZONE_MANAGEMENT_RECEIVE),
                                ("DWORDCOUNT", ULONG),
                                ("CDW13", NVME_CDW13_ZONE_MANAGEMENT_RECEIVE),
                                ("CDW14", ULONG),
                                ("CDW15", ULONG),
                            ],
                            _pack_,
                        ),
                    ),
                    # NVM Command: Zone Append
                    (
                        "ZONEAPPEND",
                        make_struct(
                            [
                                ("CDW1011", NVME_CDW10_ZONE_APPEND),
                                ("CDW12", NVME_CDW12_ZONE_APPEND),
                                ("CDW13", ULONG),
                                ("ILBRT", ULONG),
                                ("CDW15", NVME_CDW15_ZONE_APPEND),
                            ],
                            _pack_,
                        ),
                    ),
                ],
                _pack_,
            ),
        ),
    ]


assert sizeof(NVME_COMMAND) == 64  # NVMe commands are always 64 bytes
# (defined by constant STORAGE_PROTOCOL_COMMAND_LENGTH_NVME)


# The SCSI name string identifier used for the page 83 descriptor in NVMe to SCSI translation
# For NVMe devices compliant with revision 1.0.
class NVME_SCSI_NAME_STRING(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("PCIVendorID", CHAR * 4),
        ("ModelNumber", CHAR * 40),
        ("NamespaceID", CHAR * 4),
        ("SerialNumber", CHAR * 20),
    ]


# if _MSC_VER >= 1200
# pragma warning(pop)
# else
# pragma warning(default:4214)
# pragma warning(default:4201)
# pragma warning(default:4200)
# endif


# endif ''' WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PKG_STORAGE) '''
# pragma endregion

# endif #NVME_INCLUDED
