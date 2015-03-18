#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hello(object):
    def hello(self,name='world'):
        print('Hello, %s.' % name)

"""
' a test module'

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()
"""

'''# print absolute value of an integer:
a = -100
if a >= 0:
    print a
else:
    print -a

name = raw_input('please enter you name:')
print 'hello,', name
'''


