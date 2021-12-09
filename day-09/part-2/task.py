# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

cavesList = []

TOP_RESULTS = 3

while True:
    try:
        line = list(input().strip())
        line.insert(0, '9')
        line.append('9')
        cavesList.append(line)
    except EOFError:
        break

for i in range(len(cavesList)):
    for j in range(len(cavesList[i])):
        if cavesList[i][j] != '9':
            cavesList[i][j] = 'i'
        if cavesList[i][j] == '9':
            cavesList[i][j] = 'l'

emptyLine = ['l'] * len(cavesList[0])
cavesList.insert(0, emptyLine)
cavesList.append(emptyLine)

counter = 0


def setNeighborhood(pointX, pointY, counter):
    if cavesList[pointX + 1][pointY] == 'i':
        cavesList[pointX + 1][pointY] = str(counter)
        setNeighborhood(pointX + 1, pointY, counter)

    if cavesList[pointX - 1][pointY] == 'i':
        cavesList[pointX - 1][pointY] = str(counter)
        setNeighborhood(pointX - 1, pointY, counter)

    if cavesList[pointX][pointY + 1] == 'i':
        cavesList[pointX][pointY + 1] = str(counter)
        setNeighborhood(pointX, pointY + 1, counter)

    if cavesList[pointX][pointY - 1] == 'i':
        cavesList[pointX][pointY - 1] = str(counter)
        setNeighborhood(pointX, pointY - 1, counter)

    return


for i in range(len(cavesList)):
    for j in range(len(cavesList[i])):
        if cavesList[i][j] == 'i':
            setNeighborhood(i, j, counter)
            counter += 1

resultsMap = {}
for i in range(counter):
    resultsMap[str(i)] = 0

for i in range(len(cavesList)):
    for j in range(len(cavesList[i])):
        point = cavesList[i][j]
        if point != 'l':
            resultsMap[point] += 1

sortedResultList = sorted(resultsMap, key=resultsMap.get, reverse=True)[:TOP_RESULTS]

result = 1

for i in sortedResultList:
    result *= resultsMap[i]

print('Result = {}'.format(result))
# 1330560
