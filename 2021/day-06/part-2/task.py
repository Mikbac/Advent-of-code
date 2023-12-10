# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

DAYS = 256
MAX_START_DAYS = 5
MAX_DAYS = 8

while True:
    try:
        fishes = list(map(int, input().strip().split(',')))
    except EOFError:
        break

fishOptionsList = {}


def getChildsQuantity(fish, day):
    global fishesQuantity

    if str(day) + '-' + str(fish) in fishOptionsList:
        fishesQuantity += fishOptionsList[str(day) + '-' + str(fish)]
        return

    if day < DAYS:
        if fish == 0:
            getChildsQuantity(6, day + 1)
            getChildsQuantity(8, day + 1)
            fishesQuantity += 1
        else:
            getChildsQuantity(fish - 1, day + 1)


fishesQuantity = 0
for k in range(DAYS + 1):
    day = DAYS - k
    for j in range(MAX_DAYS):
        fishesQuantity = 0
        getChildsQuantity(j, day)
        # day-day_to_birth_of_child : children
        fishOptionsList[str(day) + '-' + str(j)] = fishesQuantity

fishesFinalQuantity = len(fishes)

for i in fishes:
    fishesFinalQuantity += fishOptionsList['0-' + str(i)]

print('Fishes quantity: {}'.format(fishesFinalQuantity))
# 1682576647495
