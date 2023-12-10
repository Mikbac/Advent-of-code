# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

tress = []


def main():
	while True:
		try:
			tress.append(list(input().strip()))
		except EOFError:
			break

	visible_tress = 0

	for x in range(len(tress)):
		for y in range(len(tress)):
			if is_visible(x, y):
				visible_tress += 1

	print('Answer: {}'.format(visible_tress))


def is_visible(x, y):
	if x == 0 or y == 0 or x == len(tress) - 1 or y == len(tress) - 1:
		return True
	else:
		new_x = x
		while new_x < len(tress) - 1:
			new_x += 1
			if tress[x][y] <= tress[new_x][y]:
				break
			if new_x == len(tress) - 1:
				return True

		new_x = x
		while new_x > 0:
			new_x -= 1
			if tress[x][y] <= tress[new_x][y]:
				break
			if new_x == 0:
				return True

		new_y = y
		while new_y < len(tress) - 1:
			new_y += 1
			if tress[x][y] <= tress[x][new_y]:
				break
			if new_y == len(tress) - 1:
				return True

		new_y = y
		while new_y > 0:
			new_y -= 1
			if tress[x][y] <= tress[x][new_y]:
				break
			if new_y == 0:
				return True

		return False


if __name__ == "__main__":
	main()
