import sys
def sumOfDivisors(num):
	if num == 220:
		print "yo"
	sum = 1
	i = 2
	while (i < (num**.5 + 1)):
		if num % i == 0:
			sum += i
			sum += num/i
		i += 1
	if num == 220:
		print str(sum)
	return sum

def main():
	numbers = []
	amicable = []
	sum = 0
	checkSum = 0
	amicableSum = 0
	for i in range(1,10000):
		numbers.append(i)
	print str(numbers)
	for num in numbers:
		sum = sumOfDivisors(num)
		checkSum = sumOfDivisors(sum)
		if checkSum == num:
			if num != sum:
				amicable.append(num)
	print str(amicable)
	for x in amicable:
		amicableSum += x
	print str(amicableSum)
main()
