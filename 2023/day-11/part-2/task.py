# Created by MikBac on 2023

TIMES_LARGER = 1000000


def main():
	galactic = []
	insert_columns = []
	insert_rows = []

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			map_entry = list(line.strip())
			galactic.append(map_entry)
			if '#' not in map_entry:
				insert_rows.append(row)

	for i in range(len(galactic[0])):
		new_column = True
		for j in range(len(galactic)):
			if galactic[j][i] == '#':
				new_column = False
				break
		if new_column:
			insert_columns.append(i)

	galaxy_list = []
	for i in range(len(galactic)):
		for j in range(len(galactic[i])):
			if galactic[i][j] == '#':
				galaxy_list.append([i, j])

	shortest_paths_sum = 0

	round = 1
	for i in range(len(galaxy_list)):
		for j in range(round, len(galaxy_list)):
			additional_rows = 0
			for r in insert_rows:
				if (galaxy_list[i][0] < r < galaxy_list[j][0]) or (galaxy_list[i][0] > r > galaxy_list[j][0]):
					additional_rows += 1

			additional_columns = 0
			for c in insert_columns:
				if (galaxy_list[i][1] < c < galaxy_list[j][1]) or (galaxy_list[i][1] > c > galaxy_list[j][1]):
					additional_columns += 1

			shortest_paths_sum += (abs(galaxy_list[i][0] - galaxy_list[j][0]) - additional_rows + (
					additional_rows * TIMES_LARGER)) + (
					                      abs(galaxy_list[i][1] - galaxy_list[j][1]) - additional_columns + (
					                      additional_columns * TIMES_LARGER))

		round += 1

	print('Answer: {}'.format(shortest_paths_sum))


if __name__ == "__main__":
	main()
