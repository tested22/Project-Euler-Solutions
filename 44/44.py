def next(n):
	return n*(3*n-1)/2

def main():
	p = [ next(1), next(2) ]
	check = 0
	n = 2
	found = False
	while not found:
		p1 = p[check]
		for p2 in p:
			if p2 >= p1:
				break
			ps = p1+p2
			if p[len(p)-1] < ps:
				while True:
					n += 1
					np = next(n)
					p.append(np)
					if np >= ps:
						break
			if ps in p:
				pd = abs(p1-p2)
				if pd in p:
					print pd
					found = True
					break
		check += 1
main()
