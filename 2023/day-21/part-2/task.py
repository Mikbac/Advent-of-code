# Created by MikBac on 2023

import copy

STEPS_NUMBER = 26501365

elf_map = []


def main():
	global elf_map

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			elf_map.append(list(line.strip()))

	s_position = []
	for i in range(len(elf_map)):
		for j in range(len(elf_map[i])):
			if elf_map[i][j] == 'S':
				s_position = [i, j, 0, 0]

	# 65 -> 3751
	y1 = get_elf_steps(s_position, len(elf_map[0]) // 2)
	# 196 -> 33531
	y2 = get_elf_steps(s_position, len(elf_map[0]) // 2 + len(elf_map[0]))
	# 327 -> 92991
	y3 = get_elf_steps(s_position, len(elf_map[0]) // 2 + (2 * len(elf_map[0])))
	n = STEPS_NUMBER // len(elf_map[0])

	# Quadratic Interpolation
	answer = y1 * (n - 1) * (n - 2) / 2 - y2 * n * (n - 2) + y3 * n * (n - 1) / 2

	print('Answer: {}'.format(answer))


def get_elf_steps(start_position, steps_number):
	global elf_map

	elf_next_queue = [start_position]

	for _ in range(steps_number):

		elf_queue = copy.deepcopy(elf_next_queue)
		elf_next_queue = []

		while len(elf_queue) != 0:
			ec = elf_queue.pop(0)

			if ec[0] - 1 >= 0:
				if elf_map[ec[0] - 1][ec[1]] != '#' and [ec[0] - 1, ec[1], ec[2], ec[3]] not in elf_next_queue:
					elf_next_queue.append([ec[0] - 1, ec[1], ec[2], ec[3]])
			else:
				if [len(elf_map) - 1, ec[1], ec[2] - 1, ec[3]] not in elf_next_queue:
					elf_next_queue.append([len(elf_map) - 1, ec[1], ec[2] - 1, ec[3]])

			if ec[0] + 1 < len(elf_map):
				if elf_map[ec[0] + 1][ec[1]] != '#' and [ec[0] + 1, ec[1], ec[2], ec[3]] not in elf_next_queue:
					elf_next_queue.append([ec[0] + 1, ec[1], ec[2], ec[3]])
			else:
				if [0, ec[1], ec[2] + 1, ec[3]] not in elf_next_queue:
					elf_next_queue.append([0, ec[1], ec[2] + 1, ec[3]])

			if ec[1] - 1 >= 0:
				if elf_map[ec[0]][ec[1] - 1] != '#' and [ec[0], ec[1] - 1, ec[2], ec[3]] not in elf_next_queue:
					elf_next_queue.append([ec[0], ec[1] - 1, ec[2], ec[3]])
			else:
				if [ec[0], len(elf_map[0]) - 1, ec[2], ec[3] - 1] not in elf_next_queue:
					elf_next_queue.append([ec[0], len(elf_map[0]) - 1, ec[2], ec[3] - 1])

			if ec[1] + 1 < len(elf_map[0]):
				if elf_map[ec[0]][ec[1] + 1] != '#' and [ec[0], ec[1] + 1, ec[2], ec[3]] not in elf_next_queue:
					elf_next_queue.append([ec[0], ec[1] + 1, ec[2], ec[3]])
			else:
				if [ec[0], 0, ec[2], ec[3] + 1] not in elf_next_queue:
					elf_next_queue.append([ec[0], 0, ec[2], ec[3] + 1])

	return len(elf_next_queue)


if __name__ == "__main__":
	main()
