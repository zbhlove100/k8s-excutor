__author__ = 'zhangbohan'

import json
from pkg.infrastructure.integration.kubernetes.model.replicationController.PodTemplate import PodTemplate


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
    def fromJSON(replicationControllerStateJSON):
        replicationControllerStateDict = json.loads(replicationControllerStateJSON)
        replicationControllerState = ReplicationControllerState.fromDict(replicationControllerStateDict)
        return replicationControllerState

    @staticmethod
    def fromDict(replicationControllerStateDict):
        if replicationControllerStateDict.has_key("replicas") :
            replicas = replicationControllerStateDict["replicas"]
        else :
            replicas = None

        if replicationControllerStateDict.has_key("replicaSelector") :
            replicaSelector = replicationControllerStateDict["replicaSelector"]
        else :
            replicaSelector = None

        if replicationControllerStateDict.has_key("podTemplate") :
            tempPodTemplate = replicationControllerStateDict["podTemplate"]
            podTemplate = PodTemplate.fromDict(tempPodTemplate)
        else :
            podTemplate = None

        replicationControllerState = ReplicationControllerState(replicas, replicaSelector, podTemplate)
        return replicationControllerState

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

    def setReplicas(self, replicas):
        self.replicas = replicas

    def getReplicas(self):
        return self.replicas

    def setReplicaSelector(self, replicaSelector):
        self.replicaSelector = replicaSelector

    def getReplicaSelector(self):
        return self.replicaSelector

    def setPodTemplate(self, podTemplate):
        self.podTemplate = podTemplate

    def getPodTemplate(self):
        return self.podTemplate