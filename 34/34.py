from math import *

def main():
	answer = 0
	for n in range(10, 2540161):
		sum = 0
		sN = str(n)
		lN = list(sN)
		for digit in lN:
			digit = int(digit)
			sum += factorial(digit)
			if sum > n:
				break	
		if sum == n:
			answer += n
	print answer

main()
