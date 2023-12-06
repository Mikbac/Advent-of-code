# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

import math

def main():
	while True:
		try:
			time = [eval(i) for i in input().strip().split(':')[1].split()]
			distance = [eval(i) for i in input().strip().split(':')[1].split()]
		except EOFError:
			break

		beat_records = []

		for i in range(len(time)):
			beat_records.append(0)
			for hold_button_time in range(time[i]):
				travel_time = (time[i] - hold_button_time) * hold_button_time
				if travel_time > distance[i]:
					beat_records[i] += 1

		result = math.prod(beat_records)

	print('Answer: {}'.format(result))


if __name__ == "__main__":
	main()
