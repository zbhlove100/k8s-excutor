__author__ = 'zhangbohan'
import json


class ContainerOperationRequestParser(object):
    def __init__(self):
        pass

    def parseJsonToModel(self, requestData):
        result = ""
        requestDataDict = json.loads(requestData)
        targetType = requestData['type']
        if targetType == "pod":
            self.parsePodModel(requestDataDict)
        elif targetType == "service":
            self.parseServiceModel(requestDataDict)
        elif targetType == "replicationController":
            self.parseReplicationControllerModel(requestDataDict)
        return result

    def parsePodModel(self, podRequestDataDict):

        return

    def parseServiceModel(self, serviceRequestDataDict):
        return

    def parseReplicationControllerModel(self, replicationControllerRequestDataDict):
        return