# Created by MikBac on 2023


def main():
	response = 0
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			schema = line.strip().split(' ')[0]
			requirements = [eval(i) for i in line.strip().split(' ')[1].split(',')]

			schema = "?".join([schema] * 5)
			requirements = requirements * 5

			response += find(schema, requirements, {}, 0, 0, 0)

	print('Answer: {}'.format(response))


def find(schema, requirements, cache, current_position, current_block_position, block_size):
	cache_key = (current_position, current_block_position, block_size)
	if cache_key in cache:
		return cache[cache_key]

	if current_position == len(schema):
		if current_block_position == len(requirements) and block_size == 0:
			return 1
		elif current_block_position == len(requirements) - 1 and block_size == requirements[current_block_position]:
			return 1
		else:
			return 0

	sum = 0
	if schema[current_position] == '.' or schema[current_position] == '?':
		if block_size == 0:
			sum += find(schema, requirements, cache, current_position + 1, current_block_position, 0)
		elif block_size > 0:
			if current_block_position < len(requirements) and requirements[current_block_position] == block_size:
				sum += find(schema, requirements, cache, current_position + 1, current_block_position + 1, 0)

	if schema[current_position] == '#' or schema[current_position] == '?':
		sum += find(schema, requirements, cache, current_position + 1, current_block_position, block_size + 1)

	cache[cache_key] = sum

	return sum


if __name__ == "__main__":
	main()
