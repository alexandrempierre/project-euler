#!/usr/bin/env python3

from unittest.case import TestCase
import problem002
import unittest

class TestProblem002(unittest.TestCase):
    def setUp(self):
        self.fibo = problem002.fibonacci()
        self.even_fibo = problem002.even_fibonacci()

    def test_first_thousand_fibonacci_terms(self):
        f0, f1 = 0, 1
        for i,f in enumerate(self.fibo):
            if i >= 1_000:
                self.fibo.close()
            
            self.assertEqual(f, f0+f1)
            f0, f1 = f1, f


    def test_first_thousand_even_fibonacci_terms(self):
        for i,f in enumerate(self.even_fibo):
            if i >= 1_000:
                self.even_fibo.close()
            
            self.assertEqual(f % 2, 0)