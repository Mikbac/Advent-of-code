# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	sum = 0
	while True:
		try:
			numb = ''
			calibration = input().strip()
			for i in calibration:
				if i.isdigit():
					numb = i
					break

			for i in reversed(calibration):
				if i.isdigit():
					numb = numb + i
					break

			sum = sum + int(numb)

		except EOFError:
			break

	print('Answer: {}'.format(sum))


if __name__ == "__main__":
	main()
