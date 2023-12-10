# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

scores = []

while True:
    try:

        isCorrupted = False
        line = list(input().strip())

        pairs = {"{": "}", "(": ")", "[": "]", "<": ">"}
        queue = []

        for c in line:
            if c in "{[(<":
                queue.append(c)
            elif queue and c == pairs[queue[-1]]:
                queue.pop()
            else:
                isCorrupted = True
                break

        if not isCorrupted:
            score = 0
            reversedQueue = []

            while queue:
                reversedQueue.append(queue.pop())

            for i in reversedQueue:
                point = 0

                if i == '(':
                    point = 1

                if i == '[':
                    point = 2

                if i == '{':
                    point = 3

                if i == '<':
                    point = 4

                score = (score * 5) + point

            scores.append(score)
    except EOFError:
        break


scores.sort()

result = scores[(len(scores) // 2)]

print('Result = {}'.format(result))
# 2429644557
