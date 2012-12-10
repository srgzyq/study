#coding=utf-8
import string
import os


def prase_dic_struct(jsonValue,keyValue,index):
    strLua=""
    if keyValue != "":
        strLua = "[\""+str(keyValue)+"\"]="

    typeStr = get_type_class(jsonValue) 

    if typeStr == "dict":
        strLua += "{"
        for key in jsonValue:
            value = jsonValue[key]
            strLua += prase_dic_struct(value,key,index+1)
        if index == 0:
            strLua+="}"
        else:
            strLua += "},"

    elif typeStr == "list":
        strLua += "{"
        for key in range(len(jsonValue)):
            value = jsonValue[key]
            strLua += prase_dic_struct(value,key+1,index+1)
        if index == 0:
            strLua += "}"
        else:
            strLua += "},"
    elif typeStr == "int":
        strLua += str(jsonValue)+","
    elif typeStr == "str" or typeStr=="unicode":
        strLua += "\""+str(jsonValue)+"\","
    elif typeStr == "float":
        strLua += str(jsonValue)+","
    
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
    allStr="a="+string.join(lua_table,"")
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
    #fileName="/Users/shirui/Develop/ares/svn/Resources/config/item.json"
    #prase_file_name(fileName)


    #testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1},"chichi":{"hard":{"shenzhang":"pig"},"age":12},"srgzyq":"name"}}
    #testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1}},"srgzyq":[{"value":2000,"key":"test"}]}
    testData={"srgzyq":{"age":12,"name":"srgzyq","person":[{"value":2000,"key":"test"},{"value":1234,"key":"playcrab"}]}}
    """testData={"srgzyq":
                {
                    "name":
                        [
                            {
                                "srgzyq":{"age":12,"time":1},
                                "chichi":["c","d"]
                            }
                        ]
                }
            }

    """
    #testData={"person":{"age":12,"name":"srgzyq"},"person1":{"age":13,"name":"chichi"}}
    #testData={"person1":{"age":13,"name":"chichi"}}
    #testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1}}}
    print testData
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
    
