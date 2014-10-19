from sys import *

def next_step(num):
	if num%2 == 0:
		return num/2
	else:
		return (3*num + 1)

def num_steps(num):
	numSteps = 0
	num1 = num
	loop = True
	if num == 1:
		return numSteps
	while(loop):
		numSteps += 1
		num1 = next_step(num1)
		if num1 == 1:
			if numSteps == 524:
				print str(num)
			return numSteps
def main():
	greatest = 1
	count = 1
	loop = True
	while(loop):			
		count += 1
#		print str(count)
		if count >= 1000000:
			loop = False
		temp = num_steps(count)
		if temp > greatest:
			greatest = temp
	print str(greatest)		
main()
