#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
    """
    Fibonacci da pior forma
    """
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1

def html_rgb(color='#000000'): #000000 é um valor default, se a funcção for chamada sem parâmetro
    """
    Recebe um valor em HTML no formato #xxxxxx
    e retorna uma tupla com os valores das componentes r, g e b em decimais
    """
    if color.startswith('#'):
        color = color[1:]
        
    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b

def cels_fahr(tempc=0.0):
    """
    Recebe um valor em celsius
    e retorna o valor em fahrenheit
    """
    return round(tempc * 9.0 / 5.0 + 32.0, 2)

def fahr_cels(tempf=0.0):
    """
    Recebe um valor em fahrenheit
    e retorna o valor em celsius
    """
    return round(5.0 * (tempf - 32.0)/ 9.0, 2)

if __name__ == '__main__':

    for i in range(0, 6):
        print i, ' - ', fibonacci(i)

    print html_rgb('#435354')
    print html_rgb()

    print cels_fahr(123.0)
    print cels_fahr(253.4)