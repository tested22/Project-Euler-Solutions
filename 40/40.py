def main():
	dn = 1000000
	s = "."
	count = 0
	product = 1
	while len(s) < (dn+2+count):
		count += 1
		s += str(count)
	while dn > .9:
		product *= int(s[dn])
		dn /= 10
	print product
main()


