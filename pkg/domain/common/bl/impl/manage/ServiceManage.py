__author__ = 'zhangbohan'
from pkg.infrastructure.common.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ServiceManage(object):
    def __init__(self, kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.configDao = JsonFileDao()
        pass

    def createService(self, serviceRequest):


        self.kubenetesClient.createResource(serviceRequest)
        pass

    def deleteService(self, serviceRequest):

        result = self.kubenetesClient.deleteResource(serviceRequest)
        return result

    def queryService(self, serviceRequest):
        result = self.kubenetesClient.querryResource(serviceRequest)
        return result

    def queryServicesInFarm(self, serviceRequest):
        labelName = "farmLabel"
        result = self.kubenetesClient.querryResourceByLabel(serviceRequest, labelName)
        return result

    def queryServicesInRole(self, serviceRequest):
        labelName = "roleLabel"
        result = self.kubenetesClient.querryResourceByLabel(serviceRequest, labelName)
        return result