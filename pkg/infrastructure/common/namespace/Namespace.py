__author__ = 'zhangbohan'
import uuid
import random
import os
from pkg.infrastructure.common.file.FileUtil import FileUtil
class Namespace(object):
    PUBLIC_IP_PORT_FILE = "/tmp/k8sFiles/publicIpPortForK8s"
    def __init__(self):
        pass
    def getUuidName(self):
        result = uuid.uuid4()
        return str(result)

    def getRadomPort(self):
        result = random.randrange(80,65535)
        return result

    def getUnusedPort(self, hostip):
        result = ""
        if os.path.exists(Namespace.PUBLIC_IP_PORT_FILE):
            ipAndPortContents = FileUtil.readContent(Namespace.PUBLIC_IP_PORT_FILE)
            iapArray = []
            for item in ipAndPortContents.splitlines():
                    iap = item.split(":")
                    iapArray.append((iap[0],iap[1]))
            used = True

            while (used):
                port = random.randrange(80,65535)
                iapTouple = (hostip,port)
                if iapTouple not  in iapArray:
                    used = False
                    newIap = "%s:%s \n" % (hostip,port)
                    FileUtil.appendContent(Namespace.PUBLIC_IP_PORT_FILE,newIap)
                    result = port

        else:
            dir_path = os.path.dirname(Namespace.PUBLIC_IP_PORT_FILE)
            os.system("mkdir -p %s" % dir_path)
            port = random.randrange(80,65535)
            iap = "%s:%s \n" % (hostip,port)
            FileUtil.writeContent(Namespace.PUBLIC_IP_PORT_FILE,iap)
            result = port
        return port


