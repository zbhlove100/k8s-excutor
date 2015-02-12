__author__ = 'zhangbohan'
import  json
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationControllerState import ReplicationControllerState
class ReplicationController(object):
    def __init__(self
                 , desiredState=None
                 , currentState=None
                 , labels=None
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
        self.desiredState = desiredState
        self.currentState = currentState
        self.labels = labels
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
        replicationController = ReplicationController.fromDict(replicationControllerDict)
        return replicationController

    @staticmethod
    def fromDict(replicationControllerDict):
        if replicationControllerDict.has_key("desiredState"):
            tmpDesiredState = replicationControllerDict["desiredState"]
            desiredState = ReplicationControllerState.fromDict(tmpDesiredState)
        else:
            desiredState = None

        if replicationControllerDict.has_key("currentState"):
            tmpCurrentState = replicationControllerDict["currentState"]
            currentState = ReplicationControllerState.fromDict(tmpCurrentState)
        else:
            currentState = None

        if replicationControllerDict.has_key("labels"):
            labels = replicationControllerDict["labels"]
        else:
            labels = None

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

        return ReplicationController(desiredState
                   , currentState
                   , labels
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

    def toDict(self):
        replicationControllerDict = {
        }
        if None != self.desiredState:
            replicationControllerDict["desiredState"] = self.desiredState.toDict()

        if None != self.currentState:
            replicationControllerDict["currentState"] = self.currentState.toDict()

        if None != self.labels:
            replicationControllerDict["labels"] = self.labels

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
        rc_dict = self.toDict()
        rc_json = json.dumps(rc_dict, indent=2)
        return rc_json

    def setDesiredState(self, desiredState):
        self.desiredState = desiredState

    def getDesiredState(self):
        return self.desiredState

    def setCurrentState(self, currentState):
        self.currentState = currentState

    def getCurrentState(self):
        return self.currentState

    def setLabels(self, labels):
        self.labels = labels

    def getLabels(self):
        return self.labels

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