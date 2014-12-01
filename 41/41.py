import sys
#sys.path.insert(0, '/home/Neils/PE/functions')
#from functions import *

def is_prime(num):
        if num < 2:
                return False
        limit = int(num**.5 + 1)
        for i in range(2,limit):
                if num % i == 0:
                        return False
        return True

def check_pan(numString, length):
#        if len(numString) is not length:
#               return False
        for charNum in range(1,length+1):
                if numString.find(str(charNum)) is -1:
                        return False
        return True

def main():
	num = 987654323
	while num>0:
		print num
		num -= 2
		strNum = str(num)
		length = len(strNum)
		if check_pan(str(num),length):
			if is_prime(num):
				print num
				break			
	


main()
