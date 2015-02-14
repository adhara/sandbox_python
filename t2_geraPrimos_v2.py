# -*- coding: utf-8 -*-

import math
import timeit

def geradorPrimos():
    n = 2
    primos = [2]
    while True:
        for i in filter(lambda x: x > int(math.sqrt(n)), primos):
            if not n % i:
                break   # tem pelo menos um divisor
        else:
            primos.append(n)
            yield n
        n += 1


if __name__ == '__main__':
    gera = geradorPrimos()
    for i in range(1000):
        print gera.next(),