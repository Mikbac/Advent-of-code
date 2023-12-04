# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

import copy

cards_quantity = 0
cards_list = []


def main():
	global cards_quantity
	global cards_list

	while True:
		try:
			cards_list.append(input().strip())
		except EOFError:
			break

	cards_quantity = len(cards_list)

	for i in range(len(cards_list)):
		resolve_card(cards_list[i])

	print('Answer: {}'.format(cards_quantity))


def resolve_card(card):
	global cards_quantity
	global cards_list

	card_id = int(card.split(':')[0].split()[1])
	win_numbers = card.split(':')[1].split('|')[0].split()
	elf_numbers = card.split(':')[1].split('|')[1].split()

	win_quantity = 0

	for wn in win_numbers:
		if wn in elf_numbers:
			win_quantity += 1

	for i in range(card_id, card_id + win_quantity):
		cards_quantity += 1
		resolve_card(copy.deepcopy(cards_list[i]))


if __name__ == "__main__":
	main()
