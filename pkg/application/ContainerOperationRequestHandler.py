__author__ = 'zhangbohan'
import json

from pkg.infrastructure.integration.kubernetes.model.service.Service import Service
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import \
    ReplicationController
from pkg.domain.common.bl.impl.namespace.UserNamespace import UserNamespace
from pkg.domain.common.bl.impl.namespace.PortNamespace import PortNamespace
from pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient import KubernetesWSClient
from pkg.domain.common.model.ContainerOperationRequest import ContainerOperationRequest
from pkg.domain.common.dao.namespcaeDao.PortNamespcaeFileDao import PortNamespcaeFileDao


class ContainerOperationRequestHandler(object):
    def __init__(self):
        pass

    def handle(self, jsonContainerOperationRequest):
        result = ""
        containerOperationRequest = ContainerOperationRequest.fromJSON(jsonContainerOperationRequest)

        requestModel = self.parseModel(containerOperationRequest)

        uNamespace = UserNamespace()
        modelWithNsAndLabels = uNamespace.setModelLabelsAndNamespace(containerOperationRequest.getUserId()
                                                                     , containerOperationRequest.getFarmName()
                                                                     , containerOperationRequest.getRoleName()
                                                                     , requestModel)

        #modelWithNsAndLabelsAndId = uNamespace.setModelId(modelWithNsAndLabels)
        self.exucteAction(containerOperationRequest, modelWithNsAndLabels)

        pass

    def parseModel(self, containerOperationRequest):
        requestModel = None
        type = containerOperationRequest.getModelType()

        dataDict = containerOperationRequest.getDataDict()
        if type == "Pod":
            requestModel = Pod.fromDict(dataDict)
        elif type == "Service":
            requestModel = Service.fromDict(dataDict)
        elif type == "ReplicationController":
            requestModel = ReplicationController.fromDict(dataDict)
        return requestModel

    def setServiceIpPort(self, model):
        portDap = PortNamespcaeFileDao()
        portNamespace = PortNamespace(portDap)
        modelWithPort = portNamespace.setServicePublicIpPort(model)
        return modelWithPort

    def createInstance(self, class_name, *args, **kwargs):
        (module_name, class_name) = class_name.rsplit(".", 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        object = class_meta(*args, **kwargs)
        return object

    def exucteAction(self, containerOperationRequest, model):
        kind = containerOperationRequest.getModelType()
        namespace = model.getNamespace()
        targetEndpoint = containerOperationRequest.getTargetEndpoint()

        kubernetesWSClient = KubernetesWSClient(targetEndpoint, namespace)

        actionMappingDict = {
            "PodCreate": {"className": "pkg.domain.common.bl.impl.manage.PodManage.PodManage",
                          "methodName": "createPod"},
            "PodDelete": {"className": "pkg.domain.common.bl.impl.manage.PodManage.PodManage",
                          "methodName": "deletePod"},
            "PodQuery": {"className": "pkg.domain.common.bl.impl.manage.PodManage.PodManage", "methodName": "queryPod"},
            "ServiceCreate": {"className": "pkg.domain.common.bl.impl.manage.ServiceManage.ServiceManage",
                              "methodName": "createService"},
            "ServiceDelete": {"className": "pkg.domain.common.bl.impl.manage.ServiceManage.ServiceManage",
                              "methodName": "createService"},
            "ServiceQuery": {"className": "pkg.domain.common.bl.impl.manage.ServiceManage.ServiceManage",
                             "methodName": "createService"},
            "ReplicationControllerCreate": {
                "className": "pkg.domain.common.bl.impl.manage.ReplicationControllerManage.ReplicationControllerManage"
                , "methodName": "createReplicationController"},
            "ReplicationControllerDelete": {
                "className": "pkg.domain.common.bl.impl.manage.ReplicationControllerManage.ReplicationControllerManage",
                "methodName": "createReplicationController"},
            "ReplicationControllerQuery": {
                "className": "pkg.domain.common.bl.impl.manage.ReplicationControllerManage.ReplicationControllerManage",
                "methodName": "createReplicationController"}
        }
        actionKey = kind + containerOperationRequest.getAction()
        excutorDict = actionMappingDict[actionKey]
        excutorInstance = self.createInstance(excutorDict["className"], kubernetesWSClient)
        excutor = getattr(excutorInstance, excutorDict["methodName"])

        excutor(model)




