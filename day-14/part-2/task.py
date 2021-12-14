# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

STEPS = 40
RAINBOW = STEPS / 2

polymerTemplate = input().strip()
input().strip()

rainbowTable = {}

insertionList = {}

while True:
    try:
        line = input().strip().split(' -> ')
        insertionList[line[0]] = line[0][0] + line[1] + line[0][1]
    except EOFError:
        break


def getStep(partOne, partTwo):
    element = partOne + partTwo
    return insertionList[element]


def mergeDict(a, b):
    for key in a:
        if key in b:
            b[key] += a[key]
        else:
            b[key] = a[key]


def coutRes(l, resultMap):
    for i in l:
        if i in resultMap:
            resultMap[i] += 1
        else:
            resultMap[i] = 1


def getChilds(steps, step, part, resultMap, rainbowMode):
    partOne = part[0]
    partTwo = part[1]

    if part in rainbowTable and RAINBOW - 1 == (steps - step) and not rainbowMode:
        mergeDict(rainbowTable[part], resultMap)
        return

    if steps == step:
        coutRes(getStep(partOne, partTwo)[0:2], resultMap)

    else:
        ans = getStep(partOne, partTwo)
        getChilds(steps, step + 1, ans[0:2], resultMap, rainbowMode)
        getChilds(steps, step + 1, ans[1:3], resultMap, rainbowMode)


response = ""

size = len(polymerTemplate) - 1
rainbowTableMaxSize = len(insertionList)
i = 1
for key in insertionList:
    print('{}/{}'.format(i, rainbowTableMaxSize))
    i += 1
    rainbowTable[key] = {}
    getChilds(RAINBOW, 1, key, rainbowTable[key], True)

resultMap = {}

for i in range(len(polymerTemplate) - 1):
    print('{}/{}'.format(i + 1, size))
    elementOne = polymerTemplate[i]
    elementTwo = polymerTemplate[i + 1]
    getChilds(STEPS, 1, elementOne + elementTwo, resultMap, False)

resultMap[polymerTemplate[-1]] += 1

maxValue = max(resultMap.values())
minValue = min(resultMap.values())

print('Result = {}'.format(maxValue - minValue))
# 2399822193707
