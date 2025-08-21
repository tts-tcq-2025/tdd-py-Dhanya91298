# TDD Driven StringCalculator

Build a StringCalculator functionality that can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.

> DO NOT jump into implementation! Read the example and the starting task below.

- For an empty string it will return 0
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: “1\n2,3” (will equal 6)
  - the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
- Support different delimiters : to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
- Calling Method with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. if there are multiple negatives, show all of them in the exception message.
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

## Tasks



Establish quality parameters:

- Ensure  maximum complexity (CCN) per function == 3

- Ensure 100% line and branch coverage at every step

  

Start Test-driven approach

1. Write the smallest possible failing test: give input `"" assert output to be 0 ` .
2. Write the minimum amount of code that'll make it pass.
3. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.


# Test specification
Feature: String Calculator

  Scenario: Empty string input returns 0
    Given the input is ""
    When I calculate the sum
    Then the result should be 0

  Scenario: Single value input returns the same value itself
    Given the input is "5"
    When I calculate the sum
    Then the result should be 5

  Scenario: Return sum when 2 numbers are passed separated by comma
    Given the input is "2,3"
    When I calculate the sum
    Then the result should be 5

  Scenario: Return sum when 2 numbers are passed separated by newline
    Given the input is "2\n3"
    When I calculate the sum
    Then the result should be 5

  Scenario: Return sum when unknown number of inputs are passed separated by comma
    Given the input is "1,2,3,4,5"
    When I calculate the sum
    Then the result should be 15

  Scenario: Return sum when unknown number of inputs are passed separated by newline
    Given the input is "1\n2\n3\n4\n5"
    When I calculate the sum
    Then the result should be 15

  Scenario: Return sum when custom delimiter separates the numbers
    Given the input is "//;\n1;2;3"
    When I calculate the sum
    Then the result should be 6

  Scenario: Throw exception when negative number is parsed
    Given the input is "2,-4,3"
    When I calculate the sum
    Then an exception should be thrown with message "negatives not allowed: -4"

  Scenario: Ignore numbers greater than or equal to 1000
    Given the input is "2,1000,1001,6"
    When I calculate the sum
    Then the result should be 1008

  Scenario: Return False for invalid input
    Given the input is "1,\n"
    When I calculate the sum
    Then the result should be False

