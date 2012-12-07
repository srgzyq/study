#coding=utf-8
import string

def prase_dic_struct(dictData,keyValue,index):
    print keyValue
    strLua=""
    if keyValue != "":
        strLua = "[\""+keyValue+"\"]={"
    for key in dictData:
        list_lua = []
        value = dictData[key]
        typeStr = get_type_class(str(type(value))) 
        if typeStr == "dict":
            strLua += prase_dic_struct(value,key,index+1)
        else:
            #print "key="+key+"  value="+str(value)
            strLua += "[\""+key+"\"]=\""+str(value) + "\","
    if index != 0:    
        strLua += "}," 
    return strLua

def prase_dic_struct_one(dictData,luaTableData):
    strLua = ""
    for key in dictData:
        value = dictData[key]
        strLua += "[\""+str(key)+"\"]" + "="+"\""+str(value)+"\""
    #print strLua
    luaTableData.append(strLua)

def get_type_class(typeStr):
    return typeStr.replace("<type '","").replace("'>","")

def file_write_into_lua(fileName,strLua):
    lua_file = open(fileName,'w')
    lua_file.truncate()
    lua_file.write(strLua)

if __name__ == "__main__":
    ##testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1},"person1":{"age":13,"name":"chichi"}}}

    testData={"person":{"age":12,"name":"srgzyq","skill":{"python":1,"lua":1,"as3":1}}}
    #testData={"person":{"age":12,"name":"srgzyq"}}
    testData2={"person1":{"age":13,"name":"chichi"}}

    testLuaStr="person={[\"skill\"]={[\"python\"]=12,[\"lua\"]=\"srgzyq\",[\"as3\"]=1},[\"age\"]=12,[\"name\"]=\"srgzyq\"}"
    #file_write_into_lua("luafile.lua",testLuaStr)

    index=0
    a = prase_dic_struct(testData,"",index)

