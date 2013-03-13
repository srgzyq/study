#coding=utf-8

def parseStrContent(value):
    strValue = str(value)
    if strValue == None or strValue.find("[") < 0 or strValue.find("]") < 0 or strValue.find("--") > -1:
        return -1

    strValue = "".join(str(value).split()) 

    keyStartIndex = strValue.index("[")
    keyEndIndex = strValue.index("]")

    keyStr = strValue[keyStartIndex+1:keyEndIndex]

    contStartIndex = strValue.index("=")+2
    contEndIndex = len(strValue)-2
    contStr = strValue[contStartIndex:contEndIndex]

    return keyStr,contStr


def testParseStrContent():
    strValue = None
    result = parseStrContent(strValue)
    assert(result == -1)


if __name__ == "__main__":
    dicData = {}
    words="[\"DuomijiGetCanZhangDes\"] =  \"恭喜掌  门，果然在对手身上搜出了#1，距离获得#2又近了一步！\","
    #wordTows="\"DuomijiGetCanZhangDes\"] =  \"恭喜掌  门，果然在对手身上搜出了#1，距离获得#2又近了一步！\","
    #noBlank="".join(words.split())

    #noBlank="".join(words.split())
    keyStr,contStr = parseStrContent(words)
    print "key="+keyStr+" content="+contStr
    dicData[keyStr] = contStr
    print dicData


    wordsThree="[\"IntroCanpianPopupTitle\"] =\"武功残章介绍\","
    keyStr3,contStr3 = parseStrContent(wordsThree)
    print "key="+keyStr3+" content="+contStr3
    dicData[keyStr3] = contStr3
    print dicData



   
    dicData1 = {}   
    wordsTwo="[\"IntroCanpianPopupTitle\"] =\"武功残章介绍\","
    keyStr1,contStr1 = parseStrContent(wordsTwo)
    print "key="+keyStr1+" content="+contStr1
    dicData1[keyStr1] = contStr1
    print dicData1

    if dicData[keyStr3] == dicData1[keyStr1]:
        print "ok is equip"
    #print noBlank
    #testParseStrContent()
