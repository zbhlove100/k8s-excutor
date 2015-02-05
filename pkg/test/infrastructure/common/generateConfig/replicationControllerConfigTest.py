__author__ = 'zhangbohan'
import unittest

from pkg.domain.common.model.pod.Manifest import Manifest
from pkg.domain.common.model.pod.Containers import Containers
from pkg.domain.common.model.replicationController.ReplicationControllerState import ReplicationControllerState
from pkg.domain.common.model.replicationController.ReplicationController import ReplicationController
from pkg.domain.common.model.replicationController.PodTemplate import PodTemplate
from pkg.domain.common.model.pod.PodState import PodState
from pkg.domain.common.bl.impl.generateConfig import GenerateConfig
from pkg.infrastructure.common.file.FileUtil import FileUtil


class replicationControllerConfigTest(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass


    def testGenerateJsonFile(self):
        print ""
        containers  = Containers("111","zbhlove/mysql",["cmd","everything"], ports=["80"])
        manifest = Manifest("1.0", "xxxx", containers=[containers])
        podState = PodState(manifest)
        podTemplate = PodTemplate(podState, {"name":"podTemplate"})
        rcState = ReplicationControllerState(3, {"name":"wordpress-server"}, podTemplate)
        replicationController = ReplicationController("wordpress-controller", "replicationController","V2", {"name":"test-controller"},rcState)
        #result = pod.toDict()
        path = "/tmp/rctest.json"
        podconfig = GenerateConfig(replicationController,path)

        podconfig.generateJsonFile();
        result = FileUtil.readContent(path)
        print result



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
