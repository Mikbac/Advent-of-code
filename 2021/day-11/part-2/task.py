# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

octopusesMap = []
SIMULATION_DAYS = 100

maxHeight = 0
maxWidth = 0

flashesQuantity = 0

while True:
	try:
		line = list(map(int, input().strip()))
		octopusesMap.append(line)
	except EOFError:
		break

maxHeight = len(octopusesMap)
maxWidth = len(octopusesMap[0])


def octopusAction(i, j):
	global flashesQuantity
	global octopusesMap

	if octopusesMap[i][j] != 0:
		octopusesMap[i][j] += 1
		if octopusesMap[i][j] >= 10:
			flashesQuantity += 1
			octopusesMap[i][j] = 0
			updateOctopusNeighborhood(i, j)


def updateOctopusNeighborhood(i, j):
	global flashesQuantity
	global octopusesMap

	if i - 1 >= 0 and j - 1 >= 0:
		octopusAction(i - 1, j - 1)

	if i - 1 >= 0:
		octopusAction(i - 1, j)

	if i - 1 >= 0 and j + 1 < maxWidth:
		octopusAction(i - 1, j + 1)

	if j + 1 < maxWidth:
		octopusAction(i, j + 1)

	if i + 1 < maxWidth and j + 1 < maxHeight:
		octopusAction(i + 1, j + 1)

	if i + 1 < maxHeight:
		octopusAction(i + 1, j)

	if i + 1 < maxHeight and j - 1 >= 0:
		octopusAction(i + 1, j - 1)

	if j - 1 >= 0:
		octopusAction(i, j - 1)


flashesQuantity = 0
day = 0

while flashesQuantity != maxWidth * maxHeight:
	day += 1
	flashesQuantity = 0
	for i in range(len(octopusesMap)):
		for j in range(len(octopusesMap[i])):
			octopusesMap[i][j] += 1

	for i in range(len(octopusesMap)):
		for j in range(len(octopusesMap[i])):
			if octopusesMap[i][j] >= 10:
				flashesQuantity += 1
				octopusesMap[i][j] = 0
				updateOctopusNeighborhood(i, j)

print('Day = {}'.format(day))
# 273
