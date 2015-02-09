__author__ = 'zhangbohan'


class UserNamespace(object):
    def __init__(self):
        pass

    def getUserNamespace(self,userId):
        userNamespace = "%s.samsungcloud.org" % userId
        return userNamespace

    def getFarmLabel(self, userId, farmName):
        labelValue = "%s-%s" % (userId, farmName)
        farmLabel = labelValue
        return farmLabel

    def getRoleLabel(self, userId, farmName, roleName):
        labelValue = "%s-%s-%s" % (userId, farmName, roleName)
        roleLabel = labelValue
        return roleLabel

    def setModelLabelsAndNamespace(self, userId, farmName, roleName, model):
        #modelKind = model.getKind()
        namespace = self.getUserNamespace(userId)
        farmLabel = self.getFarmLabel(userId, farmName)
        roleLabel = self.getRoleLabel(userId, farmName, roleName)
        labels = {}
        labels['farmLabel'] = farmLabel
        labels['roleLabel'] = roleLabel
        model.setNamespace(namespace)
        model.setLabels(labels)

        return model