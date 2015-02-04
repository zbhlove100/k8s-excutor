__author__ = 'zhangbohan'
import json
class PodTemplate(object):
    def __init__(self
                ,desiredState
                ,labels
                ):
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
        podTemplateDict = {
            "desiredState" : self.desiredState.toDict(),
            "labels" : self.labels
        }
        return podTemplateDict

    def toJSON(self):
        podTemplate_dict = self.toDict()
        podTemplate_json = json.dumps(podTemplate_dict, indent=2)
        return podTemplate_json