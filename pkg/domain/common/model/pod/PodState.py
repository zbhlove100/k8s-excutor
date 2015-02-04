__author__ = 'zhangbohan'

import json

class PodState(object):

    def __init__(self,manifest=None
                    ,status=None
                   # ,Message=None
                    ,host=None
                    ,hostip=None
                    ,podip=None
                   # ,PodInfo=None
                ):
        self.manifest = manifest
        self.status = status
        #self.Message = Message
        self.host = host
        self.hostip = hostip
        self.podip = podip
        #self.PodInfo = PodInfo

    @staticmethod
    def fromJSON(buildJSON):
        buildDict = json.loads(buildJSON)
        build = PodState.fromDict(buildDict)
        return build

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        podStateDict = {}

        if None!= self.status:
            podStateDict['status'] = self.status
        if None!= self.host:
            podStateDict['host'] = self.host
        if None!= self.hostip:
            podStateDict['hostip'] = self.hostip
        if None!= self.podip:
            podStateDict['podip'] = self.podip
        if None!= self.manifest:
            podStateDict['manifest'] = self.manifest.toDict()
        return podStateDict

    def toJSON(self):
        build_dict = self.toDict()
        build_json = json.dumps(build_dict, indent=2)
        return build_json