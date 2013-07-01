#coding=utf-8

import json
import logging
import os
import re
import string

def run(config):
    ingorFile = []#"translateDiff2.json","translateDiff1.json","translate.json"]
    current_dir = config['current_dir']
    global input_config_json_dir 
    input_config_json_dir = current_dir +os.sep + config['config_input_path']
    global output_config_lua_dir
    output_config_lua_dir = current_dir+os.sep+config['config_output_path']
    
    all_json_file_name = {}
    get_json_file_all_name(input_config_json_dir,all_json_file_name)
    for fileName in all_json_file_name:
        if not fileName in ingorFile:
            fileKey = os.path.splitext(fileName)[0]
            lastFileType = os.path.splitext(fileName)[1]
            if lastFileType == ".json":
                file_one_json_file_to_lua_file(all_json_file_name,fileName,fileKey)


# 完整的转化为lua 文件
def file_one_json_file_to_lua_file(all_json_file_name,fileName,fileKey):
    itemFile = all_json_file_name[fileName]
    itemAllDic = getDicListByFileName(itemFile)
    itemTable = encode_one_by_one(itemAllDic,fileKey,fileName)
    outFile = output_config_lua_dir+os.sep+fileName
    file_write_into_lua(outFile,itemTable)


# 写文件
def file_write_into_lua(fileName,strLua):
    newFileName = prase_file_name(fileName)
    lua_file = open(newFileName,'w')
    lua_file.truncate()
    lua_file.write(strLua)

# 转化文件名
def prase_file_name(fileName):
    name = os.path.basename(fileName)
    filespilte = os.path.splitext(fileName)
    newFileName = filespilte[0]+".lua"
    return newFileName

# 转化所有item
def encode_one_by_one(allDicData,leadKey,fileName):
    lua_table = []
    testIndex=0
    index=0
    allStr = leadKey+"_config="+prase_dic_struct(allDicData,"",index,fileName)
    return allStr

# 单一一个dict 转化为lua格式
def prase_dic_struct(jsonValue,keyValue,index,fileName):
    strLua=""
    if keyValue != "":
        strLua = "[\""+str(keyValue)+"\"]="
    #elif index==0:
    #    strLua="{"

    typeStr = get_type_class(jsonValue) 
    if typeStr == "dict":
        strLua += "{"
        for key in jsonValue:
            value = jsonValue[key]
            strLua += prase_dic_struct(value,key,index+1,fileName)
        if index == 0:
            strLua+="}"
        else:
            strLua += "},"

    elif typeStr == "list":
        strLua += "{"
        for key in range(len(jsonValue)):
            value = jsonValue[key]
            strLua += prase_dic_struct(value,key+1,index+1,fileName)
        if index == 0:
            strLua += "}"
        else:
            strLua += "},"
    elif typeStr == "int":
        strLua += str(jsonValue)+","
    elif typeStr == "str" or typeStr=="unicode":
        if fileName.find("translate") > -1:
            strLua += "\""+jsonValue.encode('utf8')+"\","
        else:
            strLua += "\""+str(jsonValue)+"\","
    elif typeStr == "float":
        strLua += str(jsonValue)+","
    
    #if index == 0:
    #    strLua+="}"
    return strLua

# 判断类型
def get_type_class(value):
    typeStr = str(type(value))
    return typeStr.replace("<type '","").replace("'>","")

# 获取所以的配置文件
def get_json_file_all_name(find_dir,all_json_file_name):
    list = os.listdir(find_dir)
    for li in list:
        filepath = os.path.join(find_dir,li)
        if os.path.isdir(filepath):
            get_json_file_all_name(filepath,all_json_file_name)
        elif os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            all_json_file_name[filename] = filepath

# 获取某各配置文件的所以数值
def getDicListByFileName(filename):
    out_json_file = open(filename)
    dic_list={}
    first = True
    while True:
        line = out_json_file.readline()
        if len(line) == 0:
            break
        decoded = json.loads(line)
        if type(decoded) == list:
            for e in decoded:
                for key,value in e.items():
                    dic_list[key] = value
            continue
            
        for key,value in decoded.items():
            dic_list[key] = value
    return dic_list

if __name__ == "__main__":
    config_info = {}
    config_info["current_dir"] = "."
    config_info["config_output_path"] = "other"
    config_info["config_input_path"] = "json"
    run(config_info)
    print "finish ok"
