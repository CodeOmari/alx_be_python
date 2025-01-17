import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTests(unittest.TestCase):
    #arrange
    def setUp(self):
        """Set up SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """test the addition method"""
        self.assertEqual(self.calc.add(5,2), 7)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(-5,-4), -9)
    
    def test_subtraction(self):
        "test the subtraction method"
        self.assertEqual(self.calc.subtract(5,2), 3)
        self.assertEqual(self.calc.subtract(-1,1), -2)
        self.assertEqual(self.calc.subtract(1,-1), 2)
        self.assertEqual(self.calc.subtract(-1,-1), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,2),10)
        self.assertEqual(self.calc.multiply(-1,1), -1)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(-1,-1), 1)
    
    def test_division(self):
        """testing for normal division"""
        self.assertEqual(self.calc.divide(4,2), 2)
        self.assertEqual(self.calc.divide(-4,2), -2)
        self.assertEqual(self.calc.divide(4,-2), -2)
        """test that dividing by zero returns None"""
        self.assertEqual(self.calc.divide(10,0), None)
        self.assertEqual(self.calc.divide(-10, 0), None)
   

if __name__ == "__main__":
    unittest.main()