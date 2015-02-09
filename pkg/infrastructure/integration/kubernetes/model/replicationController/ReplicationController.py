__author__ = 'zhangbohan'
import  json
class ReplicationController(object):
    def __init__(self
                ,id
                ,apiVersion
                ,labels
                ,desiredState
                ,namespace
                ):
        self.id = id
        self.kind = "ReplicationController"
        self.apiVersion = apiVersion
        self.labels = labels
        self.desiredState = desiredState
        self.namespace = namespace
        pass

    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        rcDict = {
            "id" : self.id,
            "kind" : self.kind,
            "apiVersion" : self.apiVersion,
            "desiredState" : self.desiredState.toDict(),
            "labels" : self.labels,
            "namespace":self.namespace
        }
        return rcDict

    def toJSON(self):
        rc_dict = self.toDict()
        rc_json = json.dumps(rc_dict, indent=2)
        return rc_json

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

    def setDesiredState(self, desiredState):
        self.desiredState = desiredState

    def getDesiredState(self):
        return self.desiredState