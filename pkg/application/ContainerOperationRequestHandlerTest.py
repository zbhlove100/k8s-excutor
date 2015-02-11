__author__ = 'zhangbohan'
import unittest
import json
from pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient import KubernetesWSClient
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod
from pkg.infrastructure.integration.kubernetes.model.service.Service import Service
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController
from pkg.application.ContainerOperationRequestHandler import ContainerOperationRequestHandler

class ContainerOperationRequestHandlerTest(unittest.TestCase):
    def setUp(self):
        self.KUBERNETES_ENDPOINT = "http://54.248.167.168:8080"
        self.kubernetesWSClient = KubernetesWSClient(self.KUBERNETES_ENDPOINT, namespace="default")
        #pod = Pod(id="c26b6f55-adec-11e4-8d9a-22000aba1b4e", apiVersion="v1beta1", desiredState={}, labels={}, namespace="default")
        pass

    def tearDown(self):
        pass


    def testDeploySuit(self):
        print """Test class : ContainerOperationRequestHandler
                 function : handle
              """

        podTaskRequest = """

            {
             "modelType": "Pod",
                "action": "Create",
                "dataDict" : {
                      "id": "suit-test-createpod",
                      "kind": "Pod",
                      "apiVersion": "v1beta2",
                      "desiredState": {
                        "manifest": {
                          "version": "v1beta2",
                          "id": "mysql-test",
                          "containers": [{
                            "name": "suit-test-createpod",
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
                        "name": "suit-test-createpod"
                      }
                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }

        """

        corh = ContainerOperationRequestHandler()
        corh.handle(podTaskRequest)

        print "test pass!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()