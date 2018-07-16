def main():
	count = 0
	base = 1
	while base < 10:
		pow = 1
		while True:
			digits = len(str(base**pow))
			if pow > digits:
				break
			if digits == pow:
				print base**pow, base, pow
				count += 1
			pow += 1
		base += 1
	print count
main()
