# -*- coding: utf-8 -*-

import math

def geradorPrimos():
    n = 2
    while True:
        for i in range(2, int(math.sqrt(n)) + 1):
            if not n % i:
                break    # tem pelo menos um divisor
        else:
            yield n
        n += 1

if __name__ == '__main__':
    gera = geradorPrimos()
    for i in range(1000):
        print gera.next(),