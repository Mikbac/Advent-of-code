# Created by MikBac on 2023


def main():
	response = 0
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			schema = line.strip().split(' ')[0]
			requirements = [eval(i) for i in line.strip().split(' ')[1].split(',')]

			schema = "?".join([schema] * 5)
			requirements = requirements * 5

			response += find(schema, requirements, 0)

	print('Answer: {}'.format(response))


def find(schema, requirements, changed_position):
	if sum(requirements) < schema.count('#'):
		return 0

	if changed_position != 0:
		checked_part = list(filter(None, schema[:changed_position].split('.')))
		for i in range(len(checked_part) - 1):
			if requirements[i] != len(checked_part[i]):
				return 0

		if checked_part != [] and requirements[len(checked_part) - 1] < len(checked_part[-1]):
			return 0

	if '?' in schema:
		changed_position = schema.index('?')
		return find(schema.replace('?', '.', 1), requirements, changed_position) + find(schema.replace('?', '#', 1),
		                                                                                requirements, changed_position)
	else:
		new_schema = list(filter(None, schema.split('.')))
		if len(new_schema) == len(requirements):
			for i in range(len(new_schema)):
				if len(new_schema[i]) != requirements[i]:
					return 0
			return 1
		return 0


if __name__ == "__main__":
	main()
