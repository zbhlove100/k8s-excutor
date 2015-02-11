__author__ = 'zhangbohan'
import json
from pkg.infrastructure.integration.kubernetes.model.pod.PodState import PodState
class PodTemplate(object):
    def __init__(self
                ,desiredState
                ,labels
                ):
         self.desiredState = desiredState
         self.labels = labels
         pass

    @staticmethod
    def fromJSON(podTemplateJSON):
        podTemplateDict = json.loads(podTemplateJSON)
        podTemplate = PodTemplate.fromDict(podTemplateDict)
        return podTemplate

    @staticmethod
    def fromDict(podTemplateDict):
        if podTemplateDict.has_key("desiredState") :
            tmpDesiredState = podTemplateDict["desiredState"]
            desiredState = PodState.fromDict(tmpDesiredState)
        else :
            desiredState = None

        if podTemplateDict.has_key("labels") :
            labels = podTemplateDict["labels"]
        else :
            labels = None

        podtemplate = PodTemplate(desiredState, labels)
        return podtemplate

    def toDict(self):
        podTemplateDict = {
            "desiredState" : self.desiredState.toDict(),
            "labels" : self.labels
        }
        return podTemplateDict

    def toJSON(self):
        podTemplate_dict = self.toDict()
        podTemplate_json = json.dumps(podTemplate_dict, indent=2)
        return podTemplate_json


    def setDesiredState(self, desiredState):
        self.desiredState = desiredState

    def getDesiredState(self):
        return self.desiredState

    def setLabels(self, labels):
        self.labels = labels

    def getLabels(self):
        return self.labels