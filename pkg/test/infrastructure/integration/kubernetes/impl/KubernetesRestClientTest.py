__author__ = 'zhangbohan'
import unittest
import json
from pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient import KubernetesWSClient
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
        print """Test class : kubernetesWSClient
                 function : queryPod
                 description: test to get pod
              """

        queryId = "c26b6f55-adec-11e4-8d9a-22000aba1b4e"
        result = self.kubernetesWSClient.queryPod(queryId)
        print("status :", result[0])
        print("result :", result[1])
        print(type(result))
        expect = "c26b6f55-adec-11e4-8d9a-22000aba1b4e"

        #assert expect == resultPod['id']

        print "test pass!"

    def testQuerryService(self):
        print """Test class : kubernetesWSClient
                 function : querryService
                 description: test to get service
              """
        #service = Service(id="mysqlservice", apiVersion="v1beta1", selector={}, protocol="tcp", containerPort=80, port=80, namespace="default")
        serviceId = "mysqlservice"
        result = self.kubernetesWSClient.queryResource(serviceId)
        print("result :", result)
        resultService = json.loads(result)

        expect = "mysqlservice"

        assert expect == resultService['id']

        print "test pass!"

    def testQuerryResourceRc(self):
        print """Test class : kubernetesWSClient
                 function : getPodApi
                 description: test to get replication controller
              """
        rc = ReplicationController(id="wordpressController",apiVersion="",labels={},desiredState={},namespace="default")
        result = self.kubernetesWSClient.queryResource(rc)
        print("result :", result)
        resultRc = json.loads(result)
        expect = "wordpressController"

        assert expect == resultRc['id']

        print "test pass!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()