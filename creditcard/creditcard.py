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
	count = 0
	digits = []
	
	if number <= 0:
		return digits
		
	while count < 16:
		digits.append(last_digit(number))
		number = drop_last_digit(number)
		count += 1
	digits.reverse()
	return digits
	
# [Integer] -> [Integer]
# Double every other digit beginning from the right.
def double_every_other(digits):
	size = len(digits)
	count = 1
	digits.reverse()
	
	while count < size:
		if count % 2 == 0:
			digits[count] = 2 * digits[count]
		count += 1

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
	if sum_digits(double_every_other(break_digits(cc_num))) % 10 == True:
		return True
	else:
		return False


print "Last digit: ", last_digit(cc_number)
print "Number with last digit dropped: ", drop_last_digit(cc_number)

digits = break_digits(cc_number)
print digits

every_other_doubled = double_every_other(digits)
print every_other_doubled

sum_of_digits = sum_digits(every_other_doubled)
print sum_of_digits

print validate(cc_number) # Expect True
print validate(bad_cc_number) # Expect False
