__author__ = 'zhangbohan'
import logging, os
logging.basicConfig(filename='/tmp/k8s-excutor.log', level=logging.DEBUG)
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.common.logger.LoggerFactory import LoggerFactory


class KubernetesRestClient(IKubernetesClient):
    def __init__(self, kubernetesRestDao):
        self.kubernetesRestDao = kubernetesRestDao
        self.operationResponse = ""
        logging.debug("Init KubernetesRestClient")
        pass

    def setKubernetesRestDao(self, kubernetesRestDao):
        self.kubernetesRestDao = kubernetesRestDao

    def sendRequest(self, requestUrl, requestType, header=None, data=None, timeout=None):
        try:
            customTimeout = 30
            if None != timeout:
                customTimeout = timeout

            import requests

            r = ""
            if requestType == "GET":
                r = requests.get(requestUrl, timeout=timeout)
            elif requestType == "POST":
                r = requests.post(requestUrl, data=data, headers=header, timeout=customTimeout)
            elif requestType == "DELETE":
                r = requests.delete(requestUrl)

            if str(r.status_code) == "200":
                print "-- OK"
            else:
                print "-- [ERROR] " + str(r.status_code)
                print r.text

        except Exception, e:
            msg = "[ERROR] POST request error!"

            print msg
            print str(e)
        return str(r.status_code),str(r.text)

    def createResource(self, objModel):
        kind = objModel.getKind()
        result = ""
        if "Pod" == kind:
            logging.debug("create pod request!")
            result = self.createPod(objModel)
        elif "Service" == kind:
            logging.debug("create service request!")
            result = self.createService(objModel)
        elif "Replication" == kind:
            logging.debug("create replication request!")
            result = self.createReplication(objModel)

        return result

    def deleteResource(self, objModel):
        kind = objModel.getKind()
        result = ""
        if "Pod" == kind:
            result = self.deletePod(objModel)
        elif "Service" == kind:
            result = self.deleteService(objModel)
        elif "ReplicationController" == kind:
            result = self.deleteReplication(objModel)

        return result

    def queryResource(self, objModel):
        kind = objModel.getKind()
        result = ""
        logging.debug("Method queryResource kind:%s", kind)
        if "Pod" == kind:
            logging.debug("querry pod request!")
            result = self.queryPod(objModel)
        elif "Service" == kind:
            result = self.queryService(objModel)
        elif "ReplicationController" == kind:
            result = self.queryReplicationController(objModel)

        return result

    def queryResourceByLabel(self, objModel, labelName):
        kind = objModel.getKind()
        labels = objModel.getLabels()
        labelValue = labels[labelName]
        queryLabel = "%s=%s" % (labelName, labelValue)
        result = ""
        if "pod" == kind:
            result = self.queryPodByLabel(objModel, queryLabel)
        elif "service" == kind:
            result = self.queryServiceByLabel(objModel, queryLabel)
        elif "ReplicationController" == kind:
            result = self.queryReplicationControllerByLabel(objModel, queryLabel)

        return result


    def createPod(self, podModel):
        jsonObj = podModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(podModel.getNamespace())
        requestUrl = "%s%s" % (endpoint, podApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return

    def deletePod(self, podModel):
        podId = podModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(podModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryPod(self, podModel):
        podId = podModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(podModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, podApi, podId)
        logging.debug(requestUrl)
        print(requestUrl)
        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryPodByLabel(self, podModel, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApiWithNamespcae(podModel.getNamespace())
        requestUrl = "%s%s?labels=%s" % (endpoint, podApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse


    def createService(self, serviceModel):
        jsonObj = serviceModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(serviceModel.getNamespace())
        requestUrl = "%s%s" % (endpoint, serviceApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return

    def deleteService(self, serviceModel):
        serviceId = serviceModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(serviceModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryService(self, serviceModel):
        serviceId = serviceModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(serviceModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, serviceApi, serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryServiceByLabel(self, serviceModel, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApiWithNamespcae(serviceModel.getNamespace())
        requestUrl = "%s%s?labels=%s" % (endpoint, serviceApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def createReplicationController(self, replicationControllerModel):
        jsonObj = replicationControllerModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            replicationControllerModel.getNamespace())
        requestUrl = "%s%s" % (endpoint, replicationControllerApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return

    def deleteReplicationController(self, replicationControllerModel):
        replicationControllerId = replicationControllerModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            replicationControllerModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryReplicationController(self, replicationControllerModel):
        replicationControllerId = replicationControllerModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            replicationControllerModel.getNamespace())
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi, replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def queryReplicationControllerByLabel(self, replicationControllerModel, labels):
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApiWithNamespcae(
            replicationControllerModel.getNamespace())
        requestUrl = "%s%s?labels=%s" % (endpoint, replicationControllerApi, labels)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse
