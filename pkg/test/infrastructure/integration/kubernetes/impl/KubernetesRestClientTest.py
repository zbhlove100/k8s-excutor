__author__ = 'zhangbohan'
import unittest,json
from pkg.infrastructure.integration.kubernetes.dao.KubernetesRestDao import KubernetesRestDao
from pkg.infrastructure.integration.kubernetes.impl.KubernetesRestClient import KubernetesRestClient
from pkg.domain.common.model.pod.Pod import Pod
from pkg.domain.common.model.service.Service import Service
from pkg.domain.common.model.replicationController.ReplicationController import ReplicationController


class KubernetesRestClientTest(unittest.TestCase):
    def setUp(self):
        kubernetesRestDao = KubernetesRestDao()
        self.kubernetesRestClient = KubernetesRestClient(kubernetesRestDao)
        self.kubernetesRestClient.setKubernetesRestDao(kubernetesRestDao)
        pass

    def tearDown(self):
        pass


    def testQuerryResourcePod(self):
        print """Test class : KubernetesRestClient
                 function : getPodApi
                 description: test to get pod
              """
        pod = Pod(id="c26b6f55-adec-11e4-8d9a-22000aba1b4e", apiVersion="v1beta1", desiredState={}, labels={}, namespace="default")
        result = self.kubernetesRestClient.queryResource(pod)
        print("result :", result)
        resultPod = json.loads(result)
        expect = "c26b6f55-adec-11e4-8d9a-22000aba1b4e"

        assert expect == resultPod['id']

        print "test pass!"

    def testQuerryResourceService(self):
        print """Test class : KubernetesRestClient
                 function : getPodApi
                 description: test to get service
              """
        service = Service(id="mysqlservice", apiVersion="v1beta1", selector={}, protocol="tcp", containerPort=80, port=80, namespace="default")
        result = self.kubernetesRestClient.queryResource(service)
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