#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path

def filestat(fn):
    
    if not os.path.exists(fn):
        print 'Tente outra vez...'
        sys.exit()

    lines = words = chars = 0
    for linha in open(fn, 'r'):
        lines += 1
        chars += len(linha)
        if linha.strip():
            words += len(linha.split())
        
    return lines, words, chars

if __name__ == '__main__':
    
    fn = raw_input('Nome do arquivo: ').strip()
    print filestat(fn)
