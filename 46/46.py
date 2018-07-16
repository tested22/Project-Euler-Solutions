def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    primes = []
    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primes

def check(primes,i):
	for prime in primes:
		for sq in xrange(1,int(i**.5)+2):
			sum = prime + 2*sq**2
			if sum == i:
				return True
			if sum > i:
				break
	return False		


def main():
	limit = 1000000
	primes = primes_sieve(limit)
	i = 9
	while True:
		if i not in primes:
			if not check(primes,i):
				print i
				break
		i += 2
		if i > limit:
			limit += limit
			primes = primes_sieve(limit)
main()
