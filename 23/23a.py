import sys
from math import *

#find all abundant numbers less than 28124
#check all numbers less than 28124 for ones that are not the sum of two abundant numbers

def checkAbundant(num):
	sum = 1
	for divisor in range(2,int(num**.5+1)):
		if num % divisor == 0:
			sum += divisor
			pair = num/divisor
			if pair is not divisor:
				sum += pair
	if sum > num:
		return True
	return False

def findAbundantNumbers():
	abundantNumbers = []
	for num in range(1,1000):
		check = checkAbundant(num)
		if check:
			abundantNumbers.append(num)
	return abundantNumbers

def checkSumOfAbundant(num,abundantNumbers):
	for i in abundantNumbers:
		for j in abundantNumbers:
			if i+j == num:
				return True
	return False				

def main():
	sum = 0
	abundantNumbers = findAbundantNumbers()
#	print str(abundantNumbers)
	l = []
	for num in range(1,1000):
		check = checkSumOfAbundant(num,abundantNumbers)
		if not check:
#			l.append(num)
			sum += num
#	print str(l)
	print str(sum)
		
				
main()
