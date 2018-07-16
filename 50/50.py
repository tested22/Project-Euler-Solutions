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


def main():
    primes = primes_sieve(1000000)
    s = 0
    best = 21
    limit = 0
    for prime in primes:
        if s+prime < 1000000:
            s += prime
            limit += 1
        else:
            break
    found = False
    for con in reversed(range(21,limit+1)):
        if found:
            break
        start = 0
        while True:
            s = sum(primes[start:start+con+1])
            if s > 1000000:
                break
            if s in primes:
                print s
                found = True
                break
            start += 1
main()

