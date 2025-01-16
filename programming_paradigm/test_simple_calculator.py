import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 0), None)  # Test division by zero
        self.assertEqual(self.calc.divide(0, 0), None)  # Test zero divided by zero

    def test_edge_cases(self):
        """Test edge cases for large numbers and floating points."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.subtract(5.5, 3.2), 2.3)
        self.assertAlmostEqual(self.calc.multiply(2.1, 3.3), 6.93, places=2)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=4)
        self.assertAlmostEqual(self.calc.divide(1e6, 1e3), 1e3)

if __name__ == "__main__":
    unittest.main()



