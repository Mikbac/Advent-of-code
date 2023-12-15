# Created by MikBac on 2023


def main():
	sum = 0
	boxes = [[] for i in range(256)]
	initialization_sequence = []
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			initialization_sequence = line.strip().split(',')

	for i in initialization_sequence:

		if '-' in i:
			for b in range(len(boxes)):
				for bi in range(len(boxes[b])):
					if boxes[b][bi][0] == i.split('-')[0]:
						del boxes[b][bi]
						break

		if '=' in i:
			hash_input = i.split('=')[0]
			label = get_hash(hash_input)
			lens = i.split('=')[1]
			is_label = False
			for bi in range(len(boxes[label])):
				if boxes[label][bi][0] == hash_input:
					boxes[label][bi][1] = lens
					is_label = True

			if not is_label:
				boxes[label].append([hash_input, lens])

	for b in range(len(boxes)):
		for bi in range(len(boxes[b])):
			sum += (b + 1) * (bi + 1) * int(boxes[b][bi][1])

	print('Answer: {}'.format(sum))


def get_hash(input):
	current_value = 0
	for i in input:
		current_value += ord(i)
		current_value = current_value * 17
		current_value = current_value % 256
	return current_value


if __name__ == "__main__":
	main()
