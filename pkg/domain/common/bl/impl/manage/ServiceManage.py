__author__ = 'zhangbohan'
from pkg.domain.common.bl.impl.namespace.PortNamespace import PortNamespace
from pkg.domain.common.dao.namespcaeDao.PortNamespcaeFileDao import PortNamespcaeFileDao

class ServiceManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.portNamespaceDao = PortNamespcaeFileDao()
        pass

    def setPortNamespaceDap(self,portNamespaceDao):
        self.portNamespaceDao = portNamespaceDao
        pass

    def createService(self,serviceRequest):
        portNamespace = PortNamespace(self.portNamespaceDao)
        serviceModel = portNamespace.setServicePublicIpPort(serviceRequest)
        self.kubenetesClient.createService(serviceModel)
        pass

    def deleteService(self, serviceRequest):
        serviceId = serviceRequest.getId()
        result = self.kubenetesClient.deleteService(serviceId)
        return result

    def queryService(self, serviceRequest):
        serviceId = serviceRequest.getId()
        result = self.kubenetesClient.queryService(serviceId)
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