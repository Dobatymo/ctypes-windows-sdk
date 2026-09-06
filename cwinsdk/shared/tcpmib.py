from ctypes import POINTER, Structure, Union, c_ubyte
from ctypes.wintypes import DWORD, LARGE_INTEGER

from .. import CEnum
from .basetsd import DWORD64
from .in6addr import IN6_ADDR
from .ntdef import ANYSIZE_ARRAY, ULONGLONG

TCPIP_OWNING_MODULE_SIZE = 16


class MIB_TCP_STATE(CEnum):
    MIB_TCP_STATE_CLOSED = 1
    MIB_TCP_STATE_LISTEN = 2
    MIB_TCP_STATE_SYN_SENT = 3
    MIB_TCP_STATE_SYN_RCVD = 4
    MIB_TCP_STATE_ESTAB = 5
    MIB_TCP_STATE_FIN_WAIT1 = 6
    MIB_TCP_STATE_FIN_WAIT2 = 7
    MIB_TCP_STATE_CLOSE_WAIT = 8
    MIB_TCP_STATE_CLOSING = 9
    MIB_TCP_STATE_LAST_ACK = 10
    MIB_TCP_STATE_TIME_WAIT = 11
    MIB_TCP_STATE_DELETE_TCB = 12
    MIB_TCP_STATE_RESERVED = 100


PMIB_TCP_STATE = POINTER(MIB_TCP_STATE)


class TCP_CONNECTION_OFFLOAD_STATE(CEnum):
    TcpConnectionOffloadStateInHost = 0
    TcpConnectionOffloadStateOffloading = 1
    TcpConnectionOffloadStateOffloaded = 2
    TcpConnectionOffloadStateUploading = 3
    TcpConnectionOffloadStateMax = 4


PTCP_CONNECTION_OFFLOAD_STATE = POINTER(TCP_CONNECTION_OFFLOAD_STATE)


class MIB_TCPROW_UNION(Union):
    _fields_ = [("dwState", DWORD), ("State", MIB_TCP_STATE)]


class MIB_TCPROW_LH(Structure):
    _anonymous_ = ("_state",)
    _fields_ = [
        ("_state", MIB_TCPROW_UNION),
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwRemoteAddr", DWORD),
        ("dwRemotePort", DWORD),
    ]


PMIB_TCPROW_LH = POINTER(MIB_TCPROW_LH)
MIB_TCPROW = MIB_TCPROW_LH
PMIB_TCPROW = PMIB_TCPROW_LH


class MIB_TCPROW_W2K(Structure):
    _fields_ = [(name, DWORD) for name in ("dwState", "dwLocalAddr", "dwLocalPort", "dwRemoteAddr", "dwRemotePort")]


PMIB_TCPROW_W2K = POINTER(MIB_TCPROW_W2K)


class MIB_TCPTABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCPROW * ANYSIZE_ARRAY)]


PMIB_TCPTABLE = POINTER(MIB_TCPTABLE)


class MIB_TCPROW2(Structure):
    _fields_ = [
        ("dwState", DWORD),
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwRemoteAddr", DWORD),
        ("dwRemotePort", DWORD),
        ("dwOwningPid", DWORD),
        ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE),
    ]


PMIB_TCPROW2 = POINTER(MIB_TCPROW2)


class MIB_TCPTABLE2(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCPROW2 * ANYSIZE_ARRAY)]


PMIB_TCPTABLE2 = POINTER(MIB_TCPTABLE2)


class MIB_TCPROW_OWNER_PID(Structure):
    _fields_ = [
        ("dwState", DWORD),
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwRemoteAddr", DWORD),
        ("dwRemotePort", DWORD),
        ("dwOwningPid", DWORD),
    ]


PMIB_TCPROW_OWNER_PID = POINTER(MIB_TCPROW_OWNER_PID)


class MIB_TCPTABLE_OWNER_PID(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCPROW_OWNER_PID * ANYSIZE_ARRAY)]


PMIB_TCPTABLE_OWNER_PID = POINTER(MIB_TCPTABLE_OWNER_PID)


class MIB_TCPROW_OWNER_MODULE(Structure):
    _fields_ = [
        ("dwState", DWORD),
        ("dwLocalAddr", DWORD),
        ("dwLocalPort", DWORD),
        ("dwRemoteAddr", DWORD),
        ("dwRemotePort", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
    ]


PMIB_TCPROW_OWNER_MODULE = POINTER(MIB_TCPROW_OWNER_MODULE)


class MIB_TCPTABLE_OWNER_MODULE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCPROW_OWNER_MODULE * ANYSIZE_ARRAY)]


PMIB_TCPTABLE_OWNER_MODULE = POINTER(MIB_TCPTABLE_OWNER_MODULE)


class MIB_TCP6ROW(Structure):
    _fields_ = [
        ("State", MIB_TCP_STATE),
        ("LocalAddr", IN6_ADDR),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("RemoteAddr", IN6_ADDR),
        ("dwRemoteScopeId", DWORD),
        ("dwRemotePort", DWORD),
    ]


PMIB_TCP6ROW = POINTER(MIB_TCP6ROW)


class MIB_TCP6TABLE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCP6ROW * ANYSIZE_ARRAY)]


PMIB_TCP6TABLE = POINTER(MIB_TCP6TABLE)


class MIB_TCP6ROW2(Structure):
    _fields_ = [
        ("LocalAddr", IN6_ADDR),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("RemoteAddr", IN6_ADDR),
        ("dwRemoteScopeId", DWORD),
        ("dwRemotePort", DWORD),
        ("State", MIB_TCP_STATE),
        ("dwOwningPid", DWORD),
        ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE),
    ]


PMIB_TCP6ROW2 = POINTER(MIB_TCP6ROW2)


class MIB_TCP6TABLE2(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCP6ROW2 * ANYSIZE_ARRAY)]


PMIB_TCP6TABLE2 = POINTER(MIB_TCP6TABLE2)


class MIB_TCP6ROW_OWNER_PID(Structure):
    _fields_ = [
        ("ucLocalAddr", c_ubyte * 16),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("ucRemoteAddr", c_ubyte * 16),
        ("dwRemoteScopeId", DWORD),
        ("dwRemotePort", DWORD),
        ("dwState", DWORD),
        ("dwOwningPid", DWORD),
    ]


PMIB_TCP6ROW_OWNER_PID = POINTER(MIB_TCP6ROW_OWNER_PID)


class MIB_TCP6TABLE_OWNER_PID(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCP6ROW_OWNER_PID * ANYSIZE_ARRAY)]


PMIB_TCP6TABLE_OWNER_PID = POINTER(MIB_TCP6TABLE_OWNER_PID)


class MIB_TCP6ROW_OWNER_MODULE(Structure):
    _fields_ = [
        ("ucLocalAddr", c_ubyte * 16),
        ("dwLocalScopeId", DWORD),
        ("dwLocalPort", DWORD),
        ("ucRemoteAddr", c_ubyte * 16),
        ("dwRemoteScopeId", DWORD),
        ("dwRemotePort", DWORD),
        ("dwState", DWORD),
        ("dwOwningPid", DWORD),
        ("liCreateTimestamp", LARGE_INTEGER),
        ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE),
    ]


PMIB_TCP6ROW_OWNER_MODULE = POINTER(MIB_TCP6ROW_OWNER_MODULE)


class MIB_TCP6TABLE_OWNER_MODULE(Structure):
    _fields_ = [("dwNumEntries", DWORD), ("table", MIB_TCP6ROW_OWNER_MODULE * ANYSIZE_ARRAY)]


PMIB_TCP6TABLE_OWNER_MODULE = POINTER(MIB_TCP6TABLE_OWNER_MODULE)


class TCP_RTO_ALGORITHM(CEnum):
    TcpRtoAlgorithmOther = 1
    TcpRtoAlgorithmConstant = 2
    TcpRtoAlgorithmRsre = 3
    TcpRtoAlgorithmVanj = 4
    MIB_TCP_RTO_OTHER = 1
    MIB_TCP_RTO_CONSTANT = 2
    MIB_TCP_RTO_RSRE = 3
    MIB_TCP_RTO_VANJ = 4


PTCP_RTO_ALGORITHM = POINTER(TCP_RTO_ALGORITHM)


class MIB_TCPSTATS_UNION(Union):
    _fields_ = [("dwRtoAlgorithm", DWORD), ("RtoAlgorithm", TCP_RTO_ALGORITHM)]


class MIB_TCPSTATS_LH(Structure):
    _anonymous_ = ("_rto",)
    _fields_ = [
        ("_rto", MIB_TCPSTATS_UNION),
        ("dwRtoMin", DWORD),
        ("dwRtoMax", DWORD),
        ("dwMaxConn", DWORD),
        ("dwActiveOpens", DWORD),
        ("dwPassiveOpens", DWORD),
        ("dwAttemptFails", DWORD),
        ("dwEstabResets", DWORD),
        ("dwCurrEstab", DWORD),
        ("dwInSegs", DWORD),
        ("dwOutSegs", DWORD),
        ("dwRetransSegs", DWORD),
        ("dwInErrs", DWORD),
        ("dwOutRsts", DWORD),
        ("dwNumConns", DWORD),
    ]


PMIB_TCPSTATS_LH = POINTER(MIB_TCPSTATS_LH)
MIB_TCPSTATS = MIB_TCPSTATS_LH
PMIB_TCPSTATS = PMIB_TCPSTATS_LH


class MIB_TCPSTATS_W2K(Structure):
    _fields_ = [("dwRtoAlgorithm", DWORD)] + [(name, field_type) for name, field_type in MIB_TCPSTATS_LH._fields_[1:]]


PMIB_TCPSTATS_W2K = POINTER(MIB_TCPSTATS_W2K)


class MIB_TCPSTATS2(Structure):
    _fields_ = [
        ("RtoAlgorithm", TCP_RTO_ALGORITHM),
        ("dwRtoMin", DWORD),
        ("dwRtoMax", DWORD),
        ("dwMaxConn", DWORD),
        ("dwActiveOpens", DWORD),
        ("dwPassiveOpens", DWORD),
        ("dwAttemptFails", DWORD),
        ("dwEstabResets", DWORD),
        ("dwCurrEstab", DWORD),
        ("dw64InSegs", DWORD64),
        ("dw64OutSegs", DWORD64),
        ("dwRetransSegs", DWORD),
        ("dwInErrs", DWORD),
        ("dwOutRsts", DWORD),
        ("dwNumConns", DWORD),
    ]


PMIB_TCPSTATS2 = POINTER(MIB_TCPSTATS2)
