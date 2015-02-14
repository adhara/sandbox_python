#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.etree.ElementTree import Element, ElementTree

# writes elements to file

root = Element('Animal')
canino = Element('Canino')
primata = Element('Primata')
felino = Element('Felino')
cachorro = Element('Cachorro')
valente = Element('Valente', raca='Labrador', cor='Mel')
humano = Element('Humano')
lobo = Element('Lobo')
root.append(canino)
root.append(primata)
root.append(felino)
canino.append(cachorro)
canino.append(lobo)
primata.append(humano)
cachorro.append(valente)
ElementTree(root).write('data/animais.xml')

# reads elements from file

tree = ElementTree(file='data/animais.xml')
root = tree.getroot()

# lists all nodes under root
print root.getchildren()

# finds the dog and prints its attributes
canino = root.find('Canino')
cachorro = canino.find('Cachorro')
valente = cachorro.find('Valente')
print valente.tag, valente.attrib

# removes the intruder
root.remove(root.find('Felino'))
print root.getchildren()
