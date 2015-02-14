#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fibdoctest
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        
    def test0(self):
        self.assertEqual(fibdoctest.fib(0), 1)
        
    def test1(self):
        self.assertEqual(fibdoctest.fib(1), 1)

    def test10(self):
        self.assertEqual(fibdoctest.fib(10), 89)
        
    def testseq(self):
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for x, y in zip(fibs, [ fibdoctest.fib(x) for x in self.seq ]):
            self.assert_(x is y)
            
    def testtype(self):
        self.assertRaises(TypeError, fibdoctest.fib, '')


if __name__ == '__main__':
    unittest.main()