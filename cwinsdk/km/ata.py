from ctypes import POINTER, Structure, Union, sizeof
from ctypes.wintypes import ULONG, USHORT

from .. import make_struct
from ..shared.ntdef import ANYSIZE_ARRAY, UCHAR, ULONGLONG

_pack_ = 0

"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    ata.h

Abstract:

    Defines the structures used by ATA port and the miniport drivers.

Authors:

Revision History:

--"""

# ifndef _NTATA_
# define _NTATA_

# if _MSC_VER >= 1200
# pragma warning(push)
# endif

# pragma warning(disable:4200) # zero-sized array in struct/union
# pragma warning(disable:4214) # bit field types other than int
# pragma warning(disable:4201) # nameless struct/union

# 11/7/2011: update to ACS3 - D2161r1b; and SATA 3.1 Gold version.

# IDENTIFY device data (response to 0xEC)
_pack_ += 1


class IDENTIFY_DEVICE_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "GeneralConfiguration",
            make_struct(
                [
                    ("Reserved1", USHORT, 1),
                    ("Retired3", USHORT, 1),
                    ("ResponseIncomplete", USHORT, 1),
                    ("Retired2", USHORT, 3),
                    ("FixedDevice", USHORT, 1),  # obsolete
                    ("RemovableMedia", USHORT, 1),  # obsolete
                    ("Retired1", USHORT, 7),
                    ("DeviceType", USHORT, 1),
                ],
                _pack_,
            ),
        ),  # word 0
        ("NumCylinders", USHORT),  # word 1, obsolete
        ("SpecificConfiguration", USHORT),  # word 2
        ("NumHeads", USHORT),  # word 3, obsolete
        ("Retired1", USHORT * 2),
        ("NumSectorsPerTrack", USHORT),  # word 6, obsolete
        ("VendorUnique1", USHORT * 3),
        ("SerialNumber", UCHAR * 20),  # word 10-19
        ("Retired2", USHORT * 2),
        ("Obsolete1", USHORT),
        ("FirmwareRevision", UCHAR * 8),  # word 23-26
        ("ModelNumber", UCHAR * 40),  # word 27-46
        (
            "MaximumBlockTransfer",
            UCHAR,
        ),  # word 47. 01h-10h = Maximum number of sectors that shall be transferred per interrupt on READ/WRITE MULTIPLE commands
        ("VendorUnique2", UCHAR),
        (
            "TrustedComputing",
            make_struct(
                [
                    ("FeatureSupported", USHORT, 1),
                    ("Reserved", USHORT, 15),
                ],
                _pack_,
            ),
        ),  # word 48
        (
            "Capabilities",
            make_struct(
                [
                    ("CurrentLongPhysicalSectorAlignment", UCHAR, 2),
                    ("ReservedByte49", UCHAR, 6),
                    ("DmaSupported", UCHAR, 1),
                    ("LbaSupported", UCHAR, 1),  # Shall be set to one to indicate that LBA is supported.
                    ("IordyDisable", UCHAR, 1),
                    ("IordySupported", UCHAR, 1),
                    ("Reserved1", UCHAR, 1),  # Reserved for the IDENTIFY PACKET DEVICE command
                    ("StandybyTimerSupport", UCHAR, 1),
                    ("Reserved2", UCHAR, 2),  # Reserved for the IDENTIFY PACKET DEVICE command
                    ("ReservedWord50", USHORT),
                ],
                _pack_,
            ),
        ),  # word 49-50
        ("ObsoleteWords51", USHORT * 2),
        (
            "TranslationFieldsValid",
            USHORT,
            3,
        ),  # word 53, bit 0 - Obsolete; bit 1 - words 70:64 valid; bit 2; word 88 valid
        ("Reserved3", USHORT, 5),
        ("FreeFallControlSensitivity", USHORT, 8),
        ("NumberOfCurrentCylinders", USHORT),  # word 54, obsolete
        ("NumberOfCurrentHeads", USHORT),  # word 55, obsolete
        ("CurrentSectorsPerTrack", USHORT),  # word 56, obsolete
        ("CurrentSectorCapacity", ULONG),  # word 57, word 58, obsolete
        ("CurrentMultiSectorSetting", UCHAR),  # word 59
        ("MultiSectorSettingValid", UCHAR, 1),
        ("ReservedByte59", UCHAR, 3),
        ("SanitizeFeatureSupported", UCHAR, 1),
        ("CryptoScrambleExtCommandSupported", UCHAR, 1),
        ("OverwriteExtCommandSupported", UCHAR, 1),
        ("BlockEraseExtCommandSupported", UCHAR, 1),
        ("UserAddressableSectors", ULONG),  # word 60-61, for 28-bit commands
        ("ObsoleteWord62", USHORT),
        ("MultiWordDMASupport", USHORT, 8),  # word 63
        ("MultiWordDMAActive", USHORT, 8),
        ("AdvancedPIOModes", USHORT, 8),  # word 64. bit 0:1 - PIO mode supported
        ("ReservedByte64", USHORT, 8),
        ("MinimumMWXferCycleTime", USHORT),  # word 65
        ("RecommendedMWXferCycleTime", USHORT),  # word 66
        ("MinimumPIOCycleTime", USHORT),  # word 67
        ("MinimumPIOCycleTimeIORDY", USHORT),  # word 68
        (
            "AdditionalSupported",
            make_struct(
                [
                    ("ZonedCapabilities", USHORT, 2),
                    ("NonVolatileWriteCache", USHORT, 1),  # All write cache is non-volatile
                    ("ExtendedUserAddressableSectorsSupported", USHORT, 1),
                    ("DeviceEncryptsAllUserData", USHORT, 1),
                    ("ReadZeroAfterTrimSupported", USHORT, 1),
                    ("Optional28BitCommandsSupported", USHORT, 1),
                    ("IEEE1667", USHORT, 1),  # Reserved for IEEE 1667
                    ("DownloadMicrocodeDmaSupported", USHORT, 1),
                    ("SetMaxSetPasswordUnlockDmaSupported", USHORT, 1),
                    ("WriteBufferDmaSupported", USHORT, 1),
                    ("ReadBufferDmaSupported", USHORT, 1),
                    ("DeviceConfigIdentifySetDmaSupported", USHORT, 1),  # obsolete
                    (
                        "LPSAERCSupported",
                        USHORT,
                        1,
                    ),  # Long Physical Sector Alignment Error Reporting Control is supported.
                    ("DeterministicReadAfterTrimSupported", USHORT, 1),
                    ("CFastSpecSupported", USHORT, 1),
                ],
                _pack_,
            ),
        ),  # word 69
        ("ReservedWords70", USHORT * 5),  # word 70 - reserved
        # word 71:74 - Reserved for the IDENTIFY PACKET DEVICE command
        # Word 75
        ("QueueDepth", USHORT, 5),  #  Maximum queue depth - 1
        ("ReservedWord75", USHORT, 11),
        (
            "SerialAtaCapabilities",
            make_struct(
                [
                    # Word 76
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("SataGen1", USHORT, 1),  # Supports SATA Gen1 Signaling Speed (1.5Gb/s)
                    ("SataGen2", USHORT, 1),  # Supports SATA Gen2 Signaling Speed (3.0Gb/s)
                    ("SataGen3", USHORT, 1),  # Supports SATA Gen3 Signaling Speed (6.0Gb/s)
                    ("Reserved1", USHORT, 4),
                    ("NCQ", USHORT, 1),  # Supports the NCQ feature set
                    ("HIPM", USHORT, 1),  # Supports HIPM
                    ("PhyEvents", USHORT, 1),  # Supports the SATA Phy Event Counters log
                    ("NcqUnload", USHORT, 1),  # Supports Unload while NCQ commands are outstanding
                    ("NcqPriority", USHORT, 1),  # Supports NCQ priority information
                    ("HostAutoPS", USHORT, 1),  # Supports Host Automatic Partial to Slumber transitions
                    ("DeviceAutoPS", USHORT, 1),  # Supports Device Automatic Partial to Slumber transitions
                    ("ReadLogDMA", USHORT, 1),  # Supports READ LOG DMA EXT as equivalent to READ LOG EXT
                    # Word 77
                    ("Reserved2", USHORT, 1),  # shall be set to 0
                    ("CurrentSpeed", USHORT, 3),  # Coded value indicating current negotiated Serial ATA signal speed
                    ("NcqStreaming", USHORT, 1),  # Supports NCQ Streaming
                    ("NcqQueueMgmt", USHORT, 1),  # Supports NCQ Queue Management Command
                    ("NcqReceiveSend", USHORT, 1),  # Supports RECEIVE FPDMA QUEUED and SEND FPDMA QUEUED commands
                    ("DEVSLPtoReducedPwrState", USHORT, 1),
                    ("Reserved3", USHORT, 8),
                ],
                _pack_,
            ),
        ),
        # Word 78
        (
            "SerialAtaFeaturesSupported",
            make_struct(
                [
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("NonZeroOffsets", USHORT, 1),  # Device supports non-zero buffer offsets in DMA Setup FIS
                    ("DmaSetupAutoActivate", USHORT, 1),  # Device supports DMA Setup auto-activation
                    ("DIPM", USHORT, 1),  # Device supports DIPM
                    ("InOrderData", USHORT, 1),  # Device supports in-order data delivery
                    ("HardwareFeatureControl", USHORT, 1),  # Hardware Feature Control is supported
                    ("SoftwareSettingsPreservation", USHORT, 1),  # Device supports Software Settings Preservation
                    ("NCQAutosense", USHORT, 1),  # Supports NCQ Autosense
                    ("DEVSLP", USHORT, 1),  # Device supports link power state - device sleep
                    (
                        "HybridInformation",
                        USHORT,
                        1,
                    ),  # Device supports Hybrid Information Feature (If the device does not support NCQ (word 76 bit 8 is 0), then this bit shall be cleared to 0.)
                    ("Reserved1", USHORT, 6),
                ],
                _pack_,
            ),
        ),
        # Word 79
        (
            "SerialAtaFeaturesEnabled",
            make_struct(
                [
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("NonZeroOffsets", USHORT, 1),  # Non-zero buffer offsets in DMA Setup FIS enabled
                    ("DmaSetupAutoActivate", USHORT, 1),  # DMA Setup auto-activation optimization enabled
                    ("DIPM", USHORT, 1),  # DIPM enabled
                    ("InOrderData", USHORT, 1),  # In-order data delivery enabled
                    ("HardwareFeatureControl", USHORT, 1),  # Hardware Feature Control is enabled
                    ("SoftwareSettingsPreservation", USHORT, 1),  # Software Settings Preservation enabled
                    ("DeviceAutoPS", USHORT, 1),  # Device Automatic Partial to Slumber transitions enabled
                    ("DEVSLP", USHORT, 1),  # link power state - device sleep is enabled
                    ("HybridInformation", USHORT, 1),  # Hybrid Information Feature is enabled
                    ("Reserved1", USHORT, 6),
                ],
                _pack_,
            ),
        ),
        (
            "MajorRevision",
            USHORT,
        ),  # word 80. bit 5 - supports ATA5; bit 6 - supports ATA6; bit 7 - supports ATA7; bit 8 - supports ATA8-ACS; bit 9 - supports ACS-2;
        ("MinorRevision", USHORT),  # word 81. T13 minior version number
        (
            "CommandSetSupport",
            make_struct(
                [
                    # Word 82
                    ("SmartCommands", USHORT, 1),  # The SMART feature set is supported
                    ("SecurityMode", USHORT, 1),  # The Security feature set is supported
                    ("RemovableMediaFeature", USHORT, 1),  # obsolete
                    ("PowerManagement", USHORT, 1),  # shall be set to 1
                    (
                        "Reserved1",
                        USHORT,
                        1,
                    ),  # PACKET feature set, set to 0 indicates not supported for ATA devices (only support for ATAPI devices)
                    ("WriteCache", USHORT, 1),  # The volatile write cache is supported
                    ("LookAhead", USHORT, 1),  # Read look-ahead is supported
                    ("ReleaseInterrupt", USHORT, 1),  # obsolete
                    ("ServiceInterrupt", USHORT, 1),  # obsolete
                    (
                        "DeviceReset",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the DEVICE RESET command is not supported
                    ("HostProtectedArea", USHORT, 1),  # obsolete
                    ("Obsolete1", USHORT, 1),
                    ("WriteBuffer", USHORT, 1),  # The WRITE BUFFER command is supported
                    ("ReadBuffer", USHORT, 1),  # The READ BUFFER command is supported
                    ("Nop", USHORT, 1),  # The NOP command is supported
                    ("Obsolete2", USHORT, 1),
                    # Word 83
                    ("DownloadMicrocode", USHORT, 1),  # The DOWNLOAD MICROCODE command is supported
                    ("DmaQueued", USHORT, 1),  # obsolete
                    ("Cfa", USHORT, 1),  # The CFA feature set is supported
                    ("AdvancedPm", USHORT, 1),  # The APM feature set is supported
                    ("Msn", USHORT, 1),  # obsolete
                    ("PowerUpInStandby", USHORT, 1),  # The PUIS feature set is supported
                    ("ManualPowerUp", USHORT, 1),  # SET FEATURES subcommand is required to spin-up after power-up
                    ("Reserved2", USHORT, 1),
                    ("SetMax", USHORT, 1),  # obsolete
                    ("Acoustics", USHORT, 1),  # obsolete
                    ("BigLba", USHORT, 1),  # The 48-bit Address feature set is supported
                    ("DeviceConfigOverlay", USHORT, 1),  # obsolete
                    (
                        "FlushCache",
                        USHORT,
                        1,
                    ),  # Shall be set to one to indicate that the mandatory FLUSH CACHE command is supported
                    ("FlushCacheExt", USHORT, 1),  # The FLUSH CACHE EXT command is supported
                    ("WordValid83", USHORT, 2),  # shall be 01b
                    # Word 84
                    ("SmartErrorLog", USHORT, 1),  # SMART error logging is supported
                    ("SmartSelfTest", USHORT, 1),  # The SMART self-test is supported
                    ("MediaSerialNumber", USHORT, 1),  # Media serial number is supported
                    ("MediaCardPassThrough", USHORT, 1),  # obsolete
                    ("StreamingFeature", USHORT, 1),  # The Streaming feature set is supported
                    ("GpLogging", USHORT, 1),  # The GPL feature set is supported
                    ("WriteFua", USHORT, 1),  # The WRITE DMA FUA EXT and WRITE MULTIPLE FUA EXT commands are supported
                    ("WriteQueuedFua", USHORT, 1),  # obsolete
                    ("WWN64Bit", USHORT, 1),  # The 64-bit World wide name is supported
                    ("URGReadStream", USHORT, 1),  # obsolete
                    ("URGWriteStream", USHORT, 1),  # obsolete
                    ("ReservedForTechReport", USHORT, 2),
                    ("IdleWithUnloadFeature", USHORT, 1),  # The IDLE IMMEDIATE command with UNLOAD feature is supported
                    ("WordValid", USHORT, 2),  # shall be 01b
                ],
                _pack_,
            ),
        ),
        (
            "CommandSetActive",
            make_struct(
                [
                    # Word 85
                    ("SmartCommands", USHORT, 1),  # The SMART feature set is enabled
                    ("SecurityMode", USHORT, 1),  # The Security feature set is enabled
                    ("RemovableMediaFeature", USHORT, 1),  # obsolete
                    (
                        "PowerManagement",
                        USHORT,
                        1,
                    ),  # Shall be set to one to indicate that the mandatory Power Management feature set is supported
                    (
                        "Reserved1",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the PACKET feature set is not supported
                    ("WriteCache", USHORT, 1),  # The volatile write cache is enabled
                    ("LookAhead", USHORT, 1),  # Read look-ahead is enabled
                    ("ReleaseInterrupt", USHORT, 1),  # The release interrupt is enabled
                    ("ServiceInterrupt", USHORT, 1),  # The SERVICE interrupt is enabled
                    (
                        "DeviceReset",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the DEVICE RESET command is not supported
                    ("HostProtectedArea", USHORT, 1),  # obsolete
                    ("Obsolete1", USHORT, 1),
                    ("WriteBuffer", USHORT, 1),  # The WRITE BUFFER command is supported
                    ("ReadBuffer", USHORT, 1),  # The READ BUFFER command is supported
                    ("Nop", USHORT, 1),  # The NOP command is supported
                    ("Obsolete2", USHORT, 1),
                    # Word 86
                    ("DownloadMicrocode", USHORT, 1),  # The DOWNLOAD MICROCODE command is supported
                    ("DmaQueued", USHORT, 1),  # obsolete
                    ("Cfa", USHORT, 1),  # The CFA feature set is supported
                    ("AdvancedPm", USHORT, 1),  # The APM feature set is enabled
                    ("Msn", USHORT, 1),  # obsolete
                    ("PowerUpInStandby", USHORT, 1),  # The PUIS feature set is enabled
                    ("ManualPowerUp", USHORT, 1),  # SET FEATURES subcommand is required to spin-up after power-up
                    ("Reserved2", USHORT, 1),
                    ("SetMax", USHORT, 1),  # obsolete
                    ("Acoustics", USHORT, 1),  # obsolete
                    ("BigLba", USHORT, 1),  # The 48-bit Address features set is supported
                    ("DeviceConfigOverlay", USHORT, 1),  # obsolete
                    ("FlushCache", USHORT, 1),  # FLUSH CACHE command supported
                    ("FlushCacheExt", USHORT, 1),  # FLUSH CACHE EXT command supported
                    ("Resrved3", USHORT, 1),
                    ("Words119_120Valid", USHORT, 1),  # Words 119..120 are valid
                    # Word 87
                    ("SmartErrorLog", USHORT, 1),  # SMART error logging is supported
                    ("SmartSelfTest", USHORT, 1),  # SMART self-test supported
                    ("MediaSerialNumber", USHORT, 1),  # Media serial number is valid
                    ("MediaCardPassThrough", USHORT, 1),  # obsolete
                    ("StreamingFeature", USHORT, 1),  # obsolete
                    ("GpLogging", USHORT, 1),  # The GPL feature set is supported
                    ("WriteFua", USHORT, 1),  # The WRITE DMA FUA EXT and WRITE MULTIPLE FUA EXT commands are supported
                    ("WriteQueuedFua", USHORT, 1),  # obsolete
                    ("WWN64Bit", USHORT, 1),  # The 64-bit World wide name is supported
                    ("URGReadStream", USHORT, 1),  # obsolete
                    ("URGWriteStream", USHORT, 1),  # obsolete
                    ("ReservedForTechReport", USHORT, 2),
                    ("IdleWithUnloadFeature", USHORT, 1),  # The IDLE IMMEDIATE command with UNLOAD FEATURE is supported
                    ("Reserved4", USHORT, 2),  # bit 14 shall be set to 1; bit 15 shall be cleared to 0
                ],
                _pack_,
            ),
        ),
        (
            "UltraDMASupport",
            USHORT,
            8,
        ),  # word 88. bit 0 - UDMA mode 0 is supported ... bit 6 - UDMA mode 6 and below are supported
        ("UltraDMAActive", USHORT, 8),  # word 88. bit 8 - UDMA mode 0 is selected ... bit 14 - UDMA mode 6 is selected
        (
            "NormalSecurityEraseUnit",
            make_struct(
                [  # word 89
                    ("TimeRequired", USHORT, 15),
                    ("ExtendedTimeReported", USHORT, 1),
                ],
                _pack_,
            ),
        ),
        (
            "EnhancedSecurityEraseUnit",
            make_struct(
                [  # word 90
                    ("TimeRequired", USHORT, 15),
                    ("ExtendedTimeReported", USHORT, 1),
                ],
                _pack_,
            ),
        ),
        ("CurrentAPMLevel", USHORT, 8),  # word 91
        ("ReservedWord91", USHORT, 8),
        ("MasterPasswordID", USHORT),  # word 92. Master Password Identifier
        ("HardwareResetResult", USHORT),  # word 93
        ("CurrentAcousticValue", USHORT, 8),  # word 94. obsolete
        ("RecommendedAcousticValue", USHORT, 8),
        ("StreamMinRequestSize", USHORT),  # word 95
        ("StreamingTransferTimeDMA", USHORT),  # word 96
        ("StreamingAccessLatencyDMAPIO", USHORT),  # word 97
        ("StreamingPerfGranularity", ULONG),  # word 98, 99
        ("Max48BitLBA", ULONG * 2),  # word 100-103
        ("StreamingTransferTime", USHORT),  # word 104. Streaming Transfer Time - PIO
        ("DsmCap", USHORT),  # word 105
        (
            "PhysicalLogicalSectorSize",
            make_struct(
                [
                    ("LogicalSectorsPerPhysicalSector", USHORT, 4),  # n power of 2: logical sectors per physical sector
                    ("Reserved0", USHORT, 8),
                    ("LogicalSectorLongerThan256Words", USHORT, 1),
                    ("MultipleLogicalSectorsPerPhysicalSector", USHORT, 1),
                    ("Reserved1", USHORT, 2),  # bit 14 - shall be set to  1; bit 15 - shall be clear to 0
                ],
                _pack_,
            ),
        ),  # word 106
        ("InterSeekDelay", USHORT),  # word 107.     Inter-seek delay for ISO 7779 standard acoustic testing
        ("WorldWideName", USHORT * 4),  # words 108-111
        ("ReservedForWorldWideName128", USHORT * 4),  # words 112-115
        ("ReservedForTlcTechnicalReport", USHORT),  # word 116
        ("WordsPerLogicalSector", USHORT * 2),  # words 117-118 Logical sector size (DWord)
        (
            "CommandSetSupportExt",
            make_struct(
                [
                    ("ReservedForDrqTechnicalReport", USHORT, 1),
                    ("WriteReadVerify", USHORT, 1),  # The Write-Read-Verify feature set is supported
                    ("WriteUncorrectableExt", USHORT, 1),  # The WRITE UNCORRECTABLE EXT command is supported
                    (
                        "ReadWriteLogDmaExt",
                        USHORT,
                        1,
                    ),  # The READ LOG DMA EXT and WRITE LOG DMA EXT commands are supported
                    ("DownloadMicrocodeMode3", USHORT, 1),  # Download Microcode mode 3 is supported
                    ("FreefallControl", USHORT, 1),  # The Free-fall Control feature set is supported
                    ("SenseDataReporting", USHORT, 1),  # Sense Data Reporting feature set is supported
                    ("ExtendedPowerConditions", USHORT, 1),  # Extended Power Conditions feature set is supported
                    ("Reserved0", USHORT, 6),
                    ("WordValid", USHORT, 2),  # shall be 01b
                ],
                _pack_,
            ),
        ),  # word 119
        (
            "CommandSetActiveExt",
            make_struct(
                [
                    ("ReservedForDrqTechnicalReport", USHORT, 1),
                    ("WriteReadVerify", USHORT, 1),  # The Write-Read-Verify feature set is enabled
                    ("WriteUncorrectableExt", USHORT, 1),  # The WRITE UNCORRECTABLE EXT command is supported
                    (
                        "ReadWriteLogDmaExt",
                        USHORT,
                        1,
                    ),  # The READ LOG DMA EXT and WRITE LOG DMA EXT commands are supported
                    ("DownloadMicrocodeMode3", USHORT, 1),  # Download Microcode mode 3 is supported
                    ("FreefallControl", USHORT, 1),  # The Free-fall Control feature set is enabled
                    ("SenseDataReporting", USHORT, 1),  # Sense Data Reporting feature set is enabled
                    ("ExtendedPowerConditions", USHORT, 1),  # Extended Power Conditions feature set is enabled
                    ("Reserved0", USHORT, 6),
                    ("Reserved1", USHORT, 2),  # bit 14 - shall be set to  1; bit 15 - shall be clear to 0
                ],
                _pack_,
            ),
        ),  # word 120
        ("ReservedForExpandedSupportandActive", USHORT * 6),
        ("MsnSupport", USHORT, 2),  # word 127. obsolete
        ("ReservedWord127", USHORT, 14),
        (
            "SecurityStatus",
            make_struct(
                [  # word 128
                    ("SecuritySupported", USHORT, 1),
                    ("SecurityEnabled", USHORT, 1),
                    ("SecurityLocked", USHORT, 1),
                    ("SecurityFrozen", USHORT, 1),
                    ("SecurityCountExpired", USHORT, 1),
                    ("EnhancedSecurityEraseSupported", USHORT, 1),
                    ("Reserved0", USHORT, 2),
                    ("SecurityLevel", USHORT, 1),  # Master Password Capability: 0 = High, 1 = Maximum
                    ("Reserved1", USHORT, 7),
                ],
                _pack_,
            ),
        ),
        ("ReservedWord129", USHORT * 31),  # word 129...159. Vendor specific
        (
            "CfaPowerMode1",
            make_struct(
                [  # word 160
                    ("MaximumCurrentInMA", USHORT, 12),
                    ("CfaPowerMode1Disabled", USHORT, 1),
                    ("CfaPowerMode1Required", USHORT, 1),
                    ("Reserved0", USHORT, 1),
                    ("Word160Supported", USHORT, 1),
                ],
                _pack_,
            ),
        ),
        ("ReservedForCfaWord161", USHORT * 7),  # Words 161-167
        ("NominalFormFactor", USHORT, 4),  # Word 168
        ("ReservedWord168", USHORT, 12),
        (
            "DataSetManagementFeature",
            make_struct(
                [  # Word 169
                    ("SupportsTrim", USHORT, 1),
                    ("Reserved0", USHORT, 15),
                ],
                _pack_,
            ),
        ),
        ("AdditionalProductID", USHORT * 4),  # Words 170-173
        ("ReservedForCfaWord174", USHORT * 2),  # Words 174-175
        ("CurrentMediaSerialNumber", USHORT * 30),  # Words 176-205
        (
            "SCTCommandTransport",
            make_struct(
                [  # Word 206
                    ("Supported", USHORT, 1),  # The SCT Command Transport is supported
                    ("Reserved0", USHORT, 1),  # obsolete
                    ("WriteSameSuported", USHORT, 1),  # The SCT Write Same command is supported
                    ("ErrorRecoveryControlSupported", USHORT, 1),  # The SCT Error Recovery Control command is supported
                    ("FeatureControlSuported", USHORT, 1),  # The SCT Feature Control command is supported
                    ("DataTablesSuported", USHORT, 1),  # The SCT Data Tables command is supported
                    ("Reserved1", USHORT, 6),
                    ("VendorSpecific", USHORT, 4),
                ],
                _pack_,
            ),
        ),
        ("ReservedWord207", USHORT * 2),  # Words 207-208
        (
            "BlockAlignment",
            make_struct(
                [  # Word 209
                    ("AlignmentOfLogicalWithinPhysical", USHORT, 14),
                    ("Word209Supported", USHORT, 1),  # shall be set to 1
                    ("Reserved0", USHORT, 1),  # shall be cleared to 0
                ],
                _pack_,
            ),
        ),
        ("WriteReadVerifySectorCountMode3Only", USHORT * 2),  # Words 210-211
        ("WriteReadVerifySectorCountMode2Only", USHORT * 2),  # Words 212-213
        (
            "NVCacheCapabilities",
            make_struct(
                [
                    ("NVCachePowerModeEnabled", USHORT, 1),
                    ("Reserved0", USHORT, 3),
                    ("NVCacheFeatureSetEnabled", USHORT, 1),
                    ("Reserved1", USHORT, 3),
                    ("NVCachePowerModeVersion", USHORT, 4),
                    ("NVCacheFeatureSetVersion", USHORT, 4),
                ],
                _pack_,
            ),
        ),  # Word 214. obsolete
        ("NVCacheSizeLSW", USHORT),  # Word 215. obsolete
        ("NVCacheSizeMSW", USHORT),  # Word 216. obsolete
        ("NominalMediaRotationRate", USHORT),  # Word 217; value 0001h means non-rotating media.
        ("ReservedWord218", USHORT),  # Word 218
        (
            "NVCacheOptions",
            make_struct(
                [
                    ("NVCacheEstimatedTimeToSpinUpInSeconds", UCHAR),
                    ("Reserved", UCHAR),
                ],
                _pack_,
            ),
        ),  # Word 219. obsolete
        ("WriteReadVerifySectorCountMode", USHORT, 8),  # Word 220. Write-Read-Verify feature set current mode
        ("ReservedWord220", USHORT, 8),
        ("ReservedWord221", USHORT),  # Word 221
        (
            "TransportMajorVersion",
            make_struct(
                [  # Word 222 Transport major version number
                    ("MajorVersion", USHORT, 12),  # 0000h or FFFFh = device does not report version
                    ("TransportType", USHORT, 4),
                ],
                _pack_,
            ),
        ),
        ("TransportMinorVersion", USHORT),  # Word 223
        ("ReservedWord224", USHORT * 6),  # Word 224...229
        (
            "ExtendedNumberOfUserAddressableSectors",
            ULONG * 2,
        ),  # Words 230...233 Extended Number of User Addressable Sectors
        (
            "MinBlocksPerDownloadMicrocodeMode03",
            USHORT,
        ),  # Word 234 Minimum number of 512-byte data blocks per Download Microcode mode 03h operation
        (
            "MaxBlocksPerDownloadMicrocodeMode03",
            USHORT,
        ),  # Word 235 Maximum number of 512-byte data blocks per Download Microcode mode 03h operation
        ("ReservedWord236", USHORT * 19),  # Word 236...254
        ("Signature", USHORT, 8),  # Word 255
        ("CheckSum", USHORT, 8),
    ]


PIDENTIFY_DEVICE_DATA = POINTER(IDENTIFY_DEVICE_DATA)
_pack_ -= 1

# identify packet data (response to 0xA1)
_pack_ += 1


class IDENTIFY_PACKET_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "GeneralConfiguration",
            make_struct(
                [
                    ("PacketType", USHORT, 2),  # 00b = 12 byte command packet; 01b = 16 byte command packet
                    ("IncompleteResponse", USHORT, 1),  # Incomplete response
                    ("Reserved1", USHORT, 2),
                    (
                        "DrqDelay",
                        USHORT,
                        2,
                    ),  # 00b = Device shall set DRQ to one within 3 ms of receiving PACKET command. 10b = Device shall set DRQ to one within 50 us of receiving PACKET command.
                    ("RemovableMedia", USHORT, 1),  # obsolete
                    (
                        "CommandPacketType",
                        USHORT,
                        5,
                    ),  # This value follows the peripheral device type as defined in SPC-4 (e.g., 05h indicates a CD/DVD device).
                    ("Reserved2", USHORT, 1),
                    ("DeviceType", USHORT, 2),  # 10b = ATAPI device
                ],
                _pack_,
            ),
        ),
        ("ResevedWord1", USHORT),  # word 1
        ("UniqueConfiguration", USHORT),  # word 2
        ("ReservedWords3", USHORT * 7),  # word 3...9
        ("SerialNumber", UCHAR * 20),  # word 10...19
        ("ReservedWords20", USHORT * 3),  # word 20...22
        ("FirmwareRevision", UCHAR * 8),  # word 23...26
        ("ModelNumber", UCHAR * 40),  # word 27...46
        ("ReservedWords47", USHORT * 2),  # word 47...48
        (
            "Capabilities",
            make_struct(
                [  # word 49...50
                    ("VendorSpecific", USHORT, 8),
                    ("DmaSupported", USHORT, 1),
                    ("LbaSupported", USHORT, 1),  # shall be set to 1
                    ("IordyDisabled", USHORT, 1),
                    ("IordySupported", USHORT, 1),
                    ("Obsolete", USHORT, 1),
                    ("OverlapSupported", USHORT, 1),  # obsolete
                    ("QueuedCommandsSupported", USHORT, 1),  # obsolete
                    ("InterleavedDmaSupported", USHORT, 1),  # obsolete
                    (
                        "DeviceSpecificStandbyTimerValueMin",
                        USHORT,
                        1,
                    ),  # Shall be set to one to indicate a device specific Standby timer value minimum.
                    ("Obsolete1", USHORT, 1),
                    ("ReservedWord50", USHORT, 12),
                    ("WordValid", USHORT, 2),  # value shall be 01b
                ],
                _pack_,
            ),
        ),
        ("ObsoleteWords51", USHORT * 2),
        (
            "TranslationFieldsValid",
            USHORT,
            3,
        ),  # word 53.  bit 0 - obsolete; bit 1 - words 64..70 are valid; bit 2 -  word 88 is valid
        ("Reserved3", USHORT, 13),
        ("ReservedWords54", USHORT * 8),  # word 54...61
        (
            "DMADIR",
            make_struct(
                [  # word 62
                    ("UDMA0Supported", USHORT, 1),
                    ("UDMA1Supported", USHORT, 1),
                    ("UDMA2Supported", USHORT, 1),
                    ("UDMA3Supported", USHORT, 1),
                    ("UDMA4Supported", USHORT, 1),
                    ("UDMA5Supported", USHORT, 1),
                    ("UDMA6Supported", USHORT, 1),
                    ("MDMA0Supported", USHORT, 1),
                    ("MDMA1Supported", USHORT, 1),
                    ("MDMA2Supported", USHORT, 1),
                    ("DMASupported", USHORT, 1),
                    ("ReservedWord62", USHORT, 4),
                    ("DMADIRBitRequired", USHORT, 1),  # DMADIR bit in the PACKET command is required for DMA transfers
                ],
                _pack_,
            ),
        ),
        ("MultiWordDMASupport", USHORT, 8),  # word 63
        ("MultiWordDMAActive", USHORT, 8),
        ("AdvancedPIOModes", USHORT, 8),  # word 64
        ("ReservedByte64", USHORT, 8),
        (
            "MinimumMWXferCycleTime",
            USHORT,
        ),  # word 65. Minimum Multiword DMA transfer cycle time per word. Cycle time in nanoseconds
        (
            "RecommendedMWXferCycleTime",
            USHORT,
        ),  # word 66. Manufacturer recommended Multiword DMA transfer cycle time. Cycle time in nanoseconds
        (
            "MinimumPIOCycleTime",
            USHORT,
        ),  # word 67. Minimum PIO transfer cycle time without flow control. Cycle time in nanoseconds
        (
            "MinimumPIOCycleTimeIORDY",
            USHORT,
        ),  # word 68. Minimum PIO transfer cycle time with IORDY. Cycle time in nanoseconds
        ("ReservedWords69", USHORT * 2),  # word 69...70
        ("BusReleaseDelay", USHORT),  # word 71. obsolete
        ("ServiceCommandDelay", USHORT),  # word 72. obsolete
        ("ReservedWords73", USHORT * 2),  # word 73...74
        # Word 75. obsolete
        ("QueueDepth", USHORT, 5),
        ("ReservedWord75", USHORT, 11),
        (
            "SerialAtaCapabilities",
            make_struct(
                [
                    # Word 76
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("SataGen1", USHORT, 1),  # The SATA Gen1 Signaling Speed (1.5Gb/s) is supported
                    ("SataGen2", USHORT, 1),  # The SATA Gen2 Signaling Speed (3.0Gb/s) is supported
                    ("SataGen3", USHORT, 1),  # The SATA Gen3 Signaling Speed (6.0Gb/s) is supported
                    ("Reserved1", USHORT, 5),
                    ("HIPM", USHORT, 1),  # Support HIPM
                    ("PhyEvents", USHORT, 1),  # The SATA Phy Event Counters log is supported
                    ("Reserved3", USHORT, 2),
                    ("HostAutoPS", USHORT, 1),  # Supports Host Automatic Partial to Slumber transitions
                    ("DeviceAutoPS", USHORT, 1),  # Supports Device Automatic Partial to Slumber transitions
                    ("Reserved4", USHORT, 1),
                    # Word 77
                    ("Reserved5", USHORT, 1),  # shall be set to 0
                    ("CurrentSpeed", USHORT, 3),  # Coded value indicating current negotiated Serial ATA signal speed
                    ("SlimlineDeviceAttention", USHORT, 1),  # Supports Device Attention on slimline connected device
                    ("HostEnvironmentDetect", USHORT, 1),  # Supports host environment detect
                    ("Reserved", USHORT, 10),
                ],
                _pack_,
            ),
        ),
        # Word 78
        (
            "SerialAtaFeaturesSupported",
            make_struct(
                [
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("Reserved1", USHORT, 2),
                    ("DIPM", USHORT, 1),  # Device initiated power management is supported
                    ("Reserved2", USHORT, 1),
                    ("AsynchronousNotification", USHORT, 1),  # Asynchronous notification supported
                    ("SoftwareSettingsPreservation", USHORT, 1),  # The SSP feature set is supported
                    ("Reserved3", USHORT, 9),
                ],
                _pack_,
            ),
        ),
        # Word 79
        (
            "SerialAtaFeaturesEnabled",
            make_struct(
                [
                    ("Reserved0", USHORT, 1),  # shall be set to 0
                    ("Reserved1", USHORT, 2),
                    ("DIPM", USHORT, 1),  # Device initiated power management is enabled
                    ("Reserved2", USHORT, 1),
                    ("AsynchronousNotification", USHORT, 1),  # Asynchronous notification enabled
                    ("SoftwareSettingsPreservation", USHORT, 1),  # The SSP feature set is enabled
                    ("DeviceAutoPS", USHORT, 1),  # Device Automatic Partial to Slumber transitions enabled
                    ("Reserved3", USHORT, 8),
                ],
                _pack_,
            ),
        ),
        (
            "MajorRevision",
            USHORT,
        ),  # word 80. 0000h or FFFFh = device does not report version; bit 0...4 obsolete; bit 5 - ATA5 is supported; bit 6 - ATA6 is supported; bit 7 - ATA7 is supported; bit 8 - ATA8-ACS is supported;
        ("MinorRevision", USHORT),  # word 81
        (
            "CommandSetSupport",
            make_struct(
                [  # word 82...83
                    (
                        "SmartCommands",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the SMART feature set is not supported
                    ("SecurityMode", USHORT, 1),  # The Security feature set is supported
                    ("RemovableMedia", USHORT, 1),  # obsolete
                    ("PowerManagement", USHORT, 1),  # The Power Management feature set supported
                    (
                        "PacketCommands",
                        USHORT,
                        1,
                    ),  # Shall be set to one indicating the PACKET feature set is supported.
                    ("WriteCache", USHORT, 1),  # The volatile write cache is supported
                    ("LookAhead", USHORT, 1),  # Read look-ahead supported
                    ("ReleaseInterrupt", USHORT, 1),  # obsolete
                    ("ServiceInterrupt", USHORT, 1),  # obsolete
                    (
                        "DeviceReset",
                        USHORT,
                        1,
                    ),  # Shall be set to one to indicate that the DEVICE RESET command is supported
                    ("HostProtectedArea", USHORT, 1),  # obsolete
                    ("Obsolete1", USHORT, 1),
                    (
                        "WriteBuffer",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the WRITE BUFFER command is not supported
                    (
                        "ReadBuffer",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the READ BUFFER command is not supported
                    ("Nop", USHORT, 1),  # Shall be set to one to indicate that the NOP command is supported
                    ("Obsolete2", USHORT, 1),
                    (
                        "DownloadMicrocode",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the DOWNLOAD MICROCODE command is not supported
                    ("Reserved1", USHORT, 2),
                    ("AdvancedPm", USHORT, 1),  # The APM feature set is supported
                    ("Msn", USHORT, 1),  # obsolete
                    ("PowerUpInStandby", USHORT, 1),  # The PUIS feature set is supported
                    ("ManualPowerUp", USHORT, 1),  # The SET FEATURES subcommand is required to spin-up after power-up
                    ("Reserved2", USHORT, 1),
                    ("SetMax", USHORT, 1),  # obsolete
                    ("Reserved3", USHORT, 3),
                    ("FlushCache", USHORT, 1),  # The FLUSH CACHE command is supported
                    ("Reserved4", USHORT, 1),
                    ("WordValid", USHORT, 2),  # shall be 01b
                ],
                _pack_,
            ),
        ),
        (
            "CommandSetSupportExt",
            make_struct(
                [  # word 84
                    ("Reserved0", USHORT, 5),
                    ("GpLogging", USHORT, 1),  # The GPL feature set is supported
                    ("Reserved1", USHORT, 2),
                    ("WWN64Bit", USHORT, 1),  # shall be set to one to indicate that the mandator WWN is supported
                    ("Reserved2", USHORT, 5),
                    ("WordValid", USHORT, 2),  # shall be 01b
                ],
                _pack_,
            ),
        ),
        (
            "CommandSetActive",
            make_struct(
                [  # word 85...86
                    (
                        "SmartCommands",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the SMART feature set is not supported
                    ("SecurityMode", USHORT, 1),  # The Security feature set is enabled
                    ("RemovableMedia", USHORT, 1),  # obsolete
                    ("PowerManagement", USHORT, 1),  # Power Management feature set is enabled
                    (
                        "PacketCommands",
                        USHORT,
                        1,
                    ),  # Shall be set to one indicating the PACKET feature set is supported.
                    ("WriteCache", USHORT, 1),  # The volatile write cache is enabled
                    ("LookAhead", USHORT, 1),  # Read look-ahead is enabled
                    ("ReleaseInterrupt", USHORT, 1),  # obsolete
                    ("ServiceInterrupt", USHORT, 1),  # obsolete
                    (
                        "DeviceReset",
                        USHORT,
                        1,
                    ),  # Shall be set to one to indicate that the DEVICE RESET command is supported
                    ("HostProtectedArea", USHORT, 1),  # obsolete
                    ("Obsolete1", USHORT, 1),
                    (
                        "WriteBuffer",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the WRITE BUFFER command is not supported
                    (
                        "ReadBuffer",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the READ BUFFER command is not supported
                    ("Nop", USHORT, 1),  # Shall be set to one to indicate that the NOP command is supported
                    ("Obsolete2", USHORT, 1),
                    (
                        "DownloadMicrocode",
                        USHORT,
                        1,
                    ),  # Shall be cleared to zero to indicate that the DOWNLOAD MICROCODE command is not supported
                    ("Reserved1", USHORT, 2),
                    ("AdvancedPm", USHORT, 1),  # The APM feature set is enabled
                    ("Msn", USHORT, 1),  # obsolete
                    ("PowerUpInStandby", USHORT, 1),  # The PUIS feature set is enabled
                    ("ManualPowerUp", USHORT, 1),  # SET FEATURES subcommand required to spin-up after power-up
                    ("Reserved2", USHORT, 1),
                    ("SetMax", USHORT, 1),  # obsolete
                    ("Reserved3", USHORT, 3),
                    ("FlushCache", USHORT, 1),  # The FLUSH CACHE command is supported
                    ("Reserved", USHORT, 3),
                ],
                _pack_,
            ),
        ),
        (
            "CommandSetActiveExt",
            make_struct(
                [  # word 87
                    ("Reserved0", USHORT, 5),
                    ("GpLogging", USHORT, 1),  # This bit is a copy of word 84 bit 5
                    ("Reserved1", USHORT, 2),
                    ("WWN64Bit", USHORT, 1),  # shall be set to one to indicate that the mandator WWN is supported
                    ("Reserved2", USHORT, 5),
                    ("WordValid", USHORT, 2),  # shall be 01b
                ],
                _pack_,
            ),
        ),
        ("UltraDMASupport", USHORT, 8),  # word 88
        ("UltraDMAActive", USHORT, 8),
        ("TimeRequiredForNormalEraseModeSecurityEraseUnit", USHORT),  # word 89
        ("TimeRequiredForEnhancedEraseModeSecurityEraseUnit", USHORT),  # word 90
        ("CurrentAPMLevel", USHORT),  # word 91
        ("MasterPasswordID", USHORT),  # word 92
        ("HardwareResetResult", USHORT),  # word 93
        ("ReservedWords94", USHORT * 14),  # word 94...107
        ("WorldWideName", USHORT * 4),  # word 108...111
        ("ReservedWords112", USHORT * 13),  # word 112...124
        ("AtapiZeroByteCount", USHORT),  # word 125
        ("ReservedWord126", USHORT),  # word 126. obsolete
        ("MsnSupport", USHORT, 2),  # word 127. obsolete
        ("ReservedWord127", USHORT, 14),
        ("SecurityStatus", USHORT),  # word 128
        ("VendorSpecific", USHORT * 31),  # Word 129...159
        ("ReservedWord160", USHORT * 16),  # Word 160...175. Reserved for assignment by the CompactFlash Association
        ("ReservedWord176", USHORT * 46),  # Word 176...221
        (
            "TransportMajorVersion",
            make_struct(
                [  # Word 222 Transport major version number.  0000h or FFFFh = device does not report version
                    ("MajorVersion", USHORT, 12),
                    ("TransportType", USHORT, 4),
                ],
                _pack_,
            ),
        ),
        ("TransportMinorVersion", USHORT),  # Word 223
        ("ReservedWord224", USHORT * 31),  # Word 224...254
        ("Signature", USHORT, 8),
        ("CheckSum", USHORT, 8),
    ]


PIDENTIFY_PACKET_DATA = POINTER(IDENTIFY_PACKET_DATA)
_pack_ -= 1

# Register FIS
_pack_ += 1


class REGISTER_FIS(Structure):
    _pack_ = _pack_
    _fields_ = [
        # dword 0
        ("FisType", UCHAR),
        ("Reserved0", UCHAR, 7),
        ("CmdReg", UCHAR, 1),
        ("Command", UCHAR),
        ("Features", UCHAR),
        # dword 1
        ("SectorNumber", UCHAR),
        ("CylinderLow", UCHAR),
        ("CylinderHigh", UCHAR),
        ("DeviceHead", UCHAR),
        # dword 2
        ("SectorNumberExp", UCHAR),
        ("CylinderLowExp", UCHAR),
        ("CylinderHighExp", UCHAR),
        ("FeaturesExp", UCHAR),
        # dword 3
        ("SectorCount", UCHAR),
        ("SectorCountExp", UCHAR),
        ("Reserved2", UCHAR),
        ("Control", UCHAR),
        # dword 4
        ("Reserved3", ULONG),
    ]


PREGISTER_FIS = POINTER(REGISTER_FIS)
_pack_ -= 1

# ATAPI specific scsiops
ATAPI_MODE_SENSE = 0x5A
ATAPI_MODE_SELECT = 0x55
ATAPI_LS120_FORMAT_UNIT = 0x24

# IDE driveSelect register bit for LBA mode
IDE_LBA_MODE = 1 << 6

# IDE drive control definitions
IDE_DC_DISABLE_INTERRUPTS = 0x02
IDE_DC_RESET_CONTROLLER = 0x04
IDE_DC_REENABLE_CONTROLLER = 0x00

# IDE status definitions
IDE_STATUS_ERROR = 0x01
IDE_STATUS_INDEX = 0x02
IDE_STATUS_CORRECTED_ERROR = 0x04
IDE_STATUS_DRQ = 0x08
IDE_STATUS_DSC = 0x10
IDE_STATUS_DEVICE_FAULT = 0x20
IDE_STATUS_DRDY = 0x40
IDE_STATUS_IDLE = 0x50
IDE_STATUS_BUSY = 0x80

# IDE error definitions
IDE_ERROR_BAD_BLOCK = 0x80
IDE_ERROR_CRC_ERROR = IDE_ERROR_BAD_BLOCK
IDE_ERROR_DATA_ERROR = 0x40
IDE_ERROR_MEDIA_CHANGE = 0x20
IDE_ERROR_ID_NOT_FOUND = 0x10
IDE_ERROR_MEDIA_CHANGE_REQ = 0x08
IDE_ERROR_COMMAND_ABORTED = 0x04
IDE_ERROR_END_OF_MEDIA = 0x02
IDE_ERROR_ILLEGAL_LENGTH = 0x01
IDE_ERROR_ADDRESS_NOT_FOUND = IDE_ERROR_ILLEGAL_LENGTH


# IDE command definitions
IDE_COMMAND_NOP = 0x00
IDE_COMMAND_DATA_SET_MANAGEMENT = 0x06
IDE_COMMAND_ATAPI_RESET = 0x08
IDE_COMMAND_GET_PHYSICAL_ELEMENT_STATUS = 0x12
IDE_COMMAND_READ = 0x20
IDE_COMMAND_READ_EXT = 0x24
IDE_COMMAND_READ_DMA_EXT = 0x25
IDE_COMMAND_READ_DMA_QUEUED_EXT = 0x26
IDE_COMMAND_READ_MULTIPLE_EXT = 0x29
IDE_COMMAND_READ_LOG_EXT = 0x2F
IDE_COMMAND_WRITE = 0x30
IDE_COMMAND_WRITE_EXT = 0x34
IDE_COMMAND_WRITE_DMA_EXT = 0x35
IDE_COMMAND_WRITE_DMA_QUEUED_EXT = 0x36
IDE_COMMAND_WRITE_MULTIPLE_EXT = 0x39
IDE_COMMAND_WRITE_DMA_FUA_EXT = 0x3D
IDE_COMMAND_WRITE_DMA_QUEUED_FUA_EXT = 0x3E
IDE_COMMAND_WRITE_LOG_EXT = 0x3F
IDE_COMMAND_VERIFY = 0x40
IDE_COMMAND_VERIFY_EXT = 0x42
IDE_COMMAND_ZAC_MANAGEMENT_IN = 0x4A  # Report Zones Ext
IDE_COMMAND_WRITE_LOG_DMA_EXT = 0x57
IDE_COMMAND_TRUSTED_NON_DATA = 0x5B
IDE_COMMAND_TRUSTED_RECEIVE = 0x5C
IDE_COMMAND_TRUSTED_RECEIVE_DMA = 0x5D
IDE_COMMAND_TRUSTED_SEND = 0x5E
IDE_COMMAND_TRUSTED_SEND_DMA = 0x5F
IDE_COMMAND_READ_FPDMA_QUEUED = 0x60  # NCQ Read command
IDE_COMMAND_WRITE_FPDMA_QUEUED = 0x61  # NCQ Write command
IDE_COMMAND_NCQ_NON_DATA = 0x63  # NCQ Non-Data command
IDE_COMMAND_SEND_FPDMA_QUEUED = 0x64  # NCQ Send command
IDE_COMMAND_RECEIVE_FPDMA_QUEUED = 0x65  # NCQ Receive command
IDE_COMMAND_SET_DATE_AND_TIME = 0x77  # optional 48bit command
IDE_COMMAND_REMOVE_ELEMENT_AND_TRUNCATE = 0x7C
IDE_COMMAND_EXECUTE_DEVICE_DIAGNOSTIC = 0x90
IDE_COMMAND_SET_DRIVE_PARAMETERS = 0x91
IDE_COMMAND_DOWNLOAD_MICROCODE = 0x92  # Optional 28bit command
IDE_COMMAND_DOWNLOAD_MICROCODE_DMA = 0x93  # Optional 28bit command
IDE_COMMAND_ZAC_MANAGEMENT_OUT = 0x9F  # Close Zone Ext; Finish Zone Ext; Open Zone Ext; Reset Write Pointer Ext.
IDE_COMMAND_ATAPI_PACKET = 0xA0
IDE_COMMAND_ATAPI_IDENTIFY = 0xA1
IDE_COMMAND_SMART = 0xB0
IDE_COMMAND_READ_LOG_DMA_EXT = 0xB1
IDE_COMMAND_SANITIZE_DEVICE = 0xB4
IDE_COMMAND_READ_MULTIPLE = 0xC4
IDE_COMMAND_WRITE_MULTIPLE = 0xC5
IDE_COMMAND_SET_MULTIPLE = 0xC6
IDE_COMMAND_READ_DMA = 0xC8
IDE_COMMAND_WRITE_DMA = 0xCA
IDE_COMMAND_WRITE_DMA_QUEUED = 0xCC
IDE_COMMAND_WRITE_MULTIPLE_FUA_EXT = 0xCE
IDE_COMMAND_GET_MEDIA_STATUS = 0xDA
IDE_COMMAND_DOOR_LOCK = 0xDE
IDE_COMMAND_DOOR_UNLOCK = 0xDF
IDE_COMMAND_STANDBY_IMMEDIATE = 0xE0
IDE_COMMAND_IDLE_IMMEDIATE = 0xE1
IDE_COMMAND_CHECK_POWER = 0xE5
IDE_COMMAND_SLEEP = 0xE6
IDE_COMMAND_FLUSH_CACHE = 0xE7
IDE_COMMAND_FLUSH_CACHE_EXT = 0xEA
IDE_COMMAND_IDENTIFY = 0xEC
IDE_COMMAND_MEDIA_EJECT = 0xED
IDE_COMMAND_SET_FEATURE = 0xEF
IDE_COMMAND_SECURITY_SET_PASSWORD = 0xF1
IDE_COMMAND_SECURITY_UNLOCK = 0xF2
IDE_COMMAND_SECURITY_ERASE_PREPARE = 0xF3
IDE_COMMAND_SECURITY_ERASE_UNIT = 0xF4
IDE_COMMAND_SECURITY_FREEZE_LOCK = 0xF5
IDE_COMMAND_SECURITY_DISABLE_PASSWORD = 0xF6
IDE_COMMAND_NOT_VALID = 0xFF

# IDE Set Transfer Mode
# define IDE_SET_DEFAULT_PIO_MODE(mode)      ((UCHAR) 1)     # disable I/O Ready
# define IDE_SET_ADVANCE_PIO_MODE(mode)      ((UCHAR) ((1 << 3) | (mode)))
# define IDE_SET_SWDMA_MODE(mode)            ((UCHAR) ((1 << 4) | (mode)))
# define IDE_SET_MWDMA_MODE(mode)            ((UCHAR) ((1 << 5) | (mode)))
# define IDE_SET_UDMA_MODE(mode)             ((UCHAR) ((1 << 6) | (mode)))

# Set features parameter list
IDE_FEATURE_ENABLE_WRITE_CACHE = 0x2
IDE_FEATURE_SET_TRANSFER_MODE = 0x3
IDE_FEATURE_ENABLE_PUIS = 0x6
IDE_FEATURE_PUIS_SPIN_UP = 0x7
IDE_FEATURE_ENABLE_SATA_FEATURE = 0x10
IDE_FEATURE_DISABLE_MSN = 0x31
IDE_FEATURE_DISABLE_REVERT_TO_POWER_ON = 0x66
IDE_FEATURE_DISABLE_WRITE_CACHE = 0x82
IDE_FEATURE_DISABLE_PUIS = 0x86
IDE_FEATURE_DISABLE_SATA_FEATURE = 0x90
IDE_FEATURE_ENABLE_MSN = 0x95

# SATA Features Sector Count parameter list

IDE_SATA_FEATURE_NON_ZERO_DMA_BUFFER_OFFSET = 0x1
IDE_SATA_FEATURE_DMA_SETUP_FIS_AUTO_ACTIVATE = 0x2
IDE_SATA_FEATURE_DEVICE_INITIATED_POWER_MANAGEMENT = 0x3
IDE_SATA_FEATURE_GUARANTEED_IN_ORDER_DELIVERY = 0x4
IDE_SATA_FEATURE_ASYNCHRONOUS_NOTIFICATION = 0x5
IDE_SATA_FEATURE_SOFTWARE_SETTINGS_PRESERVATION = 0x6
IDE_SATA_FEATURE_DEVICE_AUTO_PARTIAL_TO_SLUMBER = 0x7
IDE_SATA_FEATURE_ENABLE_HARDWARE_FEATURE_CONTROL = 0x8
IDE_SATA_FEATURE_DEVSLP = 0x9
IDE_SATA_FEATURE_HYBRID_INFORMATION = 0xA

# SMART sub command list
IDE_SMART_READ_ATTRIBUTES = 0xD0
IDE_SMART_READ_THRESHOLDS = 0xD1
IDE_SMART_ENABLE_DISABLE_AUTOSAVE = 0xD2
IDE_SMART_SAVE_ATTRIBUTE_VALUES = 0xD3
IDE_SMART_EXECUTE_OFFLINE_DIAGS = 0xD4
IDE_SMART_READ_LOG = 0xD5
IDE_SMART_WRITE_LOG = 0xD6
IDE_SMART_ENABLE = 0xD8
IDE_SMART_DISABLE = 0xD9
IDE_SMART_RETURN_STATUS = 0xDA
IDE_SMART_ENABLE_DISABLE_AUTO_OFFLINE = 0xDB

# Features for IDE_COMMAND_DATA_SET_MANAGEMENT
IDE_DSM_FEATURE_TRIM = 0x0001  # bit 0 of WORD

# NCQ sub command list

# SubCommand of IDE_COMMAND_NCQ_NON_DATA
IDE_NCQ_NON_DATA_ABORT_NCQ_QUEUE = 0x00
IDE_NCQ_NON_DATA_DEADLINE_HANDLING = 0x01
IDE_NCQ_NON_DATA_HYBRID_CHANGE_BY_SIZE = 0x02  # this subCommand has been renamed to Hybrid Demote by Size.
IDE_NCQ_NON_DATA_HYBRID_DEMOTE_BY_SIZE = 0x02
IDE_NCQ_NON_DATA_HYBRID_CHANGE_BY_LBA_RANGE = 0x03
IDE_NCQ_NON_DATA_HYBRID_CONTROL = 0x04

# SubCommand of IDE_COMMAND_SEND_FPDMA_QUEUED
IDE_NCQ_SEND_DATA_SET_MANAGEMENT = 0x00
IDE_NCQ_SEND_HYBRID_EVICT = 0x01

# "Hybrid Information Field Bits" structure definition. e.g. Auxiliary(23:16) field.
_pack_ += 1


class ATA_HYBRID_INFO_FIELDS(Union):
    _pack_ = _pack_
    _fields_ = [
        (
            "_unnamed_struct",
            make_struct(
                [
                    ("HybridPriority", UCHAR, 4),
                    ("Reserved0", UCHAR, 1),
                    ("InfoValid", UCHAR, 1),
                    ("Reserved1", UCHAR, 2),
                ],
                _pack_,
            ),
        ),
        ("AsUchar", UCHAR),
    ]


PATA_HYBRID_INFO_FIELDS = POINTER(ATA_HYBRID_INFO_FIELDS)
_pack_ -= 1

# "Device Set Password " structure definition.
_pack_ += 1


class DEVICE_SET_PASSWORD(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "ControlWord",
            make_struct(
                [
                    ("PasswordIdentifier", USHORT, 1),  # (0 - set user password, 1 = set master password)
                    ("Reserved1", USHORT, 7),
                    ("MasterPasswordCapability", USHORT, 1),  # (0 = High, 1 = Maximum)
                    ("Reserved2", USHORT, 7),
                ],
                _pack_,
            ),
        ),
        ("Password", USHORT * 16),  # Bytes 2-33
        ("MasterPasswordIdentifier", USHORT),  # byte 34
        ("Reserved", USHORT * 238),  # Bytes 36-511
    ]


PDEVICE_SET_PASSWORD = POINTER(DEVICE_SET_PASSWORD)
_pack_ -= 1

ATA_DEVICE_SET_PASSWORD_MASTER = 0x01
ATA_DEVICE_SET_PASSWORD_USER = 0x00


# Features and definitions for IDE_COMMAND_READ_LOG_EXT, aka general purpose logging

"""
    Table A.2 from ACS-4 , snapshot as of June 2010

    Log     Address     Log     Name    Feature     Set     R/W     Access
    =======================================================================
    00h     Log directory, see A.2 and A.3 N/A RO GPL,SL
    01h Summary SMART Error Log, see A.16 SMART RO SL
    02h Comprehensive SMART Error Log, see A.4 SMART RO SL
    03h Extended Comprehensive SMART Error Log,
    see A.7
    SMART RO GPL
    04h Device Statistics, see A.5 N/A RO GPL,SL
    05h Reserved
    06h SMART Self-Test Log, see A.15 SMART RO SL
    07h Extended SMART Self-Test Log, see A.8 SMART RO GPL
    08h Reserved N/A Reserved
    09h Selective Self-Test Log, see A.14 SMART R/W SL
    0Ah-0Ch Reserved N/A Reserved
    0Dh LPS Mis-alignment log, see A.10 LPS RO GPL,SL
    0Eh-0Fh Reserved
    10h NCQ Command Error, see A.11 NCQ RO GPL
    11h SATA Phy Event Counters, see A.13 N/A RO GPL
    12h-17h Reserved for Serial ATA N/A Reserved
    18h-1Fh Reserved N/A Reserved
    20h Obsolete
    21h Write Stream Error Log, see A.17 Streaming RO GPL
    22h Read Stream Error Log, see A.12 Streaming RO GPL
    23h Obsolete
    24h-7Fh Reserved N/A Reserved
    80h-9Fh Host Vendor Specific, see A.9 SMART R/W GPL,SL
    A0h-DFh Device Vendor Specific, see A.6 SMART VS GPL,SL
    E0h SCT Command/Status, see 8.1 SCT R/W GPL,SL
    E1h SCT Data Transfer, see 8.1 SCT R/W GPL,SL
    E2h-FFh Reserved N/A

    Table A3 - General Purpose Log Directory

    Word Description
    ===============================================
    0 General Purpose Logging Version (word)
    1 Number of log pages at log address 01h (word)
    2 Number of log pages at log address 02h (word)
    3 Number of log pages at log address 03h (word)
    4 Number of log pages at log address 04h (word)

    128 Number of log pages at log address 80h (word)
    129 Number of log pages at log address 81h (word)

    255 Number of log pages at log address FFh (word)
"""

# GP Log directory resides at the address 0

IDE_GP_LOG_DIRECTORY_ADDRESS = 0x00

IDE_GP_SUMMARY_SMART_ERROR = 0x01  # Access: SMART Logging
IDE_GP_COMPREHENSIVE_SMART_ERROR = 0x02  # Access: SMART Logging
IDE_GP_EXTENDED_COMPREHENSIVE_SMART_ERROR = 0x03
IDE_GP_LOG_DEVICE_STATISTICS_ADDRESS = 0x04
IDE_GP_SMART_SELF_TEST = 0x06  # Access: SMART Logging
IDE_GP_EXTENDED_SMART_SELF_TEST = 0x07
IDE_GP_LOG_POWER_CONDITIONS = 0x08
IDE_GP_SELECTIVE_SELF_TEST = 0x09  # Access: SMART Logging
IDE_GP_DEVICE_STATISTICS_NOTIFICATION = 0x0A
IDE_GP_PENDING_DEFECTS = 0x0C
IDE_GP_LPS_MISALIGNMENT = 0x0D

IDE_GP_LOG_NCQ_COMMAND_ERROR_ADDRESS = 0x10
IDE_GP_LOG_PHY_EVENT_COUNTER_ADDRESS = 0x11
IDE_GP_LOG_NCQ_NON_DATA_ADDRESS = 0x12
IDE_GP_LOG_NCQ_SEND_RECEIVE_ADDRESS = 0x13
IDE_GP_LOG_HYBRID_INFO_ADDRESS = 0x14
IDE_GP_LOG_REBUILD_ASSIST = 0x15
IDE_GP_LOG_LBA_STATUS = 0x19

IDE_GP_LOG_WRITE_STREAM_ERROR = 0x21
IDE_GP_LOG_READ_STREAM_ERROR = 0x22
IDE_GP_LOG_CURRENT_DEVICE_INTERNAL_STATUS = 0x24
IDE_GP_LOG_SAVED_DEVICE_INTERNAL_STATUS = 0x25

IDE_GP_LOG_IDENTIFY_DEVICE_DATA_ADDRESS = 0x30

IDE_GP_LOG_SCT_COMMAND_STATUS = 0xE0
IDE_GP_LOG_SCT_DATA_TRANSFER = 0xE1

IDE_GP_LOG_SECTOR_SIZE = (
    0x200  # 512 bytes - independent of the device media sector / block size GP log sector size is always 512
)
IDE_GP_LOG_VERSION = 0x0001

IDE_GP_LOG_SUPPORTED_PAGES = 0x00  # common value used by multiple Log Address if multiple pages supported


# Log page for Identify Device Data log
IDE_GP_LOG_IDENTIFY_DEVICE_DATA_SUPPORTED_CAPABILITIES_PAGE = 0x03
IDE_GP_LOG_IDENTIFY_DEVICE_DATA_SATA_PAGE = 0x08
IDE_GP_LOG_IDENTIFY_DEVICE_DATA_ZONED_DEVICE_INFORMATION_PAGE = 0x09

_pack_ += 1


class IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("RevisionNumber", ULONGLONG, 16),  # Shall be set to 0001h
        ("PageNumber", ULONGLONG, 8),  # Shall be set to the page number
        ("Reserved", ULONGLONG, 39),
        ("Valid", ULONGLONG, 1),
    ]


PIDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER = POINTER(IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER)
_pack_ -= 1

# Values of ZonedCapabilities.Zoned field.
ATA_ZONED_CAPABILITIES_NOT_REPORTED = 0x0
ATA_ZONED_CAPABILITIES_HOST_AWARE = 0x1
ATA_ZONED_CAPABILITIES_DEVICE_MANAGED = 0x2

_pack_ += 1


class IDENTIFY_DEVICE_DATA_LOG_PAGE_SUPPORTED_CAPABILITIES(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER),  # byte 0..7
        (
            "SupportedCapabilities",
            make_struct(
                [
                    ("WRV", ULONGLONG, 1),
                    ("WriteUncorrectable", ULONGLONG, 1),
                    ("GplDma", ULONGLONG, 1),
                    ("DmMode3", ULONGLONG, 1),
                    ("FreeFall", ULONGLONG, 1),
                    ("SenseData", ULONGLONG, 1),
                    ("EPC", ULONGLONG, 1),
                    ("SmartErrorLogging", ULONGLONG, 1),
                    ("SmartSelfTest", ULONGLONG, 1),
                    ("Reserved9", ULONGLONG, 1),
                    ("Streaming", ULONGLONG, 1),
                    ("GPL", ULONGLONG, 1),
                    ("WriteFuaExt", ULONGLONG, 1),
                    ("Unload", ULONGLONG, 1),
                    ("DownloadMicrocode", ULONGLONG, 1),
                    ("Reserved15ForCFA", ULONGLONG, 1),
                    ("APM", ULONGLONG, 1),
                    ("PUIS", ULONGLONG, 1),
                    ("SpinUp", ULONGLONG, 1),
                    ("Reserved19", ULONGLONG, 1),
                    ("Cmd48Bit", ULONGLONG, 1),
                    ("Reserved21", ULONGLONG, 1),
                    ("FlushCacheExt", ULONGLONG, 1),
                    ("Smart", ULONGLONG, 1),
                    ("VolatileWriteCache", ULONGLONG, 1),
                    ("ReadLookahead", ULONGLONG, 1),
                    ("Reserved26", ULONGLONG, 1),
                    ("WriteBuffer", ULONGLONG, 1),
                    ("ReadBuffer", ULONGLONG, 1),
                    ("NOP", ULONGLONG, 1),
                    ("Reserved30", ULONGLONG, 1),
                    ("RZAT", ULONGLONG, 1),
                    ("Cmd28bit", ULONGLONG, 1),
                    ("DownloadMicrocodeDma", ULONGLONG, 1),
                    ("Reserved34", ULONGLONG, 1),
                    ("WriteBufferDma", ULONGLONG, 1),
                    ("ReadBufferDma", ULONGLONG, 1),
                    ("Reserved37", ULONGLONG, 1),
                    ("LpsMisalignmentReporting", ULONGLONG, 1),
                    ("DRAT", ULONGLONG, 1),
                    ("Reserved40ForCFA", ULONGLONG, 1),
                    ("AmaxAddr", ULONGLONG, 1),
                    ("SetEpcPowerSource", ULONGLONG, 1),
                    ("LowPowerStandby", ULONGLONG, 1),
                    ("DSN", ULONGLONG, 1),
                    ("RequestSenseDeviceFault", ULONGLONG, 1),
                    ("Reserved", ULONGLONG, 17),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 8..15
        (
            "DownloadMicrocodeCapabilities",
            make_struct(
                [
                    ("DmMinTransferSize", ULONGLONG, 16),
                    ("DmMaxTransferSize", ULONGLONG, 16),
                    ("DmOffsetsImmediateSupported", ULONGLONG, 1),  # subcommand 03h is supported.
                    ("DmImmediateSupported", ULONGLONG, 1),  # subcommand 07h is supported.
                    ("DmOffsetsDeferredSupported", ULONGLONG, 1),  # subcommand 0Eh and 0Fh are supported.
                    ("Reserved", ULONGLONG, 28),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 16..23
        (
            "NominalMediaRotationRate",
            make_struct(
                [
                    ("Rate", ULONGLONG, 16),
                    ("Reserved", ULONGLONG, 47),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 24..31
        (
            "NominalFormFactor",
            make_struct(
                [
                    ("Factor", ULONGLONG, 4),
                    ("Reserved", ULONGLONG, 59),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 32..39
        (
            "WRVSectorCountMode3",
            make_struct(
                [
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 31),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 40..47
        (
            "WRVSectorCountMode2",
            make_struct(
                [
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 31),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 48..55
        (
            "WorldWideName",
            make_struct(
                [
                    ("Name", ULONGLONG),
                    ("Reserved", ULONGLONG, 63),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 56..71
        (
            "DataSetManagement",
            make_struct(
                [
                    ("TrimSupported", ULONGLONG, 1),
                    ("Reserved", ULONGLONG, 62),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 72..79
        (
            "UtilizationPerUnitTime",
            make_struct(
                [
                    ("UtilizationA", ULONGLONG, 32),
                    ("UtilizationB", ULONGLONG, 32),
                    ("Reserved0", ULONGLONG, 32),
                    ("UtilizationInterval", ULONGLONG, 8),
                    ("UtilizationUnit", ULONGLONG, 8),
                    ("UtilizationType", ULONGLONG, 8),
                    ("Reserved1", ULONGLONG, 7),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 80..95
        (
            "UtilizationUsageRateSupport",
            make_struct(
                [
                    ("DateTimeRateBasisSupported", ULONGLONG, 1),
                    ("Reserved0", ULONGLONG, 3),
                    ("PowerOnHoursRateBasisSupported", ULONGLONG, 1),
                    ("Reserved1", ULONGLONG, 3),
                    ("SincePowerOnRateBasisSupported", ULONGLONG, 1),
                    ("Reserved2", ULONGLONG, 14),
                    ("SettingRateBasisSupported", ULONGLONG, 1),
                    ("Reserved3", ULONGLONG, 39),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 96..103
        (
            "ZonedCapabilities",
            make_struct(
                [
                    ("Zoned", ULONGLONG, 2),
                    ("Reserved", ULONGLONG, 61),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 104..111
        (
            "SupportedZacCapabilities",
            make_struct(
                [
                    ("ReportZonesExtSupported", ULONGLONG, 1),
                    ("NonDataOpenZoneExtSupported", ULONGLONG, 1),
                    ("NonDataCloseZoneExtSupported", ULONGLONG, 1),
                    ("NonDataFinishZoneExtSupported", ULONGLONG, 1),
                    ("NonDataResetWritePointersExtSupported", ULONGLONG, 1),
                    ("Reserved", ULONGLONG, 58),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 112..119
        ("Reserved", UCHAR * 392),  # byte 120..511
    ]


PIDENTIFY_DEVICE_DATA_LOG_PAGE_SUPPORTED_CAPABILITIES = POINTER(IDENTIFY_DEVICE_DATA_LOG_PAGE_SUPPORTED_CAPABILITIES)
_pack_ -= 1

# Data Structure of IDE_GP_LOG_IDENTIFY_DEVICE_DATA_ZONED_DEVICE_INFORMATION_PAGE
ZAC_REVISION_NOT_REPORTED_1 = 0x0000
ZAC_REVISION_NOT_REPORTED_2 = 0xFFFF
ZAC_REVISION_01 = 0xB6E8
ZAC_REVISION_04 = 0xA36C

_pack_ += 1


class IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER),  # byte 0..7
        (
            "ZonedDeviceCapabilities",
            make_struct(
                [
                    ("URSWRZ", ULONGLONG, 1),  # unrestricted read in sequential write required zone
                    ("Reserved", ULONGLONG, 62),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 8..15
        (
            "ZonedDeviceSettings",
            make_struct(
                [
                    ("Reserved", ULONGLONG, 63),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 16..23
        (
            "OptimalNumberOfOpenSequentialWritePreferredZones",
            make_struct(
                [
                    ("Number", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 31),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 24..31
        (
            "OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZones",
            make_struct(
                [
                    ("Number", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 31),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 32..39
        (
            "MaxNumberOfOpenSequentialWriteRequiredZones",
            make_struct(
                [
                    ("Number", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 31),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 40..47
        (
            "Version",
            make_struct(
                [
                    ("ZacMinorVersion", ULONGLONG, 16),
                    ("Reserved0", ULONGLONG, 47),
                    ("Valid", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),  # byte 48..55
        ("Reserved", UCHAR * 456),  # byte 56..511
    ]


PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO = POINTER(IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO)
_pack_ -= 1


# "Current Device Internal Status Data Log" structure definition.

CURRENT_DEVICE_INTERNAL_STATUS_DATA_LOG_ADDRESS = 0x24

_pack_ += 1


class CURRENT_DEVICE_INTERNAL_STATUS_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogAddress", UCHAR),  # Byte 0
        ("Reserved0", UCHAR * 3),  # Byte 1-3
        ("OrganizationID", ULONG),  # Bytes 4-7, 31:24 reserved, 23:0 - IEEE OUI
        ("Area1LastLogPage", USHORT),  # Bytes 8-9
        ("Area2LastLogPage", USHORT),  # Bytes 10-11
        ("Area3LastLogPage", USHORT),  # Bytes 12-13
        ("Reserved2", UCHAR * 368),  # Bytes 14-381
        ("SavedDataAvailable", UCHAR),  # Byte 382
        ("SavedDataGenerationNumber", UCHAR),  # Byte 383
        ("ReasonIdentifier", UCHAR * 128),  # Bytes 384-511
    ]


PCURRENT_DEVICE_INTERNAL_STATUS_LOG = POINTER(CURRENT_DEVICE_INTERNAL_STATUS_LOG)
_pack_ -= 1

# "Saved Device Internal Status Data Log" structure definition.

SAVED_DEVICE_INTERNAL_STATUS_DATA_LOG_ADDRESS = 0x25

_pack_ += 1


class SAVED_DEVICE_INTERNAL_STATUS_LOG(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("LogAddress", UCHAR),  # Byte 0
        ("Reserved0", UCHAR * 3),  # Byte 1-3
        ("OrganizationID", ULONG),  # Bytes 4-7, 31:24 reserved, 23:0 - IEEE OUI
        ("Area1LastLogPage", USHORT),  # Bytes 8-9
        ("Area2LastLogPage", USHORT),  # Bytes 10-11
        ("Area3LastLogPage", USHORT),  # Bytes 12-13
        ("Reserved2", UCHAR * 368),  # Bytes 14-381
        ("SavedDataAvailable", UCHAR),  # Byte 382
        ("GenerationNumber", UCHAR),  # Byte 383
        ("ReasonIdentifier", UCHAR * 128),  # Bytes 384-511
    ]


PSAVED_DEVICE_INTERNAL_STATUS_LOG = POINTER(SAVED_DEVICE_INTERNAL_STATUS_LOG)
_pack_ -= 1


# Log page for Device Statistics log

IDE_GP_LOG_DEVICE_STATISTICS_GENERAL_PAGE = 0x01
IDE_GP_LOG_DEVICE_STATISTICS_FREE_FALL_PAGE = 0x02
IDE_GP_LOG_DEVICE_STATISTICS_ROTATING_MEDIA_PAGE = 0x03
IDE_GP_LOG_DEVICE_STATISTICS_GENERAL_ERROR_PAGE = 0x04
IDE_GP_LOG_DEVICE_STATISTICS_TEMPERATURE_PAGE = 0x05
IDE_GP_LOG_DEVICE_STATISTICS_TRANSPORT_PAGE = 0x06
IDE_GP_LOG_DEVICE_STATISTICS_SSD_PAGE = 0x07

_pack_ += 1


class DEVICE_STATISTICS_LOG_PAGE_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("RevisionNumber", ULONGLONG, 16),  # Shall be set to 0001h
        ("PageNumber", ULONGLONG, 8),  # Shall be set to the page number
        ("Reserved", ULONGLONG, 40),
    ]


PDEVICE_STATISTICS_LOG_PAGE_HEADER = POINTER(DEVICE_STATISTICS_LOG_PAGE_HEADER)
_pack_ -= 1

# Device Statistics Log Page structure definitions.
# Snapshot from February 18 2016 draft of ACS-4.

# define GP_LOG_DEVICE_STATISTICS_FLAGS ... copy and pasted


# Supported Device Statistics Log Pages structure definition.
_pack_ += 1


class GP_LOG_SUPPORTED_DEVICE_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        ("NumberOfEntries", UCHAR),  # byte 8
        ("LogPageNumbers", UCHAR * 503),  # byte 9..512
    ]


PGP_LOG_SUPPORTED_DEVICE_STATISTICS = POINTER(GP_LOG_SUPPORTED_DEVICE_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_SUPPORTED_DEVICE_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# General Statistics Log Page structure definition.
_pack_ += 1


class GP_LOG_GENERAL_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "LifeTimePoweronResets",
            make_struct(
                [  # byte 8..15
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "PoweronHours",
            make_struct(
                [  # byte 16..23
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "LogicalSectorsWritten",
            make_struct(
                [  # byte 24..31
                    ("Count", ULONGLONG, 48),
                    ("Reserved", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "WriteCommandCount",
            make_struct(
                [  # byte 32..39
                    ("Count", ULONGLONG, 48),
                    ("Reserved", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "LogicalSectorsRead",
            make_struct(
                [  # byte 40..47
                    ("Count", ULONGLONG, 48),
                    ("Reserved", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "ReadCommandCount",
            make_struct(
                [  # byte 48..55
                    ("Count", ULONGLONG, 48),
                    ("Reserved", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "DateAndTime",
            make_struct(
                [  # byte 56..63
                    ("TimeStamp", ULONGLONG, 48),
                    ("Reserved", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "PendingErrorCount",
            make_struct(
                [  # byte 64..71
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "WorkloadUtilizaton",
            make_struct(
                [  # byte 72..79
                    ("Value", ULONGLONG, 16),
                    ("Reserved", ULONGLONG, 40),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "UtilizationUsageRate",
            make_struct(
                [  # byte 80..87
                    ("Value", ULONGLONG, 8),
                    ("Reserved0", ULONGLONG, 28),
                    ("RateBasis", ULONGLONG, 4),
                    ("RateValidity", ULONGLONG, 8),
                    ("Reserved1", ULONGLONG, 8),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 424),
    ]


PGP_LOG_GENERAL_STATISTICS = POINTER(GP_LOG_GENERAL_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_GENERAL_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# Free Fall Statistics Log Page structure defintion.
_pack_ += 1


class GP_LOG_FREE_FALL_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "NumberofFreeFallEventsDetected",
            make_struct(
                [  # byte 8..15
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "OverlimitShockEvents",
            make_struct(
                [  # byte 16..23
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 488),
    ]


PGP_LOG_FREE_FALL_STATISTICS = POINTER(GP_LOG_FREE_FALL_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_FREE_FALL_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# Rotating Media Statistics Log Page structure defintion.
_pack_ += 1


class GP_LOG_ROTATING_MEDIA_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "SpindleMotorPoweronHours",
            make_struct(
                [  # byte 8..15
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "HeadFlyingHours",
            make_struct(
                [  # byte 16..23
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "HeadLoadEvents",
            make_struct(
                [  # byte 24..31
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfReallocatedLogicalSectors",
            make_struct(
                [  # byte 32..39
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "ReadRecoveryAttempts",
            make_struct(
                [  # byte 40..47
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfMechanicalStartFailures",
            make_struct(
                [  # byte 48..55
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfReallocationCandidateLogicalSectors",
            make_struct(
                [  # byte 56..63
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfHighPriorityUnloadEvents",
            make_struct(
                [  # byte 64..71
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 440),
    ]


PGP_LOG_ROTATING_MEDIA_STATISTICS = POINTER(GP_LOG_ROTATING_MEDIA_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_ROTATING_MEDIA_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# General Error Statistics Log Page structure defintion.
_pack_ += 1


class GP_LOG_GENERAL_ERROR_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "NumberOfReportedUncorrectableErrors",
            make_struct(
                [  # byte 8..15
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfResetsBetweenCommandAcceptanceAndCommandCompletion",
            make_struct(
                [  # byte 16..23
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 488),
    ]


PGP_LOG_GENERAL_ERROR_STATISTICS = POINTER(GP_LOG_GENERAL_ERROR_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_GENERAL_ERROR_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# Temperature Statistics Log Page structure definition.
# NOTE: all temperature value fields are signed byte.
_pack_ += 1


class GP_LOG_TEMPERATURE_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "CurrentTemperature",
            make_struct(
                [  # byte 8..15
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "AverageShortTermTemperature",
            make_struct(
                [  # byte 16..23
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "AverageLongTermTemperature",
            make_struct(
                [  # byte 24..31
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "HighestTemperature",
            make_struct(
                [  # byte 32..39
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "LowestTemperature",
            make_struct(
                [  # byte 40..47
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "HighestAverageShortTermTemperature",
            make_struct(
                [  # byte 48..55
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "LowestAverageShortTermTemperature",
            make_struct(
                [  # byte 56..63
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "HighstAverageLongTermTemperature",
            make_struct(
                [  # byte 64..71
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "LowestAverageLongTermTemperature",
            make_struct(
                [  # byte 72..79
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "TimeInOverTemperature",
            make_struct(
                [  # byte 80..87
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "SpecifiedMaximumOperatingTemperature",
            make_struct(
                [  # byte 88..95
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "TimeInUnderTemperature",
            make_struct(
                [  # byte 96..103
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "SpecifiedMinimumOperatingTemperature",
            make_struct(
                [  # byte 104..111
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 400),
    ]


PGP_LOG_TEMPERATURE_STATISTICS = POINTER(GP_LOG_TEMPERATURE_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_TEMPERATURE_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# Transport Statistics Log Page structure defintion.
_pack_ += 1


class GP_LOG_TRANSPORT_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "NumberOfHardwareResets",
            make_struct(
                [  # byte 8..15
                    ("Count", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfAsrEvents",
            make_struct(
                [  # byte 16..23
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        (
            "NumberOfInterfaceCrcErrors",
            make_struct(
                [  # byte 24..31
                    ("Count", ULONGLONG, 32),
                    ("Reserved", ULONGLONG, 24),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 480),
    ]


PGP_LOG_TRANSPORT_STATISTICS = POINTER(GP_LOG_TRANSPORT_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_TRANSPORT_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# Solid State Device Statistics Log Page structure defintion.
_pack_ += 1


class GP_LOG_SOLID_STATE_DEVICE_STATISTICS(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", DEVICE_STATISTICS_LOG_PAGE_HEADER),  # byte 0..7
        (
            "PercentageUsedEnduranceIndicator",
            make_struct(
                [  # byte 8..15
                    ("Value", ULONGLONG, 8),
                    ("Reserved", ULONGLONG, 48),
                    ("ReservedFlags", ULONGLONG, 3),
                    ("MonitoredConditionMet", ULONGLONG, 1),
                    ("StatisticsSupportsDsn", ULONGLONG, 1),
                    ("Normalized", ULONGLONG, 1),
                    ("ValidValue", ULONGLONG, 1),
                    ("Supported", ULONGLONG, 1),
                ],
                _pack_,
            ),
        ),
        ("Reserved", UCHAR * 496),
    ]


PGP_LOG_SOLID_STATE_DEVICE_STATISTICS = POINTER(GP_LOG_SOLID_STATE_DEVICE_STATISTICS)
_pack_ -= 1

assert sizeof(GP_LOG_SOLID_STATE_DEVICE_STATISTICS) == IDE_GP_LOG_SECTOR_SIZE
# "NCQ Command Error log page" structure definition.
_pack_ += 1


class GP_LOG_NCQ_COMMAND_ERROR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NcqTag", UCHAR, 5),
        ("Reserved0", UCHAR, 1),
        ("UNL", UCHAR, 1),  # error: IDLE IMMEDIATE with UNLOAD
        ("NonQueuedCmd", UCHAR, 1),
        ("Reserved1", UCHAR),
        ("Status", UCHAR),
        ("Error", UCHAR),
        ("LBA7_0", UCHAR),
        ("LBA15_8", UCHAR),
        ("LBA23_16", UCHAR),
        ("Device", UCHAR),
        ("LBA31_24", UCHAR),
        ("LBA39_32", UCHAR),
        ("LBA47_40", UCHAR),
        ("Reserved2", UCHAR),
        ("Count7_0", UCHAR),
        ("Count15_8", UCHAR),
        ("SenseKey", UCHAR),
        ("ASC", UCHAR),
        ("ASCQ", UCHAR),
        ("Reserved3", UCHAR * 239),
        ("Vendor", UCHAR * 255),
        ("Checksum", UCHAR),
    ]


PGP_LOG_NCQ_COMMAND_ERROR = POINTER(GP_LOG_NCQ_COMMAND_ERROR)
_pack_ -= 1


# "NCQ Non-data log page" structure definition.
_pack_ += 1


class GP_LOG_NCQ_NON_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "SubCmd0",
            make_struct(
                [
                    ("AbortNcq", ULONG, 1),
                    ("AbortAll", ULONG, 1),
                    ("AbortStreaming", ULONG, 1),
                    ("AbortNonStreaming", ULONG, 1),
                    ("AbortSelectedTTag", ULONG, 1),
                    ("Reserved", ULONG, 27),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd1",
            make_struct(
                [
                    ("DeadlineHandling", ULONG, 1),
                    ("WriteDataNotContinue", ULONG, 1),
                    ("ReadDataNotContinue", ULONG, 1),
                    ("Reserved", ULONG, 29),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd2",
            make_struct(
                [
                    ("HybridDemoteBySize", ULONG, 1),
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd3",
            make_struct(
                [
                    ("HybridChangeByLbaRange", ULONG, 1),
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd4",
            make_struct(
                [
                    ("HybridControl", ULONG, 1),
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd5",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd6",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd7",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd8",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmd9",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdA",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdB",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdC",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdD",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdE",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        (
            "SubCmdF",
            make_struct(
                [
                    ("Reserved", ULONG, 32),
                ],
                _pack_,
            ),
        ),
        ("Reserved", ULONG * 112),
    ]


PGP_LOG_NCQ_NON_DATA = POINTER(GP_LOG_NCQ_NON_DATA)
_pack_ -= 1

# "NCQ Send Receive log page" strucutre definition
_pack_ += 1


class GP_LOG_NCQ_SEND_RECEIVE(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "SubCmd",
            make_struct(
                [
                    ("DataSetManagement", ULONG, 1),
                    ("HybridEvict", ULONG, 1),
                    ("Reserved", ULONG, 30),
                ],
                _pack_,
            ),
        ),
        (
            "DataSetManagement",
            make_struct(
                [
                    ("Trim", ULONG, 1),
                    ("Reserved", ULONG, 31),
                ],
                _pack_,
            ),
        ),
        ("Reserved", ULONG * 126),
    ]


PGP_LOG_NCQ_SEND_RECEIVE = POINTER(GP_LOG_NCQ_SEND_RECEIVE)
_pack_ -= 1

# "Hybrid Information log page" strucutre definition
HYBRID_INFORMATION_DISABLED = 0x00
HYBRID_INFORMATION_DISABLE_IN_PROCESS = 0x80
HYBRID_INFORMATION_ENABLED = 0xFF

HYBRID_HEALTH_UNUSEABLE = 0x01
HYBRID_HEALTH_NVM_SIZE_CHANGED = 0x02
HYBRID_HEALTH_READ_ONLY = 0x04
HYBRID_HEALTH_DATA_LOSS = 0x08

_pack_ += 1


class GP_LOG_HYBRID_INFORMATION_HEADER(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("HybridInfoDescrCount", USHORT, 4),
        ("Reserved0", USHORT, 12),
        ("Enabled", UCHAR),  # Can be 0x00, 0x80 or 0xFF
        ("HybridHealth", UCHAR),
        ("DirtyLowThreshold", UCHAR),
        ("DirtyHighThreshold", UCHAR),
        ("OptimalWriteGranularity", UCHAR),
        ("MaximumHybridPriorityLevel", UCHAR, 4),
        ("Reserved1", UCHAR, 4),
        ("PowerCondidtion", UCHAR),
        ("CachingMediumEnabled", UCHAR),
        (
            "SupportedOptions",
            make_struct(
                [
                    ("MaximumPriorityBehavior", UCHAR, 1),
                    ("SupportCacheBehavior", UCHAR, 1),
                    ("Reserved", UCHAR, 6),
                ],
                _pack_,
            ),
        ),
        ("Reserved2", UCHAR),  # byte 11
        ("TimeSinceEnabled", ULONG),
        ("NVMSize", ULONGLONG),
        ("EnableCount", ULONGLONG),
        ("MaximumEvictionCommands", USHORT, 5),
        ("Reserved3", USHORT, 11),
        (
            "MaximumEvictionDataBlocks",
            USHORT,
        ),  # how many data blocks (one block is 512 bytes) an Evict command can carry with.
        ("Reserved", UCHAR * 28),
    ]


PGP_LOG_HYBRID_INFORMATION_HEADER = POINTER(GP_LOG_HYBRID_INFORMATION_HEADER)
_pack_ -= 1

_pack_ += 1


class GP_LOG_HYBRID_INFORMATION_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("HybridPriority", UCHAR),
        ("ConsumedNVMSizeFraction", UCHAR),
        ("ConsumedMappingResourcesFraction", UCHAR),
        ("ConsumedNVMSizeForDirtyDataFraction", UCHAR),
        ("ConsumedMappingResourcesForDirtyDataFraction", UCHAR),
        ("Reserved", UCHAR * 11),
    ]


PGP_LOG_HYBRID_INFORMATION_DESCRIPTOR = POINTER(GP_LOG_HYBRID_INFORMATION_DESCRIPTOR)
_pack_ -= 1

_pack_ += 1


class GP_LOG_HYBRID_INFORMATION(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Header", GP_LOG_HYBRID_INFORMATION_HEADER),
        ("Descriptor", GP_LOG_HYBRID_INFORMATION_DESCRIPTOR * 0),
    ]


PGP_LOG_HYBRID_INFORMATION = POINTER(GP_LOG_HYBRID_INFORMATION)
_pack_ -= 1

# Device Signature
ATA_DEVICE_SIGNATURE_ATA = 0x00000101
ATA_DEVICE_SIGNATURE_ATAPI = 0xEB140101
ATA_DEVICE_SIGNATURE_HOST_ZONED = 0xABCD0101
ATA_DEVICE_SIGNATURE_ENCLOSURE = 0xC33C0101
ATA_DEVICE_SIGNATURE_PORT_MULTIPLIER = 0x96690101

# Zone Management Command ZM_ACTION values
ZM_ACTION_REPORT_ZONES = 0x00
ZM_ACTION_CLOSE_ZONE = 0x01
ZM_ACTION_FINISH_ZONE = 0x02
ZM_ACTION_OPEN_ZONE = 0x03
ZM_ACTION_RESET_WRITE_POINTER = 0x04

# "All" Zones bit for Close, Finish, and Open Zone command.
# Bit 8 of FEATURE field
# define ZM_ALL_ZONES_BIT                (1 << 8)

# REPORTING OPTIONS field for REPORT ZONES EXT command.
ATA_REPORT_ZONES_OPTION_LIST_ALL_ZONES = 0x00
ATA_REPORT_ZONES_OPTION_LIST_EMPTY_ZONES = 0x01
ATA_REPORT_ZONES_OPTION_LIST_IMPLICITLY_OPENED_ZONES = 0x02
ATA_REPORT_ZONES_OPTION_LIST_EXPLICITLY_OPENED_ZONES = 0x03
ATA_REPORT_ZONES_OPTION_LIST_CLOSED_ZONES = 0x04
ATA_REPORT_ZONES_OPTION_LIST_FULL_ZONES = 0x05
ATA_REPORT_ZONES_OPTION_LIST_READ_ONLY_ZONES = 0x06
ATA_REPORT_ZONES_OPTION_LIST_OFFLINE_ZONES = 0x07

ATA_REPORT_ZONES_OPTION_LIST_RWP_ZONES = 0x10
ATA_REPORT_ZONES_OPTION_LIST_NON_SEQUENTIAL_WRITE_RESOURCES_ACTIVE_ZONES = 0x11

ATA_REPORT_ZONES_OPTION_LIST_NOT_WRITE_POINTER_ZONES = 0x3F

# Data structures of REPORT ZONES EXT returned data.
# Returned data buffer contains REPORT_ZONES_EXT_DATA, may follow with ATA_ZONE_DESCRIPTOR.

ATA_ZONES_TYPE_AND_LENGTH_MAY_DIFFERENT = 0x0
ATA_ZONES_TYPE_SAME_LENGTH_SAME = 0x1
ATA_ZONES_TYPE_SAME_LAST_ZONE_LENGTH_DIFFERENT = 0x2
ATA_ZONES_TYPE_MAY_DIFFERENT_LENGTH_SAME = 0x3


_pack_ += 1


class REPORT_ZONES_EXT_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        (
            "ZoneListLength",
            ULONG,
        ),  # the length in bytes of the zone descriptors list. e.g. bytes of data following this data structure.
        ("SAME", UCHAR, 4),
        ("Reserved0", UCHAR, 4),
        ("Reserved1", UCHAR * 3),
        ("MaxLBA", ULONGLONG, 48),
        ("Reserved2", ULONGLONG, 16),
        ("Reserved3", UCHAR * 48),
    ]


PREPORT_ZONES_EXT_DATA = POINTER(REPORT_ZONES_EXT_DATA)
_pack_ -= 1


ATA_ZONE_TYPE_CONVENTIONAL = 0x1
ATA_ZONE_TYPE_SEQUENTIAL_WRITE_REQUIRED = 0x2
ATA_ZONE_TYPE_SEQUENTIAL_WRITE_PREFERRED = 0x3

ATA_ZONE_CONDITION_NOT_WRITE_POINTER = 0x0
ATA_ZONE_CONDITION_EMPTY = 0x1
ATA_ZONE_CONDITION_IMPLICITLY_OPENED = 0x2
ATA_ZONE_CONDITION_EXPLICITLY_OPENED = 0x3
ATA_ZONE_CONDITION_CLOSED = 0x4
ATA_ZONE_CONDITION_READ_ONLY = 0xD
ATA_ZONE_CONDITION_FULL = 0xE
ATA_ZONE_CONDITION_OFFLINE = 0xF

_pack_ += 1


class ATA_ZONE_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("ZoneType", UCHAR, 4),
        ("Reserved0", UCHAR, 4),
        ("Reset", UCHAR, 1),
        ("NonSeq", UCHAR, 1),
        ("Reserved1", UCHAR, 2),
        ("ZoneCondition", UCHAR, 4),
        ("Reserved2", UCHAR * 6),
        ("ZoneLength", ULONGLONG, 48),
        ("Reserved3", ULONGLONG, 16),
        ("ZoneStartLBA", ULONGLONG, 48),
        ("Reserved4", ULONGLONG, 16),
        ("WritePointerLBA", ULONGLONG, 48),
        ("Reserved5", ULONGLONG, 16),
        ("Reserved6", UCHAR * 32),
    ]


PATA_ZONE_DESCRIPTOR = POINTER(ATA_ZONE_DESCRIPTOR)
_pack_ -= 1

_pack_ += 1


class ATA_PHYSICAL_ELEMENT_STATUS_DESCRIPTOR(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("Reserved1", UCHAR * 4),
        ("ElementIdentifier", ULONG),
        ("Reserved2", UCHAR * 6),
        ("PhysicalElementType", UCHAR),
        ("PhysicalElementHealth", UCHAR),
        ("AssociatedCapacity", ULONGLONG),
        ("Reserved3", UCHAR * 8),
    ]


PATA_PHYSICAL_ELEMENT_STATUS_DESCRIPTOR = POINTER(ATA_PHYSICAL_ELEMENT_STATUS_DESCRIPTOR)
_pack_ -= 1

_pack_ += 1


class ATA_GET_PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA(Structure):
    _pack_ = _pack_
    _fields_ = [
        ("NumberOfDescriptors", ULONG),
        ("NumberOfDescriptorsReturned", ULONG),
        ("ElementIdentifierBeingDepoped", ULONG),
        ("Reserved", UCHAR * 20),
        ("Descriptors", ATA_PHYSICAL_ELEMENT_STATUS_DESCRIPTOR * ANYSIZE_ARRAY),
    ]


PATA_GET_PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA = POINTER(ATA_GET_PHYSICAL_ELEMENT_STATUS_PARAMETER_DATA)
_pack_ -= 1


# if _MSC_VER >= 1200
# pragma warning(pop)
# else
# pragma warning(default:4214)
# pragma warning(default:4200)
# pragma warning(default:4201)
# endif

# endif
