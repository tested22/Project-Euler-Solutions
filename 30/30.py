import sys

def main():
	num = 2
	validNums = []
	validNumSum = 0

	while (True):
		sum = 0
		sNum = str(num)
		lSNum = list(sNum)
		for digit in lSNum:
			digit = int(digit)
			sum += digit**5
		
#		if num == 99999:
#			print num
#			print sum
#			print lSNum
#			print set(lSNum)

		if len(set(lSNum)) == 1 and '9' in lSNum and sum < num:
			break

		if sum == num:
			validNums.append(num)
			
		num += 1	

	for validNum in validNums:
		validNumSum += validNum
	
	print validNums
	print validNumSum
main()
