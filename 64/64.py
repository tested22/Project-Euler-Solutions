from math import *
from fractions import *
#as soon as it starts to repeat?

def solve(i):
	block = floor(sqrt(i))
#	print "block", block
	comp = (i,block)
	block, comp, diff = get_next(comp,1)
	ans = [block]
	count = 1
	check = 0
	while True:
		count += 1
		block, comp, diff = get_next(comp, diff)
		ans.append(block)
		if count > 10:
			check = guess_seq_len(ans, count)
		if check > 0:
#			if check%2 == 1:
#				print "i", i
			return check
#		print "BLOCK", ans

def get_next(comp, denom):
	diff = comp[0] - comp[1]**2
#	print "diff", diff
	div = gcd(denom,diff)
	diff /= div
	denom /= div
	new_block = floor( (denom*sqrt(comp[0]) + denom*comp[1]) / diff)
#	print "new_block", new_block
	digit_comp = abs (comp[1] - diff*new_block)
#	print "digit_comp", digit_comp
	new_comp = (comp[0],digit_comp)
#	print "new_comp", new_comp
	return new_block, new_comp, diff

def guess_seq_len(seq, length):
	if length%2 == 1:
		return 0
	for i in xrange(1,(length/2)+1):
		if length%i > 0:
			continue
		if seq[:i] * (length/i) == seq:
#			print "FOUND", i
			return i
	return 0

squares = []

for i in xrange(1,101):
	squares.append(i*i)
ans = 0
for i in xrange(2,10001):
	if i in squares:
		continue
	elif solve(i)%2 == 1:
		ans += 1
print ans