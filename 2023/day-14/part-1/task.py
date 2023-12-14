# Created by MikBac on 2023


def main():
	sum = 0
	platform = []
	with open('input', 'r', encoding='utf-8') as input_:

		for row, line in enumerate(input_):
			platform.append(list(line.strip()))

	for i in range(1, len(platform)):
		for j in range(len(platform[i])):
			for k in range(i, 0, -1):
				if platform[k][j] == 'O' and platform[k - 1][j] == '.':
					platform[k][j] = '.'
					platform[k - 1][j] = 'O'

	for i in range(len(platform)):
		sum += platform[i].count('O') * (len(platform) - i)

	print('Answer: {}'.format(sum))


if __name__ == "__main__":
	main()
