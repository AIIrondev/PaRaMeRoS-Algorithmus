import csv
from queue import PriorityQueue
import logging
import networkx as nx
import matplotlib.pyplot as plt

logger = logging.getLogger('Dijkstra´s_Algeruethmus.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('sys.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Graph:
    def __init__(self, num_of_vertices):
        logger.info('init')
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        logger.info('add edge')
        if 0 <= u < self.v and 0 <= v < self.v:
            self.edges[u][v] = weight
            self.edges[v][u] = weight
        else:
            logger.error(f"Invalid edge: ({u}, {v})")

    def dijkstra(self, start_vertex):
        logger.info('dijkstra')
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
    logger.info('open file')
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        data.append(tuple(map(int, row)))

# Create a list of graphs
graphs = []
logger.info('create list of graphs')
for i in range(9):
    g = Graph(9)
    for row in data:
        g.add_edge(row[0], row[1], row[2])
    graphs.append(g)

# Calculate and print the shortest distances for each starting vertex
logger.info('calculate and print the shortest distances for each starting vertex')
for i, g in enumerate(graphs):
    D = g.dijkstra(i)
    G = nx.Graph()
    
    # Add nodes to the graph
    for vertex in range(len(D)):
        G.add_node(vertex)
    
    # Add edges with their weights to the graph
    for u in range(len(g.edges)):
        for v in range(len(g.edges[u])):
            weight = g.edges[u][v]
            if weight != -1:
                G.add_edge(u, v, weight=weight)
    
    # Plot the graph
    pos = nx.spring_layout(G)  # Define the layout for the graph
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    
    plt.title(f"Shortest Path from vertex {i}")
    plt.show()

    for vertex in range(len(D)):
        print("Distance from vertex", i, "to vertex", vertex, "is", D[vertex])