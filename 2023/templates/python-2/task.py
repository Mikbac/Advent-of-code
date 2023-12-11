# Created by MikBac on 2023

def main():
	ans = ''
	with open('input', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			ans = line.strip()

	print('Answer: {}'.format(ans))


if __name__ == "__main__":
	main()
