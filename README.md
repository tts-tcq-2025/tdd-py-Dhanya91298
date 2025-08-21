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
# String Calculator Specification

## Rules & Expected Behavior

| **Scenario**                                      | **Input**        | **Expected Output**                     |
|---------------------------------------------------|------------------|-----------------------------------------|
| Empty string input returns 0                      | `""`             | `0`                                     |
| Single value input returns the same value itself  | `"5"`            | `5`                                     |
| Sum when 2 numbers separated by comma             | `"2,3"`          | `5`                                     |
| Sum when 2 numbers separated by newline           | `"2\n3"`         | `5`                                     |
| Sum when unknown numbers separated by comma       | `"1,2,3,4,5"`    | `15`                                    |
| Sum when unknown numbers separated by newline     | `"1\n2\n3\n4\n5"`| `15`                                    |
| Sum with custom delimiter (single/multi-char)     | `"//;\n1;2;3"`   | `6`                                     |
| Throw exception on negative numbers               | `"2,-4,3"`       | Exception: `"negatives not allowed: -4"`|
| Ignore numbers >= 1000                            | `"2,1000,1001,6"`| `1008`                                  |
| Return False for invalid input                    | `"1,\n"`         | `False`                                 |
