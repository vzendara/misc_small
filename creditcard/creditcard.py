
cc_number = 4012888888881881
def last_digit(number):
	return number % 10
	

def drop_last_digit(number):
	return number / 10

print last_digit(cc_number)
print drop_last_digit(cc_number)
