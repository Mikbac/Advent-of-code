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

			for i in range(len(datastream_buffer) - 3):
				marker = datastream_buffer[i:i + 4]

				if marker.count(marker[0]) == 1 and marker.count(marker[1]) == 1 and marker.count(
						marker[2]) == 1 and marker.count(marker[3]) == 1:
					marker_position = i + 4
					break

		except EOFError:
			break

	print('Answer: {}'.format(marker_position))


if __name__ == "__main__":
	main()
