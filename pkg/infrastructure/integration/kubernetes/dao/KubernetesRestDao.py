__author__ = 'zhangbohan'


class KubernetesRestDao(object):
    kubernetesPodAPI = "/api/v1beta1/pods"
    kubernetesServiceAPI = "/api/v1beta1/pods"
    kubernetesReplicationControllerAPI = "/api/v1beta1/replicationControllers"
    kubernetesPodAPIWithNamespcae = "/api/v1beta1/ns/%s/pods"
    kubernetesServiceAPIWithNamespcae = "/api/v1beta1/ns/%s/services"
    kubernetesReplicationControllerAPIWithNamespcae = "/api/v1beta1/ns/%s/replicationControllers"
    kubernetesEndpoint = "http://54.248.167.168:8080"
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