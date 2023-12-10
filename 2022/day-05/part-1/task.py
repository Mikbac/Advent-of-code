# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022


def main():
	stacks = []

	while True:
		try:
			instruction = input()

			if len(stacks) == 0:
				for i in range(int((len(instruction) + 1) / 4)):
					stacks.append([])

			if '[' in instruction:
				for i in range(len(stacks)):
					current_object = instruction[(i + 1) * 4 - 3]
					if current_object.strip() != '':
						stacks[i].insert(0, current_object)

			if 'move' in instruction:
				stacks_moves_quantity = int(instruction.split(' ')[1])
				origin_stack = int(instruction.split(' ')[3]) - 1
				destiny_stack = int(instruction.split(' ')[5]) - 1

				for i in range(stacks_moves_quantity):
					element = stacks[origin_stack].pop()
					stacks[destiny_stack].append(element)

		except EOFError:
			break

	answer = ''
	for stack in stacks:
		answer += stack[-1]

	print('Answer: {}'.format(answer))


if __name__ == "__main__":
	main()
