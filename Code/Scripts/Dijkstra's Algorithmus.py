import csv
import logging
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
import os

# Erstelle einen Ordner für die exportierten Bilder
if not os.path.exists('exported_images'):
    os.makedirs('exported_images')

# Erstelle einen Ordner für die CSV-Dateien
csv_folder = '../csv_files'
log_folder = '../log_files'
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logger = logging.getLogger('Dijkstra´s_Algorithm.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_folder, 'sys.log'))
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
with open(os.path.join(csv_folder, "dijkstra_data.csv"), "r") as file:
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

# Create a CSV file to store the results
with open(os.path.join(csv_folder, "dijkstra_results.csv"), mode='w', newline='') as csv_file:
    fieldnames = ['Start Vertex', 'End Vertex', 'Shortest Distance', 'Shortest Path']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Calculate and export the shortest distances and paths for each starting vertex
    logger.info('calculate and print the shortest distances and paths for each starting vertex')
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

        # Find the shortest path from the starting vertex to all other vertices
        shortest_paths = {vertex: nx.shortest_path(G, source=i, target=vertex, weight='weight') for vertex in range(len(D))}

        # Write the results to the CSV file
        for vertex in range(len(D)):
            if vertex != i:
                writer.writerow({
                    'Start Vertex': i,
                    'End Vertex': vertex,
                    'Shortest Distance': D[vertex],
                    'Shortest Path': shortest_paths[vertex]
                })

        # Erhöhe die Auflösung auf 4K (3840x2160)
        plt.figure(figsize=(16, 9))

        # Plot the graph with the shortest path highlighted in orange
        pos = nx.spring_layout(G)  # Define the layout for the graph
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

        # Draw the shortest path with orange color and arrows
        shortest_path_edges = [(shortest_paths[i][j], shortest_paths[i][j + 1]) for j in range(len(shortest_paths[i]) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='orange', width=2, arrows=True)

        plt.title(f"Shortest Path from vertex {i}")

        # Speichere das Bild im Ordner "exported_images" mit dem Dateinamen "shortest_path_i.png"
        image_filename = os.path.join('exported_images', f'shortest_path_{i}.png')
        plt.savefig(image_filename, dpi=300)  # 300 DPI entspricht 4K-Auflösung

        # Schließe die Matplotlib-Figur
        plt.close()

# Funktion zum Speichern der Koordinaten in einer CSV-Datei
def save_coordinates_to_csv(coordinates, filename):
    with open(os.path.join(csv_folder, filename), mode='w', newline='') as csv_file:
        fieldnames = ['X Coordinate', 'Y Coordinate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for graph_id, graph_coordinates in enumerate(coordinates):
            for vertex, x, y in graph_coordinates:
                writer.writerow({
#                    'Graph': graph_id,
#                    'Vertex': vertex,
                    'X Coordinate': x + 3,
                    'Y Coordinate': y + 3
                })

# Erstellen Sie eine Liste, um die Koordinaten der Knoten zu speichern
coordinates_list = []

# Calculate and export the shortest distances and paths for each starting vertex
logger.info('calculate and print the shortest distances and paths for each starting vertex')
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

    # Find the shortest path from the starting vertex to all other vertices
    shortest_paths = {vertex: nx.shortest_path(G, source=i, target=vertex, weight='weight') for vertex in range(len(D))}

    # Get the positions of nodes for this graph layout
    pos = nx.spring_layout(G)

    # Prepare the coordinates for this graph
    graph_coordinates = [(vertex, pos[vertex][0], pos[vertex][1]) for vertex in range(len(D))]
    coordinates_list.append(graph_coordinates)

# Speichern Sie die Koordinaten in einer CSV-Datei
coordinates_filename = "../node_coordinates.csv"
save_coordinates_to_csv(coordinates_list, coordinates_filename)

logging.info('Programm erfolgreich beendet')
