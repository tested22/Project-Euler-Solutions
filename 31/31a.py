#.01, .02, .05, .10, .20, .50, 1, 2

def checkTotal(total):
#	print "checking total : " + str(total) + ", type of total is: " + str(type(total))
	if total == .20:
		return True
#	print str(total) + " is not equal to .1"
	return False

def keepGoing(total):
	if total < 2:
		return True
	return False

def addPenny(total):
	total += 2
	return total

def addTwoPennies(total):
	total += .02
	return total

def addFivePence(total):
	total += .05
	return total

def addTenPence(total):
	total += .10
	return total

def addTwentyPence(total):
	total += .20
	return total

def addFiftyPence(total):
	total += .50
	return total

def addPound(total):
	total += 1
	return total

def addTwoPounds(total):
	total += 2
	return total

def findACC(aCC, pCC, total):
	total = round(total, 2)
	lCC = pCC[:]
	lTotal = total

#	print total
#	print "pCC: " + str(pCC) + " total: " + str(total)

	if checkTotal(total):
#		print "FOUND " + str(pCC)
		aCC.append(pCC)
		return aCC

	while(keepGoing(total)):

		total = lTotal		
		total = addPenny(total)
		pCC = lCC[:]
		pCC.append(.01)
		aCC = findACC(aCC, pCC, total)
		
		total = lTotal
		total = addTwoPennies(total)
		pCC = lCC[:]
		pCC.append(.02)
		aCC = findACC(aCC, pCC, total)

		total = lTotal
		total = addFivePence(total)
		pCC = lCC[:]
		pCC.append(.05)
		aCC = findACC(aCC, pCC, total)

		total = lTotal
		total = addTenPence(total)
		pCC = lCC[:]
		pCC.append(.10)
		aCC = findACC(aCC, pCC, total)

		total = lTotal
		total = addTwentyPence(total)
		pCC = lCC[:]
		pCC.append(.20)
		aCC = findACC(aCC, pCC, total)

		total = lTotal
		total = addFiftyPence(total)
		pCC = lCC[:]
		pCC.append(.50)
		aCC = findACC(aCC, pCC, total)

		total = lTotal
		total = addPound(total)
		pCC = lCC[:]
		pCC.append(1)
		aCC = findACC(aCC, pCC, total)

#		total = lTotal
#		total = addTwoPounds(total)
#		pCC = lCC[:]
#		pCC.append(2)
#		aCC = findACC(aCC, pCC, total)


	return aCC

def findUCC(aCC):
	uCC = []
	for cC in aCC:
		uCC.append(str((sorted(cC))))		
	uCC = set(uCC)
	return uCC

def solve():
	aCC = []
	pCC = []
	aCC = findACC(aCC, pCC, 0)
	print "aCC: " + str(aCC)
	uCC = findUCC(aCC)
	print "uCC: " + str(uCC)
	return len(uCC) + 1

def main():
	answer = solve()
	print answer
main()
