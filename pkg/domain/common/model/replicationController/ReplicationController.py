__author__ = 'zhangbohan'
import  json
class ReplicationController(object):
    def __init__(self
                ,id
                ,apiVersion
                ,labels
                ,desiredState
                ):
        self.id = id
        self.kind = "ReplicationController"
        self.apiVersion = apiVersion
        self.labels = labels
        self.desiredState = desiredState
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
            "labels" : self.labels
        }
        return rcDict

    def toJSON(self):
        rc_dict = self.toDict()
        rc_json = json.dumps(rc_dict, indent=2)
        return rc_json