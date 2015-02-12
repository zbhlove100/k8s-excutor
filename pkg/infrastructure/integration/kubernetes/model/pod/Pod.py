__author__ = 'zhangbohan'
import json

from pkg.infrastructure.integration.kubernetes.model.pod.PodState import PodState
from pkg.infrastructure.integration.kubernetes.model.TypeMeta import TypeMeta


class Pod(object):
    def __init__(self
                 , desiredState=None
                 , currentState=None
                 , nodeSelector=None
                 , labels=None
                 , id=None
                 , apiVersion=None
                 , kind="Pod"
                 , uid=None
                 , creationTimestamp=None
                 , selfLink=None
                 , resourceVersion=None
                 , namespace=None
                 , annotations=None

    ):
        self.desiredState = desiredState
        self.currentState = currentState
        self.nodeSelector = nodeSelector
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
    def fromJSON(podJSON):
        podDict = json.loads(podJSON)
        pod = Pod.fromDict(podDict)
        return pod

    @staticmethod
    def fromDict(podDict):
        if podDict.has_key("desiredState"):
            tmpDesiredState = podDict["desiredState"]
            desiredState = PodState.fromDict(tmpDesiredState)
        else:
            desiredState = None

        if podDict.has_key("currentState"):
            tmpCurrentState = podDict["currentState"]
            currentState = PodState.fromDict(tmpCurrentState)
        else:
            currentState = None

        if podDict.has_key("nodeSelector"):
            nodeSelector = podDict["nodeSelector"]
        else:
            nodeSelector = None

        if podDict.has_key("labels"):
            labels = podDict["labels"]
        else:
            labels = None

        if podDict.has_key("id"):
            id = podDict["id"]
        else:
            id = None

        if podDict.has_key("apiVersion"):
            apiVersion = podDict["apiVersion"]
        else:
            apiVersion = None

        if podDict.has_key("kind"):
            kind = podDict["kind"]
        else:
            kind = None

        if podDict.has_key("uid"):
            uid = podDict["uid"]
        else:
            uid = None

        if podDict.has_key("creationTimestamp"):
            creationTimestamp = podDict["creationTimestamp"]
        else:
            creationTimestamp = None

        if podDict.has_key("selfLink"):
            selfLink = podDict["selfLink"]
        else:
            selfLink = None

        if podDict.has_key("resourceVersion"):
            resourceVersion = podDict["resourceVersion"]
        else:
            resourceVersion = None

        if podDict.has_key("namespace"):
            namespace = podDict["namespace"]
        else:
            namespace = None

        if podDict.has_key("annotations"):
            annotations = podDict["annotations"]
        else:
            annotations = None
        pod = Pod(desiredState
                  , currentState
                  , nodeSelector
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

        return pod

    def toDict(self):
        podDict = {
        }

        if None != self.desiredState:
            podDict["desiredState"] = self.desiredState.toDict()

        if None != self.currentState:
            podDict["currentState"] = self.currentState.toDict()

        if None != self.nodeSelector:
            podDict["nodeSelector"] = self.nodeSelector

        if None != self.labels:
            podDict["labels"] = self.labels

        if None != self.id:
            podDict["id"] = self.id

        if None != self.apiVersion:
            podDict["apiVersion"] = self.apiVersion

        if None != self.kind:
            podDict["kind"] = self.kind

        if None != self.uid:
            podDict["uid"] = self.uid

        if None != self.creationTimestamp:
            podDict["creationTimestamp"] = self.creationTimestamp

        if None != self.selfLink:
            podDict["selfLink"] = self.selfLink

        if None != self.resourceVersion:
            podDict["resourceVersion"] = self.resourceVersion

        if None != self.namespace:
            podDict["namespace"] = self.namespace

        if None != self.annotations:
            podDict["annotations"] = self.annotations
        return podDict

    def toJSON(self):
        pod_dict = self.toDict()
        pod_json = json.dumps(pod_dict, indent=2)
        return pod_json


    def setDesiredState(self, desiredState):
        self.desiredState = desiredState

    def getDesiredState(self):
        return self.desiredState

    def setCurrentState(self, currentState):
        self.currentState = currentState

    def getCurrentState(self):
        return self.currentState

    def setNodeSelector(self, nodeSelector):
        self.nodeSelector = nodeSelector

    def getNodeSelector(self):
        return self.nodeSelector

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





