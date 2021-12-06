from cwinsdk import CEnum


class EXCEPTION_DISPOSITION(CEnum):
    ExceptionContinueExecution = 0
    ExceptionContinueSearch = 1
    ExceptionNestedException = 2
    ExceptionCollidedUnwind = 3


EXCEPTION_EXECUTE_HANDLER = 1
EXCEPTION_CONTINUE_SEARCH = 0
EXCEPTION_CONTINUE_EXECUTION = -1
