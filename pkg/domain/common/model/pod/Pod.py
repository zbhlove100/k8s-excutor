__author__ = 'zhangbohan'
import json
from pkg.domain.common.model.pod.PodState import PodState
class Pod(object):

    def __init__(self
                ,id
                ,apiVersion
                ,desiredState
                ,labels
                ,namespace

    ):
        self.id = id
        self.kind = "Pod"
        self.apiVersion = apiVersion
        self.desiredState = desiredState
        self.labels = labels
        self.namespace = namespace
        pass

    @staticmethod
    def fromJSON(poddJSON):
        pass

    @staticmethod
    def fromDict(poddDict):
        if poddDict.has_key("id") :
            id = poddDict["id"]
        else :
            id = None

        if poddDict.has_key("apiVersion") :
            apiVersion = poddDict["apiVersion"]
        else :
            apiVersion = None

        if poddDict.has_key("labels") :
            labels = poddDict["labels"]
        else :
            labels = None

        if poddDict.has_key("namespace") :
            namespace = poddDict["namespace"]
        else :
            id = None

        if poddDict.has_key("desiredState") :
            tmpDesiredState = poddDict["desiredState"]
            desiredState = PodState.fromDict(tmpDesiredState)
        else :
            desiredState = None


        return Pod(id, apiVersion, desiredState, labels, namespace)

    def toDict(self):
        podDict = {
            "id" : self.id,
            "apiVersion" : self.apiVersion,
            "kind" : self.kind,
            "desiredState" : self.desiredState.toDict(),
            "labels" : self.labels,
            "namespace": self.namespace
        }


        return podDict

    def toJSON(self):
        pod_dict = self.toDict()
        pod_json = json.dumps(pod_dict, indent=2)
        return pod_json

    def setId(self,id):
        self.id = id

    def setApiVersion(self,apiVersion):
        self.apiVersion = apiVersion

    def setDesiredState(self,desiredState):
        self.desiredState = desiredState

    def setLabels(self,labels):
        self.labels = labels

    def getId(self):
        return self.id

    def getApiVersion(self):
        return self.apiVersion

    def getDesiredState(self):
        return self.desiredState

    def getLabels(self):
        return self.labels

    def getKind(self):
        return self.kind

    def setNamespace(self,namespace):
        self.namespace = namespace

    def getNamespace(self):
        return self.namespace