import json
import os

def getJsonDict(fileName):
    if not os.path.exists(fileName):
        return None

    jsonFile = open(fileName)
    dic_list={}
    while True:
        line = jsonFile.readline()
        if len(line) == 0:
            break
        decoded = json.loads(line)
        for key,value in decoded.items():
            dic_list[key] = value
    return dic_list

if __name__ == "__main__":
    jsonDict = getJsonDict('item.json')
    exJsonDict = getJsonDict('exchange.json')
    for key,value in jsonDict.items():
        if value.has_key('ex_id'):
            exId = value['ex_id']
            if not exJsonDict.has_key(exId):
                print 'tag=',key," item config error ex_id:",exId
