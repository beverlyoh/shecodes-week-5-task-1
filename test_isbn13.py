import unittest
from isbn13 import calculate_isbn13_barcode_check_digit, validate_isbn13_barcode_check_digit


class ISBN13Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_calculate_isbn13_barcode_check_digit(self):
        self.assertEqual(calculate_isbn13_barcode_check_digit('978174266046'), '2')

    def test_second_calculate_isbn13_barcode_check_digit(self):
        self.assertEqual(calculate_isbn13_barcode_check_digit('978071485726'), '8')

    def test_valid_validate_isbn13_barcode_check_digit(self):
        self.assertEqual(
            validate_isbn13_barcode_check_digit('9781742660462'),
            'This is a valid isbn13 barcode.'
        )
    
    def test_invalid_validate_isbn13_barcode_check_digit(self):
        self.assertEqual(
            validate_isbn13_barcode_check_digit('9781742660461'),
            'This is an invalid isbn13 barcode.'
        )


if __name__ == "__main__":
    tests = unittest.TestSuite((
        unittest.makeSuite(ISBN13Test)
    ))
    unittest.TextTestRunner().run(tests)