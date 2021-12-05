# cat sample | python3 task.py
# cat input | python3 task.py

counter = 0

lineOne = int((input().strip()))
lineTwo = int((input().strip()))
lineThree = int((input().strip()))

while True:

    sumOne = lineOne + lineTwo + lineThree

    try:

        lineOne = lineTwo
        lineTwo = lineThree

        lineThree = int((input().strip()))

        sumTwo = lineOne + lineTwo + lineThree

        print('{} - {} - {}'.format(sumOne, sumTwo, sumOne < sumTwo))

        if sumOne < sumTwo:
            counter += 1

        sumOne = sumTwo

    except EOFError:
        break

print('final sum: {}'.format(counter))
