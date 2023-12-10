# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

from functools import cmp_to_key
from itertools import groupby

CARD_ORDERS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def main():
	cards = []

	while True:
		try:
			cards.append(input().strip().split())
		except EOFError:
			break

	sorted_cards = sorted(cards, key=cmp_to_key(is_bigger))

	response = 0
	for i in range(len(sorted_cards)):
		response += int(sorted_cards[i][1]) * (i + 1)

	print('Answer: {}'.format(response))


def is_bigger(card_one, card_two):
	card_one_stats = [''.join(g) for _, g in groupby(sorted(card_one[0]))]
	card_two_stats = [''.join(g) for _, g in groupby(sorted(card_two[0]))]

	card_one_type = get_type(card_one_stats)
	card_two_type = get_type(card_two_stats)

	if card_one_type > card_two_type:
		return 1
	elif card_one_type < card_two_type:
		return -1
	else:
		for i in range(len(card_one[0])):
			if card_one[0][i] == card_two[0][i]:
				continue
			return CARD_ORDERS.index(card_two[0][i]) - CARD_ORDERS.index(card_one[0][i])


def get_type(card_stats):
	jokers_quantity = 0
	for i in card_stats:
		if i[0] == 'J':
			jokers_quantity = len(i)
			card_stats.remove(i)
			break
	card_stats_sorted = sorted(card_stats, key=len, reverse=True)

	# 6 - Five of a kind
	if len(card_stats_sorted) >= 1 and len(card_stats_sorted[0]) + jokers_quantity == 5:
		return 6
	if len(card_stats_sorted) == 0 and jokers_quantity == 5:
		return 6

	# 5 - Four of a kind
	if len(card_stats_sorted) >= 1 and len(card_stats_sorted[0]) + jokers_quantity == 4:
		return 5
	if len(card_stats_sorted) == 0 and jokers_quantity == 4:
		return 5

	# 4 - Full house
	if len(card_stats_sorted) >= 2 and (len(card_stats_sorted[0]) + len(card_stats_sorted[1]) + jokers_quantity) == 5:
		return 4
	if len(card_stats_sorted) == 1 and (len(card_stats_sorted[0]) + jokers_quantity) == 5:
		return 4
	if len(card_stats_sorted) == 0 and jokers_quantity == 5:
		return 4

	# 3 - Three of a kind
	if len(card_stats_sorted) >= 1 and (len(card_stats_sorted[0]) + jokers_quantity) == 3:
		return 3
	if len(card_stats_sorted) == 0 and jokers_quantity == 3:
		return 3

	# 2 - Two pair
	if len(card_stats_sorted) >= 2 and (len(card_stats_sorted[0]) + len(card_stats_sorted[1]) + jokers_quantity) == 4:
		return 2
	if len(card_stats_sorted) == 1 and (len(card_stats_sorted[0]) + jokers_quantity) == 4:
		return 2
	if len(card_stats_sorted) == 0 and jokers_quantity == 4:
		return 2

	# 1 - One pair
	if (len(card_stats_sorted[0]) + jokers_quantity) == 2:
		return 1

	# 0 - High card
	if len(card_stats) + jokers_quantity == 5:
		return 0


if __name__ == "__main__":
	main()
