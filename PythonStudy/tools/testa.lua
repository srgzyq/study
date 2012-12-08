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
--[[a={
    ["person"] ={
        "tongren",  
        "tongren",
    }
  }
--]]
--print(a["person"][1])
a={["srgzyq"]={["name"]={12,13,14,15,},},}
--print(a["srgzyq"]["name"][2])
--a={["srgzyq"]={["person"]={[0]={["key"]="test",["value"]=2000,},[1]={["key"]="playcrab",["value"]=1234,},},["age"]=12,["name"]="srgzyq",},}
--[ { ["key"] = "xxx",["value"]=100, } , { ["key"] = "xxx",["value"]=100, } , ]

---print(a["srgzyq"]["person"][0]["key"])
--print(a["person"][1]["key"])

--[[print(a["person"]["name"])
print(a["person"]["skill"]["lua"])
print(a["person"]["skill"]["python"])
print(a["chichi"]["hard"]["shenzhang"])
print(a["chichi"]["age"])
print(a["srgzyq"])
--]]
--a={["srgzyq"]={["name"]={["1"]={["chichi"]={["1"]="c",["2"]="d",},["srgzyq"]={["age"]=12,["time"]=1,},},},},}
--a={["person"]={["skill"]={["python"]=1,["lua"]=1,["as3"]=1,},["age"]=12,["name"]="srgzyq",},}
--[[a={
    ["srgzyq"]={
                ["name"]={
                    ["1"]={
                        ["chichi"]={["1"]="c",["2"]="d",},
                        ["srgzyq"]={["age"]=12,["time"]=1,},
                          },
                        },
                },
    }
--]]
a={["person"]={["srgzyq"]="name",["skill"]={["python"]=1,["lua"]=1,["as3"]=1,},["age"]=12,["chichi"]={["age"]=12,["hard"]={["shenzhang"]="pig",},},["name"]="srgzyq",},}
--print(a["srgzyq"]["name"]["1"]["srgzyq"]["age"])
print(a["person"]["skill"]["lua"])
