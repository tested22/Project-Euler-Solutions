from itertools import permutations, combinations

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

def check_sequence(l):
	l = list(l)
	l.sort()
	if l[0] == 1487:
		return False
	if (l[1]-l[0]) == (l[2]-l[1]):
		return True
	return False

def main():
	all_primes = primes_sieve(9999)
	primes = []
	for prime in all_primes:
		if prime > 1000:
			primes.append(prime)
	found = False
	for prime in primes:
		prime = str(prime)
		perms = permutations(prime,4)
		count = 0
		l = []
		for perm in perms:
			n = int("".join(map(str,perm)))
			if n in l:
				continue
			if n in primes:
				count += 1
				l.append(n)
		if count > 2:
			l_3 = combinations(l,3)
			for check in l_3:
				if check_sequence(check):
					print "".join(map(str,check))
					found = True
					break
		if found:
			break
main()
