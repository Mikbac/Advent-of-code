# cat sample | python3 task.py
# cat input | python3 task.py

positionHorizontal = 0
positionDepth = 0
aim = 0

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
        positionDepth += aim * value

    if action == 'down':
        aim += value

    if action == 'up':
        aim -= value

print('final positionHorizontal: {}'.format(positionHorizontal))
#

print('final positionDepth: {}'.format(positionDepth))
#

print('final answer (positionDepth * positionDepth: {})'.format(positionHorizontal * positionDepth))