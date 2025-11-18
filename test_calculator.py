# https://github.com/Gautampillai/lab11-GP-PS
# Partner 1: Gautam Pillai
# Partner 2: Priya Schramm

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, 5), 3)

    def test_subtract(self):
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(5, 2), 3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,3), 3.0)
        self.assertEqual(mul(1, 0), 0.0)
        self.assertAlmostEqual(mul(-4.0, 0.25000001), -1.0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1,19),19.0)
        self.assertEqual(div(2, -3), -1.5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 20)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(3, 27), 3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1, 10)
        with self.assertRaises(ValueError):
            log(1, -10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(6, 8), 10.0)
        self.assertEqual(hypotenuse(-4, -3), 5.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-25)
        self.assertEqual(square_root(25),5.0)
        self.assertAlmostEqual(square_root(3),1.7320508)

if __name__ == "__main__":
    unittest.main()