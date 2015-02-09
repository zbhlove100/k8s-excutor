__author__ = 'zhangbohan'


class IKubernetesClient(object):
    def __init__(self):
        self.operationResponse = ""
        pass

    def createPod(self, podModel):

        return self.operationResponse

    def deletePod(self, podId):
        return self.operationResponse

    def queryPod(self, podId):
        return self.operationResponse

    def queryPodByLabel(self, labels):
        return self.operationResponse


    def createService(self, serviceModel):
        return self.operationResponse

    def deleteService(self, serviceId):
        return self.operationResponse

    def queryService(self, serviceId):
        return self.operationResponse

    def queryServiceByLabel(self, labels):
        return self.operationResponse

    def createReplicationController(self, replicationControllerModel):
        return self.operationResponse

    def deleteReplicationController(self, replicationControllerId):
        return self.operationResponse

    def queryReplicationController(self, replicationControllerId):
        return self.operationResponse

    def queryReplicationControllerByLabel(self, labels):
        return self.operationResponse