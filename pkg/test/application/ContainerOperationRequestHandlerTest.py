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

    mysqlPodTaskRequest = """

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
    QUERY_MYSQL_POD_TASK = """
    {
             "modelType": "Pod",
                "action": "Query",
                "dataDict" : {
                      "id": "suit-test-createpod",
                      "kind": "Pod",
                      "apiVersion": "v1beta2"

                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }
    """
    CREATE_MYSQL_SERVICE_TASK = """
     {
             "modelType": "Service",
                "action": "Create",
                "dataDict" : {
                      "id": "suit-test-mysqlservice",
                      "kind": "Service",
                      "apiVersion": "v1beta2",
                      "selector": {
                        "name": "user1-farm1-role1-suit-test-createpod"
                      },
                      "protocol": "TCP",
                      "containerPort": 3306,
                      "publicIPs":["10.184.28.57"],
                      "port": 3306
                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }

    """
    CREATE_WORDPRESS_REPLICATION_CONTROLLER_TASK = """
     {
             "modelType": "ReplicationController",
                "action": "Create",
                "dataDict" : {
                      "id": "suit-test-wordpress-replication-controller",
                      "kind": "ReplicationController",
                      "apiVersion": "v1beta2",
                      "desiredState": {
                        "replicas": 1,
                        "replicaSelector": {"name": "suit-test-wordpress-replication-controller"},
                        "podTemplate": {
                          "desiredState": {
                             "manifest": {
                               "version": "v1beta2",
                               "id": "suit-test-wordpress-replication-controller",
                               "containers": [{
                                 "name": "slave",
                                 "image": "zbhlove100/wordpress",
                                 "cpu": 200,
                                 "ports": [{"containerPort": 80}],
                                  "command":["apache2-foreground","10.0.99.214:33727","cloudpi"]
                               }]
                             }
                           },
                           "labels": {
                             "name": "suit-test-wordpress-replication-controller",
                             "uses": "mysql"
                           }
                          }
                       },
                      "labels": {"name": "suit-test-wordpress-replication-controller"}
                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }

    """
    CREATE_WORDPRESS_SERVICE_TASK = """
     {
             "modelType": "Service",
                "action": "Create",
                "dataDict" : {
                      "id": "suit-test-wd-service",
                      "kind": "Service",
                      "apiVersion": "v1beta2",
                      "selector": {
                        "name": "suit-test-wordpress-replication-controller"
                      },
                      "protocol": "TCP",
                      "containerPort": 80,
                      "publicIPs":["10.186.27.208"],
                      "port": 8080
                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }

    """

    DELETE_WORDPRESS_SERVICE_TASK = """
    {
             "modelType": "Service",
                "action": "Delete",
                "dataDict" : {
                      "id": "suit-test-wd-service",
                      "kind": "Service",
                      "apiVersion": "v1beta2"

                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }
    """

    DELETE_MYSQL_SERVICE_TASK = """
    {
             "modelType": "Service",
                "action": "Delete",
                "dataDict" : {
                      "id": "suit-test-mysqlservice",
                      "kind": "Service",
                      "apiVersion": "v1beta2"

                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }
    """

    DELETE_MYSQL_POD_TASK = """
    {
             "modelType": "Pod",
                "action": "Delete",
                "dataDict" : {
                      "id": "suit-test-createpod",
                      "kind": "Pod",
                      "apiVersion": "v1beta2"

                    },
                "userId" : "user1",
                "farmName" : "farm1",
                "roleName" : "role1",
                "targetEndpoint" : "http://54.248.167.168:8080"
         }
    """
    def testDeploySuit(self):
        print """Test class : ContainerOperationRequestHandler
                 function : handle
              """



        corh = ContainerOperationRequestHandler()
        corh.handle(self.QUERY_MYSQL_POD_TASK)

        print "test pass!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()