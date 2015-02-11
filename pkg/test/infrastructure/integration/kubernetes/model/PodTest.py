__author__ = 'zhangbohan'
import unittest,json
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod


class PodTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testFromJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.pod.Pod
            test function : fromJSON
        """
        podJson = """
            {
              "typeMeta":{
                    "id": "kubernetes-client-test-createpod",
                    "kind": "Pod",
                    "apiVersion": "v1beta2"
              },
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
        pod = Pod.fromJSON(podJson)

        print("reuslt :%s" % pod.toJSON())
        print("--------------------------------")
        exceptResult = {
                "name": "kuberneteswsclient-testcreatepod"
              }
        result = pod.getLabels()
        assert result == exceptResult
        print("test pass!")

    def testToJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.pod.Pod
            test function : fromJSON
        """
        podJson = """
            {
              "typeMeta":{
                    "id": "mysql-test",
                    "kind": "Pod",
                    "apiVersion": "v1beta2"
              },
              "desiredState": {
                "manifest": {
                  "version": "v1beta2",
                  "id": "mysql-test",
                  "containers": [{
                    "name": "namespace-test",
                    "image": "zbhlove100/mysql5.6",
                    "ports": [{
                      "containerPort": 3306,
                      "hostPort": 3300
                    }],
                "env":[{
                "name":"MYSQL_ROOT_PASSWORD",
                "value":"cloudpi"
                }]
                  }]
                }
              },
              "labels": {
                "name": "testdatabase"
              }
            }
        """
        pod = Pod.fromJSON(podJson)
        result = pod.toJSON()
        print("reuslt :%s" % pod.toJSON())
        print("--------------------------------")


        assert result !=None
        print("test pass!")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()