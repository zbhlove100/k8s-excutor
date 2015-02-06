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

