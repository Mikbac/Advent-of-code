# Created by MikBac on 2023

import copy


def main():
	bricks = []
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			bricks.append([[int(x) for x in line.strip().split('~')[0].split(',')],
			               [int(x) for x in line.strip().split('~')[1].split(',')]])

	bricks.sort(key=lambda x: x[0][2])

	is_moved = True
	while is_moved:
		is_moved = False
		for b in reversed(range(len(bricks))):
			if bricks[b][0][2] == 1:
				continue
			else:
				is_support = False
				for bb in reversed(range(len(bricks))):
					if b == bb:
						continue
					else:
						if bricks[bb][1][2] == bricks[b][0][2] - 1:
							if check_line(bricks[b], bricks[bb]):
								is_support = True
								break
				if not is_support:
					is_moved = True
					bricks[b][0][2] -= 1
					bricks[b][1][2] -= 1

	max_height = 0
	for b in bricks:
		if b[1][2] > max_height:
			max_height = b[1][2]

	supported = {}
	for b in range(len(bricks)):
		if bricks[b][0][2] == 1:
			pass
		else:
			for bb in range(len(bricks)):
				if b == bb:
					continue
				else:
					if bricks[bb][1][2] + 1 == bricks[b][0][2]:
						if check_line(bricks[b], bricks[bb]):
							if b in supported:
								supported[b].append(bb)
							else:
								supported[b] = [bb]

	ans = 0
	for b in range(len(bricks)):
		queue = [b]
		s = copy.deepcopy(supported)
		while len(queue) > 0:
			d = queue.pop(0)
			for key, value in s.items():
				if d in value:
					s[key].remove(d)
					if len(s[key]) == 0:
						queue.append(key)
		for key, value in s.items():
			if len(value) == 0:
				ans += 1

	print('Answer: {}'.format(ans))


def check_line(b1, b2):
	check_map = []
	for i in range(10):
		check_map.append(['.'] * 10)

	for i in range(b1[0][0], b1[1][0] + 1):
		for j in range(b1[0][1], b1[1][1] + 1):
			check_map[j - 1][i - 1] = '-'

	for i in range(b2[0][0], b2[1][0] + 1):
		for j in range(b2[0][1], b2[1][1] + 1):
			if check_map[j - 1][i - 1] == '-':
				return True
	return False


if __name__ == "__main__":
	main()
