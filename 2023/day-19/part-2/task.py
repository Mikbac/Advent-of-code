# Created by MikBac on 2023

import copy

accepted_ranges = []


def main():
	global accepted_ranges

	workflows = {}
	elves = []

	with open('input', 'r', encoding='utf-8') as input_:
		are_workflows = True
		for row, line in enumerate(input_):
			if len(line.strip()) == 0:
				are_workflows = False
				continue

			if are_workflows:
				workflows[line.strip().split('{')[0]] = line.strip().split('{')[1].replace('}', '').split(',')
			else:
				elf_attributes = {}
				for a in line.strip().replace('}', '').replace('{', '').split(','):
					elf_attributes[a.split('=')[0]] = int(a.split('=')[1])
				elves.append(elf_attributes.copy())

	go_to_next_workflow(workflows, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in')

	# sum accepted ranges
	sum = 0
	for ar in accepted_ranges:
		round_value = 1
		for k in 'xmas':
			round_value *= ar[k][1] - ar[k][0] + 1
		sum += round_value

	print('Answer: {}'.format(sum))


def go_to_next_workflow(workflows, elfs_stats, workflow_id):
	global accepted_ranges

	for w in workflows[workflow_id]:
		new_workflow = ''
		new_elf_stats = {}
		if '<' in w:
			future_name = w.split('<')[0]
			future_value = int(w.split('<')[1].split(':')[0])

			if elfs_stats[future_name][0] < future_value:
				new_workflow = w.split('<')[1].split(':')[1]
				new_elf_stats = copy.deepcopy(elfs_stats)
				new_elf_stats[future_name] = [elfs_stats[future_name][0], future_value - 1]
				elfs_stats[future_name] = [future_value, elfs_stats[future_name][1]]
		elif '>' in w:
			future_name = w.split('>')[0]
			future_value = int(w.split('>')[1].split(':')[0])

			if elfs_stats[future_name][1] > future_value:
				new_workflow = w.split('>')[1].split(':')[1]
				new_elf_stats = copy.deepcopy(elfs_stats)
				new_elf_stats[future_name] = [future_value + 1, elfs_stats[future_name][1]]
				elfs_stats[future_name] = [elfs_stats[future_name][0], future_value]
		else:
			if w in 'R':
				new_workflow = 'R'
				new_elf_stats = copy.deepcopy(elfs_stats)
			elif w in 'A':
				new_workflow = 'A'
				new_elf_stats = copy.deepcopy(elfs_stats)
			else:
				new_workflow = w
				new_elf_stats = copy.deepcopy(elfs_stats)

		if new_workflow == 'R':
			pass
		elif new_workflow == 'A':
			accepted_ranges.append(new_elf_stats)
		else:
			go_to_next_workflow(workflows, copy.deepcopy(new_elf_stats), new_workflow)


if __name__ == "__main__":
	main()
