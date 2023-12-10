# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

while True:
    try:
        crabs = list(map(int, input().strip().split(',')))
    except EOFError:
        break

maxValue = max(crabs)
minValue = min(crabs)

results = {}

for i in range(minValue, maxValue + 1):
    results[i] = 0
    for j in crabs:
        distance = abs(i - j)
        for k in range(1, distance + 1):
            results[i] += k
    print('{}/{}'.format(i, maxValue))

minAnsKey = max(results.values())
minAnsValue = max(results.values())

for key, value in results.items():
    if value < minAnsValue:
        minAnsKey = key
        minAnsValue = value

print('Min position: {}, min fuel: {}'.format(minAnsKey, minAnsValue))
# 96678050
