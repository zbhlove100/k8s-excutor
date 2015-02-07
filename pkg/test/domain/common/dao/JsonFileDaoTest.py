__author__ = 'zhangbohan'
import unittest

from pkg.domain.common.dao.JsonFileDao import JsonFileDao
from pkg.infrastructure.common.file.FileUtil import FileUtil
import json
import uuid

class PortNamespaceFileDaoTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testSetObj(self):
        print "Test class : PortNamespaceFileDao ,function : setObj"
        testFilePath = "/tmp/"

        pnfDao = JsonFileDao()
        pnfDao.setFilePathDir(testFilePath)
        jsonDict = {"name":"test"}
        filename = pnfDao.setObj(json.dumps(jsonDict, indent=2))
        content = FileUtil.readContent(filename)
        resultJson = json.loads(content)
        print resultJson['name']


        assert resultJson['name'] == jsonDict['name']

        print "test pass!"



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
