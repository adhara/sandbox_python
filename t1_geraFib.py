# -*- coding: utf-8 -*-

def fibGenerator():
    """
    Gerador de sequência de Fibonacci
    """
    x = 0
    y = 1
    while True:
        x, y = y, x + y
        yield x
        
if __name__ == "__main__":
    gera = fibGenerator()
    for i in range(0, 12):
        print gera.next()