import sys
sys.path.insert(0, '/home/Neils/PE/functions')
from functions import *

def rotate_num(num):
	numList = list(num)
	temp = numList.pop(0)
	numList.append(temp)
	num = ''.join(numList)
	return num

def check_all_rotations(num):
	num = str(num)
	size = len(num)
	if not is_prime(int(num)):
		return False
	for i in range(0,size):
		num = rotate_num(num)
		if not is_prime(int(num)):
			return False
	return True

def main():

	count = 0
	for num in range(0,1000000):
		if check_all_rotations(num):
			print num
			count += 1

	print count	
main()
