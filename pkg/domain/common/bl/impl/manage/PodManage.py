__author__ = 'zhangbohan'


class PodManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        pass

    def createPod(self,podRequest):

        self.kubenetesClient.createPod(podRequest)
        pass

    def deletePod(self, podRequest):
        podId = podRequest.getId()
        result = self.kubenetesClient.deletePod(podId)
        return result

    def queryPod(self, podRequest):
        podId = podRequest.getId()
        result = self.kubenetesClient.queryPod(podId)
        return result

    def queryPodsInFarm(self, podRequest):
        labels = podRequest.getLabels()
        labelName = "farmLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryPodByLabel(queryLabels)
        return result

    def queryPodsInRole(self, podRequest):
        labels = podRequest.getLabels()
        labelName = "roleLabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryPodByLabel(queryLabels)
        return result