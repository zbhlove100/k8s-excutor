__author__ = 'zhangbohan'
import json
class Pod(object):

    def __init__(self
                ,id=None
                ,apiVersion=None
                ,desiredState=None
                ,labels=None

    ):
        self.id = id
        self.kind = "Pod"
        self.apiVersion = apiVersion
        self.desiredState = desiredState
        self.labels = labels
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
            "labels" : self.labels
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

    def getId(self,id):
        return self.id

    def getApiVersion(self,apiVersion):
        return self.apiVersion

    def getDesiredState(self,desiredState):
        return self.desiredState

    def getLabels(self,labels):
        return self.labels