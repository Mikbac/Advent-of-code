# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	points_sum = 0
	while True:
		try:
			card = input().strip()
		except EOFError:
			break

		win_numbers = card.split(':')[1].split('|')[0].split()
		elf_numbers = card.split(':')[1].split('|')[1].split()

		card_points = 0

		for wn in win_numbers:
			if wn in elf_numbers:
				if card_points == 0:
					card_points = 1
				else:
					card_points *= 2
		points_sum += card_points

	print('Answer: {}'.format(points_sum))


if __name__ == "__main__":
	main()
