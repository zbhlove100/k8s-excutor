__author__ = 'zhangbohan'
from pkg.infrastructure.common.generateConfig import GenerateConfig
from pkg.domain.common.dao.JsonFileDao import JsonFileDao


class ReplicationControllerManage(object):
    def __init__(self, kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        pass

    def createReplicationController(self,replicationControllerRequest):
        self.kubenetesClient.createReplicationController(replicationControllerRequest)
        pass

    def deleteReplicationController(self, replicationControllerRequest):
        ReplicationControllerId = replicationControllerRequest.getId()
        result = self.kubenetesClient.deleteReplicationController(ReplicationControllerId)
        return result

    def queryReplicationController(self, replicationControllerRequest):
        ReplicationControllerId = replicationControllerRequest.getId()
        result = self.kubenetesClient.queryReplicationController(ReplicationControllerId)
        return result

    def queryReplicationControllersInFarm(self, replicationControllerRequest):
        labels = replicationControllerRequest.getLabels()
        labelName = "farmLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryReplicationControllerByLabel(queryLabels)
        return result

    def queryReplicationControllersInRole(self, replicationControllerRequest):
        labels = replicationControllerRequest.getLabels()
        labelName = "roleLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryReplicationControllerByLabel(queryLabels)
        return result