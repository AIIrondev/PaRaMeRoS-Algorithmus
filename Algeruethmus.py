import tkinter as tk
from PIL import ImageTk, Image
import threading
import random
import datetime
from PIL import ImageDraw
import csv
import logging


#Def Area
def create_shapes(event):
    logger.debug('Create shapes')
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
    logger.debug('finisch line')
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
    logger.debug('last shape deletet')
    if shapes and line_coordinates_list:
        shape_type, shape = shapes.pop()
        line_coordinates_list.pop()
        canvas.delete(shape)
        if shape_type == "circle":
            print("Der letzte Kreis wurde gelöscht!")
        elif shape_type == "line":
            print("Die letzte Linie wurde gelöscht!")


def calculate_paths_thread():
    logger.debug("calculate_path_thread wurde gestartet")
    # Algorithmus für das Path Finding System
    path_order = [i for i in range(len(line_coordinates_list))]
    path_found = False
    max_iterations = 10000  # Maximale Anzahl von Iterationen, um einen gültigen Pfad zu finden

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

    iteration_count = 0
    while not path_found and iteration_count < max_iterations:
        current_path = []
        for order in path_order:
            line_coordinates = line_coordinates_list[order]
            start_x, start_y, end_x, end_y = line_coordinates
            print("Hier wird eine sache gemacht_1")
            print(f"Untersuche Linie {order + 1}: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y})")

            if is_path_possible(start_x, start_y, end_x, end_y):
                current_path.append(line_coordinates)
                print("Hier wird geprueft ob ein Weg possible ist")
            else:
                print(f"Linie {order + 1} kann nicht in den Pfad aufgenommen werden.")
                break

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
                    logger.info(f"Strecke: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y}), Laenge: {length}")
                for object_id, coords in object_coordinates_c.items():
                    x, y = coords
                    file.write(f"{object_id}: ({x}, {y})\n")
                    logger.info(f"{object_id}: ({x}, {y})")
                    element_list = (f"{object_id}: ({x}, {y})")
                for object_id, coords in object_coordinates_l.items():
                    x, y = coords
                    file.write(f"{object_id}: ({x}, {y})\n")
                    logger.info(f"{object_id}: ({x}, {y})")
                file.write(f"Gesamtlaenge: {total_length}")
                logger.info(f"Gesamtlaenge: {total_length}")

            generate_diagram(current_path, path_order)

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
    logger.debug("Daten wurden in Table.csv und in Dijkstra_data.csv abgespeichert")
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
#                writer.writerow(f"({start_x}; {start_y})", f"({end_x}; {end_y})", f"{length:.2f}")

    with open("log.fll", "a") as file:
        file.write("Die Linien Laengen und Punkte Koordinaten wurden in |Dijkstra_data.csv| gespeichert!")


def create_line_network():
    logger.debug('create linenetwork wurde ausgeführt')
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

    print("jetzt werden die threats gestartet")
    logger.warning("Die Threads wurden gestartet")
    thread = threading.Thread(target=calculate_paths_thread)
    thread.start()
    logging.info("Die Threads wurden erfolgreich abgeschlossen")
    print("die Threats sind jetzt abgeschlossen")


def is_path_possible(start_x, start_y, end_x, end_y):
    logger.debug("is_path_possible wurde ausgeführt")
    for line_coordinates in line_coordinates_list:
        line_start_x1, line_start_y1, line_end_x1, line_end_y1 = line_coordinates
        if lines_intersect(start_x, start_y, end_x, end_y, line_start_x1, line_start_y1, line_end_x1, line_end_y1):
            # If die Linien gekreuzen, return True
            pass

    for shape in shapes:
        if shape[0] == "circle":
            circle_center_x, circle_center_y = canvas.coords(shape[1])[0], canvas.coords(shape[1])[1]
            radius = 50  # Set the radius as per your requirement
            distance_start = ((start_x - circle_center_x) ** 2 + (start_y - circle_center_y) ** 2) ** 0.5
            distance_end = ((end_x - circle_center_x) ** 2 + (end_y - circle_center_y) ** 2) ** 0.5

            if distance_start <= radius and distance_end <= radius:
                with open("test_speicher.fll", "a") as WRITE:
                    WRITE.write(f"Line from ({start_x}, {start_y}) to ({end_x}, {end_y}) intersects with circle ({circle_center_x}, {circle_center_y})\n")
                pass
    return True


def calculate_length(start_x, start_y, end_x, end_y):
    logger.debug("Es wurde calculate_length ausgeführt")
    print("jetzt wurde die laenge gespeichert!")
    dx = end_x - start_x
    dy = end_y - start_y
    return ((dx ** 2) + (dy ** 2)) ** 0.5


def lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    logger.debug("Es wurde lines_intersect ausgeführt")
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    denominator = dx1 * dy2 - dx2 * dy1
    if denominator == 0:
        return False  # Linien sind parallel oder identisch

    t1 = ((x1 - x3) * dy2 - (y1 - y3) * dx2) / denominator
    t2 = ((x1 - x3) * dy1 - (y1 - y3) * dx1) / denominator

    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        print("hier wird geprueft ob die linien sich durch queren")
        return True  # Linien schneiden sich
    else:
        return False  # Linien schneiden sich nicht


def next_permutation(arr):
    logger.debug("next_permutation wurde berechnet")
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
    # hier müssen noch folgende Diagramme erstellt werden: Zeit pro Aufgabe, länge pro Aufgaben, Dijkstra Alg., A_star Alg.
    logger.info("Die Diagramme wurden gespeichert und zum senden Freigegeben")
    diagram = Image.new("RGB", (705, 420), "white")
    draw = ImageDraw.Draw(diagram)

    for i, shape in enumerate(shapes):
        if shape[0] == "circle":
            object_id = f"Object{i + 1}"
            coords = canvas.coords(shape[1])
            x, y = coords[0], coords[1]
            draw.text((x, y), object_id, fill="black")

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

    for leaf_node in leaf_nodes:
        order, (x, y) = leaf_node
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.ellipse([(x - node_radius, y - node_radius), (x + node_radius, y + node_radius)], fill=color)

    for i in range(len(leaf_nodes) - 1):
        order1, (x1, y1) = leaf_nodes[i]
        order2, (x2, y2) = leaf_nodes[i + 1]
        draw.line([(x1, y1 + node_radius), (x2, y2 - node_radius)], fill="black", width=2)

    diagram.save("diagram.png")
    print("Diagramm erzeugt und als 'diagram.png' gespeichert.")


def create_button(shape_type, index):
    logger.debug("Es wurden Buttons erzeugt")


    def combined_action():
        linien_creator(index)
        button_pressed(index)

    if shape_type == "circle":
        button_text = f"Kreis {index + 1}"
        return tk.Button(root, text=button_text, command=combined_action)
    elif shape_type == "line":
        button_text = f"Linie {index + 1}"
        return tk.Button(root, text=button_text, command=combined_action)


def create_buttons_for_shapes():
    logger.debug("Es wurde create_buttons_for_shapes ausgeführt")
    global button_list
    button_list = []
    button_frame = tk.Frame(root)
    canvas.create_window(0, 0, anchor="nw", window=button_frame)
    
    for i, shape in enumerate(shapes):
        shape_type, _ = shape
        button = create_button(shape_type, i)
        button.pack(fill=tk.BOTH, padx=5, pady=5) 
        button_list.append(button)

    canvas.pack(fill=tk.BOTH, expand=True)
    
    canvas.create_window(0, 0, anchor="nw", window=button_frame)
    create_button_for_shape_var = True

def display_function_explanations():
    logger.debug("Es wurde der Fragezeichen Button ausgeführt")
    explanation_text = """
    Hier sind die Erklärungen für die verschiedenen Funktionen des Algeruethmus Programms:

    - Linksklick / Rechtsklick: Fügt einen roten Punkt (Kreis) an der Mausposition hinzu.
    - Mittelklick: Markiert den Startpunkt einer Linie.
    - Ziehen bei Mittelklick: Zeichnet eine temporäre grüne Linie.
    - Loslassen nach Mittelklick: Zeichnet eine grüne Linie und speichert sie.
    - Taste 'z': Löscht die zuletzt gezeichnete Form (Kreis oder Linie).

    Dieses Programm sollte Ausschließlich von Personen verwendet werden, die im FLL Team PaRaMeRoS sind.
    Die Schaltfläche 'Path Finding' führt den Algorithmus aus, um gültige Pfade zu berechnen.
    Die Schaltfläche 'Auflistung der Linien' zeigt Schaltflächen für jede Linie und jeden Kreis an.
    Die Schaltfläche 'Neue Verbindung kreieren' erstellt eine Verbindung zwischen zwei Punkten.
    Die Schaltfläche 'quit_VK' beendet die Funktion verbindung_kreiren(vk).
    """
    current_text = explanation_label.cget("text")
    if current_text == explanation_text:
        explanation_label.config(text="")
    else:
        explanation_label.config(text=explanation_text)

def linien_creator(shape_index):
    global selected_point_id, selected_line_id

    shape = shapes[shape_index]
    shape_type, coords = shape

    if shape_type == "line":
        start_x, start_y, end_x, end_y = canvas.coords(coords)
        length = calculate_length(start_x, start_y, end_x, end_y)
        selected_line_id = shape_index  # Hier speicherst du die ID der ausgewählten Linie
        label_4.config(text=f"Linien Verbindung {shape_index + 1}: Anfangs-Koordinate: ({start_x}, {start_y}), End-Koordinate: ({end_x}, {end_y}), Laenge: {length}")

    elif shape_type == "circle":
        selected_point_id = shape_index  # Hier speichert die ID des ausgewählten Punkts
        print(f"Ausgewählter Punkt: {shape_index + 1}")
    else:
        logger.error("Es wurde kein Shape gefunden")


def verbindung_kreieren():
    set_running = True
    global selected_objects

    if mode == "point":
        # Füge den ausgewählten Punkt zur Liste hinzu (hier musst du die ID des ausgewählten Punkts speichern)
        selected_objects.append(selected_point_id)
        print(f"Ausgewählter Punkt: {selected_point_id}")

    elif mode == "line":
        # Füge die ausgewählte Linie zur Liste hinzu (hier musst du die ID der ausgewählten Linie speichern)
        selected_objects.append(selected_line_id)
        print(f"Ausgewählte Linie: {selected_line_id}")

    while set_running:
        if button_quit_vk == "quit":
            set_running = False
        elif button_pressed_vk == "":
            lines_adding = True
            while lines_adding:
                if button_quit_vk == "quit":
                    lines_adding = False
                    set_running = False
                if button_pressed_vk == "":
                    pass
#                   get laength and add to total_laength
#                   get ID save to first button create new List in list(all way points)
                elif button_pressed_vk == "":
                    pass
#                   print( total_laength)
#                   with open(".csv", a) as file:
#                       file.write(ID from first button, ID vom End button,total_laenght)
#                   Lines_adding = False
#                   break
    pass


def calculate_length_of_line(circle_id):
    logger.debug("Hier wurde die länge der Linien ausgerechnet")
    total_length = 0
    for i in range(circle_id):
        start_x, start_y, end_x, end_y = line_coordinates_list[i]
        length = calculate_length(start_x, start_y, end_x, end_y)
        total_length += length
    return total_length


def switch_mode(new_mode):
    logger.debug("switch_mode wurde ausgeführt")
    global mode
    mode = new_mode

def set_quit_vk():
    logger.debug("quit vk")
    button_quit_vk = True

def button_pressed(id):
    logger.debug("button_pressed wurde ausgeführt")
    button_pressed_vk = id

def update_mouse_coordinates(event):
    label.config(text=f"Maus Koordinaten: ({event.x_root - root.winfo_x()}, {event.y_root - root.winfo_y()})")

# var def area
root = tk.Tk()
root.title("FLL PaRaMeRoS Algeruethmus")

logo_path = "LOGO.jpeg"
logo = ImageTk.PhotoImage(Image.open(logo_path))
root.iconphoto(True, logo)

root.geometry("701x650") # Größe des Fensters Festlegen

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

create_button_for_shape_var = False
shapes = []
line_coordinates_list = []

object_coordinates_c = {}
object_coordinates_l = {}
selected_point_id = None
selected_line_id = None
selected_objects = []
mode = "point"
button_quit_vk = False
button_pressed_vk = False

image_path = "FLL_2023-24_Map.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=photo)

logger = logging.getLogger('Algeruethmus.py')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('sys.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

canvas.bind("<Button-1>", create_shapes, logger.debug('Button1'))
canvas.bind("<Button-2>", create_shapes, logger.debug('Button2'))
canvas.bind("<Button-3>", create_shapes, logger.debug('Button3'))
canvas.bind("<B2-Motion>", draw_line, logger.debug('B2Motion'))
canvas.bind("<ButtonRelease-2>", finish_line, logger.debug('ButtonRelease2'))
root.bind("z", delete_last_shape, logger.debug('Button z'))
render_button_3 = tk.Button(root, text="?", command=display_function_explanations)
explanation_label = tk.Label(root, text="", justify=tk.LEFT)
label = tk.Label(root, text="Maus Koordinaten: (0, 0)", bd=1, relief=tk.SUNKEN, anchor=tk.W)
label_1 = tk.Label(root, text="Anfangs-Koordinate: (0, 0), End-Koordinate: (0, 0)")
label_2 = tk.Label(root, text="Beruehrungspunkte auf den Linien: (0, 0)")
render_button = tk.Button(root, text="Path Finding", command=create_line_network)
label_3 = tk.Label(root, text="Liste der Linien")
label_4 = tk.Label(root, text="Linien Verbindung 1: (0,0) Leange: (0)")
render_button_1 = tk.Button(root, text="Auflistung der Linien", command=create_buttons_for_shapes)
render_button_2 = tk.Button(root, text="Neue Verbindung kreieren", command=verbindung_kreieren)
point_button = tk.Button(root, text="Punkt auswählen", command=lambda: switch_mode("point"))
line_button = tk.Button(root, text="Linie hinzufügen", command=lambda: switch_mode("line"))
render_button_4 = tk.Button(root, text="quit_VK", command=set_quit_vk)
# run area
render_button_3.pack()
explanation_label.pack()
label.pack(side=tk.TOP, fill=tk.X)
label_1.pack()
label_2.pack()
canvas.bind("<Motion>", update_mouse_coordinates)
render_button.pack()
label_3.pack()
label_4.pack()
render_button_1.pack()
render_button_2.pack()
render_button_4.pack()
#point_button.pack()
#line_button.pack()
root.mainloop()
