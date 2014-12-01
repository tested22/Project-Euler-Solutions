#n**2 + an + b
#b is prime, n = 0
#n = odd, a = even, odd(n**2) + even*odd+ odd(b) = odd + even + odd = even.  a must be odd

import sys, profile

#checks if a number is prime
def isPrime(num):
	if num < 0:
		return False
	limit = int(num**.5 + 1)
	for i in range(2,limit):
		if num%i == 0:
			return False
	return True

#generates all prime numbers less than 1000
def generateB():
	l = [2]
	for num in range(3,1000, 2):
			if isPrime(num):
				l.append(num)
	return l

#generates all odd numbers in range -999 to 1000
def generateA():
	l = []
	for num in range(-999, 1000, 2):
		l.append(num)
	return l

def countPrimes(numA,numB):
	nextIsPrime = True
	n = 0
	count = 0
	while(True):
		if isPrime(n**2 + numA*n + numB):
			count += 1		
			n += 1
		else:
			break
	return count

def countGreatestPrimes(lA, lB):
	greatestPrimes = 0
	greatestSet = [0,0]
	for numA in lA:
		for numB in lB:
			tGreatestPrimes = countPrimes(numA,numB)
			if tGreatestPrimes > greatestPrimes:
				greatestPrimes = tGreatestPrimes
				greatestSet = [numA,numB]
	print "A = " + str(greatestSet[0]) + " B = " + str(greatestSet[1]) + " yield the greatest number of primes, " + str(greatestPrimes)
	return greatestSet
	
def solve():
	lA = generateA()
	lB = generateB()
	greatestSet = countGreatestPrimes(lA,lB)
	product = greatestSet[0]*greatestSet[1]
	print "Their product is " + str(product)

def main():
	profile.run('print solve(); print')				
main()
