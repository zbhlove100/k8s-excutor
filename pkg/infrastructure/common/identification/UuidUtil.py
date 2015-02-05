__author__ = 'zhangbohan'
import uuid
import random
import os
from pkg.infrastructure.common.file.FileUtil import FileUtil
class UuidUtil(object):

    def __init__(self):
        pass
    @staticmethod
    def getUuidName():
        result = uuid.uuid4()
        return str(result)

    @staticmethod
    def getUuidWithPrefix(prefix):
        uuidname = str(uuid.uuid4())

        result = "%s-%s" % (prefix,uuidname)

        return result


