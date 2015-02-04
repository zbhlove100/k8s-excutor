__author__ = 'zhangbohan'

from pkg.infrastructure.common.file.FileUtil import FileUtil
class JsonFileDao(object):
    def __init__(self):
        pass

    def setJsonToFile(self,json,file):
        FileUtil.writeContent(file,json)
        pass