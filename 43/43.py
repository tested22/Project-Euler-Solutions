from itertools import permutations

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

def check_prime_substrings(primes, str_num):
	i = 1
	while i<8:
		num = int(str_num[i:i+3])
		if num%primes[i-1] != 0:
			return False
		i += 1
	return True
	

def main():
	ans = 0
	primes = primes_sieve(20)
	check_prime_substrings(primes, "1406357289")
	pans =  [ ''.join(p) for p in permutations("0123456789",10)]
	for pan in pans:
		if pan[0] == '0':
			continue
		if check_prime_substrings(primes,pan):
			ans += int(pan)
	print ans
main()
