# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

oneCounter = {}
zeroCounter = {}

binaryNumber = input().strip()

for i in range(len(binaryNumber)):
    oneCounter[i] = 0
    zeroCounter[i] = 0

    if binaryNumber[i] == '1':
        oneCounter[i] += 1

    if binaryNumber[i] == '0':
        zeroCounter[i] += 1

while True:

    try:
        binaryNumber = input().strip()
    except EOFError:
        break

    for i in range(len(binaryNumber)):
        if binaryNumber[i] == '1':
            oneCounter[i] += 1

        if binaryNumber[i] == '0':
            zeroCounter[i] += 1

gammaBinary = ''
epsilonBinary = ''

for i in range(len(oneCounter)):
    oneQuantity = oneCounter[i]
    zeroQuantity = zeroCounter[i]

    print('{} - {}'.format(oneQuantity, zeroQuantity))

    if oneQuantity > zeroQuantity:
        gammaBinary += '1'
        epsilonBinary += '0'
    else:
        gammaBinary += '0'
        epsilonBinary += '1'

print('gamma binary: {} - epsilon binary: {}'.format(gammaBinary, epsilonBinary))

gamma = int(gammaBinary, 2)
epsilon = int(epsilonBinary, 2)

print('gamma: {} - epsilon: {}'.format(gamma, epsilon))

print('result: {}'.format(gamma * epsilon))
# 3633500