__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao
from pkg.infrastructure.common.shell.SimpleCmdExecutor import SimpleCmdExecutor
class replicationService(object):
    def __init__(self):
        pass

    def createPod(self,replicationConfigFile):
        cmd = KubernetesCommandDao.getCreateCommand(replicationConfigFile)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def deletePod(self, replicationname):
        cmd = KubernetesCommandDao.getDeleteCommand("replication", replicationname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryPod(self,replicationname):
        cmd = KubernetesCommandDao.getQueryCommand("replication", replicationname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult