cc_number = 4012888888881881

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
	

print "Last digit: ", last_digit(cc_number)
print "Number with last digit dropped: ", drop_last_digit(cc_number)
print break_digits(cc_number)
print double_every_other(break_digits(cc_number))
