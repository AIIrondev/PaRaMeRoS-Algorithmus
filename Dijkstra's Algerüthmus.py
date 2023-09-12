import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import csv
import logging
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
import os

# Erstelle einen Ordner für die exportierten Bilder
if not os.path.exists('exported_images'):
    os.makedirs('exported_images')

logger = logging.getLogger('Dijkstra´s_Algorithm.py')
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
        try:
            u, v, weight = map(int, row)
            data.append((u, v, weight))
        except ValueError:
            logger.error(f"Skipping row with invalid data: {row}")
            continue

# Create a list of graphs
graphs = []
logger.info('create list of graphs')
for i in range(15):
    g = Graph(15)
    for row in data:
        g.add_edge(row[0], row[1], row[2])
    graphs.append(g)

# Calculate and export the shortest distances and paths for each starting vertex
logger.info('calculate and print the shortest distances and paths for each starting vertex')

# Create data dictionary to store locations and distances
data_for_a_star = {"locations": [], "distances": []}

for i, g in enumerate(graphs):
    D = g.dijkstra(i)
    locations = [(0, 0)] * len(D)  # Initialize with dummy values
    distances = [[0] * len(D) for _ in range(len(D))]  # Initialize with zeros

    for vertex in range(len(D)):
        locations[vertex] = (vertex, 0)  # Set coordinates (you can change the y-coordinate as needed)
        distances[vertex][vertex] = 0  # Set zero distance for the same vertex

    for u in range(len(g.edges)):
        for v in range(len(g.edges[u])):
            weight = g.edges[u][v]
            if weight != -1:
                distances[u][v] = weight
                distances[v][u] = weight

    data_for_a_star["locations"].append(locations)
    data_for_a_star["distances"].append(distances)

    # Export the distances to a CSV file
    with open(f"dijkstra_results_{i}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for row in distances:
            writer.writerow(row)

    # Rest of your code for generating images and printing results

# Export the locations to a CSV file
with open("dijkstra_locations.csv", "w", newline='') as file:
    writer = csv.writer(file)
    for row in data_for_a_star["locations"]:
        writer.writerow(row)

# Rest of your code

logging.info('Programm erfolgreich beendet')
