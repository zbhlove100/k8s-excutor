__author__ = 'zhangbohan'
import unittest

from pkg.infrastructure.integration.kubernetes.model.service.Service import Service
from pkg.domain.common.bl.impl.namespace.PortNamespace import PortNamespace
from pkg.domain.common.dao.namespcaeDao.PortNamespcaeFileDao import PortNamespcaeFileDao


class PortNamespaceTest(unittest.TestCase):
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

        service = Service("11","x1",{},"tcp",80,88,{},["192.168.1.1"])
        portDao = PortNamespcaeFileDao()
        pnamespace = PortNamespace(portDao)
        service1 = pnamespace.setServicePublicIpPort(service)

        print("reuslt :%s" % service1.toJSON())
        print("--------------------------------")

        result = service1.getPort()
        assert result != None
        # assert  expectNamespace == resultNamespace
        print("test pass!")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
