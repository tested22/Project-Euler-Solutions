from string import *
from itertools import permutations

def main():
	f = open("p059_cipher.txt","r")
	letters = ascii_lowercase
	lower = ord("A")
	upper = ord("z")
	cipher = f.readline()
	perms = permutations(letters,3)
	for perm in perms:
		original = []
		found = True
		for i, char in enumerate(cipher.split(",")):
			xor = int(char)^ord(perm[i%3])
			original.append(xor)
			if xor > 31 and xor < 123 and xor != 35 and xor != 47:
				continue
			found = False
			break
		if found:
			ans = ""
			for value in original:
				ans += chr(value)
			print ans
			print sum(original)
			
main()
