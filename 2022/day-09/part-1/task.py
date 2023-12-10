# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

visited_elements = []


def main():
	global visited_elements

	BOARD_SIZE = 10000000000

	head_position_x = BOARD_SIZE - 1
	head_position_y = 0

	tail_position_x = BOARD_SIZE - 1
	tail_position_y = 0

	positions_sum = 1

	while True:
		try:
			command = input().strip()

			direction = command.split()[0]
			distance = int(command.split()[1])

			for _ in range(distance):
				if direction == 'R':
					head_position_y += 1
					if is_header_not_contact(head_position_x, head_position_y, tail_position_x, tail_position_y):
						tail_position_x = head_position_x
						tail_position_y = head_position_y - 1
						positions_sum += get_increment(tail_position_x, tail_position_y)
				if direction == 'L':
					head_position_y -= 1
					if is_header_not_contact(head_position_x, head_position_y, tail_position_x, tail_position_y):
						tail_position_x = head_position_x
						tail_position_y = head_position_y + 1
						positions_sum += get_increment(tail_position_x, tail_position_y)
				if direction == 'U':
					head_position_x -= 1
					if is_header_not_contact(head_position_x, head_position_y, tail_position_x, tail_position_y):
						tail_position_x = head_position_x + 1
						tail_position_y = head_position_y
						positions_sum += get_increment(tail_position_x, tail_position_y)
				if direction == 'D':
					head_position_x += 1
					if is_header_not_contact(head_position_x, head_position_y, tail_position_x, tail_position_y):
						tail_position_x = head_position_x - 1
						tail_position_y = head_position_y
						positions_sum += get_increment(tail_position_x, tail_position_y)

		except EOFError:
			break

	print('Answer: {}'.format(positions_sum))


def is_header_not_contact(head_position_x, head_position_y, tail_position_x, tail_position_y):
	if head_position_x == tail_position_x and head_position_y == tail_position_y:
		return False

	if head_position_x - 1 == tail_position_x and head_position_y == tail_position_y:
		return False
	if head_position_x + 1 == tail_position_x and head_position_y == tail_position_y:
		return False

	if head_position_x == tail_position_x and head_position_y + 1 == tail_position_y:
		return False
	if head_position_x == tail_position_x and head_position_y - 1 == tail_position_y:
		return False

	if head_position_y - 1 == tail_position_y and head_position_x - 1 == tail_position_x:
		return False
	if head_position_y + 1 == tail_position_y and head_position_x + 1 == tail_position_x:
		return False
	if head_position_y + 1 == tail_position_y and head_position_x - 1 == tail_position_x:
		return False
	if head_position_y - 1 == tail_position_y and head_position_x + 1 == tail_position_x:
		return False

	return True


def get_increment(tail_position_x, tail_position_y):
	global visited_elements
	if '{}-{}'.format(tail_position_x, tail_position_y) in visited_elements:
		return 0
	else:
		visited_elements.append('{}-{}'.format(tail_position_x, tail_position_y))
		return 1


if __name__ == "__main__":
	main()
