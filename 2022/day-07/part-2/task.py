# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

full_size = 0
catalogs_brutto_size = {}


def main():
	catalog_path = []
	catalogs_relations = {}
	catalogs_netto_size = {}
	full_root_catalog_size = 0

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
				full_root_catalog_size += file_size
				if current_catalog in catalogs_netto_size:
					catalogs_netto_size[current_catalog] = catalogs_netto_size[current_catalog] + file_size
				else:
					catalogs_netto_size[current_catalog] = file_size
		except EOFError:
			break

	catalog_to_remove_size = get_catalog_to_remove_size(catalogs_relations, catalogs_netto_size, full_root_catalog_size)

	print('Answer: {}'.format(catalog_to_remove_size))


def get_catalog_to_remove_size(catalogs_relations, catalogs_netto_size, full_root_catalog_size):
	global catalogs_brutto_size

	for catalog in catalogs_relations['/']:
		get_catalog_size(catalog, catalogs_relations, catalogs_netto_size)

	require_free_space = 30000000 - (70000000 - full_root_catalog_size)

	catalog_values = list(catalogs_brutto_size.values())
	catalog_values.sort()

	for value in catalog_values:
		if value >= require_free_space:
			return value


def get_catalog_size(catalog, catalogs_relations, catalogs_netto_size):
	global catalogs_brutto_size

	if catalog not in catalogs_relations:
		if catalog in catalogs_netto_size:
			catalogs_brutto_size[catalog] = catalogs_netto_size[catalog]
			return catalogs_netto_size[catalog]
		else:
			return 0
	full_catalog_size = 0
	for deep_catalog in catalogs_relations[catalog]:
		child_size = get_catalog_size(deep_catalog, catalogs_relations, catalogs_netto_size)
		full_catalog_size += child_size

	if catalog in catalogs_netto_size:
		full_catalog_size += catalogs_netto_size[catalog]

	catalogs_brutto_size[catalog] = full_catalog_size

	return full_catalog_size


if __name__ == "__main__":
	main()
