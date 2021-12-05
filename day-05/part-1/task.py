# cat sample | python3 task.py
# cat input | python3 task.py

ARRAY_HEIGHT = 10000
ARRAY_WIDTH = 10000

matrix = []

for i in range(ARRAY_HEIGHT):
	matrix.append([])
	for j in range(ARRAY_WIDTH):
		matrix[i].append(0)

while True:
	try:
		line = input().strip().split('->')

		startPointX = int(line[0].split(',')[0].strip())
		startPointY = int(line[0].split(',')[1].strip())

		endPointX = int(line[1].split(',')[0].strip())
		endPointY = int(line[1].split(',')[1].strip())

	except EOFError:
		break

	if startPointX == endPointX:
		if startPointY <= endPointY:
			startPoint = startPointY
			endPoint = endPointY
		else:
			startPoint = endPointY
			endPoint = startPointY

		for i in range(startPoint, endPoint + 1):
			matrix[i][startPointX] += 1

	if startPointY == endPointY:
		if startPointX <= endPointX:
			startPoint = startPointX
			endPoint = endPointX
		else:
			startPoint = endPointX
			endPoint = startPointX

		for i in range(startPoint, endPoint + 1):
			matrix[startPointY][i] += 1

pointSum = 0
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j] >= 2:
			pointSum += 1

print('Final points sum: {}'.format(pointSum))
# 5608
