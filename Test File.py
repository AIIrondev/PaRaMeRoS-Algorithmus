import tkinter as tk
from PIL import ImageTk, Image
import threading
import random
import datetime
from PIL import ImageDraw


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
    if len(shapes) >= 1 and len(line_coordinates_list) >= 1:
        shape_type, shape = shapes.pop()
        line_coordinates_list.pop()
        canvas.delete(shape)
    if shapes:
        shape_type, shape = shapes.pop(0)
        if shape_type == "circle":
            canvas.delete(shape)
            print("Der letzte Kreis wurde gelöscht!")
        elif shape_type == "line":
            canvas.delete(shape)
            line_coordinates_list.pop(0)
            print("Die letzte Linie wurde gelöscht!")


def calculate_paths_thread():
    # Algorithmus für das Path Finding System
    path_order = [i for i in range(len(line_coordinates_list))]
    path_found = False
    max_iterations = 10000  # Maximale Anzahl von Iterationen, um einen gültigen Pfad zu finden

    # Generiere eine eindeutige ID für jedes Objekt
    object_coordinates_c = {}
    object_coordinates_l = {}
    for i, shape in enumerate(shapes):
        if shape[0] == "circle":
            object_id = f"Punkte_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_c[object_id] = (coords[0], coords[1])
            print("Es wurde eine ID zugewiesen an einen Kreis zugewiesen")

    for i, shape in enumerate(shapes):
        if shape[0] == "line":
            object_id = f"Line_ID{i + 1}"
            coords = canvas.coords(shape[1])
            object_coordinates_l[object_id] = (coords[0], coords[1])
            print("Es wurde eine ID zugewiesen an eine Linie zugewiesen")

    # Simuliere die Strecken in der Reihenfolge
    iteration_count = 0
    while not path_found and iteration_count < max_iterations:
        current_path = []
        for order in path_order:
            line_coordinates = line_coordinates_list[order]
            start_x, start_y, end_x, end_y = line_coordinates
            print("Hier wird eine Sache gemacht_1")

            # Führe eine Debugging-Anweisung aus, um zu überprüfen, welche Linien untersucht werden
            print(f"Untersuche Linie {order + 1}: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")

            # Path-Überprüfung einfügen und Debugging-Anweisungen
            if is_path_possible(start_x, start_y, end_x, end_y):
                current_path.append(line_coordinates)
                print("Hier wird geprüft ob ein Weg möglich ist")
            else:
                print(f"Linie {order + 1} kann nicht in den Pfad aufgenommen werden.")
                break

        # Wenn alle Strecken möglich sind, wurde ein gültiger Pfad gefunden
        if len(current_path) == len(path_order):
            path_found = True
            print("Gültiger Pfad gefunden:")
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
                for object_id, coords in object_coordinates_l.items():
                    x, y = coords
                    file.write(f"{object_id}: ({x}, {y})\n")
                file.write(f"Gesamtlaenge: {total_length}")

            generate_diagram(current_path, path_order)

        iteration_count += 1

    if not path_found:
        print("Kein gültiger Pfad gefunden!")


def is_path_possible(start_x, start_y, end_x, end_y):
    # Hier kannst du die Überprüfung implementieren, ob ein Pfad möglich ist
    # Für diese Implementierung werden die Linien einfach überprüft, ob sie sich kreuzen
    # Du könntest hier einen anderen Algorithmus verwenden, um die Überprüfung zu verbessern.
    for line_coordinates in line_coordinates_list:
        line_start_x1, line_start_y1, line_end_x1, line_end_y1 = line_coordinates
        if lines_intersect(start_x, start_y, end_x, end_y, line_start_x1, line_start_y1, line_end_x1, line_end_y1):
            return False  # Linien schneiden sich
    return True


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


def create_line_network():
    if line_coordinates_list:
        print("Anfangs- und Endkoordinaten der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            print(f"Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")
        print("Berührungspunkte der Linien:")
        for line_coordinates in line_coordinates_list:
            start_x, start_y, end_x, end_y = line_coordinates
            for point in shapes:
                if point[0] == "circle":
                    point_x, point_y = canvas.coords(point[1])[0], canvas.coords(point[1])[1]
                    if point_x >= min(start_x, end_x) and point_x <= max(start_x, end_x) and point_y >= min(start_y, end_y) and point_y <= max(start_y, end_y):
                        print(f"Berührter Punkt: ({point_x}, {point_y})")

    # Führe den Algorithmus in einem separaten Thread aus
    print("Jetzt wird der Thread gestartet")
    thread = threading.Thread(target=calculate_paths_thread)
    thread.start()
    print("Der Thread ist jetzt gestartet")


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

image_path = "FLL_2023-24_Map.png"
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
