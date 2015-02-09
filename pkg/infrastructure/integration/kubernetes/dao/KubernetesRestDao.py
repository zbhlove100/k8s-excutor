__author__ = 'zhangbohan'


class KubernetesRestDao(object):

    def __init__(self):
        pass

    def getPodApiWithNamespcae(self, namespace):
        podApi = self.kubernetesPodAPIWithNamespcae % namespace
        return podApi

    def getServiceApiWithNamespcae(self, namespace):
        serviceApi = self.kubernetesServiceAPIWithNamespcae % namespace
        return serviceApi

    def getReplicationControllerApiWithNamespcae(self, namespace):
        replicationControllerApi = self.kubernetesReplicationControllerAPIWithNamespcae % namespace
        return replicationControllerApi

    def getKubernetesEndpoint(self):
        return self.kubernetesEndpoint