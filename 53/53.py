
from itertools import izip

def ncr(n,r):
	return reduce(lambda x, y: x * y[0] / y[1], izip(xrange(n - r + 1, n+1), xrange(1, r+1)), 1)

def main():
	ans = 0
	limit = 1000000
	for n in xrange(1,101):
		for r in xrange(1,n):
			if ncr(n,r) > limit:
				ans += 1
	print ans
main()
