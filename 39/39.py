
def main():
	p_list = []

	max_count = 0
	max_p = 0

	for i in range(1001):
		p_list.append(0)


	for side_a in range(1,501):
		for side_b in range(1,999-side_a):
			side_c = (side_a**2 + side_b**2)**.5
			if (int(side_c) - side_c) == 0:
				p = int(side_a + side_b + side_c)
				if p < 1001:
					p_list[p] += 1
					if p_list[p] > max_count:
						max_count = p_list[p]
						max_p = p
				else:
					break
			
	print max_p

main()
