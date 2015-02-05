__author__ = 'zhangbohan'
from pkg.domain.common.bl.impl.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ReplicationControllerManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        self.configDao = JsonFileDao()
        pass

    def createReplicationController(self,replicationRequestData):

        generator = GenerateConfig(replicationRequestData, self.configDao)
        replicationControllerConfigFile = generator.generateJson()
        self.kubenetesClient.createResource(replicationControllerConfigFile)
        pass

    def deleteReplicationController(self, replicationRequestData):
        podname = replicationRequestData.getId()
        result = self.kubenetesClient.deleteResource(podname)
        return result