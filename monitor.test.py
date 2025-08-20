class CalculatorTest(unittest.TestCase):
    def test_empty_string(self):
        ##Empty sting will return 0
        self.assertFalse(stringCalculator(' '))
    def test_single_value(self):
        ##Return the single value itself
        self.assertEqual(stringCalculator('3'),3)
        self.assertEqual(stringCalculator('47'),47)
        self.assertEqual(stringCalculator('123'),123)
    def test_double_value(self):
        ##Return sum when 2 numbers are passed
        self.assertEqual(stringCalculator('100,3'),103)
        self.assertEqual(stringCalculator('5,3'),8)
    def test_multiple_value(self):
        ##Return sum when unknown number of inputs are passed
        self.assertEqual(stringCalculator('1,2,3'),6)
        self.assertEqual(stringCalculator('1,2,3,4,5,6,7,8,9,10'),55)
    def test_newline_in_value(self):
        ##Return sum when newline is separating the numbers
        self.assertEqual(stringCalculator('1\n2,3'),6)
        self.assertEqual(stringCalculator('5\n10\n15'),30)
        self.assertFalse(stringCalculator('1,\n'))
    def test_custom_delimiters_in_value(self):
        ##Return sum when Single-character custom delimiter is separating the numbers
        self.assertEqual(stringCalculator('//;\n1;2'),3)
        self.assertEqual(stringCalculator('//|\n5|10|15'),30)
        ##Return sum when Multi-character custom delimiter is separating the numbers
        self.assertEqual(stringCalculator('//[***]\n1***2***3'),6)
    def test_negative_values(self):
        ##Throw exceptions when negative number is parsed
        with self.assertRaises(ValueError) as context:
            stringCalculator('-3')
        self.assertIn("negatives not allowed: -3", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            stringCalculator('-3,4,-8')
        self.assertIn("negatives not allowed: -3,-8", str(context.exception))

       # self.assertEqual(stringCalculator('-3,4,-8'),'negatives not allowed: -3,-8')
    def test_greater_than_thousand_value(self):
        ##Numbers bigger than 1000 are ignored
        self.assertEqual(stringCalculator('4,1002'),4)
        self.assertEqual(stringCalculator('9,1,1000'),10)
    def test_complex_delimiters(self):
        self.assertEqual(stringCalculator("//[abc]\n1abc2abc3"),6)
        self.assertEqual(stringCalculator("//[***][%%]\n1***2%%3"),6)
