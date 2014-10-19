import sys
from math import *

def is_prime(num):
	check = sqrt(num) + 1
	check = int(check)
	for j in range(2, check):
		if (num%j) == 0:
			return False
	return True

def main():
	sum = 0
	for i in range(2,2000000):
		if is_prime(i):
			sum += i
	print str(sum)
main()
