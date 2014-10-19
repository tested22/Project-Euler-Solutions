import sys, num2word

def main():
	answer = map(num2word.to_card, range(1,1001))
	answer = "".join(answer)
	answer = answer.replace(" ", "")
	answer = answer.replace("-", "")
	print answer
	print str(len(answer))
main()
