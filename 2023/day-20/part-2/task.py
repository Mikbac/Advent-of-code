# Created by MikBac on 2023

import math


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

	# find rx config (&lg -> rx)
	rx_config = ''
	for key, value in configuration.items():
		if 'rx' in value:
			rx_config = key[1:]
			break

	# find rx config configs
	lcm_values = {}
	for p in conjunction_statuses[rx_config].keys():
		lcm_values[p] = 0

	flip_flop_statuses = {}
	button_pulses = 0

	while True:
		button_pulses += 1

		commands_queue = [['broadcaster', 'L']]
		while len(commands_queue) != 0:
			command = commands_queue.pop(0)

			if command[0] == 'broadcaster':
				for i in configuration[command[0]]:
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
						commands_queue.append([i, pulse, command[0]])

			if '&' + command[0] in configuration:

				conjunction_statuses[command[0]][command[2]] = command[1]

				pulse = 'L'
				for i in conjunction_statuses[command[0]].keys():
					if conjunction_statuses[command[0]][i] == 'L':
						pulse = 'H'
						break

				if command[0] == 'lg' and 'H' in conjunction_statuses[command[0]].values():
					for key, value in conjunction_statuses[command[0]].items():
						if value == 'H':
							lcm_values[key] = button_pulses

				for i in configuration['&' + command[0]]:
					commands_queue.append([i, pulse, command[0]])
		# break if all cycles found
		if 0 not in lcm_values.values():
			break

	answer = math.lcm(*lcm_values.values())
	print('Answer: {}'.format(answer))


if __name__ == "__main__":
	main()
