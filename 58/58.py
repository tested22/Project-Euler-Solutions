from collections import defaultdict

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


def is_prime(n):
#    if n == 1: 
#		return false
    primes = primes_sieve(int(n**0.5) + 1)
    for p in primes:
        if n%p == 0:
            return False
    return True

def count_corners(size):
	corner = size**2
	count = 0
	for i in xrange(3):
		corner -= size - 1
		if is_prime(corner):
			count += 1
	return count

def main():
	i = 3
	count = 0
	while True:
		count += count_corners(i)
		if float(count)/float( (i*2) - 1) < .1:
			print i
			break
		i += 2
main()

