# Created by MikBac on 2023


def main():
	workflows = {}
	elves = []

	with open('input', 'r', encoding='utf-8') as input_:
		are_workflows = True
		for row, line in enumerate(input_):
			if len(line.strip()) == 0:
				are_workflows = False
				continue

			if are_workflows:
				workflows[line.strip().split('{')[0]] = line.strip().split('{')[1].replace('}', '').split(',')
			else:
				elf_attributes = {}
				for a in line.strip().replace('}', '').replace('{', '').split(','):
					elf_attributes[a.split('=')[0]] = int(a.split('=')[1])
				elves.append(elf_attributes.copy())

	answer = 0
	for e in elves:
		workflow = 'in'
		while True:
			for w in workflows[workflow]:
				if '<' in w:
					future_name = w.split('<')[0]
					future_value = int(w.split('<')[1].split(':')[0])
					if e[future_name] < future_value:
						workflow = w.split('<')[1].split(':')[1]
						break
					else:
						continue
				elif '>' in w:
					future_name = w.split('>')[0]
					future_value = int(w.split('>')[1].split(':')[0])
					if e[future_name] > future_value:
						workflow = w.split('>')[1].split(':')[1]
						break
					else:
						continue
				else:
					if w in 'R':
						workflow = 'R'
						break
					elif w in 'A':
						workflow = 'A'
						break
					else:
						workflow = w

			if workflow == 'R':
				break
			elif workflow == 'A':
				answer += sum(e.values())
				break

	print('Answer: {}'.format(answer))


if __name__ == "__main__":
	main()
