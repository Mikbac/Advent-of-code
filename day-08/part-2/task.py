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

	scenic_scores = []

	for x in range(len(tress)):
		for y in range(len(tress)):
			scenic_scores.append(get_visible_score(x, y))

	max_score = max(scenic_scores)

	print('Answer: {}'.format(max_score))


def get_visible_score(x, y):
	score_1 = 0
	score_2 = 0
	score_3 = 0
	score_4 = 0

	new_x = x
	while new_x < len(tress) - 1:
		new_x += 1
		score_1 += 1
		if tress[x][y] <= tress[new_x][y]:
			break

	new_x = x
	while new_x > 0:
		new_x -= 1
		score_2 += 1
		if tress[x][y] <= tress[new_x][y]:
			break

	new_y = y
	while new_y < len(tress) - 1:
		new_y += 1
		score_3 += 1
		if tress[x][y] <= tress[x][new_y]:
			break

	new_y = y
	while new_y > 0:
		new_y -= 1
		score_4 += 1
		if tress[x][y] <= tress[x][new_y]:
			break

	return score_1 * score_2 * score_3 * score_4


if __name__ == "__main__":
	main()
