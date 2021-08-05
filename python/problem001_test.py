#!/usr/bin/env python3

from unittest.case import TestCase
import problem001
import unittest

class TestProblem001(unittest.TestCase):
    def setUp(self):
        self.mult3 = problem001.multiples(3)

    def test_multiples_of_3_under_10_are_3_6_9(self):
        mult3_set = set(m if m < 10 else [self.mult3.close(), 3][1] for m in self.mult3)

        self.assertEqual(mult3_set, {3,6,9})