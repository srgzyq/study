#coding=utf-8

import re

'''
   罗马字符千位效验
'''
pattern = '^M?M?M?$'
print re.search(pattern,'M')
print re.search(pattern,'MM')
print re.search(pattern,'MMM')
print re.search(pattern,'MMMM')
print ''

'''
    方法二
'''
print 'function two'
pattern = '^M{0,3}$'
print re.search(pattern,'M')
print re.search(pattern,'MM')
print re.search(pattern,'MMM')
print re.search(pattern,'MMMM')
print ''



'''
    罗马字符百位数效验
    罗马字符有四种可能，CM， CD ，（零到三次出现C字符，D,后面跟零到三个C字符）合并为(一个可选字符D,加上零到3个字符C)
'''

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print re.search(pattern,'MCM')
print re.search(pattern,'MD')
print re.search(pattern,'MMMCCC')
print re.search(pattern,'MCMM')
print re.search(pattern,'')


'''
    罗马字符的千百十个位 
'''
print '千百十个位:'
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print re.search(pattern,'MDLV')


'''
松散表达,内带注释
'''
print '松散表达,内带注释'
pattern = """
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """
print re.search(pattern,'M', re.VERBOSE)

'''
电话号码匹配
'''
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
print phonePattern.search('work 1-(800) 555.1212 #1234').groups()  
print phonePattern.search('800-555-1212').groups() 

