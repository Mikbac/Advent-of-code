# cat sample | python3 task.py
# cat input | python3 task.py

counter = 0

lineOne = int((input().strip()))

while True:

    try:
        lineTwo = int((input().strip()))
    except EOFError:
        break

    print('{} - {} - {}'.format(lineOne, lineTwo, lineOne < lineTwo))

    if lineOne < lineTwo:
        counter += 1

    lineOne = lineTwo

print('final sum: {}'.format(counter))
# 1121
