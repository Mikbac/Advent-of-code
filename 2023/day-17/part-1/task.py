# Created by MikBac on 2023

import copy

traffic_map = []
results = []


def main():
	global traffic_map
	global results

	with open('sample', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			traffic_map.append([int(x) for x in list(line.strip())])

	go([0, 0], [], traffic_map[0][0])

	print('Answer: {}'.format(results))


def go(cs, ps, lost_heat):
	global traffic_map
	global results
	lost_heat += traffic_map[cs[0]][cs[1]]

	if cs in ps:
		return

	if len(results) > 0 and lost_heat >= min(results):
		return

	if len(ps) > 4 and (
			ps[-1][0] == ps[-2][0] == ps[-3][0] == ps[-4][0] == ps[-5][0] or
			ps[-1][1] == ps[-2][1] == ps[-3][1] == ps[-4][1] == ps[-5][1]):
		return

	if cs[0] == len(traffic_map) - 1 and cs[1] == len(traffic_map[0]) - 1:
		results.append(lost_heat)
		print(results)
		return

	ps.append(cs)

	if cs[0] == 0:
		if cs[1] == len(traffic_map[0]) - 1:
			go([cs[0] + 1, cs[1]], copy.deepcopy(ps), lost_heat)
		else:
			go([cs[0] + 1, cs[1]], copy.deepcopy(ps), lost_heat)
			go([cs[0], cs[1] + 1], copy.deepcopy(ps), lost_heat)

	elif cs[0] == len(traffic_map) - 1:
		go([cs[0] - 1, cs[1]], copy.deepcopy(ps), lost_heat)
		go([cs[0], cs[1] + 1], copy.deepcopy(ps), lost_heat)

	elif cs[1] == len(traffic_map[0]) - 1:
		go([cs[0] + 1, cs[1]], copy.deepcopy(ps), lost_heat)

	else:
		go([cs[0], cs[1] + 1], copy.deepcopy(ps), lost_heat)
		go([cs[0] + 1, cs[1]], copy.deepcopy(ps), lost_heat)
		go([cs[0] - 1, cs[1]], copy.deepcopy(ps), lost_heat)


if __name__ == "__main__":
	main()
