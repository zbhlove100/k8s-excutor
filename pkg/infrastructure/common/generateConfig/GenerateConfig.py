__author__ = 'zhangbohan'

from pkg.domain.common.model.pod.Pod import Pod
from pkg.infrastructure.common.file.FileUtil import FileUtil
class GenerateConfig(object):

    def __init__(self,obj,path):
        self.obj = obj
        self.path = path
        pass

    def generateJsonFile(self):
        podJson = self.obj.toJSON()
        FileUtil.writeContent(self.path, podJson)
        pass

    def generateYAMLFile(self):
        pass