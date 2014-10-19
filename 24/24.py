import sys
from itertools import *

def main():
	l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	permL = list(permutations(l))
	s = str(permL[999999])
	s = s.replace('(', '')
	s = s.replace(')', '')
	s = s.replace(',','')
	s = s.replace(' ', '')
	print s
main()
