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
            return str(checkDigit)
    else:
        return ('Please enter at least 9 digits') # throw error if insufficient digits

#print(calculate_isbn10_barcode_check_digit('019852663')) # test            
  
# ISBN-10 check digits validate 
def validate_isbn10_barcode_check_digit(barcode):
    checkDigit = barcode[9:]
    calcCheckDigit = calculate_isbn10_barcode_check_digit(barcode[:9])
    if calcCheckDigit == checkDigit:
        return ('This is a valid isbn10 barcode.')
    else:
        return ('This is an invalid isbn10 barcode.')

#print(validate_isbn10_barcode_check_digit('0198526636')) # test valid
#print(validate_isbn10_barcode_check_digit('0198526637')) # test invalid
