def main():
	num = 2 ** 1000
	print str(num)
	num = str(num)
	l = list(num)
	print str(l)
	sum = 0
	for i in l:
		sum += int(i)
	print str(sum)
main()
