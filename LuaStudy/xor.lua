---- tools 异或
function bxor(a,b)
    local floor = math.floor
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

d=5.122*1000000
c=bxor(d,1234567890)
print(c)
f=bxor(c,1234567890)
print(f)
