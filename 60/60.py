from collections import defaultdict
from itertools import combinations

def primes_sieve_d(limit):
    primes = defaultdict(int)
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            primes[i] += 1
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primes

def primes_sieve_l(limit):
    primes = []
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            for n in xrange(i*i, limit, i):
                a[n] = False
    return primes

def get_pairs(i, primes, d_primes, working):
	c_prime = str(primes[i])
	for prime in primes[i+1:]:
		s_prime = str(prime)
		if int(c_prime + s_prime) in d_primes and int(s_prime+c_prime) in d_primes:
			working[int(c_prime)].add(prime)
			working[prime].add(int(c_prime))
	return working

def main():
	l_primes = primes_sieve_l(10000)
	d_primes = primes_sieve_d(100000000)
	best = 100000*6
	working = defaultdict(set)
	for i, prime in enumerate(l_primes):
		working = get_pairs(i, l_primes, d_primes, working)	
	for p1 in l_primes:
		csum = p1
		if csum > best:
			break
		current = working[p1]
		for p2 in working[p1]:
			csum = p1 + p2
			if csum > best:
				break
			current = working[p2] & working[p1]
			for p3 in working[p2]:
				if p3 == p1 or p3 == p2 or p3 not in current:
					continue
				csum = p1 + p2 + p3
				if csum > best:
					break
				current = working[p3] & working[p2] & working[p1]
				for p4 in working[p3]:
					if p4 == p3 or p4 == p2 or p4 == p1 or p4 not in current:
						continue
					csum = p1 + p2 + p3 + p4
					if csum > best:
						break
					current = working[p4] & working[p3] & working[p2] & working[p1]
					for p5 in working[p4]:
						if p5 == p4 or p5 == p3 or p5 == p2 or p5 == p1 or p5 not in current:
							continue
						csum = p1 + p2 + p3 + p4 + p5
						if csum >= best:
							break
						best = csum
	print best
main()
