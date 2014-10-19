from math import *
import sys

def main():
	fact = factorial(100)
	strFact = str(fact)
	lFact = list(strFact)
	sum = 0
	for digit in lFact:
		sum += int(digit)
	print str(sum)
main()
