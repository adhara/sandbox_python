#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

# Criando arranjos
print 'Arranjo criado a partir de uma lista:'
a = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print a

print 'Arranjo criado a partir de um intervalo:'
z = arange(0., 4.5, .5)
print z
# [ 0. 0.5 1. 1.5 2. 2.5 3. 3.5 4. ]

print a + z

a.shape = 3, 3
print a
print a[1, 1]
print a[1][1]

lista= [[3,4,5], [6, 7, 8], [9, 0, 1]]
Z = matrix(lista)
print 'Z'
print Z
print 'Z.T'
print Z.T
print 'Z.I'
print Z.I

Q, R = linalg.qr(Z)

print 'decomposição linear'
print Q
print R

