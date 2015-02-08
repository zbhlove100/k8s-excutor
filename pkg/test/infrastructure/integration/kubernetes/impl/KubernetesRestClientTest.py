__author__ = 'zhangbohan'
import unittest,json
from pkg.infrastructure.integration.kubernetes.dao.KubernetesRestDao import KubernetesRestDao
from pkg.infrastructure.integration.kubernetes.impl.KubernetesWSClient import KubernetesRestClient
from pkg.domain.common.model.pod.Pod import Pod
from pkg.domain.common.model.service.Service import Service
from pkg.domain.common.model.replicationController.ReplicationController import ReplicationController


class KubernetesRestClientTest(unittest.TestCase):
    def setUp(self):
        kubernetesRestDao = KubernetesRestDao()
        self.kubernetesRestClient = KubernetesRestClient(namespace="default")
        self.kubernetesRestClient.setKubernetesRestDao(kubernetesRestDao)
        #pod = Pod(id="c26b6f55-adec-11e4-8d9a-22000aba1b4e", apiVersion="v1beta1", desiredState={}, labels={}, namespace="default")
        pass

    def tearDown(self):
        pass


    def testQuerryPod(self):
        print """Test class : KubernetesRestClient
                 function : queryPod
                 description: test to get pod
              """

        queryId = "c26b6f55-adec-11e4-8d9a-22000aba1b4e"
        result = self.kubernetesRestClient.queryPod(queryId)
        print("status :", result[0])
        print("result :", result[1])
        print(type(result))
        expect = "c26b6f55-adec-11e4-8d9a-22000aba1b4e"

        #assert expect == resultPod['id']

        print "test pass!"

    def testQuerryService(self):
        print """Test class : KubernetesRestClient
                 function : querryService
                 description: test to get service
              """
        #service = Service(id="mysqlservice", apiVersion="v1beta1", selector={}, protocol="tcp", containerPort=80, port=80, namespace="default")
        serviceId = "mysqlservice"
        result = self.kubernetesRestClient.queryResource(serviceId)
        print("result :", result)
        resultService = json.loads(result)

        expect = "mysqlservice"

        assert expect == resultService['id']

        print "test pass!"

    def testQuerryResourceRc(self):
        print """Test class : KubernetesRestClient
                 function : getPodApi
                 description: test to get replication controller
              """
        rc = ReplicationController(id="wordpressController",apiVersion="",labels={},desiredState={},namespace="default")
        result = self.kubernetesRestClient.queryResource(rc)
        print("result :", result)
        resultRc = json.loads(result)
        expect = "wordpressController"

        assert expect == resultRc['id']

        print "test pass!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()