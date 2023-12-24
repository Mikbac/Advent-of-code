# Created by MikBac on 2023

import sys

nodes_map = {}
end_position = []
longest_path = 0


def main():
	global nodes_map
	global end_position
	global longest_path

	input_map = []
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			input_map.append(list(line.strip()))

	sys.setrecursionlimit(len(input_map) * len(input_map[0]))

	for i in range(1, len(input_map) - 1):
		for j in range(1, len(input_map) - 1):
			if input_map[i + 1][j] != '#':
				add_to_map(i, j, i + 1, j)
			if input_map[i - 1][j] != '#':
				add_to_map(i, j, i - 1, j)
			if input_map[i][j + 1] != '#':
				add_to_map(i, j, i, j + 1)
			if input_map[i][j - 1] != '#':
				add_to_map(i, j, i, j - 1)

	start_position = ()
	for i in range(len(input_map[0])):
		if input_map[0][i] == '.':
			start_position = (0, i)
			add_to_map(0, i, 1, i)
			break

	end_position = ()
	for i in range(len(input_map[len(input_map) - 1])):
		if input_map[len(input_map) - 1][i] == '.':
			end_position = (len(input_map) - 1, i)
			nodes_map[end_position] = ()
			break

	dfs(start_position, set())

	print('Answer: {}'.format(longest_path))


def dfs(current, visited):
	global nodes_map
	global end_position
	global longest_path

	if current == end_position and len(visited) > longest_path:
		longest_path = max(longest_path, len(visited))
		print(longest_path)
		return
	for node in nodes_map[current]:
		if node not in visited:
			visited.add(node)
			dfs(node, visited)
			visited.remove(node)

def add_to_map(current_location_y, current_location_x, new_location_y, new_location_x):
	global nodes_map
	current_location = (current_location_y, current_location_x)
	new_location = (new_location_y, new_location_x)
	nodes_map.setdefault(current_location, []).append(new_location)


if __name__ == "__main__":
	main()
