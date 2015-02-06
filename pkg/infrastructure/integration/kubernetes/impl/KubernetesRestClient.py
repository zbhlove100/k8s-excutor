__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient

class KubernetesRestClient(IKubernetesClient):


    def __init__(self,kubernetesRestDao):
        self.kubernetesRestDao = kubernetesRestDao
        pass

    def setKubernetesRestDao(self,kubernetesRestDao):
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
        return str(r.status_code)

    def createResource(self, objModel):
        kind = objModel.getKind()
        result = ""
        if "pod" == kind:
            result = self.createPod(objModel)
        elif "service" == kind:
            result = self.createService(objModel)
        elif "replication" == kind:
            result = self.createReplication(objModel)

        return result

    def deleteResource(self,objModel):
        kind = objModel.getKind()
        result = ""
        if "pod" == kind:
            result = self.deletePod(objModel)
        elif "service" == kind:
            result = self.deleteService(objModel)
        elif "replication" == kind:
            result = self.deleteReplication(objModel)

        return result

    def querryResource(self,objModel):
        kind = objModel.getKind()
        result = ""
        if "pod" == kind:
            result = self.queryPodStatus(objModel)
        elif "service" == kind:
            result = self.queryService(objModel)
        elif "replication" == kind:
            result = self.queryReplication(objModel)

        return result

    def createPod(self,podModel):
        jsonObj = podModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApi()
        requestUrl = "%s%s" % (endpoint, podApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return
    def deletePod(self, podModel):
        podId = podModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.podApi()
        requestUrl = "%s%s/%s" % (endpoint, podApi,podId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryPod(self,podModel):
        podId = podModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        podApi = self.kubernetesRestDao.getPodApi()
        requestUrl = "%s%s/%s" % (endpoint, podApi,podId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def createService(self,serviceModel):
        jsonObj = serviceModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApi()
        requestUrl = "%s%s" % (endpoint, serviceApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return
    def deleteService(self, serviceModel):
        serviceId = serviceModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApi()
        requestUrl = "%s%s/%s" % (endpoint, serviceApi,serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryService(self,serviceModel):
        serviceId = serviceModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        serviceApi = self.kubernetesRestDao.getServiceApi()
        requestUrl = "%s%s/%s" % (endpoint, serviceApi,serviceId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse

    def createReplicationController(self,replicationControllerModel):
        jsonObj = replicationControllerModel.toJSON()
        requestHeader = {'content-type': 'application/json'}
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApi()
        requestUrl = "%s%s" % (endpoint, replicationControllerApi)
        self.operationResponse = self.sendRequest(requestUrl, "POST", requestHeader, jsonObj)
        return
    def deleteReplicationController(self, replicationControllerModel):
        replicationControllerId = replicationControllerModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApi()
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi,replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "DELETE")
        return self.operationResponse

    def queryReplicationController(self,replicationControllerModel):
        replicationControllerId = replicationControllerModel.getId()
        endpoint = self.kubernetesRestDao.getKubernetesEndpoint()
        replicationControllerApi = self.kubernetesRestDao.getReplicationControllerApi()
        requestUrl = "%s%s/%s" % (endpoint, replicationControllerApi,replicationControllerId)

        self.operationResponse = self.sendRequest(requestUrl, "GET")
        return self.operationResponse