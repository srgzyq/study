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

'''
    罗马字符百位数效验
    罗马字符有四种可能，CM， CD ，（零到三次出现C字符，D,后面跟零到三个C字符）合并为(一个可选字符D,加上零到3个字符C)
'''

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
