--require "luafile"
--require 'item'
--print(item["111011"]["description"])
--a={["person"]={["skill"]={["python"]="1",["lua"]="1",["as3"]="1",},["age"]="12",["chichi"]={["hard"]={["shenzhang"]="1",},},["name"]="srgzyq",},}

--[[a={
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
--]]
a={["srgzyq"]={["person"]={[0]={["key"]="test",["value"]=2000,},[1]={["key"]="playcrab",["value"]=1234,},},["age"]=12,["name"]="srgzyq",},}
--[ { ["key"] = "xxx",["value"]=100, } , { ["key"] = "xxx",["value"]=100, } , ]

print(a["srgzyq"]["person"][0]["key"])
--print(a["person"][1]["key"])

--[[print(a["person"]["name"])
print(a["person"]["skill"]["lua"])
print(a["person"]["skill"]["python"])
print(a["chichi"]["hard"]["shenzhang"])
print(a["chichi"]["age"])
print(a["srgzyq"])
--]]
