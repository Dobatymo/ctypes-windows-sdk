from ctypes import POINTER

from .. import CEnum


class TCP_ESTATS_TYPE(CEnum):
    TcpConnectionEstatsSynOpts = 0
    TcpConnectionEstatsData = 1
    TcpConnectionEstatsSndCong = 2
    TcpConnectionEstatsPath = 3
    TcpConnectionEstatsSendBuff = 4
    TcpConnectionEstatsRec = 5
    TcpConnectionEstatsObsRec = 6
    TcpConnectionEstatsBandwidth = 7
    TcpConnectionEstatsFineRtt = 8
    TcpConnectionEstatsMaximum = 9


PTCP_ESTATS_TYPE = POINTER(TCP_ESTATS_TYPE)
