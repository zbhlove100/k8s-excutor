__author__ = 'zhangbohan'
from pkg.domain.common.model.pod.Manifest import Manifest
import json

class PodState(object):

    def __init__(self,manifest
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
    def fromDict(PodStateDict):
        if PodStateDict.has_key("manifest") :
            tmpManifest = PodStateDict["manifest"]
            manifest = Manifest.fromDict(tmpManifest)
        else :
            manifest = None

        if PodStateDict.has_key("status") :
            status = PodStateDict["status"]
        else :
            status = None

        if PodStateDict.has_key("host") :
            host = PodStateDict["host"]
        else :
            host = None

        if PodStateDict.has_key("hostip") :
            hostip = PodStateDict["hostip"]
        else :
            hostip = None

        if PodStateDict.has_key("podip") :
            podip = PodStateDict["podip"]
        else :
            podip = None
        return PodState(manifest, status, host, hostip, podip)

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

    def setManifest(self,manifest):
        self.manifest = manifest

    def setStatus(self,status):
        self.status = status

    def setHost(self,host):
        self.host = host

    def setHostip(self,hostip):
        self.hostip = hostip

    def setPodip(self,podip):
        self.podip = podip

    def getManifest(self):
        return self.manifest

    def getStatus(self):
        return self.status

    def getHost(self):
        return self.host

    def getHostip(self):
        return self.hostip

    def getPodip(self):
        return self.podip