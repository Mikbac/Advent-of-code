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


def goDeep(node, path, edges, isTwoLowerAvailable):
	path.append(node)
	nodes = edges[node]

	if checkIsSmall(node):
		if not isTwoLowerAvailable:
			for e in edges:
				if node in edges[e]:
					edges[e].remove(node)
		else:
			if path.count(node) > 1:
				isTwoLowerAvailable = False
				for i in path:
					if checkIsSmall(i):
						for e in edges:
							if i in edges[e]:
								edges[e].remove(i)

	if node == 'end':
		paths.append(copy.deepcopy(path))
		return

	if len(path) > 100:
		return

	for n in nodes:
		goDeep(n, copy.deepcopy(path), copy.deepcopy(edges), isTwoLowerAvailable)


startNodeEdges = edges['start']
initPath = ['start']

for n in startNodeEdges:
	goDeep(n, copy.deepcopy(initPath), copy.deepcopy(edges), True)

response = len(paths)

print('Caves quantity = {}'.format(response))
# too small 116985

