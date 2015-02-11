__author__ = 'zhangbohan'
import json

from pkg.infrastructure.integration.kubernetes.model.pod.PodState import PodState
from pkg.infrastructure.integration.kubernetes.model.TypeMeta import TypeMeta


class Pod(object):
    def __init__(self
                 , typeMeta=None
                 , desiredState=None
                 , currentState=None
                 , nodeSelector=None
                 , labels=None


    ):
        self.typeMeta = typeMeta
        self.desiredState = desiredState
        self.currentState = currentState
        self.nodeSelector = nodeSelector
        self.labels = labels
        pass

    @staticmethod
    def fromJSON(podJSON):
        podDict = json.loads(podJSON)
        pod = Pod.fromDict(podDict)
        return pod

    @staticmethod
    def fromDict(podDict):

        if podDict.has_key("typeMeta"):
            tmpTypeMeta = podDict["typeMeta"]
            typeMeta = TypeMeta.fromDict(tmpTypeMeta)
        else:
            typeMeta = None

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

        return Pod(typeMeta
                   , desiredState
                   , currentState
                   , nodeSelector
                   , labels
        )

    def toDict(self):
        podDict = {

        }
        if None != self.typeMeta:
            podDict["typeMeta"] = self.typeMeta.toDict()

        if None != self.desiredState:
            podDict["desiredState"] = self.desiredState.toDict()

        if None != self.currentState:
            podDict["currentState"] = self.currentState.toDict()

        if None != self.nodeSelector:
            podDict["nodeSelector"] = self.nodeSelector

        if None != self.labels:
            podDict["labels"] = self.labels


        return podDict

    def toJSON(self):
        pod_dict = self.toDict()
        pod_json = json.dumps(pod_dict, indent=2)
        return pod_json

    def setTypeMeta(self, typeMeta):
        self.typeMeta = typeMeta

    def getTypeMeta(self):
        return self.typeMeta

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






