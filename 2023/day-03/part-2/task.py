# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	engine = []
	gears_sum = 0
	while True:
		try:
			engine.append('.' + input().strip() + '.')
		except EOFError:
			break
	engine_height = len(engine)
	engine_width = len(engine[0])

	engine.insert(0, '.' * engine_width)
	engine.append('.' * engine_width)

	for h in range(1, engine_height + 1):

		for w in range(1, engine_width - 1):
			if engine[h][w] == '*':

				connected_numbers = []

				if engine[h - 1][w + 1].isdigit():
					connected_numbers.append(getNumber(h - 1, w + 1, engine))
				if engine[h][w + 1].isdigit():
					connected_numbers.append(getNumber(h, w + 1, engine))
				if engine[h + 1][w + 1].isdigit():
					connected_numbers.append(getNumber(h + 1, w + 1, engine))
				if engine[h + 1][w].isdigit():
					connected_numbers.append(getNumber(h + 1, w, engine))
				if engine[h + 1][w - 1].isdigit():
					connected_numbers.append(getNumber(h + 1, w - 1, engine))
				if engine[h][w - 1].isdigit():
					connected_numbers.append(getNumber(h, w - 1, engine))
				if engine[h - 1][w - 1].isdigit():
					connected_numbers.append(getNumber(h - 1, w - 1, engine))
				if engine[h - 1][w].isdigit():
					connected_numbers.append(getNumber(h - 1, w, engine))

				# In this case, I assumed that two numbers are never the same
				without_duplicates_connected_numbers = list(dict.fromkeys(connected_numbers))

				if len(without_duplicates_connected_numbers) == 2:
					gears_sum += int(without_duplicates_connected_numbers[0]) * int(
						without_duplicates_connected_numbers[1])

	print('Answer: {}'.format(gears_sum))


def getNumber(h, w, engine):
	check_right = w + 1
	check_left = w - 1
	number = engine[h][w]
	while engine[h][check_right].isdigit():
		number += engine[h][check_right]
		check_right += 1
	while engine[h][check_left].isdigit():
		number = engine[h][check_left] + number
		check_left -= 1
	return number


if __name__ == "__main__":
	main()
