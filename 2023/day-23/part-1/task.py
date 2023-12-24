# Created by MikBac on 2023

import sys

map = []
end_position = ()
longest_path = 0


def main():
	global map
	global end_position
	global longest_path

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			map.append(list(line.strip()))

	sys.setrecursionlimit(len(map) * len(map[0]))

	start_position = []
	for i in range(len(map[0])):
		if map[0][i] == '.':
			start_position = (1, i)
			break

	end_position = []
	for i in range(len(map[len(map) - 1])):
		if map[len(map) - 1][i] == '.':
			end_position = (len(map) - 1, i)
			break

	find_longest_path(start_position, set())

	print('Answer: {}'.format(longest_path))


def find_longest_path(point, path):
	global map
	global end_position
	global longest_path

	if map[point[0]][point[1]] == '#' or point in path:
		return

	path.add(point)

	if point == end_position:
		if longest_path < len(path):
			longest_path = len(path)
		return

	if map[point[0]][point[1]] == '.':
		find_longest_path((point[0] + 1, point[1]), path.copy())
		find_longest_path((point[0] - 1, point[1]), path.copy())
		find_longest_path((point[0], point[1] + 1), path.copy())
		find_longest_path((point[0], point[1] - 1), path.copy())

	if map[point[0]][point[1]] == '^':
		find_longest_path((point[0] - 1, point[1]), path.copy())
	if map[point[0]][point[1]] == 'v':
		find_longest_path((point[0] + 1, point[1]), path.copy())
	if map[point[0]][point[1]] == '<':
		find_longest_path((point[0], point[1] - 1), path.copy())
	if map[point[0]][point[1]] == '>':
		find_longest_path((point[0], point[1] + 1), path.copy())


if __name__ == "__main__":
	main()
