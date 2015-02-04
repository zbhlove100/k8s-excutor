__author__ = 'zhangbohan'
import json
class Containers(object):

    def __init__(self
                , name=None
                ,image=None
                ,command=None
                ,ports=None
                ,env=None
                ,memory=None
                ,cpu=None
                ,volumeMounts=None
                #,livenessProbe=None
                #,lifecycle=None
                #,terminationMessagePath=None
                #,privileged=None
                #,imagePullPolicy=None
    ):
        self.name = name
        self.image = image
        self.command = command
        self.ports = ports
        self.env = env
        self.memory = memory
        self.cpu = cpu
        self.volumeMounts = volumeMounts
        pass

    @staticmethod
    def fromJSON(buildJSON):
        pass

    @staticmethod
    def fromDict(buildDict):
        pass

    def toDict(self):
        containerDict = {}
        paramList = ['name', 'image', 'command', 'ports', 'env', 'memory', 'cpu', 'volumeMounts']
        for p in paramList:
            if None != self.__dict__[p]:
                containerDict[p] = self.__dict__[p]

        return containerDict

    def toJSON(self):
        container_dict = self.toDict()
        container_json = json.dumps(container_dict, indent=2)
        return container_json