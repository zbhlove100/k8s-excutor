__author__ = 'zhangbohan'
import logging, os
import requests
logging.basicConfig(filename='/tmp/k8s-excutor.log', level=logging.DEBUG)
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.common.logger.LoggerFactory import LoggerFactory


class KubernetesRestClient(IKubernetesClient):
    def __init__(self, namespace=None, authToken=None):
        if None != namespace:
            self.namespace = "default"
        else:
            self.namespace = namespace

        logging.debug("Init KubernetesRestClient")
        pass

    def setKubernetesRestDao(self, kubernetesRestDao):
        self.kubernetesRestDao = kubernetesRestDao

    def setNamespace(self,namespace):
        self.namespace = namespace

    def getNamespace(self):
        return self.namespace

    def sendRequest(self, requestUrl, requestType, header=None, data=None, timeout=None):
        response = ""
        try:
            customTimeout = 30
            if None != timeout:
                customTimeout = timeout

            if requestType == "GET":
                response = requests.get(requestUrl, timeout=timeout)
            elif requestType == "POST":
                response = requests.post(requestUrl, data=data, headers=header, timeout=customTimeout)
            elif requestType == "DELETE":
                response = requests.delete(requestUrl)

            if str(response.status_code) == "200":
                print "-- OK"
            else:
                print "-- [ERROR] " + str(response.status_code)
                print response.text

        except Exception, e:
            msg = "[ERROR] request error!"

            print msg
            print str(e)
        return str(response.status_code), str(response.text)


    def createPod(self, podJson):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(self.namespace)
        requestUrl = "%s%s" % (endpoint, podApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, podJson)
        return self.operationResponse

    def deletePod(self, podId):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryPod(self, podId):

        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)
        logging.debug(requestUrl)
        print(requestUrl)
        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryPodByLabel(self, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(self.namespace)
        requestUrl = "%s%s?labels=%s" % (endpoint, podApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse


    def createService(self, serviceJson):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(self.namespace)
        requestUrl = "%s%s" % (endpoint, serviceApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, serviceJson)
        return self.operationResponse

    def deleteService(self, serviceId):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryService(self, serviceId):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryServiceByLabel(self, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(self.namespace)
        requestUrl = "%s%s?labels=%s" % (endpoint, serviceApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def createReplicationController(self, replicationControllerJson):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            self.namespace)
        requestUrl = "%s%s" % (endpoint, replicationControllerApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, replicationControllerJson)
        return self.operationResponse

    def deleteReplicationController(self, replicationControllerId):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryReplicationController(self, replicationControllerId):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            self.namespace)
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryReplicationControllerByLabel(self, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            self.namespace)
        requestUrl = "%s%s?labels=%s" % (endpoint, replicationControllerApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse
