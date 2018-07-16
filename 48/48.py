def main():
	sum = 0
	for i in xrange(1,1001):
		sum += i**i
	sum = str(sum)
	print sum[len(sum)-10:]
main()
