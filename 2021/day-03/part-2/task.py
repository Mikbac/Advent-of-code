# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

binaryOxygenNumberList = []
binaryC02NumberList = []
bingLength = 0

REMOVE_CONST = '----------'

while True:

    try:
        inputNumber = input().strip()
        binaryOxygenNumberList.append(inputNumber)
        binaryC02NumberList.append(inputNumber)
    except EOFError:
        break

bingLength = len(binaryOxygenNumberList[0])

# ------------------- oxygen

for j in range(bingLength):

    oneCounter = 0
    zeroCounter = 0

    for k in range(len(binaryOxygenNumberList)):
        binaryNumber = binaryOxygenNumberList[k]

        if binaryNumber[j] == '1':
            oneCounter += 1

        if binaryNumber[j] == '0':
            zeroCounter += 1

    mostPopular = '0'
    if oneCounter >= zeroCounter:
        mostPopular = '1'

    for k in range(len(binaryOxygenNumberList)):
        binaryNumber = binaryOxygenNumberList[k]
        if binaryNumber[j] != mostPopular:
            binaryOxygenNumberList[k] = REMOVE_CONST

    binaryOxygenNumberList = list(filter(lambda a: a != REMOVE_CONST, binaryOxygenNumberList))

    if len(binaryOxygenNumberList) == 1:
        break

oxygenBinary = binaryOxygenNumberList[0]

# ------------------- CO2

for j in range(bingLength):

    oneCounter = 0
    zeroCounter = 0

    for k in range(len(binaryC02NumberList)):
        binaryNumber = binaryC02NumberList[k]

        if binaryNumber[j] == '1':
            oneCounter += 1

        if binaryNumber[j] == '0':
            zeroCounter += 1

    mostPopular = '1'
    if zeroCounter <= oneCounter:
        mostPopular = '0'

    for k in range(len(binaryC02NumberList)):
        binaryNumber = binaryC02NumberList[k]
        if binaryNumber[j] != mostPopular:
            binaryC02NumberList[k] = REMOVE_CONST

    binaryC02NumberList = list(filter(lambda a: a != REMOVE_CONST, binaryC02NumberList))

    if len(binaryC02NumberList) == 1:
        break


CO2Binary = binaryC02NumberList[0]

print('oxygen binary: {} - CO2 binary: {}'.format(oxygenBinary, CO2Binary))

oxygen = int(oxygenBinary, 2)
CO2 = int(CO2Binary, 2)

print('gamma: {} - epsilon: {}'.format(oxygen, CO2))

print('result: {}'.format(oxygen * CO2))
# 4550283