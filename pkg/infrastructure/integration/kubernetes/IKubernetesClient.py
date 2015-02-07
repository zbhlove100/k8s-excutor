__author__ = 'zhangbohan'

class IKubernetesClient(object):
    def __init__(self):
        self.operationResponse = ""
        pass

    def createResource(self, objModel):
        return self.operationResponse

    def deleteResource(self, objModel):
        return self.operationResponse

    def queryResource(self, objModel):
        return self.operationResponse

    def queryResourceByLabel(self, objModel, labelName):
        return self.operationResponse