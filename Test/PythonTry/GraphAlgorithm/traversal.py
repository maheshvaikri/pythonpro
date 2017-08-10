from queue import Queue
from graph import *

def breadth_first(graph, start=0):
	queue=Queue()
	queue.put(start)

	visited = np.zeros(graph.numVertices)

	while not queue.empty():
		vertex = queue.get()

		if visited[vertex] == 1:
			continue

		print("Visit:", vertex)

		visited[vertex] = 1

		for v in graph.get_adjacent_vertices(vertex):
			if visited[v] != 1:
				queue.put(v)

def depth_first(graph, visited, current=0):
	if visited[current] == 1:
		return

	visited[current] = 1
	print("Visit:", current)

	for vertex in graph.get_adjacent_vertices(current):
		depth_first(graph, visited, vertex)


# g = AdjacencyMatrixGraph(9, directed=True)
g = AdjacencyMatrixGraph(9)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,7)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,8)
g.add_edge(3,5)
g.add_edge(3,6)
g.add_edge(3,7)
g.add_edge(4,8)






# breadth_first(g, 0)

visited = np.zeros(g.numVertices)

depth_first(g, visited)
