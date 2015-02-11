__author__ = 'zhangbohan'
import json

class TypeMeta(object):
    def __init__(self
                 , id=None
                 , apiVersion=None
                 , kind=None
                 , uid=None
                 , creationTimestamp=None
                 , selfLink=None
                 , resourceVersion=None
                 , namespace=None
                 , annotations=None

    ):
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
    def fromJSON(typeMetaJSON):
        typeMetaDict = json.loads(typeMetaJSON)
        typeMeta = TypeMeta.fromDict(typeMetaDict)
        return typeMeta

    @staticmethod
    def fromDict(typeMetaDict):
        
        if typeMetaDict.has_key("id"):
            id = typeMetaDict["id"]
        else:
            id = None

        if typeMetaDict.has_key("apiVersion"):
            apiVersion = typeMetaDict["apiVersion"]
        else:
            apiVersion = None

        if typeMetaDict.has_key("kind"):
            kind = typeMetaDict["kind"]
        else:
            kind = None

        if typeMetaDict.has_key("uid"):
            uid = typeMetaDict["uid"]
        else:
            uid = None

        if typeMetaDict.has_key("creationTimestamp"):
            creationTimestamp = typeMetaDict["creationTimestamp"]
        else:
            creationTimestamp = None

        if typeMetaDict.has_key("selfLink"):
            selfLink = typeMetaDict["selfLink"]
        else:
            selfLink = None

        if typeMetaDict.has_key("resourceVersion"):
            resourceVersion = typeMetaDict["resourceVersion"]
        else:
            resourceVersion = None

        if typeMetaDict.has_key("namespace"):
            namespace = typeMetaDict["namespace"]
        else:
            namespace = None

        if typeMetaDict.has_key("annotations"):
            annotations = typeMetaDict["annotations"]
        else:
            annotations = None

        return TypeMeta(
                   id
                   , apiVersion
                   , kind
                   , uid
                   , creationTimestamp
                   , selfLink
                   , resourceVersion
                   , namespace
                   , annotations)

    @staticmethod
    def fromDictToInlineProperty(typeMetaDict):
        prepertyList = []

        if typeMetaDict.has_key("id"):
            id = typeMetaDict["id"]
            prepertyList.append("id")
        else:
            id = None

        if typeMetaDict.has_key("apiVersion"):
            apiVersion = typeMetaDict["apiVersion"]
            prepertyList.append("apiVersion")
        else:
            apiVersion = None

        if typeMetaDict.has_key("kind"):
            kind = typeMetaDict["kind"]
            prepertyList.append("kind")
        else:
            kind = None

        if typeMetaDict.has_key("uid"):
            uid = typeMetaDict["uid"]
            prepertyList.append("uid")
        else:
            uid = None

        if typeMetaDict.has_key("creationTimestamp"):
            creationTimestamp = typeMetaDict["creationTimestamp"]
            prepertyList.append("creationTimestamp")
        else:
            creationTimestamp = None

        if typeMetaDict.has_key("selfLink"):
            selfLink = typeMetaDict["selfLink"]
            prepertyList.append("selfLink")
        else:
            selfLink = None

        if typeMetaDict.has_key("resourceVersion"):
            resourceVersion = typeMetaDict["resourceVersion"]
            prepertyList.append("resourceVersion")
        else:
            resourceVersion = None

        if typeMetaDict.has_key("namespace"):
            namespace = typeMetaDict["namespace"]
            prepertyList.append("namespace")
        else:
            namespace = None

        if typeMetaDict.has_key("annotations"):
            annotations = typeMetaDict["annotations"]
            prepertyList.append("annotations")
        else:
            annotations = None

        return prepertyList, TypeMeta(
                   id
                   , apiVersion
                   , kind
                   , uid
                   , creationTimestamp
                   , selfLink
                   , resourceVersion
                   , namespace
                   , annotations)

    def toDict(self):
        typeMetaDict = {

        }

        if None != self.id:
            typeMetaDict["id"] = self.id

        if None != self.apiVersion:
            typeMetaDict["apiVersion"] = self.apiVersion

        if None != self.kind:
            typeMetaDict["kind"] = self.kind

        if None != self.uid:
            typeMetaDict["uid"] = self.uid

        if None != self.creationTimestamp:
            typeMetaDict["creationTimestamp"] = self.creationTimestamp

        if None != self.selfLink:
            typeMetaDict["selfLink"] = self.selfLink

        if None != self.resourceVersion:
            typeMetaDict["resourceVersion"] = self.resourceVersion

        if None != self.namespace:
            typeMetaDict["namespace"] = self.namespace

        if None != self.annotations:
            typeMetaDict["annotations"] = self.annotations
        return typeMetaDict

    def toJSON(self):
        typeMetaDict = self.toDict()
        ptypeMetajson = json.dumps(typeMetaDict, indent=2)
        return ptypeMetajson


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