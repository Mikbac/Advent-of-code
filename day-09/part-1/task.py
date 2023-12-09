# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

import copy


def main():
	history_values = []
	while True:
		try:
			value = [eval(i) for i in input().strip().split(' ')]

			sequences = []
			sequence = 1
			sequences.append(copy.deepcopy(value))
			sequences.append([])

			while True:
				for i in range(len(value) - 1):
					sequences[sequence].append(value[i + 1] - value[i])
				if areNulls(sequences[sequence]):
					break
				else:
					value = copy.deepcopy(sequences[sequence])
					sequence += 1
					sequences.append([])

			sequences[-1].append(0)

			for i in reversed(range(len(sequences) - 1)):
				sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

			history_values.append(sequences[0][-1])

		except EOFError:
			break

	answer = sum(history_values)

	print('Answer: {}'.format(answer))


def areNulls(sequence):
	for s in sequence:
		if s != 0:
			return False
	return True


if __name__ == "__main__":
	main()
