__author__ = 'zhangbohan'

import json


class Manifest(object):
    def __init__(self
                 , version=None
                 , id=None
                 #, UUID=None
                 , volumes=None
                 , containers=None
                 #, restartPolicy=None
                 #, dNSPolicy=None
    ):
        self.version = version
        self.id = id
        # self.UUID = UUID
        self.volumes = volumes
        self.containers = containers
        #self.restartPolicy = restartPolicy
        #self.dNSPolicy = dNSPolicy
        pass


    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        manifestDict = {}
        paramList = ['version', 'id', 'volumes', 'containers']
        for p in paramList:
            if None != self.__dict__[p]:
                if p == "containers":
                    temp = []
                    for item in self.containers:
                        temp.append(item.toDict())
                    manifestDict[p] = temp
                else:
                    manifestDict[p] = self.__dict__[p]

        return manifestDict

    def toJSON(self):
        manifest_dict = self.toDict()
        manifest_json = json.dumps(manifest_dict, indent=2)
        return manifest_json

    def setVersion(self,version):
        self.version = version

    def setId(self,id):
        self.id = id

    def setVolumes(self,volumes):
        self.volumes = volumes

    def setContainers(self,containers):
        self.containers = containers

    def getVersion(self):
        return self.manifest

    def getId(self):
        return self.id

    def getVolumes(self):
        return self.volumes

    def getContainers(self):
        return self.Containers

