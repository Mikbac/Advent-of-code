# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


def main():
	possibleGamesSum = 0
	while True:
		try:
			game_possible = True
			game = input().strip()
			game_numb = int(game.split(':')[0].split()[1])
			sets = game.split(':')[1].split(';')

			for s in sets:
				cubes = s.split(',')
				for c in cubes:
					color = c.split()[1]
					cube_numb = int(c.split()[0])

					if color == 'red':
						if cube_numb > RED_CUBES:
							game_possible = False
					if color == 'green':
						if cube_numb > GREEN_CUBES:
							game_possible = False
					if color == 'blue':
						if cube_numb > BLUE_CUBES:
							game_possible = False

			if game_possible:
				possibleGamesSum += game_numb


		except EOFError:
			break

	print('Answer: {}'.format(possibleGamesSum))


if __name__ == "__main__":
	main()
