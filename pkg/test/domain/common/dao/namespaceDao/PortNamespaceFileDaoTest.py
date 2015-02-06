__author__ = 'zhangbohan'
import unittest

from pkg.domain.common.dao.namespcaeDao.PortNamespcaeFileDao import PortNamespcaeFileDao
from pkg.infrastructure.common.file.FileUtil import FileUtil
import uuid

class PortNamespaceFileDaoTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testSetAllocatePort(self):
        print ""
        testFilePath = "/tmp/%s" % str(uuid.uuid4())
        testIp = "123.456.789.111"
        testPort = 2222
        pnfDao = PortNamespcaeFileDao()
        pnfDao.setPortNamespcaeFile(testFilePath)
        pnfDao.setAllocatePort(testIp,testPort)
        content = FileUtil.readContent(testFilePath).strip()
        print content
        expectResult = "%s:%s" % (testIp,testPort)

        assert content == expectResult

    def testgetAllocatedPort(self):
        print ""
        testFilePath = "/tmp/%s" % str(uuid.uuid4())
        testIp = "123.456.789.111"
        testPort = 2222
        pnfDao = PortNamespcaeFileDao()
        pnfDao.setPortNamespcaeFile(testFilePath)
        pnfDao.setAllocatePort(testIp,testPort)
        FileUtil.readContent(testFilePath).strip()

        result = pnfDao.getAllocatedPorts(testIp)
        print result

        expectResult = [str(testPort)]
        print expectResult

        assert result == expectResult



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
