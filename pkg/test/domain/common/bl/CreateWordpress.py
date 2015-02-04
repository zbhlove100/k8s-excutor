__author__ = 'zhangbohan'
from pkg.domain.common.model.pod.Manifest import Manifest
from pkg.domain.common.model.pod.Containers import Containers
from pkg.domain.common.model.replicationController.ReplicationControllerState import ReplicationControllerState
from pkg.domain.common.model.replicationController.ReplicationController import ReplicationController
from pkg.domain.common.model.replicationController.PodTemplate import PodTemplate
from pkg.domain.common.model.pod.PodState import PodState
from pkg.infrastructure.common.generateConfig import GenerateConfig
from pkg.domain.common.model.pod.Pod import Pod
from pkg.domain.common.model.service.Service import Service
from pkg.infrastructure.common.file.FileUtil import FileUtil
from pkg.infrastructure.common.namespace.Namespace import Namespace
class CreateWordpress(object):

    def __init__(self):
        pass
    def createWdpReplicationConfig(self):
        namespace = Namespace()
        uuid = namespace.getUuidName()
        uuidname = "%s-%s" % ("wordpressrc",uuid)
        containers = Containers(name=uuidname,image="zbhlove/wordpress",command=["apache2-foreground","10.0.195.8:3306","cloudpi"], ports=[{"containerPort": 80,}],cpu=200)
        manifest = Manifest(version="v1beta2", id=uuid, containers=[containers])
        podState = PodState(manifest)
        podTemplate = PodTemplate(podState, labels={"name": uuidname,"uses": "mysql"})
        rcState = ReplicationControllerState(3, {"name":"wordpress-server"}, podTemplate)
        replicationController = ReplicationController("wordpress-controller", "ReplicationController","v1beta2", {"name":uuidname},rcState)
        #result = replicationController.toDict()
        #print(result)
        path = "/tmp/%s.json" % uuidname
        podconfig = GenerateConfig(replicationController,path)
        podconfig.generateJsonFile();
        return path, uuidname
    def createMysqlPodConfig(self):
        namespace = Namespace()
        uuid = namespace.getUuidName()
        uuidname = "%s-%s" % ("mysqlpod",uuid)
        containers  = Containers(name=uuidname,image="zbhlove100/mysql5.6", ports=[{"containerPort": 3306,}],env=[{"name":"MYSQL_ROOT_PASSWORD","value":"cloudpi"}])
        manifest = Manifest(version="v1beta2", id=uuid, containers=[containers])
        podState = PodState(manifest)
        pod = Pod(id=uuidname,apiVersion="v1beta2",desiredState=podState,labels={"name":uuidname})
        path = "/tmp/%s.json" % uuidname
        podconfig = GenerateConfig(pod,path)

        podconfig.generateJsonFile();
        return path,uuidname
    def createMysqlServiceConfig(self,selectLabel):
        namespace = Namespace()
        uuid = namespace.getUuidName()
        uuidname = "%s-%s" % ("mysqlservice",uuid)
        service = Service(id=uuidname,kind="service",apiVersion="v1beta2",selector={"name": selectLabel},protocol="TCP",containerPort=3306,port=3306)
        path = "/tmp/%s.json" % uuidname
        podconfig = GenerateConfig(service,path)

        podconfig.generateJsonFile();
        return path, uuidname
    def createWdpServiceConfig(self,selectLabel):
        namespace = Namespace()
        uuid = namespace.getUuidName()
        uuidname = "%s-%s" % ("wordpressservice",uuid)
        publicIp = "10.185.135.164"
        publicPort = namespace.getUnusedPort(publicIp)
        service = Service(id=uuidname,kind="service",apiVersion="v1beta2",selector={"name": selectLabel},protocol="TCP",containerPort=80,port=publicPort,publicIPs=[publicIp])
        path = "/tmp/%s.json" % uuidname
        podconfig = GenerateConfig(service,path)

        podconfig.generateJsonFile();
        return path, uuidname

    def createTasks(self):
        conponents = []
        namespace = Namespace()
        uuid = namespace.getUuidName()
        databaseFile = "%s-%s" % ("taskMessage",uuid)
        databaseFilePath = "/tmp/%s.json" % databaseFile
        FileUtil.writeContent(databaseFilePath,"databaseFile: \n")


        cwp = CreateWordpress()
        (filename,mysqlpodid) = cwp.createMysqlPodConfig()

        mysqlpod = {"file":filename,"id":mysqlpodid,"status":"Unknow"}
        conponents.append(mysqlpod)

        pass
    def waitAndExcute(self,state,databaseobj,nextOperation):
        if state == "begin":
            evel(nextOperation)()
        pass
cwp = CreateWordpress()
filename = cwp.createMysqlPodConfig()
print(filename)
print(FileUtil.readContent(filename))
