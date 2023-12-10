# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2023

def main():
	sum = 0
	while True:
		try:
			numb = ''
			calibration = input().strip()

			calibration = (calibration.replace('one', 'one1one')
			               .replace('two', 'two2two')
			               .replace('three', 'three3three')
			               .replace('four', 'four4four')
			               .replace('five', 'five5five')
			               .replace('six', 'six6six')
			               .replace('seven', 'seven7seven')
			               .replace('eight', 'eight8eight')
			               .replace('nine', 'nine9nine')
			               .replace('zero', 'zero0zero'))

			for i in calibration:
				if i.isdigit():
					numb = i
					break

			for i in reversed(calibration):
				if i.isdigit():
					numb += i
					break

			sum = sum + int(numb)

		except EOFError:
			break

	print('Answer: {}'.format(sum))


if __name__ == "__main__":
	main()
