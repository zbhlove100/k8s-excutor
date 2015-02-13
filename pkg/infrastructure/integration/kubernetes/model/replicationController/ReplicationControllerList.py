__author__ = 'zhangbohan'
import json
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController


class ReplicationControllerList(object):
    def __init__(self
                 , items=None
                 , id=None
                 , apiVersion=None
                 , kind="ReplicationController"
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
    def fromJSON(replicationControllerJSON):
        replicationControllerDict = json.loads(replicationControllerJSON)
        replicationController = ReplicationControllerList.fromDict(replicationControllerDict)
        return replicationController

    @staticmethod
    def fromDict(replicationControllerDict):
        if replicationControllerDict.has_key("items") and None != replicationControllerDict["items"]:
            tmpItems = replicationControllerDict["items"]
            items = []
            for item in tmpItems:
                replicationController = ReplicationController.fromDict(item)
                items.append(replicationController)
        else:
            items = None


        if replicationControllerDict.has_key("id"):
            id = replicationControllerDict["id"]
        else:
            id = None

        if replicationControllerDict.has_key("apiVersion"):
            apiVersion = replicationControllerDict["apiVersion"]
        else:
            apiVersion = None

        if replicationControllerDict.has_key("kind"):
            kind = replicationControllerDict["kind"]
        else:
            kind = None

        if replicationControllerDict.has_key("uid"):
            uid = replicationControllerDict["uid"]
        else:
            uid = None

        if replicationControllerDict.has_key("creationTimestamp"):
            creationTimestamp = replicationControllerDict["creationTimestamp"]
        else:
            creationTimestamp = None

        if replicationControllerDict.has_key("selfLink"):
            selfLink = replicationControllerDict["selfLink"]
        else:
            selfLink = None

        if replicationControllerDict.has_key("resourceVersion"):
            resourceVersion = replicationControllerDict["resourceVersion"]
        else:
            resourceVersion = None

        if replicationControllerDict.has_key("namespace"):
            namespace = replicationControllerDict["namespace"]
        else:
            namespace = None

        if replicationControllerDict.has_key("annotations"):
            annotations = replicationControllerDict["annotations"]
        else:
            annotations = None
        replicationController = ReplicationControllerList(items
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

        return replicationController

    def toDict(self):
        replicationControllerDict = {
        }

        if None != self.items:
            replicationControllers = []
            for item in self.items:
                replicationControllers.append(item)
            replicationControllerDict["items"] = replicationControllers

        if None != self.id:
            replicationControllerDict["id"] = self.id

        if None != self.apiVersion:
            replicationControllerDict["apiVersion"] = self.apiVersion

        if None != self.kind:
            replicationControllerDict["kind"] = self.kind

        if None != self.uid:
            replicationControllerDict["uid"] = self.uid

        if None != self.creationTimestamp:
            replicationControllerDict["creationTimestamp"] = self.creationTimestamp

        if None != self.selfLink:
            replicationControllerDict["selfLink"] = self.selfLink

        if None != self.resourceVersion:
            replicationControllerDict["resourceVersion"] = self.resourceVersion

        if None != self.namespace:
            replicationControllerDict["namespace"] = self.namespace

        if None != self.annotations:
            replicationControllerDict["annotations"] = self.annotations
        return replicationControllerDict

    def toJSON(self):
        replicationController_dict = self.toDict()
        replicationController_json = json.dumps(replicationController_dict, indent=2)
        return replicationController_json


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

