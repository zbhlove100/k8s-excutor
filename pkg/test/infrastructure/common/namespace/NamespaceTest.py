__author__ = 'zhangbohan'
import unittest

from pkg.infrastructure.common.identification import UuidUtil
from pkg.infrastructure.common.file.FileUtil import FileUtil


class NamespaceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testGetUnusedPort(self):
        print ""
        name = UuidUtil()
        resultport = name.getUnusedPort('127.0.0.1')
        resultFile = FileUtil.readContent(UuidUtil.PUBLIC_IP_PORT_FILE)
        print("reuslt of getUnusedPort :%s" % resultport)
        print("--------------------------------")
        print(resultFile)

    def testGetUuid(self):
        print ""
        name = UuidUtil()
        result = name.getUuidName()
        print(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
