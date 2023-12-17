# Created by MikBac on 2023


import igraph as ig

traffic_map = []


def main():
	global traffic_map
	global results
	edges = []
	weights = []

	with open('sample', 'r', encoding='utf-8') as input_:
		for row, line in enumerate(input_):
			traffic_map.append([int(x) for x in list(line.strip())])

	for i in range(len(traffic_map)):
		for j in range(len(traffic_map[i])):
			if i == 0:
				if j == len(traffic_map[i]) - 1:
					edges.append((i * 1000 + j, (i + 1) * 1000 + j))
					weights.append(traffic_map[i + 1][j])
				else:
					edges.append((i * 1000 + j, (i + 1) * 1000 + j))
					weights.append(traffic_map[i + 1][j])
					edges.append((i * 1000 + j, i * 1000 + j + 1))
					weights.append(traffic_map[i][j + 1])

			elif i == len(traffic_map) - 1:
				if j == len(traffic_map[i]) - 1:
					edges.append((i * 1000 + j, (i - 1) * 1000 + j))
					weights.append(traffic_map[i - 1][j])
				else:
					edges.append((i * 1000 + j, (i - 1) * 1000 + j))
					weights.append(traffic_map[i - 1][j])
					edges.append((i * 1000 + j, i * 1000 + j + 1))
					weights.append(traffic_map[i][j + 1])

			elif j == len(traffic_map[i]) - 1:
				edges.append((i * 1000 + j, (i - 1) * 1000 + j))
				weights.append(traffic_map[i - 1][j])
				edges.append((i * 1000 + j, (i + 1) * 1000 + j))
				weights.append(traffic_map[i + 1][j])

			else:
				edges.append((i * 1000 + j, i * 1000 + j + 1))
				weights.append(traffic_map[i][j + 1])
				edges.append((i * 1000 + j, (i - 1) * 1000 + j))
				weights.append(traffic_map[i - 1][j])
				edges.append((i * 1000 + j, (i + 1) * 1000 + j))
				weights.append(traffic_map[i + 1][j])

	G = ig.Graph(edges, directed=True)
	G.es['weight'] = weights
	results = G.get_shortest_paths(0, (len(traffic_map) - 1) * 1000 + (len(traffic_map[0]) - 1), weights='weight')

	if len(results[0]) > 0:
	# Add up the weights across all edges on the shortest path
		distance = 0
		for e in results[0]:
			print(e)
			distance += G.es[e]["weight"]
		print("Shortest weighted distance is: ", distance)
	else:
		print("End node could not be reached!")
	print('Answer: {}'.format(path))


if __name__ == "__main__":
	main()
