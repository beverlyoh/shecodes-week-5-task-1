import unittest
from isbn10 import calculate_isbn10_barcode_check_digit, validate_isbn10_barcode_check_digit


class ISBN10Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
    
    def test_calculate_isbn10_barcode_check_digit(self):
        self.assertEqual(calculate_isbn10_barcode_check_digit('188879997'), '8')

    def test_second_calculate_isbn10_barcode_check_digit(self):
        self.assertEqual(calculate_isbn10_barcode_check_digit('212345680'), '2')

    def test_calculate_isbn10_barcode_check_digit_where_check_digit_is_x(self):
        self.assertEqual(calculate_isbn10_barcode_check_digit('123456789'), 'X')

    def test_valid_validate_isbn10_barcode_check_digit(self):
        self.assertEqual(
            validate_isbn10_barcode_check_digit('1888799978'),
            'This is a valid isbn10 barcode.'
        )
    
    def test_invalid_validate_isbn10_barcode_check_digit(self):
        self.assertEqual(
            validate_isbn10_barcode_check_digit('188879997X'),
            'This is an invalid isbn10 barcode.'
        )


if __name__ == "__main__":
    tests = unittest.TestSuite((
        unittest.makeSuite(ISBN10Test)
    ))
    unittest.TextTestRunner().run(tests)