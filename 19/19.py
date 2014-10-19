from datetime import *
import sys

def main():
	count = 0
	cDay = date(1901, 1, 1)
	while cDay.year < 2001:
		if cDay.day == 1:
			wDay = cDay.weekday()
			if wDay == 6:
				count += 1
				print str(cDay)
		cDay += timedelta(1)

	print str(count)
main()
