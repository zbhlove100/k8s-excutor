__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.model import OperationStatus

class IKubernetesClient(object):
    def __init__(self):
        self.operationStatus = OperationStatus.Success


        pass

    def createPod(self, podModel):

        return self.operationStatus

    def deletePod(self, podId):
        return self.operationStatus

    def queryPod(self, podId):
        return self.operationResponse

    def queryPodByLabel(self, labels):
        return self.operationResponse


    def createService(self, serviceModel):
        return self.operationStatus

    def deleteService(self, serviceId):
        return self.operationStatus

    def queryService(self, serviceId):
        return self.operationResponse

    def queryServiceByLabel(self, labels):
        return self.operationResponse

    def createReplicationController(self, replicationControllerModel):
        return self.operationStatus

    def deleteReplicationController(self, replicationControllerId):
        return self.operationStatus

    def queryReplicationController(self, replicationControllerId):
        return self.operationResponse

    def queryReplicationControllerByLabel(self, labels):
        return self.operationResponse