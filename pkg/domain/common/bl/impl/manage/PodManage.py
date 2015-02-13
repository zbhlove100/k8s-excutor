__author__ = 'zhangbohan'


class PodManage(object):
    def __init__(self,kubenetesClient=None):
        self.kubenetesClient = kubenetesClient
        pass

    def createPod(self,podRequest):

        result = self.kubenetesClient.createPod(podRequest)
        print result
        return result

    def deletePod(self, podRequest):
        podId = podRequest.getId()
        result = self.kubenetesClient.deletePod(podId)
        return result

    def queryPod(self, podRequest):
        podId = podRequest.getId()
        result = self.kubenetesClient.queryPod(podId)
        return result.toJSON()

    def queryPodsInFarm(self, podRequest):
        labels = podRequest.getLabels()
        labelName = "farmlabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryPodByLabel(queryLabels)
        return result.toJSON()

    def queryPodsInRole(self, podRequest):
        labels = podRequest.getLabels()
        labelName = "rolelabel"
        labelValues = labels[labelName]
        queryLabels = "%s=%s" % (labelName, labelValues)
        result = self.kubenetesClient.queryPodByLabel(queryLabels)
        return result.toJSON()