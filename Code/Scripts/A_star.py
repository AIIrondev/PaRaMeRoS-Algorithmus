import math
import heapq
import csv
import os
import logging
import networkx as nx
import matplotlib.pyplot as plt

# Festlegung der Ordner für CSV-Dateien und Log-Dateien
csv_folder = '../csv_files'
log_folder = '../log_files'
data = {}  # Eine leere Datenstruktur zur Aufbewahrung von Informationen

# Konfigurieren des Loggers für die Protokollierung von Informationen
logger = logging.getLogger('A_star.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_folder, 'sys.log'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# Die AStarGraph-Klasse definiert den Graphen und den A*-Algorithmus
class AStarGraph:
    def __init__(self, data):
        self.data = data

    # Diese Methode berechnet die heuristische Schätzung (H-Wert) zwischen zwei Knoten
    def heuristic(self, start, goal):
        logger.debug('heuristic')
        x1, y1 = self.data["locations"][start]
        x2, y2 = self.data["locations"][goal]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Diese Methode gibt die Nachbarn eines Knotens zurück
    def neighbors(self, node):
        logger.debug('neighbors')
        return [neighbor for neighbor in range(len(self.data["locations"])) if self.data["distances"][node][neighbor] != 0]

    # Diese Methode führt die A*-Suche aus
    def a_star_search(self, start, goal):
        logger.debug('a_star_search')
        open_list = []
        closed_list = set()
        start_node = (start, 0)
        heapq.heappush(open_list, start_node)
        g_score = {node: float("inf") for node in range(len(self.data["locations"]))}  # Änderung hier
        g_score[start] = 0
        came_from = {}

        while open_list:
            current_node, current_cost = heapq.heappop(open_list)

            if current_node == goal:
                path = []
                while current_node in came_from:
                    path.insert(0, current_node)
                    current_node = came_from[current_node]
                path.insert(0, start)
                return path

            if current_node in closed_list:
                continue

            closed_list.add(current_node)

            for neighbor in self.neighbors(current_node):
                tentative_g_score = g_score[current_node] + self.data["distances"][current_node][neighbor]
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (neighbor, f_score))


def conf():
    logger.debug("conf...")
    global csv_folder, log_folder, export_folder

    with open("../A_star.config", "r") as f:
        lines = f.readline(1)
        lines = lines.split(" , ")
        csv_folder = lines[0].strip()
        log_folder = lines[1].strip()
        export_folder = lines[2].strip()

    # Überprüfen und Erstellen der Ordner
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)
        logger.warning(f"Folder {csv_folder} created.")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        logger.warning(f"Folder {log_folder} created.")
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
        logger.warning(f"Folder {export_folder} created.")
        

# Diese Methode erstellt das Datenmodell aus CSV-Dateien
def create_data_model():
    global data  # Deklarieren Sie data als global, um es im gesamten Skript sichtbar zu machen
    data = {}
    data["locations"] = []  # Eine Liste zur Aufbewahrung der Koordinaten der Punkte
    data["distances"] = []  # Eine Liste zur Aufbewahrung der Entfernungen zwischen den Punkten

    with open(os.path.join(csv_folder, "node_coordinates.csv"), "r") as file:
        logger.info(f'open file {csv_folder}, node_coordinates.csv')
        reader = csv.reader(file)
        next(reader)  # Überspringen Sie die Header-Zeile
        for row in reader:
            if len(row) >= 2:  # Stellen Sie sicher, dass mindestens 2 Spalten vorhanden sind
                try:
                    x, y = map(float, row)  # X- und Y-Koordinaten als Floats einlesen
                    data["locations"].append((x, y))
                except (ValueError, IndexError):
                    logger.error(f"Fehler beim Lesen der Zeile: {row}")
            else:
                logger.error(f"Ungültige Zeile: {row}")

    # Berechnen Sie die Distanzmatrix direkt hier
    num_locations = len(data["locations"])
    data["distances"] = [[0] * num_locations for _ in range(num_locations)]
    for i in range(num_locations):
        for j in range(i, num_locations):
            x1, y1 = data["locations"][i]
            x2, y2 = data["locations"][j]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            data["distances"][i][j] = distance
            data["distances"][j][i] = distance

    data["num_vehicles"] = 1
    data["depot"] = data["locations"][0]  # Hier verwenden wir den ersten Standort als Depot
    return data


# Diese Methode gibt die Lösung der Route aus
def print_solution(manager, routing, solution):
    print("Lösung:")
    index = routing.Start(0)
    plan_output = []
    route_distance = 0
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        plan_output.append(data["locations"][node_index])  # Nutzen Sie die Koordinaten aus data["locations"]
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    print(f"Entfernung: {route_distance} Einheiten")
    print(f"Geplante Routen-Koordinaten: {plan_output}")
    logger.info(f"Entfernung: {route_distance} Einheiten")
    logger.info(f"Geplante Routen-Koordinaten: {plan_output}")


def find_full_path(graph, start_node, end_node):
    # Verwenden Sie den A*-Algorithmus, um den Pfad zwischen start_node und end_node zu finden
    path = graph.a_star_search(start_node, end_node)
    return path


# Die Hauptmethode, die den A*-Algorithmus ausführt
def main():
    data = create_data_model()
    graph = AStarGraph(data)

    # Start- und Zielknoten
    start_node = 0
    end_node = 14

    full_path = [start_node]  # Beginnen Sie mit dem Startknoten

    for node in range(1, end_node + 1):
        if node != start_node:
            segment = find_full_path(graph, start_node, node)
            full_path.extend(segment[:-1])  # Vermeiden der doppelten Knoten
            start_node = node

    print("Vollständiger Weg:", full_path)
    route_coordinates = [data["locations"][node] for node in full_path]
    print("Route Koordinaten:")
    for coordinate in route_coordinates:
        print(coordinate)

    # Erstellen Sie den Graphen und zeichnen Sie die Route
    G = nx.Graph()
    G.add_nodes_from(range(len(route_coordinates)))
    for i in range(len(route_coordinates) - 1):
        G.add_edge(full_path[i], full_path[i + 1])

    pos = {i: route_coordinates[i] for i in range(len(route_coordinates))}
    nx.draw(G, pos, with_labels=True, node_size=100)
    image_filename = os.path.join(export_folder, 'shortest_path_a_star.png')
    plt.savefig(image_filename, dpi=300)  # 300 DPI entspricht 4K-Auflösung
    plt.show()

if __name__ == "__main__":
    conf()
    main()
