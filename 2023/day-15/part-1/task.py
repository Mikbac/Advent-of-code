# Created by MikBac on 2023


def main():
	sum = 0
	initialization_sequence = []
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			initialization_sequence = line.strip().split(',')

	for i in initialization_sequence:
		sum += get_hash(i)

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
