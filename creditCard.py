# Credit Card check digits calculate
def calculate_credit_card_number_check_digit(cardNum):
    codeList = list(cardNum[::-1])
    double = 0
    total = 0
    for i in list(range(0,len(codeList))):
        if i % 2 == 0: # if even
            double = int(codeList[i]) * 2
            if double > 9:
                total += (double - 9)
            else:
                total += double
        else: # if odd
            total += int(codeList[i]) # add as is
    total = str(total * 9)
    return str((total[(len(total) - 1)]))

# print(calculate_credit_card_number_check_digit('401200003333002')) #6
# print(calculate_credit_card_number_check_digit('549974000000005')) #7

# Credit Card check digits validate
def validate_credit_card_number_check_digit(cardNum):
    checkDigit = int(cardNum[(len(cardNum) - 1)])
    calcDigit = int(calculate_credit_card_number_check_digit(cardNum[:(len(cardNum) - 1)]))
    if checkDigit == 0 and calcDigit == 10:
        return ('This is a valid credit card number.')
    elif checkDigit != 0 and calcDigit == checkDigit:
        return ('This is a valid credit card number.')
    else:
        return ('This is an invalid credit card number.')

# print(validate_credit_card_number_check_digit('4012000033330026')) # test valid
# print(validate_credit_card_number_check_digit('5499740000000057')) # test
