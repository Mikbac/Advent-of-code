# Created by MikBac on 2023


def main():
	configuration = {}
	conjunction_list = []
	conjunction_statuses = {}
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			configuration[line.strip().split('->')[0].strip()] = line.strip().split('->')[1].replace(' ', '').split(',')
			if '&' in line.strip().split('->')[0].strip():
				conjunction_list.append(line.strip().split('->')[0].strip()[1:])

	for i in configuration.keys():
		for j in conjunction_list:
			if j in configuration[i]:
				if j in conjunction_statuses:
					conjunction_statuses[j][i[1:]] = 'L'
				else:
					conjunction_statuses[j] = {}
					conjunction_statuses[j][i[1:]] = 'L'

	flip_flop_statuses = {}

	low_impulses = 0
	high_impulses = 0

	for _ in range(1000):
		commands_queue = [['broadcaster', 'L']]
		low_impulses += 1
		while len(commands_queue) != 0:
			command = commands_queue.pop(0)

			if command[0] == 'broadcaster':
				for i in configuration[command[0]]:
					if command[1] == 'H':
						high_impulses += 1
					else:
						low_impulses += 1
					commands_queue.append([i, command[1], 'broadcaster'])

			if '%' + command[0] in configuration:

				if command[1] == 'L':
					flip_flop_status = True
					if command[0] in flip_flop_statuses:
						flip_flop_status = not flip_flop_statuses[command[0]]
						flip_flop_statuses[command[0]] = not flip_flop_statuses[command[0]]
					else:
						flip_flop_status = True
						flip_flop_statuses[command[0]] = True
					pulse = ''
					if flip_flop_status:
						pulse = 'H'
					else:
						pulse = 'L'

					for i in configuration['%' + command[0]]:
						if pulse == 'H':
							high_impulses += 1
						else:
							low_impulses += 1
						commands_queue.append([i, pulse, command[0]])

			if '&' + command[0] in configuration:

				conjunction_statuses[command[0]][command[2]] = command[1]

				pulse = 'L'
				for i in conjunction_statuses[command[0]].keys():
					if conjunction_statuses[command[0]][i] == 'L':
						pulse = 'H'
						break
				for i in configuration['&' + command[0]]:
					if pulse == 'H':
						high_impulses += 1
					else:
						low_impulses += 1
					commands_queue.append([i, pulse, command[0]])

	print('Answer: {}'.format(low_impulses * high_impulses))


if __name__ == "__main__":
	main()
