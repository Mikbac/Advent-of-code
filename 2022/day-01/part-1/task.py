# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	max_elves_calories = 0
	current_elves_calories = 0
	while True:
		try:
			calories = input().strip()
			if calories == '':
				if max_elves_calories < current_elves_calories:
					max_elves_calories = current_elves_calories
				current_elves_calories = 0
			else:
				current_elves_calories += int(calories)
		except EOFError:
			break

	if max_elves_calories < current_elves_calories:
		max_elves_calories = current_elves_calories

	print('Answer: {}'.format(max_elves_calories))


if __name__ == "__main__":
	main()
