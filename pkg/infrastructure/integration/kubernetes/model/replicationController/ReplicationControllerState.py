__author__ = 'zhangbohan'

import json

class ReplicationControllerState(object):

    def __init__(self
                 , replicas
                 , replicaSelector
                 , podTemplate
                ):
        self.replicas = replicas
        self.replicaSelector = replicaSelector
        self.podTemplate = podTemplate

    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        rcStateDict = {
            "replicas" : self.replicas,
            "replicaSelector" : self.replicaSelector,
            "podTemplate" : self.podTemplate.toDict()
        }
        return rcStateDict

    def toJSON(self):
        rcState_dict = self.toDict()
        rcState_json = json.dumps(rcState_dict, indent=2)
        return rcState_json