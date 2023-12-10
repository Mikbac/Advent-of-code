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
visited = []


def main():
	global pipe_map
	global visited
	while True:
		try:
			pipe_map.append(list(input().strip()))
		except EOFError:
			break

	for i in range(len(pipe_map)):
		pipe_map[i].insert(0, '#')
		pipe_map[i].append('#')
	pipe_map.insert(0, list('#' * (len(pipe_map[0]))))
	pipe_map.append(list('#' * (len(pipe_map[0]))))

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

	bfs(visited, start_location)

	is_changed = True
	while is_changed:
		is_changed = False
		for i in range(1, len(pipe_map) - 1):
			for j in range(1, len(pipe_map[i]) - 1):
				if pipe_map[i][j] == '#':
					continue

				location = '{}-{}'.format(str(i), str(j))

				if location not in visited and (
						pipe_map[i + 1][j] == '#' or pipe_map[i - 1][j] == '#' or pipe_map[i][j + 1] == '#' or
						pipe_map[i][j - 1] == '#'):
					pipe_map[i][j] = '#'
					is_changed = True

	print(pipe_map)

	sum = 0
	for i in range(1, len(pipe_map) - 1):
		for j in range(1, len(pipe_map[i]) - 1):
			location = '{}-{}'.format(str(i), str(j))
			if location not in visited and pipe_map[i][j] != '#':
				pipe_map[i][j] = '0'
				sum += 1
	print(nodes_map)
	print(visited)

	print('Answer: {}'.format(sum))


# 230 - too low
# 240 - too low
# 323 - too low


def go_deep():
	global nodes_map
	global visited


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


def map_nodes(location_Y, location_X):
	global pipe_map
	global nodes_map

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == '7' or pipe_map[location_Y][
		location_X] == 'F') and pipe_map[location_Y + 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == 'L' or pipe_map[location_Y][
		location_X] == 'J') and pipe_map[location_Y - 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == 'F' or pipe_map[location_Y][
		location_X] == 'L') and pipe_map[location_Y][location_X + 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == '7' or pipe_map[location_Y][
		location_X] == 'J') and pipe_map[location_Y][location_X - 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == '7' or pipe_map[location_Y][
		location_X] == 'F') and pipe_map[location_Y + 1][location_X] == 'L':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == 'J' or pipe_map[location_Y][
		location_X] == '7') and pipe_map[location_Y][location_X - 1] == 'L':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == '7' or pipe_map[location_Y][
		location_X] == 'F') and pipe_map[location_Y + 1][location_X] == 'J':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == 'F' or pipe_map[location_Y][
		location_X] == 'L') and pipe_map[location_Y][location_X + 1] == 'J':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == 'L' or pipe_map[location_Y][
		location_X] == 'J') and pipe_map[location_Y - 1][location_X] == '7':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == 'F' or pipe_map[location_Y][
		location_X] == 'L') and pipe_map[location_Y][location_X + 1] == '7':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if (pipe_map[location_Y][location_X] == '|' or pipe_map[location_Y][location_X] == 'L' or pipe_map[location_Y][
		location_X] == 'J') and pipe_map[location_Y - 1][location_X] == 'F':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if (pipe_map[location_Y][location_X] == '-' or pipe_map[location_Y][location_X] == 'J' or pipe_map[location_Y][
		location_X] == '7') and pipe_map[location_Y][location_X - 1] == 'F':
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
