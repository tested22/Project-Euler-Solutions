from sys import *

def main():
	data = argv[1]
	sum = 0
	numbers  = open(data, 'r').readlines()
	for number in numbers:
		number = int(number)
		sum += number
	print str(sum)
main()
