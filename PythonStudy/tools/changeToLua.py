#coding=utf-8
import string
import os

"""a={
    ["person"] = {
        [0] = {
                ["key"]="srgzyq",
                ["value"]=200,
            },
        
        [1] ={
                ["key"]="playcrab",
                ["value"]=300,
            }
    },
}
"""
def prase_list_struct(value,key):
    strLua = "[\""+key+"\"]={"
    dicIndex = 0
    for dicValue in value:
        baseType = get_type_class(dicValue)
        if baseType == "dict":
            strLua += "["+str(dicIndex)+"]={"
            dicKeys = dicValue.keys() 
            for oneKey in dicKeys:
                oneValue = dicValue[oneKey]
                valueType = get_type_class(oneValue)
                if valueType == "str" or valueType=="unicode":
                    strLua += "[\""+oneKey+"\"]=\""+str(oneValue)+"\","
                else:
                    strLua += "[\""+oneKey+"\"]="+str(oneValue)+","

            strLua += "},"
            dicIndex += 1
        else:
            if baseType == "str" or baseType == "unicode":
                strLua += "\""+str(dicValue)+"\","
            else:
                strLua += str(dicValue)+","
    strLua += "},"
    return strLua
     

def prase_dic_struct(dictData,keyValue,index):
    strLua=""
    if keyValue != "":
        strLua = "[\""+keyValue+"\"]={"
    for key in dictData:
        list_lua = []
        value = dictData[key]
        typeStr = get_type_class(value) 
        if typeStr == "dict":
            strLua += prase_dic_struct(value,key,index+1)
        elif typeStr == "list":
            strLua += prase_list_struct(value,key)
        else:
            #print "key="+key+"  value="+str(value)
            valueType = get_type_class(value)
            if valueType == "str" or valueType=="unicode":
                strLua += "[\""+key+"\"]=\""+str(value) + "\","
            else:
                strLua += "[\""+key+"\"]="+str(value) + ","

    if index != 0:    
        strLua += "}," 
    #else:
        #strLua += "}"
    return strLua

def get_type_class(value):
    typeStr = str(type(value))
    return typeStr.replace("<type '","").replace("'>","")

def file_write_into_lua(fileName,strLua):
    lua_file = open(fileName,'w')
    lua_file.truncate()
    lua_file.write(strLua)

def encond_one_by_one(allDicData):
    lua_table = []
    for key in allDicData:
        index = 0
        newDic = {key:allDicData[key]}
        a = prase_dic_struct(newDic,"",index)
        lua_table.append(a)
    allStr="a={"+string.join(lua_table,"")+"}"
    return allStr

def prase_file_name(fileName):
    name = os.path.basename(fileName)     
    filespilte = os.path.splitext(fileName)
    print name
    print filespilte
    newFileName = filespilte[0]+".lua"
    print newFileName


if __name__ == "__main__":
    ##testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1},"person1":{"age":13,"name":"chichi"}}}
    fileName="/Users/shirui/Develop/ares/svn/Resources/config/item.json"
    prase_file_name(fileName)


    #testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1}},"chichi":{"hard":{"shenzhang":"pig"},"age":12},"srgzyq":"name"}
    #testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1}},"srgzyq":[{"value":2000,"key":"test"}]}
    #testData={"srgzyq":{"age":12,"name":"srgzyq","person":[{"value":2000,"key":"test"},{"value":1234,"key":"playcrab"}]}}
    testData={"srgzyq":{"name":[12,13,14,15],"chichi":["c","d"]}}
    #testData={"person":{"age":12,"name":"srgzyq"},"person1":{"age":13,"name":"chichi"}}
    #testData2={"person1":{"age":13,"name":"chichi"}}
    allStr = encond_one_by_one(testData)
    print allStr
    #file_write_into_lua("luafile.lua",allStr)

    #allDicData = {testData,testData2}
    #print allDicData
    #test = testData.items()[0]
    #print test
    #print type(test)
    #index=0
    #a = prase_dic_struct(testData.items[0],"",index)
    #lua_table.append(a)
    #print a

    #testLuaStr="person={[\"skill\"]={[\"python\"]=12,[\"lua\"]=\"srgzyq\",[\"as3\"]=1},[\"age\"]=12,[\"name\"]=\"srgzyq\"}"
    #file_write_into_lua("luafile.lua",testLuaStr)
    #lua_table = []
    """index=0
    a = prase_dic_struct(testData,"",index)
    lua_table.append(a)
    print a
    index = 0
    b = prase_dic_struct(testData2,"",index)
    print b
    lua_table.append(b)
    print "all:\n",string.join(lua_table,",")
    """
    
