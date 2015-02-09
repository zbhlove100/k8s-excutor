__author__ = 'zhangbohan'

class KubernetesCommandDao(object):

    def __init__(self):
        pass
    @staticmethod
    def getCreateCommand(filePath):
        result = KubernetesCommandDao.KUBERNETES_CREATE_COMMAND % (filePath)
        return result
    @staticmethod
    def getDeleteCommand(kind,name):
        cmd = KubernetesCommandDao.KUBERNETES_DELETE_POD_COMMAND
        if kind == "service":
            cmd = KubernetesCommandDao.KUBERNETES_DELETE_SERVICE_COMMAND
        elif kind == "replication":
            cmd = KubernetesCommandDao.KUBERNETES_DELETE_REPLICATION_COMMAND

        result = cmd % (name)
        return result
    @staticmethod
    def getQueryCommand(kind,name):
        cmd = "%s %s" % (KubernetesCommandDao.KUBERNETES_GET_POD_COMMAND, name)
        if kind == "service":
            cmd = "%s %s" % (KubernetesCommandDao.KUBERNETES_GET_SERVICE_COMMAND, name)
        elif kind == "replication":
            cmd = "%s %s" % (KubernetesCommandDao.KUBERNETES_GET_REPLICATION_COMMAND, name)

        return cmd
    @staticmethod
    def getQueryStatusCommand(label):
        cmd = KubernetesCommandDao.KUBERNETES_QUERY_POD_STATUS_COMMAND % label


        result = cmd
        return result