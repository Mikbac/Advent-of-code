# Created by MikBac on 2023

import copy
import sys

map = []
visited_map = []
entries_map = []


def main():
	global map
	global visited_map
	global entries_map

	results = []

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			map.append(list('+' + line.strip() + '+'))

	sys.setrecursionlimit(len(map) * len(map[0]))

	map.append(list('+' * len(map[0])))
	map.insert(0, list('+' * len(map[0])))

	for i in range(1, len(map[1]) - 1):
		if [1, i] in entries_map:
			continue
		visited_map = copy.deepcopy(map)
		go([1, i], 1, 'v', [])

		sum = 0
		for i in range(len(visited_map)):
			sum += visited_map[i].count('#')

		results.append(sum)

	for i in range(1, len(map[1]) - 1):
		if [len(map) - 2, i] in entries_map:
			continue
		visited_map = copy.deepcopy(map)
		go([len(map) - 2, i], 1, '^', [])

		sum = 0
		for i in range(len(visited_map)):
			sum += visited_map[i].count('#')

		results.append(sum)

	for i in range(1, len(map) - 1):
		if [i, 1] in entries_map:
			continue
		visited_map = copy.deepcopy(map)
		go([i, 1], 1, '>', [])

		sum = 0
		for i in range(len(visited_map)):
			sum += visited_map[i].count('#')

		results.append(sum)

	for i in range(1, len(map) - 1):
		if [i, len(map[i]) - 2] in entries_map:
			continue
		visited_map = copy.deepcopy(map)
		go([i, len(map[i]) - 2], 1, '<', [])

		sum = 0
		for i in range(len(visited_map)):
			sum += visited_map[i].count('#')

		results.append(sum)

	answer = max(results)
	print('Answer: {}'.format(answer))


def go(current_position, steps, direction, visited):
	global map
	global visited_map
	global entries_map

	if map[current_position[0]][current_position[1]] == '+':
		if direction == '>':
			entries_map.append([current_position[0], current_position[1] - 1])
		if direction == '<':
			entries_map.append([current_position[0], current_position[1] + 1])
		if direction == '^':
			entries_map.append([current_position[0] + 1, current_position[1]])
		if direction == 'v':
			entries_map.append([current_position[0] - 1, current_position[1]])
		return

	visited.append(current_position)

	if steps > 10:
		for v in range(len(visited) - 3):
			if visited[v] == visited[-2] and visited[v + 1] == visited[-1]:
				return

	visited_map[current_position[0]][current_position[1]] = '#'

	if map[current_position[0]][current_position[1]] == '.':
		if direction == '>':
			go([current_position[0], current_position[1] + 1], steps + 1, direction, visited)
		if direction == '<':
			go([current_position[0], current_position[1] - 1], steps + 1, direction, visited)
		if direction == '^':
			go([current_position[0] - 1, current_position[1]], steps + 1, direction, visited)
		if direction == 'v':
			go([current_position[0] + 1, current_position[1]], steps + 1, direction, visited)

	if map[current_position[0]][current_position[1]] == '\\':
		if direction == '>':
			go([current_position[0] + 1, current_position[1]], steps + 1, 'v', visited)
		if direction == '<':
			go([current_position[0] - 1, current_position[1]], steps + 1, '^', visited)
		if direction == '^':
			go([current_position[0], current_position[1] - 1], steps + 1, '<', visited)
		if direction == 'v':
			go([current_position[0], current_position[1] + 1], steps + 1, '>', visited)

	if map[current_position[0]][current_position[1]] == '/':
		if direction == '>':
			go([current_position[0] - 1, current_position[1]], steps + 1, '^', visited)
		if direction == '<':
			go([current_position[0] + 1, current_position[1]], steps + 1, 'v', visited)
		if direction == '^':
			go([current_position[0], current_position[1] + 1], steps + 1, '>', visited)
		if direction == 'v':
			go([current_position[0], current_position[1] - 1], steps + 1, '<', visited)

	if map[current_position[0]][current_position[1]] == '|':
		if direction == '>' or direction == '<':
			go([current_position[0] - 1, current_position[1]], steps + 1, '^', visited)
			go([current_position[0] + 1, current_position[1]], steps + 1, 'v', visited)
		if direction == '^':
			go([current_position[0] - 1, current_position[1]], steps + 1, '^', visited)
		if direction == 'v':
			go([current_position[0] + 1, current_position[1]], steps + 1, 'v', visited)

	if map[current_position[0]][current_position[1]] == '-':
		if direction == '^' or direction == 'v':
			go([current_position[0], current_position[1] + 1], steps + 1, '>', visited)
			go([current_position[0], current_position[1] - 1], steps + 1, '<', visited)
		if direction == '>':
			go([current_position[0], current_position[1] + 1], steps + 1, '>', visited)
		if direction == '<':
			go([current_position[0], current_position[1] - 1], steps + 1, '<', visited)


if __name__ == "__main__":
	main()
