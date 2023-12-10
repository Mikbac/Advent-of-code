# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	engine = []
	engine_sum = 0
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
		number = ''
		active_number = False
		for w in range(1, engine_width - 1):
			if engine[h][w].isdigit():
				number += engine[h][w]
				if isSymbol(engine[h - 1][w + 1]) or isSymbol(engine[h][w + 1]) or isSymbol(
						engine[h + 1][w + 1]) or isSymbol(engine[h + 1][w]) or isSymbol(
					engine[h + 1][w - 1]) or isSymbol(
					engine[h][w - 1]) or isSymbol(engine[h - 1][w - 1]) or isSymbol(engine[h - 1][w]):
					active_number = True
			elif len(number) != 0 and active_number:
				engine_sum += int(number)
				number = ''
				active_number = False
			else:
				number = ''
				active_number = False

		# check when number is at the end of the line
		if len(number) != 0 and active_number:
			engine_sum += int(number)

	print('Answer: {}'.format(engine_sum))


def isSymbol(char):
	if not char.isdigit() and char != '.':
		return True
	else:
		return False


if __name__ == "__main__":
	main()
