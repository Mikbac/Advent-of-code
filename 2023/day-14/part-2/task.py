# Created by MikBac on 2023

import copy

CYCLES = 1_000_000_000

cycles_cache = {}


def main():
	sum = 0
	platform = []
	with open('input', 'r', encoding='utf-8') as input_:

		for row, line in enumerate(input_):
			platform.append(list(line.strip()))
	c = 0
	while c < CYCLES:
		if platform in cycles_cache.values():
			key = list(filter(lambda x: cycles_cache[x] == platform, cycles_cache))[0]
			cycle_value = c - key
			while True:
				if c + cycle_value < CYCLES:
					c += cycle_value
				else:
					break
		else:
			cycles_cache[c] = copy.deepcopy(platform)

		# north
		for i in range(1, len(platform)):
			for j in range(len(platform[i])):
				for k in range(i, 0, -1):
					if platform[k][j] == 'O' and platform[k - 1][j] == '.':
						platform[k][j] = '.'
						platform[k - 1][j] = 'O'
					else:
						break

		# west
		for i in range(len(platform)):
			for j in range(1, len(platform[i])):
				for k in range(j, 0, -1):
					if platform[i][k] == 'O' and platform[i][k - 1] == '.':
						platform[i][k] = '.'
						platform[i][k - 1] = 'O'
					else:
						break

		# south
		for i in reversed(range(len(platform) - 1)):
			for j in range(len(platform[i])):
				for k in range(i, len(platform) - 1):
					if platform[k][j] == 'O' and platform[k + 1][j] == '.':
						platform[k][j] = '.'
						platform[k + 1][j] = 'O'
					else:
						break

		# east
		for i in range(len(platform)):
			for j in reversed(range(len(platform[i]) - 1)):
				for k in range(j, len(platform[i]) - 1):
					if platform[i][k] == 'O' and platform[i][k + 1] == '.':
						platform[i][k] = '.'
						platform[i][k + 1] = 'O'
					else:
						break
		c += 1

	for i in range(len(platform)):
		sum += platform[i].count('O') * (len(platform) - i)

	print('Answer: {}'.format(sum))


if __name__ == "__main__":
	main()
