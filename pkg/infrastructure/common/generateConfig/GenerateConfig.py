__author__ = 'zhangbohan'


class GenerateConfig(object):

    def __init__(self, obj, configDao):
        self.obj = obj
        self.configDao = configDao
        pass

    def generateJson(self):
        podJson = self.obj.toJSON()
        filePath = self.configDao.setObj(podJson)
        return filePath

    def generateYAML(self):
        pass