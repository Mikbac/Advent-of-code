# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

import copy

graphList = []


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0} --------> {1}".format(i, dist[i]))

    def BellmanFord(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):

            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

            print('{}/{}'.format(i, self.V - 1))

        self.printArr(dist)
        return dist[self.V - 1]


while True:
    try:
        line = list(map(int, input().strip()))
        bigLine = line
        currentLine = line
        for i in range(4):
            line = copy.deepcopy(currentLine)
            currentLine = []
            for l in line:
                if l + 1 == 10:
                    bigLine.append(1)
                    currentLine.append(1)
                else:
                    bigLine.append(l + 1)
                    currentLine.append(l + 1)

        graphList.append(copy.deepcopy(bigLine))
    except EOFError:
        break

basicSize = len(graphList)

for i in range(4):
    newPart = graphList[-basicSize:]
    for g in newPart:
        newLine = []

        for n in g:
            if n + 1 == 10:
                newLine.append(1)
            else:
                newLine.append(n + 1)
        graphList.append(newLine)

graphSize = len(graphList)

g = Graph(graphSize * graphSize)

edgeCounter = 0

for i in range(len(graphList)):
    for j in range(len(graphList[i])):
        if i == 0:
            if j == 0:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])
            elif j == graphSize - 1:
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])
            else:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])
        elif i == graphSize - 1:
            if j == 0:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
            elif j == graphSize - 1:
                pass
            else:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
        else:
            if j == 0:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])
            elif j == graphSize - 1:
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])
            else:
                g.addEdge(edgeCounter, edgeCounter + 1, graphList[i][j + 1])
                g.addEdge(edgeCounter, edgeCounter + graphSize, graphList[i + 1][j])

        edgeCounter += 1

result = g.BellmanFord(0)

print('Result = {}'.format(result))
# 2927
