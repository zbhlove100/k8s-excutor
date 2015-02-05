__author__ = 'zhangbohan'
from pkg.domain.common.bl.impl.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ServiceManage(object):
    def __init__(self, kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.configDao = JsonFileDao()
        pass

    def createService(self, serviceRequestData):

        generator = GenerateConfig(serviceRequestData, self.configDao)
        serviceConfigFile = generator.generateJson()
        self.kubenetesClient.createResource(serviceConfigFile)
        pass

    def deleteService(self, serviceRequestData):
        podname = serviceRequestData.getId()
        result = self.kubenetesClient.deleteResource(podname)
        return result