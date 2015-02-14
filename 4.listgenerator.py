#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

def gerador(fn='.'):
        
    try:
        for linha in open(fn, 'r'):
            pLinha = linha.strip()
            if pLinha:
                yield(pLinha.split(','))
    except:
        print 'Erro na leitura do arquivo'
        raise SystemExit

if __name__ == '__main__':

    for tupla in gerador('data/testetuplas.txt'):
        print tupla
