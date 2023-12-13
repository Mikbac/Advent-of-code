# Created by MikBac on 2023

import copy


def main():
	sum = 0
	with open('input', 'r', encoding='utf-8') as input_:
		pattern = []
		for row, line in enumerate(input_):
			if line.strip() == '':
				sum += find_pattern_with_smudge(pattern)
				pattern = []
			else:
				pattern.append(list(line.strip()))
		sum += find_pattern_with_smudge(pattern)

	print('Answer: {}'.format(sum))


def find_pattern_with_smudge(pattern):
	old_pattern_value = find_pattern_value(pattern)

	for i in range(len(pattern)):
		for j in range(len(pattern[0])):
			new_pattern = copy.deepcopy(pattern)
			if pattern[i][j] == '#':
				new_pattern[i][j] = '.'
			else:
				new_pattern[i][j] = '#'
			pattern_value = find_pattern_value(new_pattern, old_pattern_value)
			if pattern_value != 0:
				return pattern_value


def find_pattern_value(pattern, old_pattern_value=0):
	for i in range(len(pattern) - 1):
		if pattern[i] == pattern[i + 1]:
			if check_row_pattern(pattern, i, i + 1):
				if (i + 1) * 100 != old_pattern_value:
					return (i + 1) * 100
	for i in range(len(pattern[0]) - 1):
		column_one = ''
		column_two = ''
		for j in range(len(pattern)):
			column_one += pattern[j][i]
			column_two += pattern[j][i + 1]
		if column_one == column_two:
			if check_column_pattern(pattern, i, i + 1):
				if i + 1 != old_pattern_value:
					return i + 1
	return 0


def check_row_pattern(pattern, typ, bottom):
	couter = 0
	while True:
		if typ - couter < 0 or bottom + couter == len(pattern):
			return True
		if pattern[typ - couter] != pattern[bottom + couter]:
			return False
		couter += 1


def check_column_pattern(pattern, left, right):
	couter = 0
	while True:
		if left - couter < 0 or right + couter == len(pattern[0]):
			return True
		column_one = ''
		column_two = ''
		for j in range(len(pattern)):
			column_one += pattern[j][left - couter]
			column_two += pattern[j][right + couter]
		if column_one != column_two:
			return False
		couter += 1


if __name__ == "__main__":
	main()
