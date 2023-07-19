import tkinter as tk
from PIL import ImageTk, Image
import threading
import random
import datetime
from PIL import ImageDraw
import time


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


def delete_last_shape(event):
    if len(shapes) >= 1 and len(line_coordinates_list) >= 1:
        shape_type, shape = shapes.pop()
        line_coordinates_list.pop()
        canvas.delete(shape)
    if shapes:
        shape_type, shape = shapes.pop(0)
        if shape_type == "circle":
            canvas.delete(shape)
        elif shape_type == "line":
            canvas.delete(shape)
            line_coordinates_list.pop(0)


def calculate_paths_thread():
    # Algorithmus für das Path Finding System
    path_order = [i for i in range(len(line_coordinates_list))]
    path_found = False

    # Generiere eine eindeutige ID für jedes Objekt
    object_coordinates_c = {}
    for i, shape in enumerate(shapes):
        if shape[0] == "circle":
            object_id = f"Punkte_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_c[object_id] = (coords[0], coords[1])

    object_coordinates_l = {}
    for i, shape in enumerate(shapes):
        if shape[0] == "line":
            object_id = f"Line_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_l[object_id] = (coords[0], coords[1])

    # Speichere die IDs und Koordinaten in einer Datei
    with open("objects.fll", "w") as file:
        for object_id_1, coords_1 in object_coordinates_c.items():
            x_1, y_1 = coords_1
            file.write(f"{object_id_1}: ({x_1}, {y_1})\n")
        for line_coordinates_1 in line_coordinates_list:
            for object_id_2, coords_2 in object_coordinates_l.items():
                start_x, start_y, end_x, end_y = line_coordinates_1
                file.write(f"{object_id_2}: ({start_x}, {start_y}); ({end_x}, {end_y})\n")

    # Simuliere die Strecken in der Reihenfolge
    while not path_found:
        current_path = []
        for order in path_order:
            line_coordinates = line_coordinates_list[order]
            start_x, start_y, end_x, end_y = line_coordinates
            # Path überprüfung einfügen
            if is_path_possible(start_x, start_y, end_x, end_y):
                current_path.append(line_coordinates)
            else:
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

    if not path_found:
        print("Kein gültiger Pfad gefunden!")


def create_line_network():
    if line_coordinates_list:
        print("Anfangs- und Endkoordinaten der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            print(f"Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")
            label_1.config(text=f"Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")
        print("Berührungspunkte der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            for point in shapes:
                if point[0] == "circle":
                    point_x, point_y = canvas.coords(point[1])[0], canvas.coords(point[1])[1]
                    if point_x >= min(start_x, end_x) and point_x <= max(start_x, end_x) and point_y >= min(start_y, end_y) and point_y <= max(start_y, end_y):
                        print(f"Berührter Punkt: ({point_x}, {point_y})")
                        label_2.config(text=f"Berührungspunkte auf den Linien: ({point_x}), ({point_y})")

    thread = threading.Thread(target=calculate_paths_thread)
    thread.start()


def is_path_possible(start_x, start_y, end_x, end_y):
    # Hier wird die Überprüfung der Strecke implementieren
    for line_coordinates in line_coordinates_list:
        line_start_x, line_start_y, line_end_x, line_end_y = line_coordinates
        if lines_intersect(start_x, start_y, end_x, end_y, line_start_x, line_start_y, line_end_x, line_end_y):
            # wenn die Punkte eine Linie berühren soll abgespeichert werden auf welcher Linie welcher Punkt Liegt
            # das dadurch die Längen besser kalibrieren kann wie z.b. create line network = is path posible
            for line_coordinates in line_coordinates_list:
                start_x, start_y, end_x, end_y = line_coordinates
                for point in shapes:
                    if point[0] == "circle":
                        point_x, point_y = canvas.coords(point[1])[0], canvas.coords(point[1])[1]
                        if point_x >= min(start_x, end_x) and point_x <= max(start_x, end_x) and point_y >= min(start_y, end_y) and point_y <= max(start_y, end_y):
                            print(f"Berührter Punkt: ({point_x}, {point_y})")
                            with open("objects-fll", "a") as WRITE:
                                WRITE.write(f"Beruehrter Punkt: ({point_x}, {point_y}) Linien ID: [ {line_coordinates()}]\n") # hier mus noch die Linien ID abgedpeichert werden!
                            return True
    return False


def calculate_length(start_x, start_y, end_x, end_y):
    # Hier kannst du die Länge der Strecke berechnen
    # Beispiel-Implementierung: Euklidischer Abstand
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
    diagram = Image.new("RGB", (1500, 1200), "white")
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

'''
def print_main():
    print(element_list())
'''

def update_mouse_coordinates(event):
    label.config(text=f"Maus Koordinaten: ({event.x_root - root.winfo_x()}, {event.y_root - root.winfo_y()})")


root = tk.Tk()
root.title("FLL PaRaMeRoS AI")

logo_path = "LOGO.jpeg"
logo = ImageTk.PhotoImage(Image.open(logo_path))
root.iconphoto(True, logo)

canvas = tk.Canvas(root)
canvas.pack()

shapes = []
line_coordinates_list = []

canvas.bind("<Button-1>", create_shapes)
canvas.bind("<Button-2>", create_shapes)
canvas.bind("<Button-3>", create_shapes)
canvas.bind("<B2-Motion>", draw_line)
canvas.bind("<ButtonRelease-2>", finish_line)
canvas.bind("z", delete_last_shape)
root.bind("b", lambda event: create_line_network())

image_path = "FLL_2022_Map.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
canvas.config(width=image.width, height=image.height)
canvas.create_image(0, 0, anchor="nw", image=photo)

label = tk.Label(root, text="Maus Koordinaten: (0, 0)", bd=1, relief=tk.SUNKEN, anchor=tk.W)
label.pack(side=tk.TOP, fill=tk.X)

label_1 = tk.Label(root, text="Anfangs-Koordinate: (0, 0), End-Koordinate: (0, 0)")
label_1.pack()

label_2 = tk.Label(root, text="Berührungspunkte auf den Linien: (0, 0)")
label_2.pack()

canvas.bind("<Motion>", update_mouse_coordinates)

render_button = tk.Button(root, text="Path Finding", command=create_line_network)
render_button.pack()

root.mainloop()
