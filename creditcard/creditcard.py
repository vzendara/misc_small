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

print last_digit(cc_number)
print drop_last_digit(cc_number)
print break_digits(cc_number)
