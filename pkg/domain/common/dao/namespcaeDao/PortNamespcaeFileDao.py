__author__ = 'zhangbohan'
import os,random
from pkg.infrastructure.common.file.FileUtil import FileUtil

class PortNamespcaeFileDao(object):


    def __init__(self):
        self.PUBLIC_IP_PORT_FILE = "/tmp/k8sFiles/publicIpPortForK8s"
        pass

    def getAllocatedPorts(self,ip):
        result = []
        if os.path.exists(self.PUBLIC_IP_PORT_FILE):
            ipAndPortContents = FileUtil.readContent(self.PUBLIC_IP_PORT_FILE)
            portsArray = []
            for item in ipAndPortContents.splitlines():
                    iap = item.split(":")
                    portsArray.append(iap[1])
            result = portsArray
        return result

    def setAllocatePort(self, ip, port):
        iap = "%s:%s \n" % (ip, port)
        if os.path.exists(self.PUBLIC_IP_PORT_FILE):
            FileUtil.writeContent(self.PUBLIC_IP_PORT_FILE, iap)

        else:
            dir_path = os.path.dirname(self.PUBLIC_IP_PORT_FILE)
            os.system("mkdir -p %s" % dir_path)
            FileUtil.writeContent(self.PUBLIC_IP_PORT_FILE, iap)

        pass