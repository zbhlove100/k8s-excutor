__author__ = 'zhangbohan'
from pkg.infrastructure.common.namespace.Namespace import Namespace
from pkg.infrastructure.common.file.FileUtil import FileUtil
import unittest
class NamespaceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testGetUnusedPort(self):
        print ""
        name = Namespace()
        resultport = name.getUnusedPort('127.0.0.1')
        resultFile = FileUtil.readContent(Namespace.PUBLIC_IP_PORT_FILE)
        print("reuslt of getUnusedPort :%s" % resultport)
        print("--------------------------------")
        print(resultFile)

    def testGetUuid(self):
        print ""
        name = Namespace()
        result = name.getUuidName()
        print(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
