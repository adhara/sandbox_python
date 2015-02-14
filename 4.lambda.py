#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log10

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#map
print map(log10, nums)
print map(lambda x: x / 3, nums)

#filter
print filter(lambda x: x % 2, nums)

#reduce
print reduce(lambda x, y: x + y, nums)
print sum(nums)
print reduce(lambda x, y: x + y, filter(lambda x: x % 2, nums))

#zip1
from string import ascii_lowercase
print zip(ascii_lowercase, range(1, 100))
#zip2
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print zip(*matriz)

#list comprehension
print [x ** 2 for x in nums if x % 2] #map + filter

import itertools
#gerador infinito de list comprehension
a = ( x**2 for x in itertools.count(1) if x % 2 )
for i in range (100):
    print a.next()