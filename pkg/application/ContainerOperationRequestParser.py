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
            self.parsePodModel(requestData)
        elif targetType == "service":
            self.parseServiceModel(requestData)
        elif targetType == "replicationController":
            self.parseReplicationControllerModel(requestData)
        return result

    def parsePodModel(self,podRequestData):
        return

    def parseServiceModel(self,serviceRequestData):
        return

    def parseReplicationControllerModel(self,replicationControllerRequestData):
        return