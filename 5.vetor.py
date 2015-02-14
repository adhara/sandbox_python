#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vetor(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y) + ', '+ str(self.z)

    def __add__(self, v2):
        return Vetor(self.x + v2.x, self.y + v2.y, self.z + v2.z)

    def __sub__(self, v2):
        return Vetor(self.x - v2.x, self.y - v2.y, self.z - v2.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2  + self.z ** 2) ** 0.5

    def __mul__(self, other) :
        if isinstance(other, Vetor):
            x1 = self.y * other.z - other.y * self.z
            y1 = self.z * other.x - other.z * self.x
            z1 = self.x * other.y - other.x * self.y
            return Vetor(x1, y1, z1)
        else:
            return Vetor(self.x * other, self.y * other, self.z * other)
    
    def produto_escalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

if __name__ == '__main__':
    v1 = Vetor(2, 3, 4)
    v2 = Vetor(1., 2., 3.)
    
    print v1 + v2
    print v1 - v2
    print abs(v2)
    print v1.produto_escalar(v2)
    print v2 * v1
    print v2 * 2
    print v2 * 2.0