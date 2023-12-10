# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

full_size = 0


def main():
	catalog_path = []
	catalogs_relations = {}
	catalogs_netto_size = {}
	while True:
		try:
			command = input().strip()

			if '$ cd ' in command:
				new_catalog = command.split(' ')[2]
				if new_catalog == '..':
					catalog_path.pop()
				else:
					catalog_path.append(new_catalog)
			elif 'dir' in command:
				current_catalog = '_'.join(catalog_path)
				if current_catalog in catalogs_relations:
					catalogs_relations[current_catalog].append(current_catalog + '_' + command.split(' ')[1])
				else:
					catalogs_relations[current_catalog] = [current_catalog + '_' + command.split(' ')[1]]
			elif '$ ls' not in command:
				current_catalog = '_'.join(catalog_path)
				file_size = int(command.split(' ')[0])
				if current_catalog in catalogs_netto_size:
					catalogs_netto_size[current_catalog] = catalogs_netto_size[current_catalog] + file_size
				else:
					catalogs_netto_size[current_catalog] = file_size
		except EOFError:
			break

	find_sum_of_directories(catalogs_relations, catalogs_netto_size)

	print('Answer: {}'.format(full_size))


def find_sum_of_directories(catalogs_relations, catalogs_netto_size):
	global full_size

	for catalog in catalogs_relations['/']:
		child_size = get_catalog_size(catalog, catalogs_relations, catalogs_netto_size)
		if child_size <= 100000:
			full_size += child_size


def get_catalog_size(catalog, catalogs_relations, catalogs_netto_size):
	global full_size

	if catalog not in catalogs_relations:
		if catalog in catalogs_netto_size:
			return catalogs_netto_size[catalog]
		else:
			return 0
	full_catalog_size = 0
	for deep_catalog in catalogs_relations[catalog]:
		child_size = get_catalog_size(deep_catalog, catalogs_relations, catalogs_netto_size)
		if child_size <= 100000:
			full_size += child_size
		full_catalog_size += child_size

	if catalog in catalogs_netto_size:
		full_catalog_size += catalogs_netto_size[catalog]

	return full_catalog_size


if __name__ == "__main__":
	main()
