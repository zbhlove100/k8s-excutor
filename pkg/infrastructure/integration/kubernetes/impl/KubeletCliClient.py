__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao
from pkg.infrastructure.common.generateConfig.GenerateConfig import GenerateConfig
from pkg.infrastructure.common.shell.SimpleCmdExecutor import SimpleCmdExecutor

class KubeletCliClient(IKubernetesClient):
    def __init__(self,KComandDao):
        self.KCommandDao = KComandDao
        pass
    def createResource(self, objModel):
        generator = GenerateConfig(objModel, self.configDao)
        podConfigFile = generator.generateJson()
        cmd = self.KCommandDao.getCreateCommand(podConfigFile)
        self.operationResponse = SimpleCmdExecutor.executeCmd(cmd)
        return self.operationResponse

    def deleteResource(self, objModel):
        kind = objModel.kind
        result = ""
        if "pod" == kind:
            result = self.deletePod(objModel)
        elif "service" == kind:
            result = self.deleteService(objModel)
        elif "replication" == kind:
            result = self.deleteReplication(objModel)

        return result

    def querryResource(self, objModel):
        kind = objModel.kind
        result = ""
        if "pod" == kind:
            result = self.queryPodStatus(objModel)
        elif "service" == kind:
            result = self.queryService(objModel)
        elif "replication" == kind:
            result = self.queryReplication(objModel)

        return result

    def deletePod(self, podModel):
        podId = podModel.getId()
        cmd = self.KCommandDao.getDeleteCommand("pod",podId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryPod(self,podModel):
        podId = podModel.getId()
        cmd = self.KCommandDao.getQueryCommand("pod",podId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryPodStatus(self,podModel):
        podId = podModel.getId()
        cmd = "%s|awk '{print $5}'" % self.KCommandDao.getQueryCommand("pod",podId)

        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        resultArray = outputresult.splitlines()
        result = {"name":podId,"status":"Error"}
        if resultArray[1]:
            result.status = resultArray[1]
        return result

    def deleteService(self, serviceModel):
        serviceId = serviceModel.getId()
        cmd = self.KCommandDao.getDeleteCommand("service",serviceId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryService(self,serviceModel):
        serviceId = serviceModel.getId()
        cmd = self.KCommandDao.getQueryCommand("service",serviceId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def deleteReplication(self, replicationControllerModel):
        replicationControllerModelId = replicationControllerModel.getId()
        cmd = self.KCommandDao.getDeleteCommand("replication", replicationControllerModelId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryReplication(self,replicationControllerModel):
        replicationControllerModelId = replicationControllerModel.getId()
        cmd = self.KCommandDao.getQueryCommand("replication", replicationControllerModelId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult