__author__ = 'zhangbohan'
import unittest
from pkg.infrastructure.common.identification.UuidUtil import  UuidUtil


class UuidUtilTest(unittest.TestCase):
    def setUp(self):

        pass

    def tearDown(self):
        pass


    def testgGtUuidName(self):
        print "Test class : UuidUtilTest ,function : getUuidName"
        result1 = UuidUtil.getUuidName()
        result2 = UuidUtil.getUuidName()
        assert result1 != result2
        print("uuid1 :", result1, "uuid2:", result2)
        print "test pass!"


    def testgGetUuidWithPrefix(self):
        print "Test class : UuidUtilTest ,function : getUuidName"
        prefix = "testprefix"
        result1 = UuidUtil.getUuidWithPrefix(prefix)
        result2 = UuidUtil.getUuidWithPrefix(prefix)
        assert result1.startswith(prefix)
        assert result1.startswith(prefix)
        assert result1 != result2
        print("uuid1 :", result1, "uuid2:", result2)
        print "test pass!"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()