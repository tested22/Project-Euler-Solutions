import sys
sys.path.insert(0, '/home/Neils/PE/functions')
from functions import *

def left_to_right(num):
	num = str(num)
	num = num[1:]
	num = int(num)
	return num
	
def right_to_left(num):
	return num/10

def main():
	count = 0
	current_number = 9
	sum = 0

	while(count < 11):
		current_number += 1
		if is_prime(current_number):
			keep_going = True
			number = current_number
			while(number > 9):
				number = left_to_right(number)
				if not is_prime(number):
					keep_going = False
					break
			if not keep_going:
				continue
			number = current_number
			while(number > 9):
				number = right_to_left(number)
				if not is_prime(number):
					keep_going = False
					break
			if not keep_going:
				continue
			count += 1
			sum += current_number
			print current_number
	print sum
	
												


main()
