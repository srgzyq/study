-- lua 十六进制转化
a = 12
b=string.format("%x",a)
print("十六进制:",b)
print(string.len(b))

-- lua 异或
local floor = math.floor
function bxor (a,b)
  local r = 0
    for i = 0, 31 do
        local x = a / 2 + b / 2
        if x ~= floor (x) then
            r = r + 2^i
        end
        a = floor (a / 2)
        b = floor (b / 2)
        end
    return r
end

c=bxor(15,23)
print("15 ^ 23 异或:",c)

-- lua 字符串截取
now="1353921758"
last = string.len(now)
print(last)
start = last - 2
print("start:",start)
str=string.sub(now,start,-1)
print(now.." get sub string:",str)
