__author__ = 'zhangbohan'
import logging, os
import requests

logging.basicConfig(filename='/tmp/k8s-excutor.log', level=logging.DEBUG)
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.integration.kubernetes.model import OperationStatus
from pkg.infrastructure.integration.kubernetes.model.pod.PodList import PodList,Pod
from pkg.infrastructure.integration.kubernetes.model.service.ServiceList import ServiceList,Service
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationControllerList import ReplicationControllerList,ReplicationController


class KubernetesWSClient(IKubernetesClient):
    KUBERNETES_POD_API = "/api/v1beta1/pods"
    KUBERNETES_SERVICE_API = "/api/v1beta1/pods"
    KUBERNETES_REPLICATIONCONTROLLER_API = "/api/v1beta1/replicationControllers"
    KUBERNETES_POD_NAMESPACE_API = "/api/v1beta1/ns/%s/pods"
    KUBERNETES_SERVICE_NAMESPACE_API = "/api/v1beta1/ns/%s/services"
    KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API = "/api/v1beta1/ns/%s/replicationControllers"
    # KUBERNETES_ENDPOINT = "http://54.248.167.168:8080"

    def __init__(self, kubernetesEndpoint, namespace=None, authToken=None):
        if None == namespace:
            self.namespace = "default"
        else:
            self.namespace = namespace
        self.kubernetesEndpoint = kubernetesEndpoint
        self.KUBERNETES_POD_NAMESPACE_API = self.KUBERNETES_POD_NAMESPACE_API % self.namespace
        self.KUBERNETES_SERVICE_NAMESPACE_API = self.KUBERNETES_SERVICE_NAMESPACE_API % self.namespace
        self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API % self.namespace
        logging.debug("Init KubernetesRestClient")
        pass

    def setKubernetesEndpoint(self, kubernetesEndpoint):
        self.kubernetesEndpoint = kubernetesEndpoint

    def getKubernetesEndpoint(self):
        return self.kubernetesEndpoint

    def setNamespace(self, namespace):
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
            elif requestType == "PUT":
                response = requests.put(requestUrl, data=data)

            if str(response.status_code).startswith("2"):
                print "-- OK"
            else:
                print "-- [ERROR] " + str(response.status_code)
                print response.text

        except Exception, e:
            msg = "[ERROR] request error!"

            print msg
            print str(e)
        return str(response.status_code), str(response.text)

    def createPod(self, podModel):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesEndpoint
        podApi = self.KUBERNETES_POD_NAMESPACE_API
        requestUrl = "%s%s" % (endpoint, podApi)
        podJson = podModel.toJSON()
        statusCode, self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, podJson)
        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def deletePod(self, podId):
        endpoint = self.kubernetesEndpoint
        podApi = self.KUBERNETES_POD_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)

        statusCode,  self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def queryPod(self, podId):

        endpoint = self.kubernetesEndpoint
        podApi = self.KUBERNETES_POD_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)
        logging.debug(requestUrl)
        status, queryResult = self.sendRequest(requestUrl, "GET")
        podListModel = Pod.fromJSON(queryResult)
        return podListModel

    def queryPodByLabel(self, labels):
        endpoint = self.kubernetesEndpoint
        podApi = self.KUBERNETES_POD_NAMESPACE_API
        requestUrl = "%s%s?labels=%s" % (endpoint, podApi, labels)

        status, queryResult = self.sendRequest(requestUrl, "GET")
        podListModel = PodList.fromJSON(queryResult)
        return podListModel


    def createService(self, serviceModel):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesEndpoint
        serviceApi = self.KUBERNETES_SERVICE_NAMESPACE_API
        requestUrl = "%s%s" % (endpoint, serviceApi)
        serviceJson = serviceModel.toJSON()
        statusCode, self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, serviceJson)
        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def deleteService(self, serviceId):
        endpoint = self.kubernetesEndpoint
        serviceApi = self.KUBERNETES_SERVICE_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        statusCode,  self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def queryService(self, serviceId):
        endpoint = self.kubernetesEndpoint
        serviceApi = self.KUBERNETES_SERVICE_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        status, queryResult = self.sendRequest(requestUrl, "GET")
        serviceListModel = Service.fromJSON(queryResult)
        return serviceListModel

    def queryServiceByLabel(self, labels):
        endpoint = self.kubernetesEndpoint
        serviceApi = self.KUBERNETES_SERVICE_NAMESPACE_API
        requestUrl = "%s%s?labels=%s" % (endpoint, serviceApi, labels)

        status, queryResult = self.sendRequest(requestUrl, "GET")
        serviceListModel = ServiceList.fromJSON(queryResult)
        return serviceListModel

    def createReplicationController(self, replicationControllerModel):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesEndpoint
        replicationControllerApi = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API
        requestUrl = "%s%s" % (endpoint, replicationControllerApi)
        replicationControllerJson = replicationControllerModel.toJSON()
        statusCode,  self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, replicationControllerJson)

        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def updateReplicationController(self, replicationControllerModel):
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesEndpoint
        replicationControllerId = replicationControllerModel.getId()
        replicationControllerApi = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)
        replicationControllerJson = replicationControllerModel.toJSON()
        status, queryResult = self.sendRequest(requestUrl, "PUT", requestHeader, replicationControllerJson)
        replicationControllerModel = ReplicationControllerList.fromJSON(queryResult)
        return replicationControllerModel

    def deleteReplicationController(self, replicationControllerId):
        endpoint = self.kubernetesEndpoint
        replicationControllerApi = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        statusCode,  self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        self.statusCode = OperationStatus.OperationStatusTranslator.translateStatus(statusCode)
        return self.statusCode

    def queryReplicationController(self, replicationControllerId):
        endpoint = self.kubernetesEndpoint
        replicationControllerApi = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        status, queryResult = self.sendRequest(requestUrl, "GET")
        replicationControllerModel = ReplicationController.fromJSON(queryResult)
        return replicationControllerModel

    def queryReplicationControllerByLabel(self, labels):
        endpoint = self.kubernetesEndpoint
        replicationControllerApi = self.KUBERNETES_REPLICATIONCONTROLLER_NAMESPACE_API
        requestUrl = "%s%s?labels=%s" % (endpoint, replicationControllerApi, labels)

        status, queryResult = self.sendRequest(requestUrl, "GET")
        replicationControllerModel = ReplicationControllerList.fromJSON(queryResult)
        return replicationControllerModel
