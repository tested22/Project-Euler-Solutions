from decimal import *

def main():
	getcontext().prec = 50050
	greatestSplit = 0
	greatestNum = 0
	for num in range(1,1000):
#		print num
		dNum = Decimal(1)/Decimal(num)
		strNum = str(dNum)
		strNum = strNum[50:]
		for split in range(1,num-1):
			c = strNum.count(strNum[0:split])
			check = 50000 / split
			check -= 1
			if c > check:
				if split > greatestSplit:
					greatestSplit = split
					greatestNum = num
				break
	print greatestSplit
	print greatestNum
main()
