__author__ = 'zhangbohan'

import random
import os
from pkg.infrastructure.common.file.FileUtil import FileUtil

class PortNamespace(object):
    def __init__(self, namespaceDao):
        self.namespcaeDao = namespaceDao
        pass

    def getRadomPort(self):
        result = random.randrange(80, 65535)
        return result

    def getUnusedPort(self, hostip):
        result = ""
        portsArray = self.namespaceDao.getAllocatedPorts(hostip)

        used = True

        while used:
            port = random.randrange(80, 65535)
            if port not in portsArray:
                used = False
                self.namespaceDao.setAllocatePort(hostip, port)
                result = port

        return result