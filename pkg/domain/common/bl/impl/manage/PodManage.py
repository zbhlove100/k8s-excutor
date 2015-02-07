__author__ = 'zhangbohan'


class PodManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        pass

    def createPod(self,podRequest):

        self.kubenetesClient.createResource(podRequest)
        pass

    def deletePod(self, podRequest):

        result = self.kubenetesClient.deleteResource(podRequest)
        return result

    def queryPod(self, podReqest):
        result = self.kubenetesClient.queryResource(podReqest)
        return result

    def queryPodsInFarm(self, podReqest):
        labelName = "farmLabel"
        result = self.kubenetesClient.queryResourceByLabel(podReqest, labelName)
        return result

    def queryPodsInRole(self, podReqest):
        labelName = "roleLabel"
        result = self.kubenetesClient.queryResourceByLabel(podReqest, labelName)
        return result