from collections import defaultdict

class card():
	def __init__(self,rank,suit):
		self.rank = rank
		self.suit = suit
		
def parse_cards(raw):
	cards = []
	print raw
	for raw_card in raw:
		rank = raw_card[0]
		if rank == "T":
			rank = 10
		elif rank == "J":
			rank = 11
		elif rank == "Q":
			rank = 12
		elif rank == "K":
			rank = 13
		elif rank == "A":
			rank = 14
		rank = int(rank)
		suit = raw_card[1]
		cards.append(card(rank,suit))
	return cards

def get_rank_d(cards):
	ranks = defaultdict(int)
	for card in cards:
		ranks[card.rank] += 1
#	print ranks
	return ranks

def get_suits_d(cards):
	suits = defaultdict(int)
	for card in cards:
		suits[card.suit] += 1
	return suits

def check_flush(suits):
	if len(suits) == 1:
		return True
	else:
		return False

def check_straight(ranks):
	if len(ranks) == 5:
		lower = min(ranks.keys())
		upper = max(ranks.keys())
		if (upper - lower) == 4:
			return upper, ranks, True
		elif 14 in ranks:
			del ranks[14]
			ranks[1] += 1
			lower = min(ranks.keys())
			upper = max(ranks.keys())
			if (upper - lower) == 4:
				return upper, ranks, True
			else:
				del ranks[1]
				ranks[14] += 1
	return 0, ranks, False

def check_straight_flush(ranks, suits):
	if check_flush(suits):
		upper, ranks, bool = check_straight(ranks)
		if bool:
			return upper, ranks, True
	return 0, ranks, False

def check_full_house(ranks):
	full_of = [0,0]
	if len(ranks)==2:
		for rank in ranks:
			if ranks[rank] == 3:
				full_of[0] = rank
			else:
				full_of[1] = rank
		return full_of, True
	return full_of, False

def check_trips(ranks):
	trips = 0
	if max(ranks.values()) == 3 and len(ranks) == 3:
		for rank in ranks:
			if ranks[rank] == 3:
				trips = rank
				return trips, True
	return trips, False

def check_two_pair(ranks):
	pairs = []
	if max(ranks.values()) == 2 and len(ranks) == 3:
		for rank in ranks:
			if ranks[rank] == 2:
				pairs.append(rank)
		pairs.sort()
		return pairs, True
	return pairs, False

def check_pair(ranks):
#	print "ranks in check_pair", ranks
#	print "len ranks", len(ranks)
	pair = 0
	if len(ranks) == 4:
#		print "len = 4"
		#op: get key of value 2 instead of looping through
		for rank in ranks:
			if ranks[rank] == 2:
				pair = rank
				return pair, True
	return pair, False

def better_rank(ranks1, ranks2): #1 if p1 win, 2 if p2 win, 0 if draw
#	print ranks1
#	print ranks2
	while True:
		if len(ranks1) == 0:
			return 0
		h1 = max(ranks1.keys())
		h2 = max(ranks2.keys())
		print h1, h2
		if h1 == h2:
			del ranks1[h1]
			del ranks2[h2]
			continue
		elif h1 > h2:
			print "p1 wins high card"
			return 1
		else:
			print "p2 wins high card"
			return 2
			


def check(cards1, cards2): #1 if p1 win, 2 if p2 win, 0 if draw
	ranks1 = get_rank_d(cards1)
	ranks2 = get_rank_d(cards2)
	suits1 = get_suits_d(cards1)
	suits2 = get_suits_d(cards2)
#	print "p1: " , cards1
#	print "p2: " , cards2
	print "p1 rank	", len(ranks1),"	",ranks1
	print "p1 suits	", len(suits1),"	",suits1
	print "p2 rank	", len(ranks2),"	",ranks2
	print "p2 suits	", len(suits2),"	",suits2
	upper1, ranks1, b1 = check_straight_flush(ranks1, suits1)
	upper1, ranks2, b2 = check_straight_flush(ranks2, suits2)
	if b1 and b2:
		if upper1 == upper2:
			return 0
		elif upper1 > upper2:
			print "p1 wins straight flush"
			return 1
		else:
			print "p2 wins straight flush"
			return 2
	elif b1:
		print "p1 wins straight flush"
		return 1
	elif b2:
		print "p2 wins straight flush"
		return 2
	full_of1, b1 = check_full_house(ranks1)
	full_of2, b2 = check_full_house(ranks2)
	if b1 and b2:
		if full_of1 == full_of2:
			return 0
		elif full_of1[0] == full_of2[0]:
			if full_of1[1] > full_of2[1]:
				print "p1 wins full house"
				return 1
			else:
				print "p2 wins full house"
				return 2
		elif full_of1[0] > full_of2[0]:
			print "p1 wins full house"
			return 1
		else:
			print "p2 wins full house"
			return 2
	elif b1:
		print "p1 wins full house"
		return 1
	elif b2:
		print "p2 wins full house"
		return 2
	b1 = check_flush(suits1)
	b2 = check_flush(suits2)
	if b1 and b2:
		print "both have flushes"
		return better_rank(ranks1, ranks2)
	elif b1:
		print "p1 wins flush"
		return 1
	elif b2:
		print "p2 wins flush"
		return 2
	upper1, ranks1, b1 = check_straight(ranks1)
	upper2, ranks2, b2 = check_straight(ranks2)
	if b1 and b2:
		if upper1 == upper2:
			return 0
		elif upper1 > upper2:
			print "p1 wins straight"
			return 1
		else:
			print "p2 wins straight"
			return 2
	elif b1:
		print "p1 wins straight"
		return 1
	elif b2:
		print "p2 wins straight"
		return 2
	trips1, b1 = check_trips(ranks1)
	trips2, b2 = check_trips(ranks2)
	if b1 and b2:
		if trips1 == trips2:
			return better_rank(ranks1, ranks2)
		elif trips1 > trips2:
			print "p1 wins trips"
			return 1
		else:
			print "p2 wins trips"
			return 2
	elif b1:
		print "p1 wins trips"
		return 1
	elif b2:
		print "p2 wins trips"
		return 2
	pairs1, b1 = check_two_pair(ranks1)
	pairs2, b2 = check_two_pair(ranks2)
	if b1 and b2:
		if pairs1 == pairs2:
			return better_rank(ranks1, ranks2)
		elif pairs1[0] == pairs2[0]:
			if pairs1[1] > pairs2[1]:
				print "p1 wins two pair"
				return 1
			else:
				print "p2 wins two pair"
				return 2
		elif pairs1[0] > pairs2[0]:
			print "p1 wins two pair"
			return 1
		else:
			print "p2 wins two pair"
			return 2
	elif b1:
		print "p1 wins two pair"
		return 1
	elif b2:
		print "p2 wins two pair"
		return 2
	pair1, b1 = check_pair(ranks1)
	pair2, b2 = check_pair(ranks2)
#	print b1, b2
	if b1 and b2:
		if pair1 == pair2:
			print "both have pair"
			return better_rank(ranks1, ranks2)
		elif pair1 > pair2:
			print "p1 wins pair"
			return 1
		else:
			print "p2 wins pair"
			return 2
	elif b1:
		print "p1 wins pairs"
		return 1
	elif b2:
		print "p2 wins pair"
		return 2
	return better_rank(ranks1, ranks2)
	
		


def main():
	raw1 = []
	raw2 = []
	count = 0
#	count2 = 0
	f = open("p054_poker.txt","r")
	for line in f.readlines():
		cards = map(str, line.split())
		raw1.append(cards[:5])
		raw2.append(cards[5:])
	for i, raw in enumerate(raw1):
		print i
		if check(parse_cards(raw), parse_cards(raw2[i])) == 1:
			count += 1
#			x = raw_input()
#		if check(parse_cards(raw), parse_cards(raw2[i])) == 2:
#			count2 += 1
	print count

main()
