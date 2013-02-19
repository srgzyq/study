#coding=utf-8

def getSubStr(value):
    strValue = str(value)
    if strValue == None:
        return -1

    if strValue.find("[") < 0:
        return -1

    startIndex = strValue.index("[")
    if startIndex < 0:
        return -1
    endIndex = strValue.index("]")
    if endIndex < 0:
        return -1
    substr = strValue[startIndex+1:endIndex]
    return substr

def readFileByName(fileName):
    dicList = []
    f = open(fileName)
    line = f.readline()
    while line:
        line = f.readline()
        key = getSubStr(line)
        if key != -1:
            dicList.append(key)
    f.close()

    return dicList

if __name__ == "__main__":
    dicList = readFileByName("LanguageConfig.lua")
    comList  = readFileByName("LanguageTWConfig.lua")
    
    for key in dicList:
        if not key in comList:
            print key

