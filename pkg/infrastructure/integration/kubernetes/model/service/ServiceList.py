__author__ = 'zhangbohan'
import json
from pkg.infrastructure.integration.kubernetes.model.service.Service import Service
class ServiceList(object):
    def __init__(self
                 , items=None
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
        self.items = items
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
        service = ServiceList.fromDict(serviceDict)
        return service

    @staticmethod
    def fromDict(serviceDict) :
        if serviceDict.has_key("items") and None != serviceDict["items"]:
            tmpItems = serviceDict["items"]
            items = []
            for item in tmpItems:
                service = Service.fromDict(item)
                items.append(service)
        else:
            items = None


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
        serviceList = ServiceList(items
                  , id
                  , apiVersion
                  , kind
                  , uid
                  , creationTimestamp
                  , selfLink
                  , resourceVersion
                  , namespace
                  , annotations
                  )

        return serviceList

    def toDict(self):
        serviceDict = {
        }

        if None != self.items:
            services = []
            for item in self.items:
                services.append(item)
            serviceDict["items"] = services

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


    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items

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

