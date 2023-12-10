# cat sample-1 | python3 task.py
# cat sample-2 | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

START = 'AAA'
GOAL = 'ZZZ'


def main():
	instructions = input().strip()
	input().strip()
	map_paths = {}
	while True:
		try:
			map_entry = input().strip()
			map_paths[map_entry.split('=')[0].strip()] = map_entry.split('=')[1].replace(' ', '').strip()[1:8].split(
				',')
		except EOFError:
			break

	instructions_size = len(instructions)

	step = 0
	step_sum = 0
	location = START

	while location != GOAL:
		if instructions_size == step:
			step = 0

		instruction = instructions[step]

		if instruction == 'L':
			location = map_paths[location][0]
		else:
			location = map_paths[location][1]

		step += 1
		step_sum += 1

	print('Answer: {}'.format(step_sum))


if __name__ == "__main__":
	main()
