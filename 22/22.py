from sys import *
import string

def readNames(fileName):
	names = open(fileName, 'r').read()
	names = names.replace('"',"")
	names = names.split(',')
	names.sort()
	return names

def calcSum(name):
	l = list(name)
	sum = 0
	for ch in l:
		for i, letter in enumerate(string.ascii_uppercase):
			if ch == letter:
				sum += i+1
				continue
	return sum

def main():
	names = readNames(argv[1])
	nameScoreSum = 0
	nameScore = 0
	sum = 0
	for i, name in enumerate(names):
		sum = calcSum(name)
		nameScore = (i+1) * sum
		nameScoreSum += nameScore
	print str(nameScoreSum)	
main()
