from sys import *

def main():
	maxA = int(argv[1])
	maxB = int(argv[2])
	powers = []
	lA = [i for i in range(2,maxA+1)]
	lB = [i for i in range(2,maxB+1)]
	for a in lA:
		for b in lB:
			powers.append(a**b)
#	print powers
#	print set(powers)
	print len(set(powers))
main()
