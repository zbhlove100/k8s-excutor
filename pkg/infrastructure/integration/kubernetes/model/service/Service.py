__author__ = 'zhangbohan'
import json


class Service(object):
    def __init__(self
                 , id
                 , apiVersion
                 , selector
                 , protocol
                 , containerPort
                 , port
                 , namespace
                 , publicIPs=None
                 , labels=None
    ):
        self.id = id
        self.kind = "Service"
        self.apiVersion = apiVersion
        self.selector = selector
        self.protocol = protocol
        self.containerPort = containerPort
        self.port = port
        self.publicIPs = publicIPs
        self.namespace = namespace
        self.labels = labels
        pass

    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        serviceDict = {
            "id": self.id,
            "apiVersion": self.apiVersion,
            "kind": self.kind,
            "selector": self.selector,
            "protocol": self.protocol,
            "containerPort": self.containerPort,
            "port": self.port,
            "namespace": self.namespace,
            "publicIPs": self.publicIPs,
            "labels": self.labels
        }
        if None != self.publicIPs:
            serviceDict["publicIPs"] = self.publicIPs

        return serviceDict

    def toJSON(self):
        service_dict = self.toDict()
        service_json = json.dumps(service_dict, indent=2)
        return service_json

    def setId(self, id):
        self.id = id

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def setLabels(self, labels):
        self.labels = labels

    def getId(self):
        return self.id

    def getApiVersion(self):
        return self.apiVersion


    def getLabels(self):
        return self.labels

    def getKind(self):
        return self.kind

    def setNamespace(self, namespace):
        self.namespace = namespace

    def getNamespace(self):
        return self.namespace

    def setSelector(self, selector):
        self.selector = selector

    def getSelector(self):
        return self.selector

    def setProtocol(self, protocol):
        self.protocol = protocol

    def getProtocol(self):
        return self.protocol

    def setContainerPort(self, containerPort):
        self.containerPort = containerPort

    def getContainerPort(self):
        return self.containerPort

    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port

    def setPublicIPs(self, publicIPs):
        self.publicIPs = publicIPs

    def getPublicIPs(self):
        return self.publicIPs
