__author__ = 'zhangbohan'
import unittest
from pkg.infrastructure.integration.kubernetes.dao.KubernetesRestDao import KubernetesRestDao


class KubernetesRestDaoTest(unittest.TestCase):
    def setUp(self):
        self.kubernetesPodAPIWithNamespcae = "/api/v1beta1/ns/%s/pods"
        self.kubernetesServiceAPIWithNamespcae = "/api/v1beta1/ns/%s/pods"
        self.kubernetesReplicationControllerAPIWithNamespcae = "/api/v1beta1/ns/%s/replicationControllers"
        self.kubernetesEndpoint = "http://54.248.167.168:8080"
        pass

    def tearDown(self):
        pass


    def testGetPodApi(self):
        print "Test class : KubernetesRestDao ,function : getPodApi"
        kubernetesDao = KubernetesRestDao()
        testNamespace = "test"
        expect = self.kubernetesPodAPIWithNamespcae % testNamespace
        result = kubernetesDao.getPodApiWithNamespcae(testNamespace)
        print("result :", result)
        assert expect == result
        print "test pass!"

    def testGetServiceApi(self):
        print "Test class : KubernetesRestDao ,function : getServiceApi"
        kubernetesDao = KubernetesRestDao()
        testNamespace = "test"
        expect = self.kubernetesServiceAPIWithNamespcae % testNamespace
        result = kubernetesDao.getServiceApiWithNamespcae(testNamespace)
        print("result :", result)
        assert expect == result
        print "test pass!"

    def testGetReplicationControllerApi(self):
        print "Test class : KubernetesRestDao ,function : getReplicationControllerApi"

        kubernetesDao = KubernetesRestDao()
        testNamespace = "test"
        expect = self.kubernetesReplicationControllerAPIWithNamespcae % testNamespace
        result = kubernetesDao.getReplicationControllerApiWithNamespcae(testNamespace)
        print("result :", result)
        assert expect == result
        print "test pass!"

    def testGetKubernetesEndpoint(self):
        print "Test class : KubernetesRestDao ,function : getKubernetesEndpoint"

        kubernetesDao = KubernetesRestDao()
        testNamespace = "test"
        expect = self.kubernetesEndpoint
        result = kubernetesDao.getKubernetesEndpoint()
        print("result :", result)
        assert expect == result
        print "test pass!"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()