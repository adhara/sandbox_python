#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path

temp = open('temp.txt', 'w')
for i in range(100):
    temp.write('%03d\n' % i)
temp.close()

temp = open('temp.txt')
for x in temp:
    print x,
temp.close()


fn = raw_input('Nome do arquivo: ').strip()
if not os.path.exists(fn):
    print 'Tente outra vez...'
    sys.exit()
    
for i, s in enumerate(open(fn)):    #numera as linhas do arquivo
    print i + 1, s,