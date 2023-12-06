# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	while True:
		try:
			time = int(input().strip().split(':')[1].replace(' ', ''))
			distance = int(input().strip().split(':')[1].replace(' ', ''))
		except EOFError:
			break

		beat_records = 0

		for hold_button_time in range(time):
			travel_time = (time - hold_button_time) * hold_button_time
			if travel_time > distance:
				beat_records += 1

	print('Answer: {}'.format(beat_records))


if __name__ == "__main__":
	main()
