#i solved it, i just need a super computer
def main():
	coins = [1,2,5,10,20,50,100,200]
	ways = [0 for i in range(0,201)]
	ways[0] = 1
	for coin in coins:
		for i in range(coin,201):
			ways[i]+=ways[i-coin]
	print ways[200]
main()
