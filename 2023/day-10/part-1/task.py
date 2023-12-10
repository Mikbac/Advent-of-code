# cat sample-1 | python3 task.py
# cat sample-2 | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

pipe_map = []
nodes_map = {}
# e.g.
# {
# 	'1': ['2','3'],
# 	'2': ['3','4'],
# 	'3': [],
# 	'4': []
# }
bfs_queue = []


def main():
	global pipe_map
	while True:
		try:
			pipe_map.append(list(input().strip()))
		except EOFError:
			break

	for i in range(len(pipe_map)):
		pipe_map[i].insert(0, '.')
		pipe_map[i].append('.')
	pipe_map.insert(0, list('.' * (len(pipe_map[0]))))
	pipe_map.append(list('.' * (len(pipe_map[0]))))

	for i in range(1, len(pipe_map) - 1):
		for j in range(1, len(pipe_map[i]) - 1):
			map_nodes(i, j)

	start_location_Y = 0
	start_location_X = 0

	for i in range(1, len(pipe_map) - 1):
		for j in range(1, len(pipe_map[i]) - 1):
			if pipe_map[i][j] == 'S':
				start_location_Y = i
				start_location_X = j

	start_location = '{}-{}'.format(str(start_location_Y), str(start_location_X))
	visited = []

	bfs(visited, start_location)

	path = shortest_path(start_location, visited[-1])

	max_value = len(path) - 1

	print('Answer: {}'.format(max_value))


def bfs(visited, node):
	global nodes_map
	global bfs_queue
	visited.append(node)
	bfs_queue.append(node)

	while bfs_queue:
		m = bfs_queue.pop(0)

		for neighbour in nodes_map[m]:
			if neighbour not in visited:
				visited.append(neighbour)
				bfs_queue.append(neighbour)


def shortest_path(start_node, end_node):
	global nodes_map
	path_list = [[start_node]]
	path_index = 0
	previous_nodes = {start_node}
	if start_node == end_node:
		return path_list[0]

	while path_index < len(path_list):
		current_path = path_list[path_index]
		last_node = current_path[-1]
		next_nodes = nodes_map[last_node]
		if end_node in next_nodes:
			current_path.append(end_node)
			return current_path
		for next_node in next_nodes:
			if not next_node in previous_nodes:
				new_path = current_path[:]
				new_path.append(next_node)
				path_list.append(new_path)
				previous_nodes.add(next_node)
		path_index += 1
	return []


def map_nodes(location_Y, location_X):
	global pipe_map
	global nodes_map

	if pipe_map[location_Y + 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y - 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X + 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y][location_X - 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if pipe_map[location_Y + 1][location_X] == 'L':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y][location_X - 1] == 'L':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if pipe_map[location_Y + 1][location_X] == 'J':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y][location_X + 1] == 'J':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y - 1][location_X] == '7':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X + 1] == '7':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y - 1][location_X] == 'F':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X - 1] == 'F':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	current_location = '{}-{}'.format(str(location_Y), str(location_X))

	if not current_location in nodes_map:
		nodes_map[current_location] = []


def add_to_map(current_location_Y, current_location_X, new_location_Y, new_location_X):
	global nodes_map
	current_location = '{}-{}'.format(str(current_location_Y), str(current_location_X))
	new_location = '{}-{}'.format(str(new_location_Y), str(new_location_X))
	if current_location in nodes_map:
		nodes_map[current_location].append(new_location)
	else:
		nodes_map[current_location] = [new_location]


if __name__ == "__main__":
	main()
