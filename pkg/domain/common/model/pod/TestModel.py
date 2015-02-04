__author__ = 'zhangbohan'

from Manifest import Manifest

from pkg.infrastructure.common.file.FileUtil import FileUtil

result = FileUtil.readContent("/tmp/testArray")

ar = result.splitlines()
for item in ar:
    hostAndPort = item.split(":")
    host = hostAndPort[0]
    port = hostAndPort[1]
    print(port)

