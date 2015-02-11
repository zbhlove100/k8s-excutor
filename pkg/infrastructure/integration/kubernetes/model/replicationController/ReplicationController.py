__author__ = 'zhangbohan'
import  json
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationControllerState import ReplicationControllerState
class ReplicationController(object):
    def __init__(self
                ,id
                ,apiVersion
                ,labels
                ,desiredState
                ,resourceVersion=None
                ,namespace=None
                ):
        self.id = id
        self.kind = "ReplicationController"
        self.apiVersion = apiVersion
        self.labels = labels
        self.desiredState = desiredState
        self.resourceVersion = resourceVersion
        self.namespace = namespace

        pass

    @staticmethod
    def fromJSON(replicationControllerJSON):
        replicationControllerDict = json.loads(replicationControllerJSON)
        replicationController = ReplicationController.fromDict(replicationControllerDict)
        return replicationController

    @staticmethod
    def fromDict(replicationControllerDict):
        if replicationControllerDict.has_key("id") :
            id = replicationControllerDict["id"]
        else :
            id = None

        if replicationControllerDict.has_key("apiVersion") :
            apiVersion = replicationControllerDict["apiVersion"]
        else :
            apiVersion = None

        if replicationControllerDict.has_key("labels") :
            labels = replicationControllerDict["labels"]
        else :
            labels = None

        if replicationControllerDict.has_key("desiredState") :
            tempDesiredState = replicationControllerDict["desiredState"]
            desiredState = ReplicationControllerState.fromDict(tempDesiredState)
        else :
            desiredState = None

        if replicationControllerDict.has_key("resourceVersion") :
            resourceVersion = replicationControllerDict["resourceVersion"]
        else :
            resourceVersion = None

        if replicationControllerDict.has_key("namespace") :
            namespace = replicationControllerDict["namespace"]
        else :
            namespace = None
        replicationController = ReplicationController(id, apiVersion, labels, desiredState, resourceVersion, namespace)
        return replicationController

    def toDict(self):
        rcDict = {
            "id" : self.id,
            "kind" : self.kind,
            "apiVersion" : self.apiVersion,
            "desiredState" : self.desiredState.toDict(),
            "labels" : self.labels,
            "namespace":self.namespace
        }
        if None != self.resourceVersion:
            rcDict["resourceVersion"] = self.resourceVersion

        return rcDict

    def toJSON(self):
        rc_dict = self.toDict()
        rc_json = json.dumps(rc_dict, indent=2)
        return rc_json

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setLabels(self, labels):
        self.labels = labels

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

    def setResourceVersion(self, resourceVersion):
        self.resourceVersion = resourceVersion

    def getResourceVersion(self):
        return self.resourceVersion