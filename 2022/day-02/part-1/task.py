# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	game_result = 0
	while True:
		try:
			game = input().strip()
			oponent_code = game.split(' ')[0]
			user = game.split(' ')[1]

			oponent = ''

			if oponent_code == 'A':
				oponent = 'X'
			elif oponent_code == 'B':
				oponent = 'Y'
			elif oponent_code == 'C':
				oponent = 'Z'

			if oponent == user:
				game_result += 3

			if (user == 'Y' and oponent == 'X') or (user == 'X' and oponent == 'Z') or (user == 'Z' and oponent == 'Y'):
				game_result += 6

			game_result += get_shape_bonus(user)

		except EOFError:
			break

	print('Answer: {}'.format(game_result))


def get_shape_bonus(shape):
	bonus = 0
	if shape == 'X':
		bonus += 1
	elif shape == 'Y':
		bonus += 2
	elif shape == 'Z':
		bonus += 3
	return bonus


if __name__ == "__main__":
	main()
