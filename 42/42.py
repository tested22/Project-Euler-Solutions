import sys
from string import *
sys.path.insert(0, '/home/Neils/PE/functions')
from functions import *

def main():
	fileName = "p042_words.txt"
	fileString = readFile(fileName)
	fileStringList = fileString[1:len(fileString)-1].split("\",\"")
	limit = len(max(fileStringList, key=len))*26

	tNums = []
	n = 1
	tNum = int(.5*n*(n+1))
	tNums.append(tNum)
	while tNum < limit:
		n += 1
		tNum = int(.5*n*(n+1))
		tNums.append(tNum)
	print tNums 

	count = 0
	ordLimit = ord('A') - 1
	for word in fileStringList:
		sum = 0
		for i in range(0,len(word)):
			sum += ord(word[i]) - ordLimit
		if sum in tNums:
			count += 1
	print count
main()
