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
    def fromDict(containerDict):
        if containerDict.has_key("name") :
            name = containerDict["name"]
        else :
            name = None

        if containerDict.has_key("image") :
            image = containerDict["image"]
        else :
            image = None

        if containerDict.has_key("command") :
            command = containerDict["command"]
        else :
            command = None

        if containerDict.has_key("ports") :
            ports = containerDict["ports"]
        else :
            ports = None

        if containerDict.has_key("env") :
            env = containerDict["env"]
        else :
            env = None

        if containerDict.has_key("memory") :
            memory = containerDict["memory"]
        else :
            memory = None

        if containerDict.has_key("cpu") :
            cpu = containerDict["cpu"]
        else :
            cpu = None

        if containerDict.has_key("volumeMounts") :
            volumeMounts = containerDict["volumeMounts"]
        else :
            volumeMounts = None

        return Containers(name, image, command, ports, env, memory, cpu, volumeMounts)

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

    def setName(self,name):
        self.name = name

    def setImage(self,image):
        self.image = image

    def setCommand(self,command):
        self.command = command

    def setPorts(self,ports):
        self.ports = ports

    def setEnv(self,env):
        self.env = env

    def setMemory(self,memory):
        self.memory = memory

    def setCpu(self,cpu):
        self.cpu = cpu

    def setVolumeMounts(self,volumeMounts):
        self.volumeMounts = volumeMounts

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def getPorts(self):
        return self.ports

    def getCommand(self):
        return self.command

    def getEnv(self):
        return self.env

    def getMemory(self):
        return self.memory

    def getCpu(self):
        return self.cpu

    def getVolumeMounts(self):
        return self.volumeMounts