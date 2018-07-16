from itertools import permutations
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

def check(primes,s):
	count = 0
	ans = []
	for i in xrange(10):
		ts = s[:]
		ts = ts.replace("*",str(i))
		if int(ts) in primes:
			ans.append(ts)
			count += 1
	if count == 8:
		return ans, True
	return ans, False		

def inc(perm, i, length):
	i = str(i)
	for zero in xrange(length-len(i)):
		i = "0" + i
	count = 0
	for idx, c in enumerate(perm):
		if c != "*":
			perm = perm.replace(perm[idx],i[count],1)
			count += 1
	return perm
	
	

def main():
	limit = 10000000
	primes = primes_sieve(limit)
	digit = 2
	found = False
	while not found:
		for stars in xrange(1,digit+1):
			str = ""
			for star in xrange(stars):
				str += "*"
			for one in xrange(digit-stars):
				str += "0"
			perms = set(list(permutations(str,digit)))
			for perm in perms:
				perm = "".join(perm)
				for i in xrange(10**(digit-stars)):
					s = inc(perm, i,digit-stars)
					ans, bool = check(primes,s)
					if bool:
						print ans
						found = True
						break
				if found:
					break	
		digit += 1
main()
