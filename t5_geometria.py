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
        return round(math.sqrt((dx ** 2 + dy ** 2 + dz ** 2)), 2)
    
    def __repr__(self):
        return '%s => %s' % (self.a, self.b)

        
class Triangulo(object):
    def __init__(self, a, b, c):    
        self.a = a
        self.b = b
        self.c = c
    
    def lados(self):        
        return Linha(self.a, self.b).comp(), Linha(self.b, self.c).comp(), Linha(self.c, self.a).comp()
        
    #Solução retirada do livro Python para desenvolvedores (Luiz Eduardo Borges)
    #Teorema de Heron
    def area(self):                
        lados = self.lados()
        p = sum(lados) / 2
        return round(math.sqrt(p * (p - lados[0]) * (p - lados[1]) * (p - lados[2])), 2)
        
    def __repr__(self):
        return '%s => %s => %s)' % (self.a, self.b, self.c)
        
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