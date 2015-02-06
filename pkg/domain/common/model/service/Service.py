__author__ = 'zhangbohan'
import json
class Service(object):
    def __init__(self
                ,id
                ,apiVersion
                ,selector
                ,protocol
                ,containerPort
                ,port
                ,publicIPs=None
                ):
        self.id = id
        self.kind = "Service"
        self.apiVersion = apiVersion
        self.selector = selector
        self.protocol = protocol
        self.containerPort = containerPort
        self.port = port
        self.publicIPs = publicIPs
        pass

    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        serviceDict = {
            "id" : self.id,
            "apiVersion" : self.apiVersion,
            "kind" : self.kind,
            "selector" : self.selector,
            "protocol" : self.protocol,
            "containerPort" : self.containerPort,
            "port" : self.port
        }
        if None != self.publicIPs:
            serviceDict["publicIPs"] = self.publicIPs

        return serviceDict

    def toJSON(self):
        service_dict = self.toDict()
        service_json = json.dumps(service_dict, indent=2)
        return service_json

    def setId(self,id):
        self.id = id

    def setApiVersion(self,apiVersion):
        self.apiVersion = apiVersion



    def setLabels(self,labels):
        self.labels = labels

    def getId(self,id):
        return self.id

    def getApiVersion(self,apiVersion):
        return self.apiVersion



    def getLabels(self,labels):
        return self.labels