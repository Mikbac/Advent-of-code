# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	elves_calories = []
	current_elves_calories = 0
	while True:
		try:
			calories = input().strip()
			if calories == '':
				elves_calories.append(int(current_elves_calories))
				current_elves_calories = 0
			else:
				current_elves_calories += int(calories)
		except EOFError:
			break
	elves_calories.append(int(current_elves_calories))

	top_three_elves = sum(sorted(elves_calories, reverse=True)[:3])

	print('Answer: {}'.format(top_three_elves))


if __name__ == "__main__":
	main()
