def check_sum(i):
	i = str(i)
	sum = 0
	for digit in i:
		sum += int(digit)
	return sum

def main():
	best = 0
	for a in xrange(100):
		for b in xrange(100):
			i = a**b
			sum = check_sum(i)
			if sum > best:
				best = sum
	print best
main()
