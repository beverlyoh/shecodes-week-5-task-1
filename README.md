# Week 5 Task 1

Your task is to implement the algorithms to calculate and validate check digits for different kinds of barcodes.

You must calculate and validate the check digit for:

- Credit Cards

And choose one or more of:

- ISBN-10 Books
- ISBN-13 Books
- GTIN-13 Product Codes

To help you get started:

- How to calculate ISBN-10 check digits: https://isbn-information.com/the-10-digit-isbn.html
- How to calculate ISBN-13 check digits https://isbn-information.com/check-digit-for-the-13-digit-isbn.html
- A list of test credit card numbers https://support.paya.com/44616-sage-virtual-terminal-not-done/315930-list-of-test-card-numbers
- The algorithm used to calculate the check digit for credit card numbers https://en.wikipedia.org/wiki/Luhn_algorithm



## GTIN-13 check digits are calculated as follows:

1. Multiply every second digit by 3, and every other digit by 1.
2. Add up all the multiplied numbers.
3. You can now get the check digit by working out what number would have to be added to the sum in order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.


## ISBN-10 check digits are calculated as follows:

1. Multiply the first digit in the barcode by 10. Add the result to the sum.
2. Multiply the second digit in the barcode by 9. Add the result to the sum.
3. Multiply the third digit in the barcode by 8. Add the result to the sum.
4. ....
5. Multiply the last number in the barcode by 1. Add the result to the sum.
6. Calculate the remainder of the sum when divided by 11.
7. The check digit is 11 minus the remainder of the result in step 6 when divided by 11. If the check digit is 10, it is replaced with an ‘X’.


## Running your program:

If I provide this input:

```
print(calculate_gtin13_barcode_check_digit('940055061977'))
```

The output I expect is:

```
5
```

If I provide this input:

```
print(validate_gtin13_barcode_check_digit('9400550619775'))
```

The output I expect is:

```
This is a valid gtin13 barcode.
```


The only thing that should change is the name of the function dependant on the type of barcode (i.e. gtin13, isbn10, isbn13 or credit_card).



Note: obviously your code should handle more test cases than just the two I provided, these are just examples to demonstrate how I expect to be able to call your code). 


## Testing

I have provided 4 test files, one for each algorithm.
To use these files you can use the following commands:

```
python3 test_credit_card.py
python3 test_gtin13.py
python3 test_isbn10.py
python3 test_isbn13.py
```

The test files assume:
- Your functions are named:
    - `calculate_credit_card_number_check_digit()`
    - `validate_credit_card_number_check_digit()`
    - `calculate_gtin13_barcode_check_digit()`
    - `validate_gtin13_barcode_check_digit()`
    - `calculate_isbn10_barcode_check_digit()`
    - `validate_isbn10_barcode_check_digit()`
    - `calculate_isbn13_barcode_check_digit()`
    - `validate_isbn13_barcode_check_digit()`
- Each algorithm has it's own file, named:
    - `creditCard.py`
    - `gtin13.py`
    - `isbn10.py`
    - `isbn13.py`
- That each algorithm's file is in the same folder as its corresponding test file.

### Troubleshooting
Here are some errors you may encounter and what they mean:

1. Module Not Found

`ModuleNotFoundError: No module named 'gtin13'`

Check you have named the gtin13 file and function correctly, and that the test file is in the same folder.

2. Assertion Errors

```
======================================================================
FAIL: test_calculate_gtin13_barcode_check_digit (__main__.GTIN13Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_gtin13.py", line 11, in test_calculate_gtin13_barcode_check_digit
    self.assertEqual(calculate_gtin13_barcode_check_digit('940055061977'), '0')
AssertionError: 5 != '0'
- 5
+ 0
```
`test_calculate_gtin13_barcode_check_digit` was expecting your `calculate_gtin13_barcode_check_digit` function to return the string `0` but it got the integer `5`.

```
======================================================================
FAIL: test_valid_validate_gtin13_barcode_check_digit (__main__.GTIN13Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_gtin13.py", line 22, in test_valid_validate_gtin13_barcode_check_digit
    'This is a valid gtin13 barcode.'
AssertionError: 'This is an invalid gtin13 barcode.' != 'This is a valid gtin13 barcode.'
- This is an invalid gtin13 barcode.
?          ^^^^
+ This is a valid gtin13 barcode.
? 
```
`test_valid_validate_gtin13_barcode_check_digit` was expecting your `validate_gtin13_barcode_check_digit` function to return `This is a valid gtin13 barcode.` but it got `This is an invalid gtin13 barcode.`
