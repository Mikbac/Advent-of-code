# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

positionHorizontal = 0
positionDepth = 0

while True:

    try:
        command = input().strip()
    except EOFError:
        break

    action = command.split()[0]
    value = int(command.split()[1])

    print('{} - {}'.format(action, value))

    if action == 'forward':
        positionHorizontal += value

    if action == 'down':
        positionDepth += value

    if action == 'up':
        positionDepth -= value

print('final positionHorizontal: {}'.format(positionHorizontal))

print('final positionDepth: {}'.format(positionDepth))

print('final answer (positionDepth * positionDepth: {})'.format(positionHorizontal * positionDepth))
# 1962940
