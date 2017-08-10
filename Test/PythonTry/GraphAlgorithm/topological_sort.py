from queue import Queue
from graph import *

def topological_sort(graph):
	queue = Queue()

	indegreeMap = {}

	for i in range(graph.numVertices):
		indegreeMap[i] = graph.get_indegree(i)

		# Queue all node which has no dependencies
		# i.e., no edges coming in

		if indegreeMap[i] == 0:
			queue.put(i)

	sortedList = []
	while not queue.empty():

		vertex = queue.get()

		sortedList.append(vertex)

		for v in graph.get_adjacent_vertices(vertex):
			indegreeMap[v] = indegreeMap[v] -1

			if indegreeMap[v] == 0:
				queue.put(v)

	if len(sortedList) != graph.numVertices:
		raise ValueError("This graph has a cycle, topological sort is not possible!")

	print(sortedList)


g = AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,4)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(2,7)
g.add_edge(3,5)
g.add_edge(3,6)
g.add_edge(3,8)
g.add_edge(4,7)
# g.add_edge(8,0)


topological_sort(g)


