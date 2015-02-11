__author__ = 'zhangbohan'
import unittest,json
from pkg.infrastructure.integration.kubernetes.model.service.Service import Service


class ServiceTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testFromJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.service.Service
            test function : fromJSON
        """
        #serviceJson = '{"id": "mysqlservice","kind": "Service","apiVersion": "v1beta2","selector": {"name": "testdatabase"},"protocol": "TCP","containerPort": 3306,"port": 3306}'
        serviceJson = """
            {
              "id": "mysqlservice",
              "kind": "Service",
              "apiVersion": "v1beta2",
              "selector": {
                "name": "testdatabase"
              },
              "protocol": "TCP",
              "containerPort": 3306,
              "port": 3306
            }

        """
        service = Service.fromJSON(serviceJson)

        print("reuslt :%s" % service.toJSON())
        print("--------------------------------")
        exceptResult = {"name": "testdatabase"}
        result = service.getSelector()
        assert result == exceptResult
        print("test pass!")

    def testToJSON(self):
        print """
            test class : pkg.infrastructure.integration.kubernetes.model.service.Service
            test function : toJSON
        """
        #serviceJson = '{"id": "mysqlservice","kind": "Service","apiVersion": "v1beta2","selector": {"name": "testdatabase"},"protocol": "TCP","containerPort": 3306,"port": 3306}'
        serviceJson = """
            {
              "id": "mysqlservice",
              "kind": "Service",
              "apiVersion": "v1beta2",
              "selector": {
                "name": "testdatabase"
              },
              "protocol": "TCP",
              "containerPort": 3306,
              "port": 3306
            }

        """
        service = Service.fromJSON(serviceJson)
        result = service.toJSON()
        print("reuslt :%s" % result)
        print("--------------------------------")

        assert result !=None
        print("test pass!")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
