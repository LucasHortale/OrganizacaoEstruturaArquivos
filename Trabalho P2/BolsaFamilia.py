import struct
import hashlib
import os
import sys

hashSize = 900001
fileName = "janeiro.csv"
indexName = "dezembro.csv"
dataFormat = "72s72s72s72s2s8s2x"
indexFormat = "8sLL"
keyColumnIndex = 5

dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize

fi = open(indexName,"rb")
f = open(fileName,"rb")

while True:
    fi.seek(offset,os.SEEK_SET)
    indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
    dataRecord = dataStruct.unpack(fi.read(dataStruct.size))
    if indexRecord[0] == dataRecord[0]
        f.seek(indexRecord[1]*dataStruct.size,os.SEEK_SET)
        record = dataStruct.unpack(f.read(dataStruct.size))
        novo arquivo = fwrite(novoarquivo.txt)
    offset = indexRecord[2]
    if offset == 0:
        break
    i += 1
fi.close()
f.close()
novoarquivo.close()

fileName = ("novoarquivo.txt")
lineCount = 0
f = open(fileName,"rb")
while True:
    line = f.read(300)
    if line == "":
        break
    lineCount += 1
f.close()

print lineCount
