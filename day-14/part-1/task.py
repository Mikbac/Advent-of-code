# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

import copy

STEPS = 10

polymerTemplate = list(input().strip())
input().strip()

insertionList = {}

while True:
    try:
        line = input().strip().split(' -> ')
        insertionList[line[0]] = line[1]
    except EOFError:
        break

for s in range(STEPS):
    print("Step: {}/{}".format(s, STEPS))
    newTemplate = []
    for i in range(len(polymerTemplate) - 1):
        elementOne = polymerTemplate[i]
        elementTwo = polymerTemplate[i + 1]
        element = elementOne + elementTwo
        if element in insertionList:
            newTemplate.append(elementOne)
            newTemplate.append(insertionList[element])
    newTemplate.append(polymerTemplate[-1])
    polymerTemplate = copy.deepcopy(newTemplate)

resultMap = {}

for i in newTemplate:
    if i in resultMap:
        resultMap[i] += 1
    else:
        resultMap[i] = 0

maxValue = max(resultMap.values())
minValue = min(resultMap.values())

print('Result = {}'.format(maxValue - minValue))
# 2321
