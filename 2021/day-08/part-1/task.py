# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

numberCounter = 0

while True:
    try:
        line = input().strip().split(' | ')
        partOne = line[0]
        partTwo = line[1]

        numbers = partTwo.split()

        for n in numbers:
            if len(n) == 2:
                numberCounter += 1
            if len(n) == 3:
                numberCounter += 1
            if len(n) == 4:
                numberCounter += 1
            if len(n) == 7:
                numberCounter += 1

    except EOFError:
        break

print('Counter = {}'.format(numberCounter))
# 284
