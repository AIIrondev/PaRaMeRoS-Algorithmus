import tkinter as tk
from PIL import ImageTk, Image
import threading
import random
import datetime
from PIL import ImageDraw
import csv

def create_shapes(event):
    x, y = event.x, event.y
    if event.num in (1, 3):  # Linker oder rechter Mausbutton
        shape = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
        shapes.append(("circle", shape))
        print(f"Punkt Koordinaten: ({x}, {y})")
    elif event.num == 2:  # Mittlerer Mausbutton
        canvas.line_start = (x, y)

def draw_line(event):
    if hasattr(canvas, 'line_start'):
        x, y = event.x, event.y
        canvas.delete("current_line")
        canvas.create_line(canvas.line_start[0], canvas.line_start[1], x, y, fill="green", width=6, tags="current_line")
        label.config(text=f"Maus Koordinaten: ({event.x}, {event.y})")

def finish_line(event):
    if hasattr(canvas, 'line_start'):
        x, y = event.x, event.y
        canvas.delete("current_line")
        shape = canvas.create_line(canvas.line_start[0], canvas.line_start[1], x, y, fill="green", width=6)
        shapes.append(("line", shape))
        line_coordinates = (canvas.line_start[0], canvas.line_start[1], x, y)
        line_coordinates_list.append(line_coordinates)
        del canvas.line_start
        print("Eine Linie wurde gezeichnet!")

def delete_last_shape(event):
    if shapes and line_coordinates_list:
        shape_type, shape = shapes.pop()
        line_coordinates_list.pop()
        canvas.delete(shape)
        if shape_type == "circle":
            print("Der letzte Kreis wurde gelöscht!")
        elif shape_type == "line":
            print("Die letzte Linie wurde gelöscht!")

object_coordinates_c = {}
object_coordinates_l = {}

def calculate_paths_thread():
    # Algorithmus für das Path Finding System
    path_order = [i for i in range(len(line_coordinates_list))]
    path_found = False
    max_iterations = 10000  # Maximale Anzahl von Iterationen, um einen gültigen Pfad zu finden

    # Generiere eine eindeutige ID für jedes Objekt
    object_coordinates_c = {}
    for i, shape in enumerate(shapes):
        if shape[0] == "circle":
            object_id = f"Punkte_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_c[object_id] = (coords[0], coords[1])
            print("es wurde eine ID zugewiesen an einen Kreis zugewiesen")

    for i, shape in enumerate(shapes):
        if shape[0] == "line":
            object_id = f"Line_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_l[object_id] = (coords[0], coords[1])
            print("es wurde eine ID zugewiesen an einen Linie zugewiesen")

    # Simuliere die Strecken in der Reihenfolge
    iteration_count = 0
    while not path_found and iteration_count < max_iterations:
        current_path = []
        for order in path_order:
            line_coordinates = line_coordinates_list[order]
            start_x, start_y, end_x, end_y = line_coordinates
            print("Hier wird eine sache gemacht_1")

            # Führe eine Debugging-Anweisung aus, um zu überprüfen, welche Linien untersucht werden
            print(f"Untersuche Linie {order + 1}: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")

            # Path-Überprüfung einfügen und Debugging-Anweisungen
            if is_path_possible(start_x, start_y, end_x, end_y):
                current_path.append(line_coordinates)
                print("Hier wird geprueft ob ein Weg possible ist")
            else:
                print(f"Linie {order + 1} kann nicht in den Pfad aufgenommen werden.")
                break

        # Wenn alle Strecken möglich sind, wurde ein gültiger Pfad gefunden
        if len(current_path) == len(path_order):
            path_found = True
            print("Gueltiger Pfad gefunden:")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("log.fll", "a") as file:
                file.write(f"\n\n--- Protokoll vom {timestamp} ---\n")
                total_length = 0
                for line_coordinates in current_path:
                    start_x, start_y, end_x, end_y = line_coordinates
                    length = calculate_length(start_x, start_y, end_x, end_y)
                    total_length += length
                    file.write(
                        f"Strecke: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y}), Laenge: {length}\n")
                for object_id, coords in object_coordinates_c.items():
                    x, y = coords
                    file.write(f"{object_id}: ({x}, {y})\n")
                    element_list = (f"{object_id}: ({x}, {y})")
                for object_id, coords in object_coordinates_l.items():
                    x, y = coords
                    file.write(f"{object_id}: ({x}, {y})\n")
                file.write(f"Gesamtlaenge: {total_length}")

            generate_diagram(current_path, path_order)

        # Permutation der Reihenfolge für die nächste Iteration
        next_permutation(path_order)
        iteration_count += 1

    if path_found:
        print("Gueltiger Pfad gefunden:")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("log.fll", "a") as file:
            generate_diagram(current_path, path_order)
            generate_table(shapes, line_coordinates_list)

    else:
        print("Kein gueltiger Pfad gefunden!")

def generate_table(shapes, line_coordinates_list):
    with open("table.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Objekt ID", "Koordinate Anfang", "Koordinate Ende", "Laenge"])
        for i, shape in enumerate(shapes):
            if shape[0] == "circle":
                object_id = f"Punkte_ID{i + 1}"
                coords = canvas.coords(shape[1])
                x, y = coords[0], coords[1]
                row = [object_id, f"({x}; {y})", "", ""]
                writer.writerow(row)

        for i, shape in enumerate(shapes):
            if shape[0] == "line":
                object_id = f"Line_ID{i + 1}"
                coords = canvas.coords(shape[1])
                start_x, start_y, end_x, end_y = coords
                length = calculate_length(start_x, start_y, end_x, end_y)
                row = [object_id, f"({start_x}; {start_y})", f"({end_x}; {end_y})", f"{length:.2f}"]
                writer.writerow(row)

    with open("Dijkstra_data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["source", "target", "weight"])
        for i, shape in enumerate(shapes):
            if shape[0] == "line":
                coords = canvas.coords(shape[1])
                start_x, start_y, end_x, end_y = coords
                length = calculate_length(start_x, start_y, end_x, end_y)
                writer.writerow(f"({start_x}; {start_y})", f"({end_x}; {end_y})", f"{length:.2f}")

    with open("log.fll", "a") as file:
        file.write("Die Linien Laengen und Punkte Koordinaten wurden in |Dijkstra_data.csv| gespeichert!")

def create_line_network():
    if line_coordinates_list:
        print("Anfangs- und Endkoordinaten der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            print(f"Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")
            label_1.config(text=f"Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")
        print("Beruehrungspunkte der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            for point in shapes:
                if point[0] == "circle":
                    point_x, point_y = canvas.coords(point[1])[0], canvas.coords(point[1])[1]
                    if point_x >= min(start_x, end_x) and point_x <= max(start_x, end_x) and point_y >= min(start_y, end_y) and point_y <= max(start_y, end_y):
                        print(f"Beruehrter Punkt: ({point_x}, {point_y})")
                        label_2.config(text=f"Beruehrungspunkte auf den Linien: ({point_x}), ({point_y})")

    # Führe den Algorithmus in einem separaten Thread aus
    print("jetzt werden die threats gestartet")
    thread = threading.Thread(target=calculate_paths_thread)
    thread.start()
    print("die Threats sind jetzt abgeschlossen")

def is_path_possible(start_x, start_y, end_x, end_y):
    # Here, we will check if the line intersects with circles' bounding areas
    for line_coordinates in line_coordinates_list:
        line_start_x1, line_start_y1, line_end_x1, line_end_y1 = line_coordinates
        if lines_intersect(start_x, start_y, end_x, end_y, line_start_x1, line_start_y1, line_end_x1, line_end_y1):
            # If die Linien gekreuzen, return True
            return True

    for shape in shapes:
        if shape[0] == "circle":
            circle_center_x, circle_center_y = canvas.coords(shape[1])[0], canvas.coords(shape[1])[1]
            radius = 50  # Set the radius as per your requirement

            # Calculate the distance from the start and end points of the line to the center of the circle
            distance_start = ((start_x - circle_center_x) ** 2 + (start_y - circle_center_y) ** 2) ** 0.5
            distance_end = ((end_x - circle_center_x) ** 2 + (end_y - circle_center_y) ** 2) ** 0.5

            # Check if the start and end points are within the circle's bounding area
            if distance_start <= radius and distance_end <= radius:
                # The line intersects with the circle's bounding area, so it's possible
                # Save the line information to a file if needed
                with open("test_speicher.fll", "a") as WRITE:
                    WRITE.write(f"Line from ({start_x}, {start_y}) to ({end_x}, {end_y}) intersects with circle ({circle_center_x}, {circle_center_y})\n")
                return True

    # If the line does not intersect with any circle's bounding area, it's possible
    return True

def calculate_length(start_x, start_y, end_x, end_y):
    # Hier kannst du die Länge der Strecke berechnen
    # Beispiel-Implementierung: Euklidischer Abstand
    print("jetzt wurde die laenge gespeichert!")
    dx = end_x - start_x
    dy = end_y - start_y
    return ((dx ** 2) + (dy ** 2)) ** 0.5

def lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Überprüft, ob sich zwei Linien schneiden
    # Rückgabe True, wenn sich die Linien schneiden, andernfalls False

    # Berechnung der Richtungsvektoren der Linien
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    # Berechnung des determinantenbasierten Kollisionsalgorithmus
    denominator = dx1 * dy2 - dx2 * dy1
    if denominator == 0:
        return False  # Linien sind parallel oder identisch

    # Berechnung der Parameter für den Schnittpunkt
    t1 = ((x1 - x3) * dy2 - (y1 - y3) * dx2) / denominator
    t2 = ((x1 - x3) * dy1 - (y1 - y3) * dx1) / denominator

    # Überprüfung, ob der Schnittpunkt innerhalb des definierten Bereichs liegt
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        print("hier wird geprueft ob die linien sich durch queren")
        return True  # Linien schneiden sich
    else:
        return False  # Linien schneiden sich nicht

def next_permutation(arr):
    # Findet die nächste Permutation des Arrays 'arr' (lexikographische Ordnung)
    # Implementierung des Algorithmus von Narayana Pandita
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while j > i and arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])

def generate_diagram(path, path_order):
    # Hier kannst du die Diagrammerzeugung implementieren
    # Beispiel: Zufällige Farben für Linien und Kreise
    diagram = Image.new("RGB", (705, 420), "white")
    draw = ImageDraw.Draw(diagram)

    # Beschriftungen der Objekte
    for i, shape in enumerate(shapes):
        if shape[0] == "circle":
            object_id = f"Object{i + 1}"
            coords = canvas.coords(shape[1])
            x, y = coords[0], coords[1]
            draw.text((x, y), object_id, fill="black")

    # Zeichne den Baum
    level_height = 60
    level_padding = 40
    node_radius = 8
    leaf_nodes = []
    for i, order in enumerate(path_order):
        line_coordinates = line_coordinates_list[order]
        start_x, start_y, end_x, end_y = line_coordinates
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line([(start_x, start_y), (end_x, end_y)], fill=color, width=6)
        leaf_nodes.append((order, (start_x, start_y)))

    # Zeichne die Blattknoten
    for leaf_node in leaf_nodes:
        order, (x, y) = leaf_node
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.ellipse([(x - node_radius, y - node_radius), (x + node_radius, y + node_radius)], fill=color)

    # Zeichne die Verbindungslinien zwischen den Knoten
    for i in range(len(leaf_nodes) - 1):
        order1, (x1, y1) = leaf_nodes[i]
        order2, (x2, y2) = leaf_nodes[i + 1]
        draw.line([(x1, y1 + node_radius), (x2, y2 - node_radius)], fill="black", width=2)

    diagram.save("diagram.png")
    print("Diagramm erzeugt und als 'diagram.png' gespeichert.")

def create_button(shape_type, index):
    if shape_type == "circle":
        button_text = f"Kreis {index + 1}"
        return tk.Button(root, text=button_text, command=lambda index=index: linien_creator(index))
    elif shape_type == "line":
        button_text = f"Linie {index + 1}"
        return tk.Button(root, text=button_text, command=lambda index=index: linien_creator(index))

def create_buttons_for_shapes():
    button_frame = tk.Frame(root)
    button_frame.pack()

    for i, shape in enumerate(shapes):
        shape_type, _ = shape
        button = create_button(shape_type, i)
        button.pack(fill=tk.BOTH, padx=5, pady=5)

def display_function_explanations():
    explanation_text = """
    Hier sind die Erklärungen für die verschiedenen Funktionen:

    - Linksklick / Rechtsklick: Fügt einen roten Punkt (Kreis) an der Mausposition hinzu.
    - Mittelklick: Markiert den Startpunkt einer Linie.
    - Ziehen bei Mittelklick: Zeichnet eine temporäre grüne Linie.
    - Loslassen nach Mittelklick: Zeichnet eine grüne Linie und speichert sie.
    - Taste 'z': Löscht die zuletzt gezeichnete Form (Kreis oder Linie).
    - Taste 'l': Erzeugt Schaltflächen für die vorhandenen Formen.
    - Taste 'b': Führt den Path Finding Algorithmus aus.

    Die Schaltfläche 'Path Finding' führt den Algorithmus aus, um gültige Pfade zu berechnen.
    Die Schaltfläche 'Auflistung der Linien' zeigt Schaltflächen für jede Linie und jeden Kreis an.
    Die Schaltfläche 'Neue Verbindung erstellen' erstellt eine neue Verbindung mit ausgewähltem Index.
    """
    current_text = explanation_label.cget("text")
    if current_text == explanation_text:
        explanation_label.config(text="")
    else:
        explanation_label.config(text=explanation_text)


def linien_creator(shape_index):
    shape = shapes[shape_index]
    shape_type, coords = shape

    if shape_type == "line":
        start_x, start_y, end_x, end_y = canvas.coords(coords)
        length = calculate_length(start_x, start_y, end_x, end_y)
        label_4.config(text=f"Linien Verbindung {shape_index + 1}: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y}), Laenge: {length}")
    else:
        print(f"Keine Linie gefunden fuer Shape {shape_index + 1}")

def update_mouse_coordinates(event):
    label.config(text=f"Maus Koordinaten: ({event.x_root - root.winfo_x()}, {event.y_root - root.winfo_y()})")

root = tk.Tk()
root.title("FLL PaRaMeRoS Algeruethmus")

logo_path = "LOGO.jpeg"
logo = ImageTk.PhotoImage(Image.open(logo_path))
root.iconphoto(True, logo)

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

shapes = []
line_coordinates_list = []

canvas.bind("<Button-1>", create_shapes)
canvas.bind("<Button-2>", create_shapes)
canvas.bind("<Button-3>", create_shapes)
canvas.bind("<B2-Motion>", draw_line)
canvas.bind("<ButtonRelease-2>", finish_line)
root.bind("z", delete_last_shape)
root.bind("l", lambda event: [create_buttons_for_shapes()])
root.bind("b", lambda event: create_line_network())

render_button_3 = tk.Button(root, text="?", command=display_function_explanations)
render_button_3.pack()

explanation_label = tk.Label(root, text="", justify=tk.LEFT)
explanation_label.pack()

image_path = "FLL_2023-24_Map.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=photo)

label = tk.Label(root, text="Maus Koordinaten: (0, 0)", bd=1, relief=tk.SUNKEN, anchor=tk.W)
label.pack(side=tk.TOP, fill=tk.X)

label_1 = tk.Label(root, text="Anfangs-Koordinate: (0, 0), End-Koordinate: (0, 0)")
label_1.pack()

label_2 = tk.Label(root, text="Beruehrungspunkte auf den Linien: (0, 0)")
label_2.pack()

canvas.bind("<Motion>", update_mouse_coordinates)

render_button = tk.Button(root, text="Path Finding", command=create_line_network)
render_button.pack()

label_3 = tk.Label(root, text="Liste der Linien")
label_3.pack()

label_4 = tk.Label(root, text="Linien Verbindung 1: (0,0) Leange: (0)")
label_4.pack()

render_button_1 = tk.Button(root, text="Auflistung der Linien", command=create_buttons_for_shapes)
render_button_1.pack()

render_button_2 = tk.Button(root, text="Neue Verbindung creiren")
render_button_2.pack()

render_fild = tk.Entry(root)
render_fild.pack()

root.mainloop()