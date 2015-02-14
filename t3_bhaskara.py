# -*- coding: utf-8 -*-

from math import sqrt

def raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    a2 = 2 * a
    mi = sqrt(abs(delta))
    #se delta for negativo, as raízes são complexas	
    if delta < 0:
        #raiz(-x) = raiz (x * -1) = i * raiz(x)
        mi = complex(0, mi)

    return (-b + mi) / a2, (-b - mi) / a2
    
    
if __name__ == '__main__':

    print raizes(1, -2, 1)
    print raizes(1, 0, 1)