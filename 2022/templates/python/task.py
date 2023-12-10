# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	ans = ''
	while True:
		try:
			ans = input().strip()
		except EOFError:
			break

	print('Answer: {}'.format(ans))


if __name__ == "__main__":
	main()
