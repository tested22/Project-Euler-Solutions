import sys

def main():
	fPrev1 = 1
	fPrev2 = 1
	count = 2
	while(True):
		f = fPrev1 + fPrev2
		count += 1
		if f >= 10** 999:
			break
		fPrev1 = fPrev2
		fPrev2 = f
	print count
		
main()
