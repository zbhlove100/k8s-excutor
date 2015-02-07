__author__ = 'zhangbohan'
import json
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
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

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