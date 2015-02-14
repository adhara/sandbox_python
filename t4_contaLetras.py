# -*- coding: utf-8 -*-

import string
import operator

def contaLetras(nomeArquivo):

    d = {k:0 for k in string.ascii_lowercase}   

    texto = file(nomeArquivo).read()
    for palavra in texto.split():
        for char in palavra:
            if char.lower() in string.ascii_lowercase:
                d[char.lower()] += 1

    #TODO: descobrir pq não funciona sorted(d, key=d.get, reverse=True)
    return sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)

if (__name__ == '__main__'):
    for letra, valor in contaLetras('t4_contaLetras.py'):
        print letra, valor