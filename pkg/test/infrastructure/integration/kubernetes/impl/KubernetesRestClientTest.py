__author__ = 'zhangbohan'
import unittest
import json
from pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient import KubernetesWSClient
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod
from pkg.infrastructure.integration.kubernetes.model.service.Service import Service
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController


class kubernetesWSClientTest(unittest.TestCase):
    def setUp(self):
        self.KUBERNETES_ENDPOINT = "http://54.248.167.168:8080"
        self.kubernetesWSClient = KubernetesWSClient(self.KUBERNETES_ENDPOINT, namespace="default")
        #pod = Pod(id="c26b6f55-adec-11e4-8d9a-22000aba1b4e", apiVersion="v1beta1", desiredState={}, labels={}, namespace="default")
        pass

    def tearDown(self):
        pass


    def testQuerryPod(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : queryPod
                 description: test to get pod
              """

        queryId = "mysql-test"
        result = self.kubernetesWSClient.queryPod(queryId)
        print("status :", result[0])
        print("result :", result[1])
        print(type(result))
        resultDict = json.loads(result[1])
        expect = "mysql-test"

        assert expect == resultDict['id']

        print "test pass!"

    def testQuerryService(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : querryService
                 description: test to get service
              """
        #service = Service(id="mysqlservice", apiVersion="v1beta1", selector={}, protocol="tcp", containerPort=80, port=80, namespace="default")
        serviceId = "mysqlservice"
        result = self.kubernetesWSClient.queryService(serviceId)
        print("status :", result[0])
        print("result :", result[1])

        expect = "mysqlservice"
        resultDict = json.loads(result[1])
        assert expect == resultDict['id']

        print "test pass!"

    def testQueryReplicationController(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : getPodApi
              """
        replicationControllerId = "wordpressController"
        result = self.kubernetesWSClient.queryReplicationController(replicationControllerId)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        resultDict = json.loads(result[1])

        assert expect == resultDict['id']

        print "test pass!"

    def testCreatePod(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : createPod
              """
        #id can't contain up-case ca
        podJson = """
            {
              "id": "kubernetes-client-test-createpod",
              "kind": "Pod",
              "apiVersion": "v1beta2",
              "desiredState": {
                "manifest": {
                  "version": "v1beta2",
                  "id": "mysql-test",
                  "containers": [{
                    "name": "kubernetes-client-test-createpod",
                    "image": "zbhlove100/mysql5.6",
                    "ports": [{
                      "containerPort": 3306
                    }],
                "env":[{
                "name":"MYSQL_ROOT_PASSWORD",
                "value":"cloudpi"
                }]
                  }]
                }
              },
              "labels": {
                "name": "kuberneteswsclient-testcreatepod"
              }
            }
        """
        podModel = Pod.fromJSON(podJson)
        result = self.kubernetesWSClient.createPod(podModel)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        #resultDict = json.loads(result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testCreateService(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : createService
              """
        #id can't contain up-case ca
        #guestbook1-user-service
        kubernetesWSClient1 = KubernetesWSClient(self.KUBERNETES_ENDPOINT)
        serviceJson = """
            {
              "id": "guest-ook-user-ser-ice",
              "kind": "Service",
              "apiVersion": "v1beta2",
              "selector": {
                "name": "kuberneteswsclient-testcreatepod"
              },
              "protocol": "TCP",
              "containerPort": 3306,

              "port": 3306
            }
        """
        serviceModel = Service.fromJSON(serviceJson)
        result = kubernetesWSClient1.createService(serviceModel)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        #resultDict = json.loads(result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testDeletePod(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : deletePod
                 description: test to get replication controller
              """
        podId = "kuberneteswsclient-testcreatepod"
        result = self.kubernetesWSClient.deletePod(podId)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        resultDict = json.loads(result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testDeletePod(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : deleteService
              """
        serviceId = "guest-ook-user-ser-ice"
        result = self.kubernetesWSClient.deleteService(serviceId)
        print("status :", result[0])
        print("result :", result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testCreateReplicationController(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : create
              """
        #id can't contain up-case ca
        #guestbook1-user-service
        kubernetesWSClient1 = KubernetesWSClient(self.KUBERNETES_ENDPOINT)
        replicationControllerJson = """
            {
              "id": "testReplicationController",
              "kind": "ReplicationController",
              "apiVersion": "v1beta2",
              "desiredState": {
                "replicas": 1,
                "replicaSelector": {"name": "test-rc-server"},
                "podTemplate": {
                  "desiredState": {
                     "manifest": {
                       "version": "v1beta2",
                       "id": "wordpressController",
                       "containers": [{
                         "name": "slave",
                         "image": "zbhlove100/wordpress",
                         "cpu": 200,
                         "ports": [{"containerPort": 80}],
                          "command":["apache2-foreground","10.0.195.8:3306","cloudpi"]
                       }]
                     }
                   },
                   "labels": {
                     "name": "test-rc-server",
                     "uses": "mysql"
                   }
                  }
               },
              "labels": {"name": "test-rc-server"}
            }
        """
        replicationControllerModel = ReplicationController.fromJSON(replicationControllerJson)
        result = kubernetesWSClient1.createReplicationController(replicationControllerModel)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        #resultDict = json.loads(result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testUpdateReplicationController(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : updateReplicationController
              """
        #id can't contain up-case ca
        #guestbook1-user-service
        kubernetesWSClient1 = KubernetesWSClient(self.KUBERNETES_ENDPOINT)
        replicationControllerJson = """
            {
              "id": "testReplicationController",
              "kind": "ReplicationController",
              "apiVersion": "v1beta2",
              "resourceVersion": 1274,
              "desiredState": {
                "replicas": 0,
                "replicaSelector": {"name": "test-rc-server"},
                "podTemplate": {
                  "desiredState": {
                     "manifest": {
                       "version": "v1beta2",
                       "id": "wordpressController",
                       "containers": [{
                         "name": "slave",
                         "image": "zbhlove100/wordpress",
                         "cpu": 200,
                         "ports": [{"containerPort": 80}],
                          "command":["apache2-foreground","10.0.195.8:3306","cloudpi"]
                       }]
                     }
                   },
                   "labels": {
                     "name": "test-rc-server",
                     "uses": "mysql"
                   }
                  }
               },
              "labels": {"name": "test-rc-server"}
            }
        """
        replicationControllerModel = ReplicationController.fromJSON(replicationControllerJson)
        result = kubernetesWSClient1.updateReplicationController(replicationControllerModel)
        print("status :", result[0])
        print("result :", result[1])
        expect = "wordpressController"
        #resultDict = json.loads(result[1])

        #assert expect == resultDict['id']

        print "test pass!"

    def testDeleteReplicationController(self):
        print """Test class : pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient
                 function : deleteReplicationController
              """
        replicationControllerId = "testReplicationController"
        result = self.kubernetesWSClient.deleteReplicationController(replicationControllerId)
        print("status :", result[0])
        print("result :", result[1])

        #assert expect == resultDict['id']

        print "test pass!"
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()