__author__ = 'zhangbohan'


class UserNamespace(object):
    MAX_POD_ID_LENGTH = 253
    MAX_ReplicationController_ID_LENGTH = 253
    MAX_SERVICE_ID_LENGTH = 24
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
    def setModelId(self,model):
        kind = model.getKind()


        return kind
    def setModelLabelsAndNamespace(self, userId, farmName, roleName, model):
        #modelKind = model.getKind()
        namespace = self.getUserNamespace(userId)
        farmLabel = self.getFarmLabel(userId, farmName)
        roleLabel = self.getRoleLabel(userId, farmName, roleName)
        labels = {}
        labels['farmlabel'] = farmLabel
        labels['rolelabel'] = roleLabel
        model.setNamespace(namespace)
        model.setLabels(labels)

        return model