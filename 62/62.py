from itertools import permutations
from collections import OrderedDict, defaultdict

def get_cubes():
	cubes = OrderedDict()
	for i in xrange(10000):
		cubes[i**3] = 1
	return cubes

def main():
	found = False
	cubes = get_cubes()
	check = defaultdict(int)
	
	for cube in cubes:
		x = list(str(cube))
		x.sort()
		check["".join(x)] += 1

	ans = []

	for c in check:
		if check[c] == 5:
			ans.append(c)

	best = None

	for cube in cubes:
		o = cube
		cube = list(str(cube))
		cube.sort()
		cube = "".join(cube)
		if cube in ans:
			if best == None or o < best:
				best = o

	print best
main()
