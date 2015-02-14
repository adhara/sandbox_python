#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

from math import degrees
from cmath import polar

for cpx in [3j, 1.5 + 1j, -2 -2j]:
    cpolar = polar(cpx)
    print 'Coord retangulares ', cpx
    print 'Coord polares ', cpolar
    print 'Amplitude ', abs(cpx)
    print 'Ângulo ', degrees(cpolar[1]), ' graus'


import random

l1 = []
l2 = []
l3 = []
for i in range(10):
    l1.append(random.choice(string.ascii_uppercase))
    l2.append(random.randrange(1, 11))
    l3.append(int(random.random() * 100))
print l1
print l2
print l3


from decimal import Decimal  # elimina problemas de arredondamento

tf = 5.0
td = Decimal ('5.0')
for i in range(50):
    tf -= 0.1
    td -= Decimal('0.1')

print ' Usando Float: ', tf
print ' Usando Decimal: ', td


from fractions import Fraction, gcd

f1 = Fraction('-2/3')
f2 = Fraction('3/4')
f3 = Fraction('0.25')
print f1, ',', f2, ',', f3
print 'Soma', f2 + f3
print gcd(300, 240)


a = string.ascii_letters #alfabeto completo
b = a[1:] + a[0] # cada letra shiftada para esquerda

msg = 'Esse texto será traduzido... Vai ficar bem estranho.'

# Cria uma tabela de tradução entre os caracteres de duas strings
# Os caracteres ausentes na tabela serão copiados para a saída
tab = string.maketrans(a, b)
print string.translate(msg, tab)


import calc # definido em calc.py

l = [17, 35, 42, 51, 19, 27]
print calc.media(l)


from os.path import getsize, getmtime
from time import localtime, asctime
import modutils

    mods = modutils.find('xml')
    for mod in mods:
        tm = asctime(localtime(getmtime(mod)))
        kb = getsize(mod) / 1024
        print '%s: (%d kbytes, %s)' % (mod, kb, tm)