__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao
from pkg.infrastructure.common.shell.SimpleCmdExecutor import SimpleCmdExecutor
class serviceService(object):
    def __init__(self):
        pass

    def createService(self,serviceConfigFile):
        cmd = KubernetesCommandDao.getCreateCommand(serviceConfigFile)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def deleteService(self, servicename):
        cmd = KubernetesCommandDao.getDeleteCommand("service",servicename)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryService(self,servicename):
        cmd = KubernetesCommandDao.getQueryCommand("service",servicename)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult