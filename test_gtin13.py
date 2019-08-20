import unittest
from gtin13 import calculate_gtin13_barcode_check_digit, validate_gtin13_barcode_check_digit


class GTIN13Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
    
    def test_calculate_gtin13_barcode_check_digit(self):
        self.assertEqual(calculate_gtin13_barcode_check_digit('940055061977'), '5')
    
    def test_second_calculate_gtin13_barcode_check_digit(self):
        self.assertEqual(calculate_gtin13_barcode_check_digit('932769300242'), '7')

    def test_calculate_gtin13_barcode_check_digit_where_check_digit_is_0(self):
        self.assertEqual(calculate_gtin13_barcode_check_digit('735005385004'), '0')

    def test_valid_validate_gtin13_barcode_check_digit(self):
        self.assertEqual(
            validate_gtin13_barcode_check_digit('7350053850040'),
            'This is a valid gtin13 barcode.'
        )
    
    def test_invalid_validate_gtin13_barcode_check_digit(self):
        self.assertEqual(
            validate_gtin13_barcode_check_digit('7350053850042'),
            'This is an invalid gtin13 barcode.'
        )



if __name__ == "__main__":
    tests = unittest.TestSuite((
        unittest.makeSuite(GTIN13Test)
    ))
    unittest.TextTestRunner().run(tests)