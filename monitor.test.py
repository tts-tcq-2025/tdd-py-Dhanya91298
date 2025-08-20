import unittest
from StringCalculator import stringCalculator

class CalculatorTest(unittest.TestCase):
    def test_empty_string(self):
       self.assertFalse(stringCalculator('1 2'))
        


if __name__ == '__main__':
  unittest.main()
