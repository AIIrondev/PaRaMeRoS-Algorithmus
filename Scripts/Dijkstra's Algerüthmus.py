import csv
from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        D = {v: float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            dist, current_vertex = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

# Read the graph data from the CSV file
data = []
with open("Dijkstra_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        data.append(tuple(map(int, row)))

# Create a list of graphs
graphs = []
for i in range(9):
    g = Graph(9)
    for row in data:
        g.add_edge(row[0], row[1], row[2])
    graphs.append(g)

# Calculate and print the shortest distances for each starting vertex
for i, g in enumerate(graphs):
    D = g.dijkstra(i)
    for vertex in range(len(D)):
        print("Distance from vertex", i, "to vertex", vertex, "is", D[vertex])
