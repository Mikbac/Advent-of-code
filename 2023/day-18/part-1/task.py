# Created by MikBac on 2023

import sys

PLAN_SIZE = 2000

plan = []


def main():
	global plan

	for i in range(PLAN_SIZE):
		plan.append(['.'] * PLAN_SIZE)

	sys.setrecursionlimit(PLAN_SIZE * PLAN_SIZE)

	current_location = [0, 0]
	plan[0][0] = '#'

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			direction = line.strip().split(' ')[0]
			length = int(line.strip().split(' ')[1])
			for i in range(length):
				if direction == 'U':
					current_location[0] = current_location[0] - 1
				if direction == 'D':
					current_location[0] = current_location[0] + 1
				if direction == 'L':
					current_location[1] = current_location[1] - 1
				if direction == 'R':
					current_location[1] = current_location[1] + 1

				plan[current_location[0]][current_location[1]] = '#'

	fill_plan([1, 1])

	answer = 0
	for i in range(PLAN_SIZE):
		answer += plan[i].count('#')

	print('Answer: {}'.format(answer))


def fill_plan(position):
	global plan

	plan[position[0]][position[1]] = '#'

	if plan[position[0] + 1][position[1]] != '#':
		fill_plan([position[0] + 1, position[1]])
	if plan[position[0] - 1][position[1]] != '#':
		fill_plan([position[0] - 1, position[1]])
	if plan[position[0]][position[1] + 1] != '#':
		fill_plan([position[0], position[1] + 1])
	if plan[position[0]][position[1] - 1] != '#':
		fill_plan([position[0], position[1] - 1])


if __name__ == "__main__":
	main()
