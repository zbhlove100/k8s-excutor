__author__ = 'zhangbohan'
import unittest,json
from pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationController import ReplicationController


class ReplicationControllerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testFromJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationControllerState
            test function : fromJSON
        """
        replicationControllerJson = """
            {
              "id": "wordpressController",
              "kind": "ReplicationController",
              "apiVersion": "v1beta2",
              "desiredState": {
                "replicas": 5,
                "replicaSelector": {"name": "wordpress-server"},
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
                     "name": "wordpress-server",
                     "uses": "mysql"
                   }
                  }
               },
              "labels": {"name": "wordpress-server"}
            }
        """
        replicationController = ReplicationController.fromJSON(replicationControllerJson)

        print("reuslt :%s" % replicationController.toJSON())
        print("--------------------------------")
        exceptResult = {"name": "wordpress-server"}
        result = replicationController.getLabels()
        assert result == exceptResult
        print("test pass!")

    def testToJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.replicationController.ReplicationControllerState
            test function : toJSON
        """
        replicationControllerJson = """
            {
              "id": "wordpressController",
              "kind": "ReplicationController",
              "apiVersion": "v1beta2",
              "desiredState": {
                "replicas": 5,
                "replicaSelector": {"name": "wordpress-server"},
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
                     "name": "wordpress-server",
                     "uses": "mysql"
                   }
                  }
               },
              "labels": {"name": "wordpress-server"}
            }
        """
        replicationController = ReplicationController.fromJSON(replicationControllerJson)
        result = replicationController.toJSON()
        print("reuslt :%s" % result)
        print("--------------------------------")

        assert result !=None
        print("test pass!")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
