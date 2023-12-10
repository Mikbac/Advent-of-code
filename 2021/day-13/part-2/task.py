# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

pointsList = []
instructionsList = []
maxX = 0
maxY = 0

while True:
    line = input().strip().split(',')
    if len(line) == 2:
        pointX = int(line[0])
        pointY = int(line[1])
        pointsList.append([pointX, pointY])

        if pointX > maxX:
            maxX = pointX

        if pointY > maxY:
            maxY = pointY
    else:
        break

while True:
    try:
        line = input().strip().split()
        instruction = line[2].split('=')
        instructionsList.append([instruction[0], instruction[1]])
    except EOFError:
        break

paper = []

for i in range(maxY + 1):
    paper.append(['.'] * (maxX + 1))

for p in pointsList:
    paper[p[1]][p[0]] = '#'

for instruction in instructionsList:

    linePosition = int(instruction[1])

    if instruction[0] == 'y':
        paper[linePosition] = ['-'] * (maxY + 1)
        for y in range(len(paper)):
            if y > linePosition:
                distance = linePosition - (y - linePosition)
                for x in range(len(paper[y])):
                    if paper[y][x] == '#':
                        paper[distance][x] = '#'

        del paper[linePosition:]
        maxX = len(paper[0])
        maxY = len(paper)

    if instruction[0] == 'x':
        for y in range(len(paper)):
            for x in range(len(paper[y])):
                if x == linePosition:
                    paper[y][x] = '-'
                if x > linePosition:
                    distance = linePosition - (x - linePosition)
                    if paper[y][x] == '#':
                        paper[y][distance] = '#'
            del paper[y][linePosition:]

for p in paper:
    print(p)

# BLHFJPJF
