from sys import *

def fillMatrix(i,j,matrix):
	value = 1
	matrix[i][j]=value
	count = 2
	loop = True
	#loop go right, go down, go left, go up
	#increase count go down
	#break if i and j = n - 1 after going right
	while(True):
		
		#check to see if at end
		if j == len(matrix)-1:
			break

		#shift right
		value += 1
		j += 1
		matrix[i][j] = value
				
		#go down count-1 times
		for x in range(0,count-1):
			value += 1
			i += 1
			matrix[i][j] = value

		#go left count*2 times
		for x in range(0,count):
			value += 1
			j -= 1
			matrix[i][j] = value

		#go up count*2 times
		for x in range(0,count):
			value += 1
			i -= 1
			matrix[i][j] = value

		#go right count*2
		for x in range(0,count):
			value += 1
			j += 1
			matrix[i][j] = value

		#increase count
		count += 2

	return matrix	

def calcSumDiagonals(matrix):
	sum = 0
	limit = len(matrix)-1
	for i in range(0,limit+1):
		sum += matrix[i][i]
		sum += matrix[limit-i][i]
	return sum-1

def main():
	n = int(argv[1])
	matrix = [[0 for i in range(n)] for j in range(n)]
	i = n/2
	j = n/2
	matrix = fillMatrix(i,j,matrix)
	sum = calcSumDiagonals(matrix)
	print sum
main()
