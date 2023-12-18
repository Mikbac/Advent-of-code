# Created by MikBac on 2023
import sys

shortest_value = None
visited_steps = {}


def main():
	global shortest_value
	traffic_map = []

	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			traffic_map.append([int(x) for x in list(line.strip())])

	sys.setrecursionlimit(len(traffic_map) * len(traffic_map[0]))
	shortest_value = len(traffic_map) * len(traffic_map[0]) * 9

	go([0, 0], 0, '', 0, traffic_map)

	print('Answer: {}'.format(shortest_value))


def go(cs, lost_heat, last_direction, jump_size, traffic_map):
	global shortest_value
	global visited_steps

	if (cs[0] > len(traffic_map) - 1 or
			cs[0] < 0 or
			cs[1] > len(traffic_map[0]) - 1 or
			cs[1] < 0):
		return

	for i in range(jump_size):
		if last_direction == '>':
			lost_heat += traffic_map[cs[0]][cs[1] - i]
		if last_direction == '<':
			lost_heat += traffic_map[cs[0]][cs[1] + i]
		if last_direction == '^':
			lost_heat += traffic_map[cs[0] + i][cs[1]]
		if last_direction == 'v':
			lost_heat += traffic_map[cs[0] - i][cs[1]]

	visited_key = '{}-{}-{}'.format(cs[0], cs[1], last_direction)
	if visited_key in visited_steps and visited_steps[visited_key] <= lost_heat:
		return

	if lost_heat >= shortest_value:
		return

	if cs[0] == len(traffic_map) - 1 and cs[1] == len(traffic_map[0]) - 1:
		if lost_heat < shortest_value:
			shortest_value = lost_heat
		return

	visited_steps['{}-{}-{}'.format(cs[0], cs[1], last_direction)] = lost_heat
	# min -> 4
	# max -> 10
	for jump in reversed(range(4, 11)):
		if last_direction != '>' and last_direction != '<':
			go([cs[0], cs[1] + jump], lost_heat, '>', jump, traffic_map)
			go([cs[0], cs[1] - jump], lost_heat, '<', jump, traffic_map)
		if last_direction != 'v' and last_direction != '^':
			go([cs[0] + jump, cs[1]], lost_heat, 'v', jump, traffic_map)
			go([cs[0] - jump, cs[1]], lost_heat, '^', jump, traffic_map)


if __name__ == "__main__":
	main()
