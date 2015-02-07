__author__ = 'zhangbohan'
from pkg.infrastructure.common.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ReplicationControllerManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.configDao = JsonFileDao()
        pass

    def createReplicationController(self,replicationRequest):
        self.kubenetesClient.createResource(replicationRequest)
        pass

    def deleteReplicationController(self, replicationRequest):
        result = self.kubenetesClient.deleteResource(replicationRequest)
        return result

    def queryReplicationController(self, replicationRequest):
        result = self.kubenetesClient.querryResource(replicationRequest)
        return result

    def queryReplicationControllersInFarm(self, replicationRequest):
        labelName = "farmLabel"
        result = self.kubenetesClient.querryResourceByLabel(replicationRequest, labelName)
        return result

    def queryReplicationControllersInRole(self, replicationRequest):
        labelName = "roleLabel"
        result = self.kubenetesClient.querryResourceByLabel(replicationRequest, labelName)
        return result