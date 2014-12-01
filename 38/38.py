from string import *

def check_pan(str):
	if len(str) is not 9:
		return False
	l = list(str)
	s = set(l)
	if len(s) is 9:
		if '0' not in s:
			return True
	return False	

def main():
	greatest = 0
	for num in range(9877):
			i = 1
			num_string = str(num)
			while(len(num_string)<9):
				i += 1
				next_num = num * i
				num_string += str(next_num)				
				if check_pan(num_string):
					if int(num_string) > greatest:
						greatest = int(num_string)
	print greatest
main()
