#!/usr/bin/env python
# -*- coding: utf-8 -*-

#a virgula determina uma tupla, nao o parenteses
a = 1,  # tupla de uma posição
b = 1   # inteiro comum
print a, b

#atribuindo estruturas em tuplas
lista = [range(1, 6), range(6, 11), range(11, 16), range(16, 21)]
for a, b, c, d, e in lista:
    print a, d

# ops em listas
l = ['Juliana', 'Ronald', 'Manu', 'Fernando']
l.sort()
l.reverse()
for i, nome in enumerate(l):
    print i+1, ' - ', nome

#fila e pilha
lista = ['a', 'b', 'c']
while lista:
    print 'Saiu ', lista.pop(0), ' e ficaram ', len(lista)
lista = ['a', 'b', 'c']
while lista:
    print 'Saiu ', lista.pop(-1), ' e ficaram ', len(lista)

# remove vs pop
lista = range(5)
lista.remove(3) #remove o numero 3
print lista
lista.pop(3) # remove o elemento na posição 3
print lista
    
#conjuntos não possuem elementos repetidos
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))

print s1.union(s2)
print s1.union(s2).difference(s3)
print s1.union(s2).intersection(s3)
if s1.issuperset([1, 2]):
    print 's1 inclui 1 e 2'
if s1.isdisjoint(s2):
    print 's1 e s2 não têm elementos em comum'
