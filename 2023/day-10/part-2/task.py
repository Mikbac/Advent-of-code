# cat sample-1 | python3 task.py
# cat sample-2 | python3 task.py
# cat sample-3 | python3 task.py
# cat sample-4 | python3 task.py
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

	# add additional frame
	for i in range(len(pipe_map)):
		pipe_map[i].insert(0, '#')
		pipe_map[i].append('#')
	pipe_map.insert(0, list('#' * (len(pipe_map[0]))))
	pipe_map.append(list('#' * (len(pipe_map[0]))))

	# create graph map
	for i in range(1, len(pipe_map) - 1):
		for j in range(1, len(pipe_map[i]) - 1):
			map_nodes(i, j)

	# find S (start)
	start_location_Y = 0
	start_location_X = 0

	for i in range(1, len(pipe_map) - 1):
		for j in range(1, len(pipe_map[i]) - 1):
			if pipe_map[i][j] == 'S':
				start_location_Y = i
				start_location_X = j

	start_location = '{}-{}'.format(str(start_location_Y), str(start_location_X))

	# find main path
	bfs(start_location)

	# check if S was inserted from top
	is_start_has_top_insert = pipe_map[start_location_Y - 1][start_location_X] in '|7F'

	# find nested/internal fields
	sum = 0
	for i in range(len(pipe_map)):
		internal = 0
		for j in range(len(pipe_map[i])):
			location = '{}-{}'.format(str(i), str(j))
			if location in visited:
				if (pipe_map[i][j] == "S" and is_start_has_top_insert) or pipe_map[i][j] in "|JL":
					if internal == 0:
						internal = 1
					else:
						internal = 0
			else:
				sum += internal

	print('Answer: {}'.format(sum))


def bfs(start_location):
	global nodes_map
	global bfs_queue
	global visited
	visited.append(start_location)
	bfs_queue.append(start_location)

	while bfs_queue:
		m = bfs_queue.pop(0)

		for neighbour in nodes_map[m]:
			if neighbour not in visited:
				visited.append(neighbour)
				bfs_queue.append(neighbour)


def map_nodes(location_Y, location_X):
	global pipe_map
	global nodes_map

	if pipe_map[location_Y][location_X] in 'S|7F' and pipe_map[location_Y + 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y][location_X] in 'S|LJ' and pipe_map[location_Y - 1][location_X] == '|':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X] in 'S-FL' and pipe_map[location_Y][location_X + 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y][location_X] in 'S-J7' and pipe_map[location_Y][location_X - 1] == '-':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if pipe_map[location_Y][location_X] in 'S|7F' and pipe_map[location_Y + 1][location_X] == 'L':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y][location_X] in 'S-J7' and pipe_map[location_Y][location_X - 1] == 'L':
		add_to_map(location_Y, location_X, location_Y, location_X - 1)

	if pipe_map[location_Y][location_X] in 'S|7F' and pipe_map[location_Y + 1][location_X] == 'J':
		add_to_map(location_Y, location_X, location_Y + 1, location_X)

	if pipe_map[location_Y][location_X] in 'S-FL' and pipe_map[location_Y][location_X + 1] == 'J':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y][location_X] in 'S|LJ' and pipe_map[location_Y - 1][location_X] == '7':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X] in 'S-FL' and pipe_map[location_Y][location_X + 1] == '7':
		add_to_map(location_Y, location_X, location_Y, location_X + 1)

	if pipe_map[location_Y][location_X] in 'S|LJ' and pipe_map[location_Y - 1][location_X] == 'F':
		add_to_map(location_Y, location_X, location_Y - 1, location_X)

	if pipe_map[location_Y][location_X] in 'S-J7' and pipe_map[location_Y][location_X - 1] == 'F':
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
