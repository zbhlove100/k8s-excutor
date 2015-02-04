__author__ = 'zhangbohan'
import unittest

from pkg.infrastructure.integration.kubernetes.dao import KubernetesCommandDao


class TestKubeDao(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testGetCreateCommand(self):
        print ""
        filePath = "/tmp/pod.json"
        cmd = KubernetesCommandDao.getCreateCommand(filePath)
        print cmd

    def testGetDeleteCommand(self):
        print ""
        kind = "pod"
        name = "pod12345"
        cmd = KubernetesCommandDao.getDeleteCommand(kind, name)
        print cmd
        print ""
        kind = "service"
        name = "service12345"
        cmd = KubernetesCommandDao.getDeleteCommand(kind, name)
        print cmd
        print ""
        kind = "replication"
        name = "replication12345"
        cmd = KubernetesCommandDao.getDeleteCommand(kind, name)
        print cmd

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
