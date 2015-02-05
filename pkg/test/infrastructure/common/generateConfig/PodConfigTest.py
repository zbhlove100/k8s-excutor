__author__ = 'zhangbohan'
import unittest

from pkg.domain.common.model.pod.Pod import Pod
from pkg.domain.common.model.pod.Manifest import Manifest
from pkg.domain.common.model.pod.Containers import Containers
from pkg.domain.common.model.pod.PodState import PodState
from pkg.domain.common.bl.impl.generateConfig import GenerateConfig
from pkg.infrastructure.common.file.FileUtil import FileUtil


class PodConfigTest(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass


    def testGenerateJsonFile(self):
        print ""
        containers  = Containers("111","zbhlove/mysql",["cmd","everything"], ports=["80"])
        manifest = Manifest("1.0", "xxxx", containers=[containers])
        podState = PodState(manifest,host="111")
        pod = Pod(id="testpod",apiVersion="x1",desiredState=podState,labels=["test","nonono"])
        #result = pod.toDict()
        path = "/tmp/podtest.json"
        podconfig = GenerateConfig(pod,path)

        podconfig.generateJsonFile();
        result = FileUtil.readContent(path)
        print result



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
