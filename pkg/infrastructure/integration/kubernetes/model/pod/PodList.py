__author__ = 'zhangbohan'
import json
from pkg.infrastructure.integration.kubernetes.model.pod.Pod import Pod


class PodList(object):
    def __init__(self
                 , items=None
                 , id=None
                 , apiVersion=None
                 , kind="Pod"
                 , uid=None
                 , creationTimestamp=None
                 , selfLink=None
                 , resourceVersion=None
                 , namespace=None
                 , annotations=None

    ):
        self.items = items
        self.id = id
        self.apiVersion = apiVersion
        self.kind = kind
        self.uid = uid
        self.creationTimestamp = creationTimestamp
        self.selfLink = selfLink
        self.resourceVersion = resourceVersion
        self.namespace = namespace
        self.annotations = annotations
        pass

    @staticmethod
    def fromJSON(podJSON):
        podDict = json.loads(podJSON)
        pod = PodList.fromDict(podDict)
        return pod

    @staticmethod
    def fromDict(podDict):
        if podDict.has_key("items") and None!=podDict["items"]:
            tmpItems = podDict["items"]
            items = []
            for item in tmpItems:
                pod = Pod.fromDict(item)
                items.append(pod)
        else:
            items = None


        if podDict.has_key("id"):
            id = podDict["id"]
        else:
            id = None

        if podDict.has_key("apiVersion"):
            apiVersion = podDict["apiVersion"]
        else:
            apiVersion = None

        if podDict.has_key("kind"):
            kind = podDict["kind"]
        else:
            kind = None

        if podDict.has_key("uid"):
            uid = podDict["uid"]
        else:
            uid = None

        if podDict.has_key("creationTimestamp"):
            creationTimestamp = podDict["creationTimestamp"]
        else:
            creationTimestamp = None

        if podDict.has_key("selfLink"):
            selfLink = podDict["selfLink"]
        else:
            selfLink = None

        if podDict.has_key("resourceVersion"):
            resourceVersion = podDict["resourceVersion"]
        else:
            resourceVersion = None

        if podDict.has_key("namespace"):
            namespace = podDict["namespace"]
        else:
            namespace = None

        if podDict.has_key("annotations"):
            annotations = podDict["annotations"]
        else:
            annotations = None
        pod = PodList(items
                  , id
                  , apiVersion
                  , kind
                  , uid
                  , creationTimestamp
                  , selfLink
                  , resourceVersion
                  , namespace
                  , annotations
                  )

        return pod

    def toDict(self):
        podDict = {
        }

        if None != self.items:
            pods = []
            for item in self.items:
                pods.append(item)
            podDict["items"] = pods

        if None != self.id:
            podDict["id"] = self.id

        if None != self.apiVersion:
            podDict["apiVersion"] = self.apiVersion

        if None != self.kind:
            podDict["kind"] = self.kind

        if None != self.uid:
            podDict["uid"] = self.uid

        if None != self.creationTimestamp:
            podDict["creationTimestamp"] = self.creationTimestamp

        if None != self.selfLink:
            podDict["selfLink"] = self.selfLink

        if None != self.resourceVersion:
            podDict["resourceVersion"] = self.resourceVersion

        if None != self.namespace:
            podDict["namespace"] = self.namespace

        if None != self.annotations:
            podDict["annotations"] = self.annotations
        return podDict

    def toJSON(self):
        pod_dict = self.toDict()
        pod_json = json.dumps(pod_dict, indent=2)
        return pod_json


    def setItems(self, items):
        self.items = items

    def getItems(self):
        return self.items

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setApiVersion(self, apiVersion):
        self.apiVersion = apiVersion

    def getApiVersion(self):
        return self.apiVersion

    def setKind(self, kind):
        self.kind = kind

    def getKind(self):
        return self.kind

    def setUid(self, uid):
        self.uid = uid

    def getUid(self):
        return self.uid

    def setCreationTimestamp(self, creationTimestamp):
        self.creationTimestamp = creationTimestamp

    def getCreationTimestamp(self):
        return self.creationTimestamp

    def setSelfLink(self, selfLink):
        self.selfLink = selfLink

    def getSelfLink(self):
        return self.selfLink

    def setResourceVersion(self, resourceVersion):
        self.resourceVersion = resourceVersion

    def getResourceVersion(self):
        return self.resourceVersion

    def setNamespace(self, namespace):
        self.namespace = namespace

    def getNamespace(self):
        return self.namespace

    def setAnnotations(self, annotations):
        self.annotations = annotations

    def getAnnotations(self):
        return self.annotations

