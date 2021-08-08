#!/usr/bin/env python3

import problem003
import unittest

class TestProblem003(unittest.TestCase):
    def setUp(self):
        self.primes = tuple(problem003.reversed_eratosthenes(1_000_000_000))
    
    def test_if_each_element_is_not_divisible_by_others(self):
        for i,p in enumerate(self.primes):
            for q in self.primes[i+1::]:
                self.assertNotEqual(p%q, 0)
    