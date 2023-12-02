# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023


def main():
	powers_sum = 0
	while True:
		try:
			min_red = 0
			min_green = 0
			min_blue = 0

			game = input().strip()
			gameNumb = int(game.split(':')[0].split()[1])
			sets = game.split(':')[1].split(';')

			for s in sets:
				cubes = s.split(',')

				for c in cubes:
					color = c.split()[1]
					cubeNumb = int(c.split()[0])

					if color == 'red':
						if cubeNumb > min_red:
							min_red = cubeNumb
					if color == 'green':
						if cubeNumb > min_green:
							min_green = cubeNumb
					if color == 'blue':
						if cubeNumb > min_blue:
							min_blue = cubeNumb

			powers_sum += min_red * min_green * min_blue

		except EOFError:
			break

	print('Answer: {}'.format(powers_sum))


if __name__ == "__main__":
	main()
