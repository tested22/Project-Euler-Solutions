
def is_prime(num):
	if num < 2:
		return False
	limit = int(num**.5 + 1)
	for i in range(2,limit):
		if num % i == 0:
			return False
	return True

def check_pan(numString, length):
#        if len(numString) is not length:
#               return False
	for charNum in range(1,length+1):
		if str(charNum) not in s:
			return False
	return True


"""def main():
	for num in range(0,100):
		if is_prime(num):
			print num
	print check_pan("123455", 6)
main()"""
