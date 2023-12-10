# cat sample-1 | python3 task.py
# cat sample-2 | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

visited_elements = []


def main():
	global visited_elements

	BOARD_SIZE = 10000000000

	positions_sum = 1

	chain = []
	for i in range(10):
		chain.append([])
		chain[i].append(BOARD_SIZE - 1)
		chain[i].append(0)

	while True:
		try:
			command = input().strip()

			direction = command.split()[0]
			distance = int(command.split()[1])

			for _ in range(distance):
				print(chain)

				last_chain_x = chain[0][0]
				last_chain_y = chain[0][1]

				if direction == 'R':
					chain[0][1] += 1
				if direction == 'L':
					chain[0][1] -= 1
				if direction == 'U':
					chain[0][0] -= 1
				if direction == 'D':
					chain[0][0] += 1


				for i in range(len(chain) - 1):

					if is_header_not_contact(chain[i][0], chain[i][1], chain[i + 1][0], chain[i + 1][1]):
						# print('{} - {} {}'.format(i, last_chain_x, last_chain_y))
						# print('{} - {} {} {} {}'.format(i, chain[i][0], chain[i][1], chain[i + 1][0], chain[i + 1][1]))

						last_chain_x_temp = chain[i + 1][0]
						last_chain_y_temp = chain[i + 1][1]

						chain[i + 1][0] = last_chain_x
						chain[i + 1][1] = last_chain_y

						last_chain_x = last_chain_x_temp
						last_chain_y = last_chain_y_temp

						if i == len(chain)-2:
							positions_sum += get_increment(chain[i + 1][0], chain[i + 1][1])

					# last_chain_x = chain[i][0]
					# last_chain_y = chain[i][1]

		except EOFError:
			break

	print(visited_elements)
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
