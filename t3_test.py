import math
import unittest

from t3_bhaskara import raizes


class BhaskaraTest(unittest.TestCase):

    def test_raizes_reais(self):
        self.assertEqual((-0.16, -1.74), tuple(map(lambda x: round(x, 2), raizes(123, 234, 34))))

    def test_unica_raiz(self):
        self.assertEqual((1, 1), raizes(1, -2, 1))

    def test_raizes_inteiras(self):
        self.assertEqual((1, -1), raizes(1, 0, -1))

    def test_raizes_complexas(self):
        self.assertEqual((1j, -1j), raizes(1, 0, 1))


if __name__ == '__main__':
    unittest.main()
