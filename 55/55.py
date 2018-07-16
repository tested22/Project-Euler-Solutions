def check_pal(i):
	i = str(i)
	ri = i[::-1]
	if i == ri:
		return True

def check(i):
	for iter in xrange(50):
		i = str(i)
		ri = i[::-1]
		i = int(i) + int(ri)
		if check_pal(i):
			return True
	return False		
	

def main():
	count = 0
	for i in xrange(10000):
		if check(i):
			continue
		count += 1
	print count
main()
