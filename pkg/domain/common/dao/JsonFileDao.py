__author__ = 'zhangbohan'

from pkg.infrastructure.common.file.FileUtil import FileUtil
from pkg.infrastructure.common.identification.UuidUtil import  UuidUtil

class JsonFileDao(object):
    def __init__(self,filePathDir):
        if None == filePathDir:
            self.filePathDir = "/tmp/"
        else:
            self.filePathDir = filePathDir
        pass

    def setObj(self,json):
        uuidname = UuidUtil.getUuidName()
        filePath = "%s%s" % (self.filePathDir, uuidname)
        FileUtil.writeContent(filePath, json)
        return filePath