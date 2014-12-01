def check_pal(str):
	limit = int(len(str)/2)
	for pos, i in enumerate(range(0,limit)):
		if not str[pos] == str[len(str)-pos-1]:
			return False
	return True
 
def main():
	sum = 0
	for num in range(0,1000000):
		if check_pal(str(num)):
			bin = "{0:b}".format(num)
			if check_pal(bin):
				print "base 10: " + str(num) + " base 2:" + bin 
				sum += num
	print sum
main()
