__author__ = 'zhangbohan'


class KubernetesRestDao(object):
    kubernetesPodAPI = "/api/v1beta1/ns/%s/pods"
    kubernetesServiceAPI = "/api/v1beta1/ns/%s/pods"
    kubernetesReplicationControllerAPI = "/api/v1beta1/ns/%s/replicationControllers"
    kubernetesEndpoint = "http://54.248.167.168:8080"
    def __init__(self):
        pass

    def getPodApi(self, namespace):
        podApi = self.kubernetesPodAPI % namespace
        return podApi

    def getServiceApi(self, namespace):
        serviceApi = self.kubernetesServiceAPI % namespace
        return serviceApi

    def getReplicationControllerApi(self, namespace):
        replicationControllerApi = self.kubernetesReplicationControllerAPI % namespace
        return replicationControllerApi

    def getKubernetesEndpoint(self):
        return self.kubernetesEndpoint