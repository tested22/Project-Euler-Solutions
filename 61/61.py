from collections import defaultdict

def get_working(value, d):
	working = defaultdict(int)
	value = str(value)[2:]
	for key in d:
		if str(key)[:2] == value:
			working[key] += 1
	return working

def get_tri_d():
	tris = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			tris[value] += 1
		value = n*(n+1)/2
		n += 1
	return tris

def get_sq_d():
	sqs = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			sqs[value] += 1
		value = n**2
		n += 1
	return sqs

def get_pent_d():
	pents = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			pents[value] += 1
		value = n*(3*n-1)/2
		n += 1
	return pents

def get_hex_d():
	hexs = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			hexs[value] += 1
		value = n*(2*n-1)
		n += 1
	return hexs

def get_hept_d():
	hepts = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			hepts[value] += 1
		value = n*(5*n-3)/2
		n += 1
	return hepts

def get_oct_d():
	octs = defaultdict(int)
	n = 2
	value = 1
	while value < 10000:
		if value >= 1000:
			octs[value] += 1
		value = n*(3*n-2)
		n += 1
	return octs


def main():
	tri = get_tri_d()
	sq = get_sq_d()
	pent = get_pent_d()
	hex = get_hex_d()
	hept = get_hept_d()
	oct = get_oct_d()
	all = defaultdict(int)
	all.update(tri)
	all.update(sq)
	all.update(pent)
	all.update(hex)
	all.update(hept)
	all.update(oct)
	working = defaultdict(int)
	for key in all:
		working[key] = get_working(key, all)
	for key1 in all:
		for key2 in working[key1]:
			if key2 == key1:
				continue
			for key3 in working[key2]:
				if key3 == key2 or key3 == key1:
					continue
				for key4 in working[key3]:
					if key4 == key3 or key4 == key2 or key4 == key1:
						continue
					for key5 in working[key4]:
						if key5 == key4 or key5 == key3 or key5 == key2 or key5 == key1:
							continue
						for key6 in working[key5]:
							if key6 == key5 or key6 == key4 or key6 == key3 or key6 == key2 or key6 == key1:
								continue
							if key1 not in working[key6]:
								continue
							keys = [key1, key2, key3, key4, key5, key6]
							checks = []
							for key in keys:
								inshapes = []
								if key in tri:
									inshapes.append(1)
								if key in sq:
									inshapes.append(2)
								if key in pent:
									inshapes.append(3)
								if key in hex:
									inshapes.append(4)
								if key in hept:
									inshapes.append(5)
								if key in oct:
									inshapes.append(6)
								checks.append(inshapes)
							for check1 in checks[0]:
								for check2 in checks[1]:
									for check3 in checks[2]:
										for check4 in checks[3]:
											for check5 in checks[4]:
												for check6 in checks[5]:
													found = True
													for value in xrange(1,7):
														if value not in [check1, check2, check3, check4, check5, check6]:
															found = False
													if found:
														print checks
														print keys
														print sum(keys)
														exit()
main()
