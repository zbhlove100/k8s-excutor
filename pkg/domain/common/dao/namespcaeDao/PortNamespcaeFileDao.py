__author__ = 'zhangbohan'
import os,random
from pkg.infrastructure.common.file.FileUtil import FileUtil

class PortNamespcaeFileDao(object):


    def __init__(self):
        self.portNamespcaeFile = "/tmp/k8sFiles/publicIpPortForK8s"
        pass

    def setPortNamespcaeFile(self,portNamespcaeFile):
        self.portNamespcaeFile = portNamespcaeFile

    def getAllocatedPorts(self,ip):
        result = []
        if os.path.exists(self.portNamespcaeFile):
            ipAndPortContents = FileUtil.readContent(self.portNamespcaeFile)
            portsArray = []
            for item in ipAndPortContents.splitlines():
                    iap = item.split(":")
                    portsArray.append(iap[1])
            result = portsArray
        return result

    def setAllocatePort(self, ip, port):
        iap = "%s:%s \n" % (ip, port)
        if os.path.exists(self.portNamespcaeFile):
            FileUtil.writeContent(self.portNamespcaeFile, iap)

        else:
            dir_path = os.path.dirname(self.portNamespcaeFile)
            os.system("mkdir -p %s" % dir_path)
            FileUtil.appendContent(self.portNamespcaeFile, iap)
        pass