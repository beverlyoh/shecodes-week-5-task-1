import unittest
from creditCard import calculate_credit_card_number_check_digit, validate_credit_card_number_check_digit

class CreditCardTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_calculate_credit_card_number_check_digit(self):
        self.assertEqual(calculate_credit_card_number_check_digit('542418027979176'), '5')

    def test_second_calculate_credit_card_number_check_digit(self):
        self.assertEqual(calculate_credit_card_number_check_digit('601100099301097'), '8')

    def test_valid_validate_credit_card_number_check_digit(self):
        self.assertEqual(
            validate_credit_card_number_check_digit('5424180279791765'),
            'This is a valid credit card number.'
        )
    
    def test_invalid_validate_credit_card_number_check_digit(self):
        self.assertEqual(
            validate_credit_card_number_check_digit('5424180279791762'),
            'This is an invalid credit card number.'
        )



if __name__ == "__main__":
    tests = unittest.TestSuite((
        unittest.makeSuite(CreditCardTest)
    ))
    unittest.TextTestRunner().run(tests)