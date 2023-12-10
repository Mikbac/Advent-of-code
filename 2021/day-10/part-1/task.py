# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

missedBrackets = []

while True:
    try:
        line = list(input().strip())

        pairs = {"{": "}", "(": ")", "[": "]", "<": ">"}
        queue = []

        for c in line:
            if c in "{[(<":
                queue.append(c)
            elif queue and c == pairs[queue[-1]]:
                queue.pop()
            else:
                missedBrackets.append(c)
                break

    except EOFError:
        break

result = 0
for s in missedBrackets:
    if s == ')':
        result += 3
    if s == ']':
        result += 57
    if s == '}':
        result += 1197
    if s == '>':
        result += 25137

print('Result = {}'.format(result))
# 193275