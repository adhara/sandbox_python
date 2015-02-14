import math
import unittest

from t1_geraFib import fibGenerator
from t2_geraPrimos import geradorPrimos
from t3_bhaskara import raizes
from t4_contaLetras import contaLetras
from t5_geometria import *


class BhaskaraTest(unittest.TestCase):

    #t1
    def test_fibonacci(self):
        gera = fibGenerator()
        for i in range(10):
            a = gera.next()
        self.assertEqual(55, a)

    #t2
    def test_primos(self):
        gera = geradorPrimos()
        for i in range(10):
            a = gera.next()
        self.assertEqual(29, a)

    #t3
    def test_raizes_reais(self):
        self.assertEqual((-0.16, -1.74), tuple(map(lambda x: round(x, 2), raizes(123, 234, 34))))

    def test_unica_raiz(self):
        self.assertEqual((1, 1), raizes(1, -2, 1))

    def test_raizes_inteiras(self):
        self.assertEqual((1, -1), raizes(1, 0, -1))

    def test_raizes_complexas(self):
        self.assertEqual((1j, -1j), raizes(1, 0, 1))
    
    #t4    
    def test_letras(self):
        self.assertEqual(('r', 47), contaLetras('t4_contaLetras.py')[0])        

    #t5
    def test_comprimento_linha(self):
        a = Ponto(1, 1, 1)
        b = Ponto(2, 2, 2)        
        l = Linha(a, b)
        self.assertEqual(1.73, l.comp())
       
    def test_comprimento_linha_vazia(self):
        a = Ponto(1, 1, 1)
        b = Ponto(1, 1, 1)        
        l = Linha(a, b)
        self.assertEqual(0, l.comp())
        
    def test_area_triangulo(self):
        a = Ponto(0, 0, 0)
        b = Ponto(1, 0, 0)
        c = Ponto(0, 1, 0)
        t = Triangulo(a, b, c)
        self.assertEqual(0.50, t.area())
        
    def test_area_triangulo_colinear(self):
        a = Ponto(0, 0, 0)
        b = Ponto(1, 0, 0)
        c = Ponto(2, 0, 0)
        t = Triangulo(a, b, c)
        self.assertEqual(0, t.area())

if __name__ == '__main__':
    unittest.main()
