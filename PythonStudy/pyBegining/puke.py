#puke
# _*_ coding: utf-8 _*_
from pprint import pprint
from random import shuffle

#创建扑克
value = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()

deck = ['%s of %s' % (v, s) for v in value for s in suits]
#pprint(deck[:])

shuffle(deck)
pprint(deck[:])

while deck: raw_input(deck.pop())
