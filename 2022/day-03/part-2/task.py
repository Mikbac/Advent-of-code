# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	priority_sum = 0
	while True:
		try:
			first_backpack = input().strip()
			second_backpack = input().strip()
			third_backpack = input().strip()

			duplicated_items = list(set(first_backpack) & set(second_backpack) & set(third_backpack))

			priority_sum += get_priority(duplicated_items[0])

		except EOFError:
			break

	print('Answer: {}'.format(priority_sum))


def get_priority(item):
	item_ascii = ord(item)
	if 97 <= item_ascii <= 122:
		return item_ascii - 96
	else:
		return item_ascii - 38


if __name__ == "__main__":
	main()
