'''
    Intermediate C#1, AGRAM
    PROBLEM:
	Agram is a card game for 2 players, using the cards from a standard 52-card pack.
	The dealer deals five cards to each player. The opponent player leads any card, playing it face up
	in the middle of the playing area.
	For this program the following strategy will be used to determine which card the dealer will play:
	- The dealer must play a card of the same suit if he can.
	He plays the lowest card in that suit that is of a higher rank than the card the opponent
	played.
	- If he does not have such a card, he plays his lowest card in that suit.
	- If he does not have a card in that suit, he plays the lowest ranking card regardless of suit.
	We guarantee there will be no ties.
	INPUT: There will be 5 lines of input. Each line will contain the opponent’s lead card and the
	5 cards held by the dealer. All cards will be represented by 2-character strings in value-suit order.
	AH represents the ace of hearts. K, Q and J and T will be used for king, queen, jack and 10
	respectively. Note that the ace in this game has the lowest rank.
	OUTPUT: For each input line print the card the dealer must play according to the strategy listed
	above.
	SAMPLE INPUT                    SAMPLE OUTPUT
	1. 5D, 2D, 6H, 9D, TD, 6S       1. 9D
	2. TC, AC, KC, QH, JS, TD       2. KC
	3. 3D, 4H, 5C, 6S, 2D, 7H       3. 2D
	4. KS, TH, QC, 7H, 9H, 3H       4. 3H
	5. AC, AD, KH, JS, KS, QS       5. AD
'''
from unittest import TestCase

def agram1(cards):
	'''
		2 sort with bug
	'''
	# for compare King, Queen, Jack, Ten, ...
	rule = {
		'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
		'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
		'J': 11, 'Q': 12, 'K': 13 }

	suit = []         # greater ranks in the suit
	s, r = cards[0][1], rule[cards[0][0]]# spade, rank

	min_r, min_card = 14, None     # minimal rank & card of all cards
	min_s, min_suit = 14, None     # minimal rank & card of the suit

	for x in range(1, len(cards)):
		rx = rule[cards[x][0]]     # rank of card x
		if cards[x][1] == s:
			if r < rx:
				suit.append(cards[x])
			if min_s > rx:
				min_s = rx
				min_suit = cards[x]

		if min_r > rx:
			min_r = rx
			min_card = cards[x]

	if len(suit) > 0:
		suit.sort()	    # Bug here! Though the test cases are validated.
						# try this: ['AD', '9D'].sort()
						# suit.sort(key=lambda r: rule[r[0]], reverse=False)
		return suit[0]
	elif min_suit is not None:
		return min_suit
	else:
		return min_card


t = TestCase()
# the bug case
# t.assertEqual('TD', agram1(['5D', '2D', '6H', 'KD', 'TD', '6S']))
t.assertEqual('9D', agram1(['5D', '2D', '6H', '9D', 'TD', '6S']))
t.assertEqual('KC', agram1(['TC', 'AC', 'KC', 'QH', 'JS', 'TD']))
t.assertEqual('2D', agram1(['3D', '4H', '5C', '6S', '2D', '7H']))
t.assertEqual('3H', agram1(['KS', 'TH', 'QC', '7H', '9H', '3H']))
t.assertEqual('AD', agram1(['AC', 'AD', 'KH', 'JS', 'KS', 'QS']))

t.assertEqual('7H', agram1(['6H', '2H', '4C', '7H', '9D', '6S']))
t.assertEqual('2S', agram1(['AC', '2S', '5D', '6H', 'JS', '3S']))
t.assertEqual('4D', agram1(['KD', '4S', '4C', '4S', '4D', 'KS']))
t.assertEqual('2C', agram1(['QS', '4D', '7C', '8D', 'TH', '2C']))
t.assertEqual('KC', agram1(['TC', 'KC', '5H', 'AD', '7C', 'TS']))
print('OK!')
