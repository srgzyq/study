'''try:
    print 'try...'
    r = 10 / 2
    print 'result:',r
except ZeroDivisionError,e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
    finally:
        print 'fianlly...'

main()
