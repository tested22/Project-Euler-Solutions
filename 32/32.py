def main():
	answers = []
	sum = 0
	for m1 in range ( 1, 10000):
		sM1 = str(m1)
		if '0' in sM1:
			continue
		for m2 in range ( 1, 100):
			sM2 = str(m2)
			if '0' in sM2:
				continue
			sTotal = sM1 + sM2
			if len(sTotal) > 9:
				break
			product = m1 * m2
			sProduct = str(product)
			if '0' in sProduct:
				continue
			sTotal += sProduct
			if len(sTotal) > 9:
				break
			if len(sTotal) == 9:
				l = list(sTotal)
				s = set(l)
				if len(s) == 9:
					print sTotal
					answers.append(product)
	answers = set(answers)
	for answer in answers:
		sum += answer
	print sum
main()
