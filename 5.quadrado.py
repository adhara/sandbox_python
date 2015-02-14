#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Quadrado:
    def __init__(self, lado=1.0):
        self.lado = lado

    def get_lado():
        return self.lado
    def set_lado(lado=1.0):
        self.lado = lado
    lado = property(get_lado, set_lado)

    @property
    def area(self):
        return self.lado ** 2

if __name__ == '__main__':
    q = Quadrado()
    print q.lado
    q.lado = 3.0
    print q.lado
    print q.area