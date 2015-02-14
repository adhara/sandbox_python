#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import itertools

def ls(path='.'):

    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in ls(fn):
                yield f
        else:
            yield fn

if __name__ == '__main__':
    
    for fn in ls('c:/temp'):
        print fn
    
    #itertools
    cont = itertools.count(1)           #gerador do contador para interromper o loop
    cicl = itertools.cycle(range(3))  #gerador que define o ciclo
    while cont.next() < 10:
        print cicl.next()
    
    #gerador infinito de lambda
    a = ( x**2 for x in itertools.count(1) if x % 2 ) 
    for i in range (100):
        print a.next()