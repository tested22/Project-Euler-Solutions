from collections import defaultdict

def next_t(n):
	return n*(n+1)/2

def next_p(n):
	return n*(3*n-1)/2

def next_h(n):
	return n*(2*n-1)

def main():
	tn = 0
	pn = 0
	hn = 0
	p = defaultdict(int)
	h = defaultdict(int)
	gp = 0
	gh = 0
	while True:
		tn += 1
		t = next_t(tn)
		while t > gp:
			pn += 1
			gp = next_p(pn)
			p[gp] += 1
		while t > gh:
			hn += 1
			gh = next_h(hn)
			h[gh] += 1
		if t == 1 or t == 40755:
			continue
		if t in p and t in h:
			print t
			break
main()
