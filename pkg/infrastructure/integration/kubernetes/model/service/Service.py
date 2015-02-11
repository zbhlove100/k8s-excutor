__author__ = 'zhangbohan'
import json


class Service(object):
    def __init__(self
                 , selector=None
                 , protocol=None
                 , containerPort=None
                 , port=None
                 , publicIPs=None
                 , labels=None
                 , proxyPort=None
                 , sessionAffinity=None
                 , id=None
                 , apiVersion=None
                 , kind="Service"
                 , uid=None
                 , creationTimestamp=None
                 , selfLink=None
                 , resourceVersion=None
                 , namespace=None
                 , annotations=None
    ):
        self.selector = selector
        self.protocol = protocol
        self.containerPort = containerPort
        self.port = port
        self.publicIPs = publicIPs
        self.labels = labels
        self.proxyPort = proxyPort
        self.sessionAffinity = sessionAffinity
        self.id = id
        self.apiVersion = apiVersion
        self.kind = kind
        self.uid = uid
        self.creationTimestamp = creationTimestamp
        self.selfLink = selfLink
        self.resourceVersion = resourceVersion
        self.namespace = namespace
        self.annotations = annotations
        pass

    @staticmethod
    def fromJSON(serviceJSON):
        serviceDict = json.loads(serviceJSON)
        service = Service.fromDict(serviceDict)
        return service

    @staticmethod
    def fromDict(serviceDict):

        if serviceDict.has_key("selector") :
            selector = serviceDict["selector"]
        else :
            selector = None

        if serviceDict.has_key("protocol") :
            protocol = serviceDict["protocol"]
        else :
            protocol = None

        if serviceDict.has_key("containerPort") :
            containerPort = serviceDict["containerPort"]
        else :
            containerPort = None

        if serviceDict.has_key("port") :
            port = serviceDict["port"]
        else :
            port = None

        if serviceDict.has_key("publicIPs") :
            publicIPs = serviceDict["publicIPs"]
        else :
            publicIPs = None

        if serviceDict.has_key("labels") :
            labels = serviceDict["labels"]
        else :
            labels = None

        if serviceDict.has_key("proxyPort") :
            proxyPort = serviceDict["proxyPort"]
        else :
            proxyPort = None

        if serviceDict.has_key("sessionAffinity") :
            sessionAffinity = serviceDict["sessionAffinity"]
        else :
            sessionAffinity = None

        if serviceDict.has_key("id"):
            id = serviceDict["id"]
        else:
            id = None

        if serviceDict.has_key("apiVersion"):
            apiVersion = serviceDict["apiVersion"]
        else:
            apiVersion = None

        if serviceDict.has_key("kind"):
            kind = serviceDict["kind"]
        else:
            kind = None

        if serviceDict.has_key("uid"):
            uid = serviceDict["uid"]
        else:
            uid = None

        if serviceDict.has_key("creationTimestamp"):
            creationTimestamp = serviceDict["creationTimestamp"]
        else:
            creationTimestamp = None

        if serviceDict.has_key("selfLink"):
            selfLink = serviceDict["selfLink"]
        else:
            selfLink = None

        if serviceDict.has_key("resourceVersion"):
            resourceVersion = serviceDict["resourceVersion"]
        else:
            resourceVersion = None

        if serviceDict.has_key("namespace"):
            namespace = serviceDict["namespace"]
        else:
            namespace = None

        if serviceDict.has_key("annotations"):
            annotations = serviceDict["annotations"]
        else:
            annotations = None
            
        service = Service(selector
                 , protocol
                 , containerPort
                 , port
                 , publicIPs
                 , labels
                 , proxyPort
                 , sessionAffinity
                 , id
                 , apiVersion
                 , kind
                 , uid
                 , creationTimestamp
                 , selfLink
                 , resourceVersion
                 , namespace
                 , annotations)
        return service

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
        }
        if None != self.selector:
            serviceDict["selector"] = self.selector

        if None != self.protocol:
            serviceDict["protocol"] = self.protocol
        if None != self.containerPort:
            serviceDict["containerPort"] = self.containerPort

        if None != self.port:
            serviceDict["port"] = self.port
        if None != self.publicIPs:
            serviceDict["publicIPs"] = self.publicIPs

        if None != self.labels:
            serviceDict["labels"] = self.labels

        if None != self.proxyPort:
            serviceDict["proxyPort"] = self.proxyPort

        if None != self.sessionAffinity:
            serviceDict["sessionAffinity"] = self.sessionAffinity

        if None != self.id:
            serviceDict["id"] = self.id

        if None != self.apiVersion:
            serviceDict["apiVersion"] = self.apiVersion

        if None != self.kind:
            serviceDict["kind"] = self.kind

        if None != self.uid:
            serviceDict["uid"] = self.uid

        if None != self.creationTimestamp:
            serviceDict["creationTimestamp"] = self.creationTimestamp

        if None != self.selfLink:
            serviceDict["selfLink"] = self.selfLink

        if None != self.resourceVersion:
            serviceDict["resourceVersion"] = self.resourceVersion

        if None != self.namespace:
            serviceDict["namespace"] = self.namespace

        if None != self.annotations:
            serviceDict["annotations"] = self.annotations
            
        return serviceDict

    def toJSON(self):
        service_dict = self.toDict()
        service_json = json.dumps(service_dict, indent=2)
        return service_json


    def setLabels(self, labels):
        self.labels = labels

    def getLabels(self):
        return self.labels

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

    def setProxyPort(self, proxyPort):
        self.proxyPort = proxyPort

    def getProxyPort(self):
        return self.proxyPort

    def setSessionAffinity(self, sessionAffinity):
        self.sessionAffinity = sessionAffinity

    def getSessionAffinity(self):
        return self.sessionAffinity

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setKind(self, kind):
        self.kind = kind

    def getKind(self):
        return self.kind

    def setUid(self, uid):
        self.uid = uid

    def getUid(self):
        return self.uid

    def setCreationTimestamp(self, creationTimestamp):
        self.creationTimestamp = creationTimestamp

    def getCreationTimestamp(self):
        return self.creationTimestamp

    def setSelfLink(self, selfLink):
        self.selfLink = selfLink

    def getSelfLink(self):
        return self.selfLink

    def setResourceVersion(self, resourceVersion):
        self.resourceVersion = resourceVersion

    def getResourceVersion(self):
        return self.resourceVersion

    def setNamespace(self, namespace):
        self.namespace = namespace

    def getNamespace(self):
        return self.namespace

    def setAnnotations(self, annotations):
        self.annotations = annotations

    def getAnnotations(self):
        return self.annotations