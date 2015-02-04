__author__ = 'zhangbohan'
import commands

class SimpleCmdExecutor(object):
    def __init__(self):
        pass
    def executeCmd(self, cmd):
        output = commands.getoutput(cmd)
        return output