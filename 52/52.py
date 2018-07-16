from collections import defaultdict

def main():
	x = 0
	while True:
		x = int(x)
		x += 1
		x = str(x)
		xd = defaultdict(int)
		for c in x:
			xd[c] += 1
		going = True
		count = 2
		while count < 7 and going:
			tx = str(int(x)*count)
			txd = defaultdict(int)
			for c in tx:
				txd[c] += 1
			if txd == xd:
				count += 1
				continue
			going = False
		if going:
			print x
			break
main()
