
gtin13_barcode = '940055061977'
barcode = '9400550619'


# function to split barcode
# def strSplit(barcode): 
#     return [char for char in barcode]  
# #print(strSplit(barcode))

multiplier = list(range(10,0,-1))
#print(multiplier)

def calculate_isbn10_barcode_check_digit(barcode):
    codeList = list(barcode) # split barcode into individual digits
    total = 0
    if len(codeList) == 9:
        multiplier = list(range(10,1,-1)) # list of numbers to multiply by
        for index, item in enumerate(codeList):
            total += (int(item) * multiplier[index])
        checkDigit = 11 - (total % 11) # modulo operator (%) gives remainder
        if checkDigit == 10:
            return ('X') # convert to return later
        else:            
            return checkDigit
    else:
        return ('Please enter the correct number of digits') # throw error here if less than 10 digit

print(calculate_isbn10_barcode_check_digit('019852663'))            
  
        ## GTIN-13 check digits are calculated as follows:
        # 1. Multiply every second digit by 3, and every other digit by 1.
        # 2. Add up all the multiplied numbers.
        # 3. You can now get the check digit by working out what number would have to be added to the sum in order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.


# # based on length of barcode list
# # branch into each defined calculation type
#     list = [1, 33, 55]
#     total = 0
#     for item in list:
#         total = total + item

# desired output
# print(calculate_gtin13_barcode_check_digit('940055061977'))