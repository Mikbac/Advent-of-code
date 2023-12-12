# Created by MikBac on 2023


def main():
	sum = 0
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			schema = line.strip().split(' ')[0]
			requirements = [eval(i) for i in line.strip().split(' ')[1].split(',')]
			sum += find(schema, requirements)

	print('Answer: {}'.format(sum))


def find(schema, requirements):
	if '?' in schema:
		return find(schema.replace('?', '.', 1), requirements) + find(schema.replace('?', '#', 1), requirements)
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
