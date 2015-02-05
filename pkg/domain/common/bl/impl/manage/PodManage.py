__author__ = 'zhangbohan'

from pkg.domain.common.bl.impl.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class PodManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.configDao = JsonFileDao()
        pass

    def createPod(self,podRequest):

        generator = GenerateConfig(podRequest, self.configDao)
        podConfigFile = generator.generateJson()
        self.kubenetesClient.createResource(podConfigFile)
        pass

    def deletePod(self, podRequest):
        podname = podRequest.getId()
        result = self.kubenetesClient.deleteResource(podname)
        return result

