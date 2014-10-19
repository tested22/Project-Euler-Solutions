import sys
from math import *
import profile

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
	for num in range(1,28124):
		check = checkAbundant(num)
		if check:
			abundantNumbers.append(num)
	return abundantNumbers

def checkSumOfAbundant(num,abundantNumbers,length):
	for i in abundantNumbers:
		lo = 0
		hi = length
		while(True):
			index = (hi + lo) / 2
			if abundantNumbers[index] + i == num:
				return True
			elif hi-lo == 1:
				break
			if abundantNumbers[index] + i < num:
				lo = index
			else:
				hi = index
				

def solve():
	sum = 0
	abundantNumbers = findAbundantNumbers()
	length = len(abundantNumbers)
#	print str(abundantNumbers)
	l = []
	for num in range(1,28124):
		check = checkSumOfAbundant(num,abundantNumbers,length)
		if not check:
#			l.append(num)
			sum += num
#	print str(l)
#	print str(sum)
	return sum
		
def main():
	profile.run('print solve(); print')				
main()
