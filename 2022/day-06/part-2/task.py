# cat sample-1 | python3 task.py
# cat sample-2 | python3 task.py
# cat sample-3 | python3 task.py
# cat sample-4 | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	marker_position = 0
	while True:
		try:

			datastream_buffer = input().strip()

			for i in range(len(datastream_buffer) - 13):
				marker = datastream_buffer[i:i + 14]

				series = 0
				for j in range(len(marker)):
					if marker.count(marker[j]) == 1:
						series += 1

				if series == 14:
					marker_position = i + 14
					break

		except EOFError:
			break

	print('Answer: {}'.format(marker_position))


if __name__ == "__main__":
	main()
