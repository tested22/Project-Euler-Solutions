from collections import defaultdict

#save the number of primes
#instead of calculating the entire matrix, just calculate the new corners

def primes_sieve(limit):
    primes = defaultdict(int)
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            primes[i] += 1
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primes

def make_matrix(size):
	matrix = []
	for i in xrange(size):
		matrix.append([1 for x in xrange(size)])
	return matrix

def matrix_copy(old, new, size):
	for i, row in enumerate(old):
		for j, value in enumerate(row):
			new[i+1][j+1] = value
	return new

def spiral(matrix, size):
	count = (size-2)**2 + 1
	for i in reversed(xrange(size-1)):
		matrix[i][size-1] = count
		count += 1
	for i in reversed(xrange(size-1)):
		matrix[0][i] = count
		count += 1
	for i in xrange(1,size):
		matrix[i][0] = count
		count += 1
	for i in xrange(1,size):
		matrix[size-1][i] = count
		count += 1
	return matrix

def print_matrix(matrix):
	for row in matrix:
		print row

def check(primes,matrix,size):
	if size == 1:
		return False
	count = 0
 	for i in xrange(size):
		if matrix[i][i] in primes:
			count += 1
		if matrix[size-1-i][i] in primes:
			count += 1
	if float(count)/float((size*2)-1) < .1:
		return True
	return False
	
		
def main():
	limit = 1000000
	primes = primes_sieve(limit)
	old_matrix = []
	i = 1
	while True:
		if i**2 > limit:
			limit += limit
			primes = primes_sieve(limit)
		new_matrix = make_matrix(i)
		new_matrix = matrix_copy(old_matrix,new_matrix,i)
		new_matrix = spiral(new_matrix,i)
		if check(primes, new_matrix, i):
			print i
			break
		old_matrix = new_matrix
		i += 2
main()

