__author__ = 'zhangbohan'
import unittest,json

from pkg.domain.common.model.pod.Pod import Pod
from pkg.domain.common.model.pod.Manifest import Manifest
from pkg.domain.common.model.pod.Containers import Containers
from pkg.domain.common.model.pod.PodState import PodState
from pkg.infrastructure.common.generateConfig.GenerateConfig import GenerateConfig
from pkg.infrastructure.common.file.FileUtil import FileUtil
from pkg.domain.common.dao.JsonFileDao import JsonFileDao

class GenerateJsonTest(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass


    def testGenerateJson(self):
        print "Test class : gnerateConfig ,function : generateJson"
        containers  = Containers("111","zbhlove/mysql",["cmd","everything"], ports=["80"])
        manifest = Manifest("1.0", "xxxx", containers=[containers])
        podState = PodState(manifest,host="111")
        pod = Pod(id="testpod",apiVersion="x1",desiredState=podState,labels=["test","nonono"],namespace="testspace")
        #result = pod.toDict()
        testFilePath = "/tmp/"

        pnfDao = JsonFileDao()
        pnfDao.setFilePathDir(testFilePath)


        podconfig = GenerateConfig(pod, pnfDao)

        resultFile = podconfig.generateJson()

        result = FileUtil.readContent(resultFile)
        print result

        poddict = json.loads(result)

        assert pod.getId() == poddict["id"]
        print "test pass"



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
