# cat sample-1 | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

import math


def main():
	starts = []
	instructions = input().strip()
	input().strip()
	map_paths = {}
	while True:
		try:
			map_entry = input().strip()
			key = map_entry.split('=')[0].strip()
			map_paths[key] = map_entry.split('=')[1].replace(' ', '').strip()[1:8].split(
				',')
			if key[2] == 'A':
				starts.append(key)
		except EOFError:
			break

	instructions_size = len(instructions)
	step_sums = []

	for start in starts:
		step = 0
		step_sum = 0
		location = start

		while location[2] != 'Z':
			if instructions_size == step:
				step = 0

			instruction = instructions[step]

			if instruction == 'L':
				location = map_paths[location][0]
			else:
				location = map_paths[location][1]

			step += 1
			step_sum += 1

		step_sums.append(step_sum)

	answer = math.lcm(*step_sums)

	print('Answer: {}'.format(answer))


if __name__ == "__main__":
	main()
