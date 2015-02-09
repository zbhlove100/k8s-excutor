__author__ = 'zhangbohan'
from pkg.infrastructure.integration.kubernetes.IKubernetesClient import IKubernetesClient
from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao
from pkg.infrastructure.common.generateConfig.GenerateConfig import GenerateConfig
from pkg.infrastructure.common.shell.SimpleCmdExecutor import SimpleCmdExecutor

class KubeletCliClient(IKubernetesClient):
    KUBERNETES_CREATE_COMMAND = "kubectl create -f %s"
    KUBERNETES_GET_POD_COMMAND = "kubectl get pod"
    KUBERNETES_GET_SERVICE_COMMAND = "kubectl get service"
    KUBERNETES_GET_REPLICATION_COMMAND = "kubectl get replicationcontroller"
    KUBERNETES_DELETE_POD_COMMAND = "kubectl delete pod %s"
    KUBERNETES_DELETE_SERVICE_COMMAND = "kubectl delete service %s"
    KUBERNETES_DELETE_REPLICATION_COMMAND = "kubectl delete replicationcontroller %s"
    KUBERNETES_QUERY_POD_STATUS_COMMAND = "kubectl get pod -l %s |awk '{print $5}'"
    def __init__(self):

        pass
    def createPod(self,podModel):
        return

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

    def createService(self,serviceModel):
        return

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

    def createReplicationController(self,replicationControllerModel):
        return

    def deleteReplicationController(self, replicationControllerModel):
        replicationControllerModelId = replicationControllerModel.getId()
        cmd = self.KCommandDao.getDeleteCommand("replication", replicationControllerModelId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult

    def queryReplication(self,replicationControllerModel):
        replicationControllerModelId = replicationControllerModel.getId()
        cmd = self.KCommandDao.getQueryCommand("replication", replicationControllerModelId)
        outputresult = SimpleCmdExecutor.executeCmd(cmd)
        return outputresult