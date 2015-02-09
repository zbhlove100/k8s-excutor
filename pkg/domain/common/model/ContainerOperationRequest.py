__author__ = 'zhangbohan'
import json


class ContainerOperationRequest(object):
    def __init__(self
                ,modelType
                ,action
                ,dataDict
                ,userId
                ,farmName
                ,roleName
                ,targetEndpoint
                ):
        self.modelType = modelType
        self.action = action
        self.dataDict = dataDict
        self.userId = userId
        self.farmName = farmName
        self.roleName = roleName
        self.targetEndpoint = targetEndpoint

        pass

    @staticmethod
    def fromJSON(requestJSON):
        requestDict = json.loads(requestJSON)
        containerOperationRequest = ContainerOperationRequest.fromDict(requestDict)
        return containerOperationRequest

    @staticmethod
    def fromDict(requestDict):
        if requestDict.has_key("modelType") :
            modelType = requestDict["modelType"]
        else :
            modelType = None

        if requestDict.has_key("action") :
            action = requestDict["action"]
        else :
            action = None

        if requestDict.has_key("dataDict") :
            dataDict = requestDict["dataDict"]
        else :
            dataDict = None

        if requestDict.has_key("userId") :
            userId = requestDict["userId"]
        else :
            userId = None

        if requestDict.has_key("farmName") :
            farmName = requestDict["farmName"]
        else :
            farmName = None

        if requestDict.has_key("roleName") :
            roleName = requestDict["roleName"]
        else :
            roleName = None

        if requestDict.has_key("targetEndpoint") :
            targetEndpoint = requestDict["targetEndpoint"]
        else :
            targetEndpoint = None


        return ContainerOperationRequest(modelType,action,dataDict,userId,farmName,roleName,targetEndpoint)

    def toDict(self):
        requestDict = {
             "modelType": self.modelType,
                "action": self.action,
                "dataDict" : self.dataDict,
                "userId" : self.userId,
                "farmName" : self.farmName,
                "roleName" : self.roleName,
                "targetEndpoint" : self.targetEndpoint
        }
        return requestDict

    def toJSON(self):
        pod_dict = self.toDict()
        pod_json = json.dumps(pod_dict, indent=2)
        return pod_json

    def setModelType(self,modelType):
        self.modelType = modelType

    def getModelType(self):
        return self.modelType

    def setAction(self,action):
        self.action = action

    def getAction(self):
        return self.action

    def setDataDict(self,dataDict):
        self.dataDict = dataDict

    def getDataDict(self):
        return self.dataDict

    def setUserId(self,userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def setFarmName(self,farmName):
        self.farmName = farmName

    def getFarmName(self):
        return self.farmName

    def setRoleName(self, roleName):
        self.roleName = roleName

    def getRoleName(self):
        return self.roleName

    def setTargetEndpoint(self, targetEndpoint):
        self.targetEndpoint = targetEndpoint

    def getTargetEndpoint(self):
        return self.targetEndpoint