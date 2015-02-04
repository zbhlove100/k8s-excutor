__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao
from pkg.infrastructure.common.shell.SimpleCmdExecutor import SimpleCmdExecutor

class KubeletCliClient(IKubernetesClient):
    def __init__(self):
        pass
    def createResource(self,filePath):
        cmd = KubernetesCommandDao.getCreateCommand(filePath)
        self.operationResponse = SimpleCmdExecutor.executeCmd(cmd)
        return self.operationResponse

    def deleteResource(self,paramMap):
        kind = paramMap.kind
        name = paramMap.name
        result = ""
        if "pod" == kind:
            result = self.deletePod(name)
        elif "service" == kind:
            result = self.deleteService(name)
        elif "replication" == kind:
            result = self.deleteReplication(name)

        return result

    def querryResource(self,paramMap):
        kind = paramMap.kind
        name = paramMap.name
        result = ""
        if "pod" == kind:
            result = self.queryPodStatus(name)
        elif "service" == kind:
            result = self.queryService(name)
        elif "replication" == kind:
            result = self.queryReplication(name)

        return result

    def deletePod(self, podname):
        cmd = KubernetesCommandDao.getDeleteCommand("pod",podname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryPod(self,podname):
        cmd = KubernetesCommandDao.getQueryCommand("pod",podname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult
    def queryPodStatus(self,podname):
        cmd = "%s|awk '{print $5}'" % KubernetesCommandDao.getQueryCommand("pod",podname)

        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        resultArray = outputresult.splitlines()
        result = {"name":podname,"status":"Error"}
        if resultArray[1]:
            result.status = resultArray[1]
        return result

    def deleteService(self, servicename):
        cmd = KubernetesCommandDao.getDeleteCommand("service",servicename)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryService(self,servicename):
        cmd = KubernetesCommandDao.getQueryCommand("service",servicename)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def deleteReplication(self, replicationname):
        cmd = KubernetesCommandDao.getDeleteCommand("replication", replicationname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryReplication(self,replicationname):
        cmd = KubernetesCommandDao.getQueryCommand("replication", replicationname)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult