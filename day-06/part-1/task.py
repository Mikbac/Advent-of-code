# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

DAYS = 80

while True:
    try:
        fishes = list(map(int, input().strip().split(',')))
        print(fishes)

    except EOFError:
        break

for i in range(DAYS):
    for j in range(len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            fishes.append(8)
        else:
            fishes[j] -= 1
    print('Day-{}, fishes quantity: {}'.format(i + 1, len(fishes)))

# 373378
