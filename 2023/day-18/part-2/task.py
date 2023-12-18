# Created by MikBac on 2023

def main():
	current_location = [0, 0]

	commands_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

	coordinates = []

	area = 0
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			command = line.strip().split(' ')[2]
			direction = commands_map[command[-2]]
			length = int(command[2:7], base=16)

			if direction == 'U':
				current_location[1] = current_location[1] + length
			if direction == 'D':
				current_location[1] = current_location[1] - length
			if direction == 'L':
				current_location[0] = current_location[0] - length
			if direction == 'R':
				current_location[0] = current_location[0] + length

			# [[x1, y1], [x2, y2]]
			coordinates.append(current_location.copy())
			area += length

	answer = shoelace_area(coordinates)

	print('Answer: {}'.format(answer + area / 2 + 1))


# https://en.wikipedia.org/wiki/Shoelace_formula
# "The shoelace formula, also known as Gauss's area formula and the surveyor's formula,[1] is a mathematical algorithm
# to determine the area of a simple polygon whose vertices are described by their Cartesian coordinates in the plane."
def shoelace_area(coordinates):
	a1, a2 = 0, 0
	coordinates.append(coordinates[0])
	for j in range(len(coordinates) - 1):
		a1 += coordinates[j][0] * coordinates[j + 1][1]
		a2 += coordinates[j][1] * coordinates[j + 1][0]
	return abs(a1 - a2) / 2


if __name__ == "__main__":
	main()
