__author__ = 'zhangbohan'


SUCCESS = "success"
ERROR = "error"

class OperationStatusTranslator(object):
    def __init__(self):
        pass
    @staticmethod
    def translateStatus(statusCode):
        if statusCode.startswith("2"):
            return SUCCESS
        else :
            return ERROR
