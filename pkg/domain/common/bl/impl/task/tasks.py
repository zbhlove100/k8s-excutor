from __future__ import absolute_import
import json
from pkg.domain.common.bl.impl.task.celery import app
from pkg.application.ContainerOperationRequestHandler import ContainerOperationRequestHandler
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod
from celery import chain

@app.task(bind=True, serializer='json', name="create-pod", igroneresult=True)
def createPod(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))
    print "-------------"+result
    if result == "success":
        result = taskobj
    return result




@app.task(bind=True, serializer='json', name="delete-pod")
def deletePod(self):

    print "hello"

@app.task(bind=True, serializer='json', name="query-pod")
def queryPod(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))

    return result

@app.task(bind=True, serializer='json', name="create-service", igroneresult=True)
def createService(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))

    return result




@app.task(bind=True, serializer='json', name="delete-service")
def deleteService(self):

    print "hello"

@app.task(bind=True, serializer='json', name="query-service")
def queryService(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))

    return result
@app.task(bind=True, serializer='json', name="create-replicationController", igroneresult=True)
def createReplicationController(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))

    return result




@app.task(bind=True, serializer='json', name="delete-replicationController")
def deleteReplicationController(self):

    print "hello"

@app.task(bind=True, serializer='json', name="query-replicationController")
def queryReplicationController(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    result = corh.handle(json.dumps(taskobj))

    return result

@app.task(bind=True, serializer='json', name="check-pod")
def checkPod(self, taskobj):
    result = ""
    corh = ContainerOperationRequestHandler()
    taskobj["action"] = "Query"
    podstat = ""
    while podstat != "Running":
        createPodresult = corh.handle(json.dumps(taskobj))
        pod = Pod.fromJSON(createPodresult)
        podCurrentstate = pod.getCurrentState()
        podstat = podCurrentstate.getStatus()
        print podstat
    return podstat

@app.task(bind=True, serializer='json', name="wordpress-task")
def wordpresstask(self,taskobj):
    podtaskData = taskobj['pod']
    #servicetaskData = taskobj['service']
    #rctaskData = taskobj['replicationController']

    createPodtask = createPod.s(podtaskData)
    createPodresult = chain(createPod.s(podtaskData), checkPod.s())()



    # replicationControllertask = createReplicationController.s(rctaskData)
    # replicationControllertask.delay()
    # rcresult = replicationControllertask.get()
    #return sum(numbers)
