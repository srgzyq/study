#coding=utf-8
import re
import os
import shutil
from ConfigParser import SafeConfigParser

def readIniFile(fileName,sheBeidic):
    #f = read(fileName)
    print '-'*20, ' following is read ini file part', '-'*20
    #f.seek(0)
    scp2 = SafeConfigParser()
    #scp2.readfp(f)
    scp2.read(fileName)
    sections = scp2.sections()
    for s in sections:
        options = scp2.options(s)
        for option in options:
            index = option.find("keyid_value")
            if index > -1:
                #print option
                value = scp2.get(s,option)
                devalue = value #.decode('gbk').encode('utf8')
                if len(devalue) > 0 and option != "keyid_value_number":
                    changeNew = strDoit(devalue,option,sheBeidic)
                    if changeNew != None:
                        #print "keyId="
                        #print "old section: %s, option: %s, value: %s" % (s,option,devalue)
                        scp2.set(s,option,changeNew)
                        scp2.write(open(fileName,'w'))

def getBlankNum(s):
    index = s.find(" ")
    if index == -1:
        patter = re.compile(r'\d{1}')
        countBlank = 0
        for i in range(0,len(s)):
            if s[i] == "#": 
                break
            elif patter.search(s[i]) == None:
                countBlank += 1 
    else:
        start = s.find(" ")
        last = s.find("#")
        countBlank = last - start
    return countBlank


def strDoit(s,option,sheBeidic):
    index = s.find(" ")
    if index == -1:
        index = s.find("#")
    length = len(s)
    oldValue = s[0:index]
    #print "find key:"+oldValue
    index = s.find("#")
    #blank num 空格数目
    desValue = s[index:length]
    if sheBeidic.has_key(oldValue):
        newValue = sheBeidic[oldValue]
        print "key " + option + " old value="+oldValue + " change new value="+newValue
        #print sheBeidic[oldValue]
        needBlank = getBlankNum(s)
        for num in range(0,needBlank):
            newValue += " "
        newValue += desValue
        index = s.find(" ")
        sheBeidic["count"] += 1
        return newValue
    else:
        return None

def findDirPath(path,cpPath):
    path = "."+os.sep+path
    cpPath = "."+os.sep+cpPath
    fileList = os.listdir(path)
    for li in fileList:
        filePath = os.path.join(path,li)
        fileName = os.path.basename(filePath)
        fileSpilte = os.path.splitext(fileName)
        if fileSpilte[1] != None and fileSpilte[1] == ".ini": 
            cpFile = cpPath+os.sep+fileName
            if os.path.exists(cpFile):
                os.remove(cpFile)
                shutil.copyfile(filePath,cpFile)
            else:
                shutil.copyfile(filePath,cpFile)

def getParseInIFile(dirPath):
    fileNameArr = [] 
    path = "."+os.sep+dirPath
    fileList = os.listdir(path)
    for li in fileList:
        filePath = os.path.join(path,li)
        fileName = os.path.basename(filePath)
        fileNameArr.append(fileName)
    return fileNameArr

def parseMapKey(sheBeidic):
    print "read etl_device_id_map.txt file"
    findFileName = "."+os.sep+"backup"+os.sep+"etl_device_id_map.txt"
    txtFile = open(findFileName,"r")
    lines = txtFile.readlines()
    count = 0
    for line in lines: 
        if count == 0:
            count = 1
            continue
        else:
            getDicYuanXianId(line,sheBeidic)
    txtFile.close()

def getDicYuanXianId(lineStr,sheBeidic):
    patter = re.compile(r'\d{1}')
    yuanSheBeiId = lineStr[0:18]
    xianSheBeiId = lineStr[68:86]
    sheBeidic[yuanSheBeiId] = xianSheBeiId
    dropBlank = xianSheBeiId.lstrip()
    if len(dropBlank) == 17:
        xianSheBeiId = lineStr[68:87]
        newId = xianSheBeiId.lstrip()
        sheBeidic[yuanSheBeiId] = newId
    

if __name__ == "__main__":
    sheBeidic = {}
    sheBeidic["count"] = 0
    srcPath = "backup"
    dirPath = "output"
    parseMapKey(sheBeidic)
    #print sheBeidic
    findDirPath(srcPath,dirPath)
    fileNameArr = getParseInIFile(dirPath)
    #print fileNameArr
    for fileName in fileNameArr:
        name="."+os.sep+dirPath+os.sep+fileName 
        print name
        readIniFile(name,sheBeidic)

    print "finish ok need count",sheBeidic["count"]
