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

def check(primes, i):
	count = 0
	for prime in primes:		
		if i % prime == 0:
			count += 1
			while i%prime == 0:
				i /= prime
				if i == 1:
					break
		if count > 4:
			return False
	if count == 4:
		return True
	return False

def main():
	limit = 1000000
	primes = primes_sieve(limit)
	i = 2
	count = 0
	while True:
		if check(primes,i):
			count += 1
			if count == 4:
				print i-3
				break
		else:
			count = 0
		if i > limit:
			limit += limit
			primes = primes_sieve(limit)
		i += 1
main()
