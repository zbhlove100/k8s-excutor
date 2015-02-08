__author__ = 'zhangbohan'
from pkg.infrastructure.common.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ServiceManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        pass

    def createService(self,serviceRequest):
        ServiceJson = serviceRequest.toJSON()
        self.kubenetesClient.createService(ServiceJson)
        pass

    def deleteService(self, serviceRequest):
        ServiceId = serviceRequest.getId()
        result = self.kubenetesClient.deleteService(ServiceId)
        return result

    def queryService(self, serviceRequest):
        ServiceId = serviceRequest.getId()
        result = self.kubenetesClient.queryService(ServiceId)
        return result

    def queryServicesInFarm(self, serviceRequest):
        labels = serviceRequest.getLabels()
        labelName = "farmLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryServiceByLabel(queryLabels)
        return result

    def queryServicesInRole(self, serviceRequest):
        labels = serviceRequest.getLabels()
        labelName = "roleLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryServiceByLabel(queryLabels)
        return result