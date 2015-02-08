__author__ = 'zhangbohan'
import json


class ContainerOperationRequestParser(object):
    def __init__(self):
        pass



    def parsePodModel(self, podRequestDataDict):
        pod = podRequestDataDict['pod']
        desiredState = podRequestDataDict['desiredState']
        manifest = desiredState['manifest']
        containers = manifest['containers']



        pod = Pod(id="c26b6f55-adec-11e4-8d9a-22000aba1b4e", apiVersion="v1beta1", desiredState={}, labels={}, namespace="default")

        return

    def parseServiceModel(self, serviceRequestDataDict):
        return

    def parseReplicationControllerModel(self, replicationControllerRequestDataDict):
        return