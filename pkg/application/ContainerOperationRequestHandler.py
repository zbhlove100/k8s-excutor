__author__ = 'zhangbohan'
import json
class ContainerOperationRequestHandler(object):
    def __init__(self,requestParser):
        self.requestParser = requestParser
        pass
    def handle(self,containerOperationRequest):
        result = ""
        requestDataDict = json.loads(containerOperationRequest)
        targetType = requestDataDict['type']
        action = requestDataDict['action']
        dataDict = requestDataDict['data']
        userId = requestDataDict['userId']
        if targetType == "pod":
            self.requestParser.parsePodModel(dataDict)
        elif targetType == "service":
            self.requestParser.parseServiceModel(dataDict)
        elif targetType == "replicationController":
            self.requestParser.parseReplicationControllerModel(dataDict)
        return result
        pass