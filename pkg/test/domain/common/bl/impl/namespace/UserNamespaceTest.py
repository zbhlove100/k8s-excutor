__author__ = 'zhangbohan'
import unittest

from pkg.infrastructure.integration.kubernetes.model.service import Service
from pkg.domain.common.bl.impl.namespace.UserNamespace import UserNamespace


class UserNamespaceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testSetModelLabelsAndNamespace(self):
        print """
            test class : pkg.domain.common.bl.impl.namespace.UserNamespace
            test function : setModelLabelsAndNamespace
        """
        userId  = "111111"
        farmName = "far"
        roleName = "rol"

        service = Service("11","x1",{},"tcp",80,88,{})
        unamespace = UserNamespace()
        service1 = unamespace.setModelLabelsAndNamespace(userId,farmName,roleName,service)

        print("reuslt :%s" % service1.toJSON())
        print("--------------------------------")
        expectLabels = {"roleLabel": "111111-far-rol","farmLabel": "111111-far"}
        resultLabels = service1.getLabels()
        expectNamespace = "111111.samsungcloud.org"
        resultNamespace = service1.getNamespace()
        assert expectLabels == resultLabels
        assert  expectNamespace == resultNamespace
        print("test pass!")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
