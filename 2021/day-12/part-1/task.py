# cat sample-1 | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

import copy

edges = {}
paths = []

while True:
	try:
		edge = input().strip().split('-')

		if edge[1] != 'start':
			if edge[0] in edges:
				edges[edge[0]].append(edge[1])
			else:
				edges[edge[0]] = [edge[1]]

		if edge[0] != 'start':
			if edge[1] in edges:
				edges[edge[1]].append(edge[0])
			else:
				edges[edge[1]] = [edge[0]]

	except EOFError:
		break

def checkIsSmall(s):
	if ord(s[0]) >= 97 and ord(s[0]) <= 122:
		return True


def goDeep(node, path, edges):
	path.append(node)
	nodes = edges[node]

	if checkIsSmall(node):
		for e in edges:
			if node in edges[e]:
				edges[e].remove(node)

	if node == 'end':
		paths.append(copy.deepcopy(path))
		return

	if len(path) > 100:
		return

	for n in nodes:
		goDeep(n, copy.deepcopy(path), copy.deepcopy(edges))


startNodeEdges = edges['start']
initPath = ['start']

for n in startNodeEdges:
	goDeep(n, copy.deepcopy(initPath), copy.deepcopy(edges))

response = 0

for i in paths:
	lowerQuantity = 0
	for j in i:
		if checkIsSmall(j):
			lowerQuantity += 1
	if lowerQuantity > 2:
		response += 1

print('Small caves quantity = {}'.format(response))
# 4773
