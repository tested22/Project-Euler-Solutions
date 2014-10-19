import sys
from math import *

def getNumFactors(tNum):
	numFactors = 0
	count = 0
	while (count <= sqrt(tNum)):
		count += 1
		if(tNum % count == 0):
			numFactors += 2
	return numFactors

def main():
	loop = True
	tNum = 1
	count = 1
	while(loop):
		numFactors = getNumFactors(tNum)
		print "Number of Factors for tNum " + str(tNum) + " is: " + str(numFactors)
		if numFactors > 500:
			loop = False
		count += 1
		tNum += count
	print str(tNum)
main()
