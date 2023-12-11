# Created by MikBac on 2023

import copy


def main():
	galactic = []

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			map_entry = list(line.strip())
			galactic.append(map_entry)
			if '#' not in map_entry:
				galactic.append(copy.deepcopy(map_entry))

	insert_columns = []
	for i in range(len(galactic[0])):
		new_column = True
		for j in range(len(galactic)):
			if galactic[j][i] == '#':
				new_column = False
				break
		if new_column:
			insert_columns.append(i)

	for ic in reversed(insert_columns):
		for i in range(len(galactic)):
			galactic[i].insert(ic, '.')

	galaxy_list = []
	for i in range(len(galactic)):
		for j in range(len(galactic[i])):
			if galactic[i][j] == '#':
				galaxy_list.append([i, j])

	shortest_paths_sum = 0
	round = 1
	for i in range(len(galaxy_list)):
		for j in range(round, len(galaxy_list)):
			shortest_paths_sum += (abs(galaxy_list[i][0] - galaxy_list[j][0])) + (
				abs(galaxy_list[i][1] - galaxy_list[j][1]))

		round += 1

	print('Answer: {}'.format(shortest_paths_sum))


if __name__ == "__main__":
	main()
