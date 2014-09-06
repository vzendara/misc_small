cc_number = 4012888888881881
bad_cc_number = 4012888888881882

# Integer -> Integer
def last_digit(number):
    return number % 10
    
# Integer -> Integer
def drop_last_digit(number):
    return number / 10

# Integer -> [Integer]  
def break_digits(number): 
    digits = []
    
    if number <= 0:
        return digits
        
    for _ in range(0,16): 
        digits.append(last_digit(number))
        number = drop_last_digit(number) 
    
    digits.reverse()
    return digits
    
# [Integer] -> [Integer]
# Double every other digit beginning from the right.
def double_every_other(digits):
    size = len(digits) 
    digits.reverse()
  
    for count in range(0, size):
        if count == 0: 
            continue 
        elif count % 2 != 0: 
            digits[count] = 2 * digits[count]

    digits.reverse()
    return digits

# [Integer] -> Integer
def sum_digits(digits):
    result = 0
    for digit in digits:
        result += digit
    return result

# Integer -> Bool   
def validate(cc_num):
    cc_digits = break_digits(cc_num)
    doubled = double_every_other(cc_digits)
    total = sum_digits(doubled) + sum_digits(cc_digits)
    if total % 10 == 0:
        return True
    else:
        return False

#Debug section
#
#print "Last digit: ", last_digit(cc_number)
#print "Number with last digit dropped: ", drop_last_digit(cc_number)

#digits = break_digits(cc_number)
#print digits

#every_other_doubled = double_every_other(digits)
#print every_other_doubled

#sum_of_digits = sum_digits(every_other_doubled)
#print sum_of_digits

print validate(cc_number) # Expect True
print validate(bad_cc_number) # Expect False
