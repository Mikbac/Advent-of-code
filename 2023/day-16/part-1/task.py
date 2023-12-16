# Created by MikBac on 2023


map = []


def main():
	global map
	sum = 0
	with open('sample', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			map.append(list('+' + line.strip() + '+'))

	map.append(list('+' * len(map[0])))
	map.insert(0, list('+' * len(map[0])))

	print(map)

	sum = go([1, 1], 1, [1, 2])

	print('Answer: {}'.format(sum))


def go(current_position, steps, trend):
	global map

	if map[current_position[0]][current_position[1]] == '+':
		return steps

	if map[current_position[0]][current_position[1]] == '.':
		new_trend = []

		if current_position[0] != trend[0]:
			if current_position[0] > trend[0]:
				new_trend = [trend[0] - 1, trend[1]]
			else:
				new_trend = [trend[0] + 1, trend[1]]
		else:
			if current_position[1] > trend[1]:
				new_trend = [trend[0], trend[1] - 1]
			else:
				new_trend = [trend[0], trend[1] + 1]
		return go(trend, steps + 1, new_trend)

	if map[current_position[0]][current_position[1]] == '|':




if __name__ == "__main__":
	main()
