import math
import heapq
import csv
import os
import logging

csv_folder = 'csv_files'
log_folder = 'log_files'
data = {}

logger = logging.getLogger('A_star.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_folder, 'sys.log'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Erstelle einen Ordner für die CSV-Dateien
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)
    logger.warning(f"Folder {csv_folder} created.")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    logger.warning(f"Folder {log_folder} created.")

class AStarGraph:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, start, goal):
        logger.debug('heuristic')
        x1, y1 = self.graph["locations"][start]
        x2, y2 = self.graph["locations"][goal]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def neighbors(self, node):
        logger.debug('neighbors')
        return [neighbor for neighbor in range(len(self.graph["locations"])) if self.graph["distances"][node][neighbor] != 0]

    def a_star_search(self, start, goal):
        logger.debug('a_star_search')
        open_list = []
        closed_list = set()
        start_node = (start, 0)
        heapq.heappush(open_list, start_node)
        g_score = {node: float("inf") for node in range(len(self.graph["locations"]))}
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
                tentative_g_score = g_score[current_node] + self.graph["distances"][current_node][neighbor]
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (neighbor, f_score))

        return None

def create_data_model():
    data = {}
    data["locations"] = []
    data["distances"] = []  # Neu hinzugefügt
    # Öffnen Sie die CSV-Datei und lesen Sie die Daten ein
    with open(os.path.join(csv_folder, "node_coordinates.csv"), "r") as file:
        logger.info(f'open file{csv_folder}, node_coordinates.csv')
        reader = csv.reader(file)
        next(reader)  # Überspringen Sie die Header-Zeile
        for row in reader:
            try:
                x, y = map(int, row[2].strip('[]').replace(' ', '').split(','))  # Angepasst für Koordinatenextraktion
                data["locations"].append((x, y))
            except (ValueError, IndexError):
                print(f"Fehler beim Lesen der Zeile: {row}")

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
    data["depot"] = 0
    return data

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

# Restlicher Code für die Ausführung des A*-Algorithmus
def main():
    data = create_data_model()
    graph = AStarGraph(data)
    start_node = 0
    goal_node = 14

    path = graph.a_star_search(start_node, goal_node)

    if path:
        print("A* Path:", path)
    else:
        print("Kein Pfad gefunden.")

if __name__ == "__main__":
    main()
