from fractions import Fraction

def main():
	ans = 0
	for i in xrange(1000):
		x = 2
		for j in xrange(i):
			x = Fraction(1,x) + 2
		value = 1 + Fraction(1,x)
		if len(str(value.numerator)) > len(str(value.denominator)):
			ans += 1
	print ans
main()
