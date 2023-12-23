# Created by MikBac on 2023

import copy

STEPS_NUMBER = 64

elf_map = []


def main():
	global elf_map
	global last_step_map
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			elf_map.append(list(line.strip()))

	last_step_map = copy.deepcopy(elf_map)

	s_position = ()
	for i in range(len(elf_map)):
		for j in range(len(elf_map[i])):
			if elf_map[i][j] == 'S':
				s_position = (i, j)

	elf_next_queue = set()
	elf_next_queue.add(s_position)

	for i in range(STEPS_NUMBER + 1):
		elf_queue = copy.deepcopy(elf_next_queue)
		elf_next_queue = set()

		while len(elf_queue) != 0:
			ec = elf_queue.pop()

			if i == STEPS_NUMBER:
				last_step_map[ec[0]][ec[1]] = 'O'

			if ec[0] - 1 >= 0 and elf_map[ec[0] - 1][ec[1]] != '#':
				elf_next_queue.add((ec[0] - 1, ec[1]))

			if ec[0] + 1 < len(elf_map) and elf_map[ec[0] + 1][ec[1]] != '#':
				elf_next_queue.add((ec[0] + 1, ec[1]))

			if ec[1] - 1 >= 0 and elf_map[ec[0]][ec[1] - 1] != '#':
				elf_next_queue.add((ec[0], ec[1] - 1))

			if ec[1] + 1 < len(elf_map[0]) and elf_map[ec[0]][ec[1] + 1] != '#':
				elf_next_queue.add((ec[0], ec[1] + 1))

	ans_sum = 0
	for i in last_step_map:
		print(''.join(i))
		ans_sum += i.count('O')

	print('Answer: {}'.format(ans_sum))


if __name__ == "__main__":
	main()
