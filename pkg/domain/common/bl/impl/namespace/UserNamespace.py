__author__ = 'zhangbohan'


class UserNamespace(object):
    def __init__(self):
        pass

    def getUserNamespace(self,userId):
        userNamespace = "%s.samsungcloud.org" % userId
        return userNamespace

    def getFarmLabel(self, userId, farmName):
        labelValue = "%s-%s" % (userId, farmName)
        farmLabel = {"farmLabel": labelValue}
        return farmLabel

    def getRoleLabel(self, userId, farmName, roleName):
        labelValue = "%s-%s-%s" % (userId, farmName, roleName)
        roleLabel = {"roleLabel": labelValue}
        return roleLabel