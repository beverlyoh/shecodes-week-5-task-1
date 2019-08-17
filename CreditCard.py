# Credit Card check digits calculate
def calculate_creditcard_number_check_digit(cardNum):
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
    return int((total[(len(total) - 1)]))

print(calculate_creditcard_number_check_digit('401200003333002')) #6
print(calculate_creditcard_number_check_digit('549974000000005')) #7

# Credit Card check digits validate
def validate_creditcard_number_check_digit(cardNum):
    checkDigit = int(cardNum[(len(cardNum) - 1)])
    calcDigit = calculate_creditcard_number_check_digit(cardNum[:(len(cardNum) - 1)])
    if checkDigit == 0 and calcDigit == 10:
        return ('This is a valid credit card number.')
    elif checkDigit != 0 and calcDigit == checkDigit:
        return ('This is a valid credit card number.')
    else:
        return ('This is an invalid credit card number.')

print(validate_creditcard_number_check_digit('4012000033330026')) # test valid
print(validate_creditcard_number_check_digit('5499740000000057')) # test

#########################################
# ISBN-10 check digits calculate
def calculate_isbn10_barcode_check_digit(barcode):
    codeList = list(barcode) # split barcode into individual digits
    total = 0
    multiplier = list(range(10,1,-1)) # list of numbers to multiply by
    
    if len(codeList) == 9:
        for index, item in enumerate(codeList):
            total += (int(item) * multiplier[index])
        checkDigit = 11 - (total % 11) # modulo operator (%) gives remainder
        if checkDigit == 10:
            return ('X') 
        else:            
            return checkDigit
    else:
        return ('Please enter at least 9 digits') # throw error if insufficient digits

print(calculate_isbn10_barcode_check_digit('019852663')) # test            
  
# ISBN-10 check digits validate 
def validate_isbn10_barcode_check_digit(barcode):
    checkDigit = int(barcode[9:])
    calcCheckDigit = calculate_isbn10_barcode_check_digit(barcode[:9])
    if checkDigit == 'X' and calcCheckDigit == 10:
        return ('This is a valid isbn10 barcode.')
    elif checkDigit != 'X' and calcCheckDigit == checkDigit:
        return ('This is a valid isbn10 barcode.')
    else:
        return ('This is a invalid isbn10 barcode.')

print(validate_isbn10_barcode_check_digit('0198526636')) # test valid
print(validate_isbn10_barcode_check_digit('0198526637')) # test invalid

## GTIN-13 check digits are calculated as follows:
# 1. Multiply every second digit by 3, and every other digit by 1.
# 2. Add up all the multiplied numbers.
# 3. You can now get the check digit by working out what number would have to be added to the sum in order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.