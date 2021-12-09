# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

cavesList = []
counter = 0

while True:
    try:
        line = list(map(int, input().strip()))
        cavesList.append(line)
    except EOFError:
        break

for i in range(len(cavesList)):
    lineLength = len(cavesList[i])
    for j in range(len(cavesList[i])):
        point = cavesList[i][j]
        if i == 0:
            if j == 0:
                if point < cavesList[i + 1][j] and point < cavesList[i][j + 1]:
                    counter += point + 1
            if j == lineLength - 1:
                if point < cavesList[i + 1][j] and point < cavesList[i][j - 1]:
                    counter += point + 1
            if j != 0 and j != lineLength - 1:
                if point < cavesList[i + 1][j] and point < cavesList[i][j + 1] and point < cavesList[i][j - 1]:
                    counter += point + 1
        if i == len(cavesList) - 1:
            if j == 0:
                if point < cavesList[i - 1][j] and point < cavesList[i][j + 1]:
                    counter += point + 1
            if j == lineLength - 1:
                if point < cavesList[i - 1][j] and point < cavesList[i][j - 1]:
                    counter += point + 1
            if j != 0 and j != lineLength - 1:
                if point < cavesList[i - 1][j] and point < cavesList[i][j + 1] and point < cavesList[i][j - 1]:
                    counter += point + 1
        if i != 0 and i != len(cavesList) - 1:
            if j == 0:
                if point < cavesList[i + 1][j] and point < cavesList[i][j + 1] and point < cavesList[i - 1][j]:
                    counter += point + 1
            if j == lineLength - 1:
                if point < cavesList[i + 1][j] and point < cavesList[i][j - 1] and point < cavesList[i - 1][j]:
                    counter += point + 1
            if j != 0 and j != lineLength - 1:
                if point < cavesList[i + 1][j] and point < cavesList[i][j + 1] and point < cavesList[i][
                    j - 1] and point < cavesList[i - 1][j]:
                    counter += point + 1

print('Counter = {}'.format(counter))
# 502
