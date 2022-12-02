# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	game_result = 0
	while True:
		try:
			game = input().strip()
			oponent_answer = game.split(' ')[0]
			user_result = game.split(' ')[1]

			if user_result == 'X':
				if oponent_answer == 'A':
					game_result += get_shape_bonus('C')
				elif oponent_answer == 'C':
					game_result += get_shape_bonus('B')
				elif oponent_answer == 'B':
					game_result += get_shape_bonus('A')
			elif user_result == 'Y':
				game_result += 3
				game_result += get_shape_bonus(oponent_answer)
			elif user_result == 'Z':
				game_result += 6
				if oponent_answer == 'A':
					game_result += get_shape_bonus('B')
				elif oponent_answer == 'C':
					game_result += get_shape_bonus('A')
				elif oponent_answer == 'B':
					game_result += get_shape_bonus('C')

		except EOFError:
			break

	print('Answer: {}'.format(game_result))


def get_shape_bonus(shape):
	bonus = 0
	if shape == 'A':
		bonus += 1
	elif shape == 'B':
		bonus += 2
	elif shape == 'C':
		bonus += 3
	return bonus


if __name__ == "__main__":
	main()
