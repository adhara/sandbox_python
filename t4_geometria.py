# -*- coding: utf-8 -*-

import math

class Ponto(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '(%2.1f, %2.1f, %2.1f)' % (self.x, self.y, self.z)

        
class Linha(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comp(self):
        dx = self.b.x - self.a.x
        dy = self.b.y - self.a.y
        dz = self.b.z - self.a.z
        return round(math.sqrt((dx ** 2 + dy ** 2 + dz ** 2)), 1)
    
    def __repr__(self):
        return '%s => %s' % (self.a, self.b)

        
class Triangulo(object):
    def __init__(self, a, b, c):    
        self.a = a
        self.b = b
        self.c = c
        
    # solução retirada do livro Python para desenvolvedores (Luiz Eduardo Borges)
    def area(self):        
        ab = Linha(a, b).comp()
        bc = Linha(b, c).comp()
        ca = Linha(c, a).comp()

        p = (ab + bc + ca) / 2.

        #Teorema de Heron 
        return round(math.sqrt(p * (p - ab) * (p - bc) * (p - ca)), 1)
        
if __name__ == '__main__':
    a = Ponto(2, 3, 1)
    b = Ponto(5, 1, 4)
    c = Ponto(4, 2, 5)
    l = Linha(a, b)
    t = Triangulo(a, b, c)
    print 'Ponto A:', a
    print 'Ponto B:', b
    print 'Ponto C:', c
    print 'Linha:', l
    print 'Comprimento:', l.comp()
    print 'Triangulo:', t
    print 'Area:', t.area()