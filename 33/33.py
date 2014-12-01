from fractions import *

def getDigits(n):
	digits = str(n)
	l = list(digits)
	return l

def checkSameDigit(digit, denomL):
	if digit in denomL and digit is not '0':
		return True
	return False

def removeDigits(digit, numerL, denomL):
	tNumerL = numerL[:]
	tDenomL = denomL[:]
	tNumerL.remove(digit)
	tDenomL.remove(digit)
	if float(tDenomL[0]) < 1:
		return -1
	dec = float(tNumerL[0]) / float(tDenomL[0])
	dec = round(dec,10)
	return dec

def reduce(top, bottom):
	return Fraction(top,bottom)

def main():

#get digits for both
#if digit1 in both
#remove digit1
#check
#if digit2 in both
#remove digit2
#check
	tops = 1
	bottoms = 1

	for top in range(10,100):
		for bottom in range(top+1,100):
			quotient = float(top)/float(bottom)
			quotient = round(quotient,10)
			numerL = getDigits(top)
			denomL = getDigits(bottom)
			if checkSameDigit(numerL[0], denomL):
				dec = removeDigits(numerL[0], numerL, denomL)
				if dec == quotient:
					print str(numerL) + " / " + str(denomL)
					tops *= top
					bottoms *= bottoms
					
					

			if checkSameDigit(numerL[1], denomL):
				dec = removeDigits(numerL[1], numerL, denomL)
				if dec == quotient:
					print str(numerL) + " / " + str(denomL)
					tops *= top
					bottoms *= bottom

	print tops
	print bottoms
	f = reduce(tops, bottoms)
	print f
main()
