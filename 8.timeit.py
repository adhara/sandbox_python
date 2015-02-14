#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit

cod = '''s = []
for i in xrange(1, 1001):
    s.append(i ** 2)
'''
print timeit.Timer(cod).timeit()
# Com Generator Expression
cod = 'list(x ** 2 for x in xrange(1, 1001))'
print timeit.Timer(cod).timeit()
# Com List Comprehesion
cod = '[x ** 2 for x in xrange(1, 1001)]'
print timeit.Timer(cod).timeit()