'''
Ablauf:
def Verbindung_kreieren():
    1. Schritt: if create_button_for_shape wurde gepressed:
    2. Schritt: wenn 1.Schritt == True dann Displayen das wir Punkt über Linien zu punkt verbindungen erstellen kann ausßerdem wird ein Button erstzellt der gedrückt wird wenn eine Strecke erstellt wurde
    3. Schritt: auflisten wenn ein Button gedrückt der Valid ist (Punkt, Linien, Punkt)
    4. Schritt: wenn Verbindung erstellt wurde dann wird die Verbindung in eine Liste gespeichert
    5. Schritt: wenn der Button für die komplette Abschließung gedrückt wird dann wird die Liste in eine Datei gespeichert
'''

'''
Code:
def verbindung_kreieren():
    if create_button_for_shape_var == True:
        explanation_text_for_shape = "Verbinden Sie die Punkte mit Linien"

        current_text_for_shapes = explanation_label.cget("text")
        if current_text_for_shapes == explanation_text_for_shape:
            explanation_label.config(text="")
        else :
            explanation_label.config(text=explanation_text_for_shape)
            for i, shape in enumerate(shapes):
                if shape == "Punkt":
                    print("Punkt, valid")
                elif shape == "Linie":
                    print("Linie, unvalid")
'''

'''def verbindung_kreieren():
    if create_button_for_shape_var:
        explanation_text_for_shape = "Verbinden Sie die Punkte mit Linien"

        current_text_for_shapes = explanation_label.cget("text")
        if current_text_for_shapes == explanation_text_for_shape:
            explanation_label.config(text="")
        else:
            explanation_label.config(text=explanation_text_for_shape)
            
            # Schritt 4: Verbindung erstellen und speichern
            line_connections = []
            for i, shape in enumerate(shapes):
                shape_type, _ = shape
                if shape_type == "circle":
                    button_text = f"Kreis {i + 1}"
                    button = create_button(shape_type, i, button_text)
                    button_frame.columnconfigure(i, weight=1)
                    button.pack(fill=tk.BOTH, padx=5, pady=5)
                    button.config(command=lambda i=i: save_connection(i))
            
            def save_connection(circle_id):
                line_id = int(render_fild.get())
                line_connections.append((circle_id + 1, line_id))
                print(f"Verbindung zwischen Kreis {circle_id + 1} und Linie {line_id}")
            
            # Schritt 5: Liste in Datei speichern
            if line_connections:
                with open("verbindungen.txt", "w") as file:
                    for circle_id, line_id in line_connections:
                        file.write(f"Kreis {circle_id} ist verbunden mit Linie {line_id}\n")
                print("Verbindungen wurden in 'verbindungen.txt' gespeichert")
            else:
                print("Keine Verbindungen zum Speichern vorhanden")

'''

'''
def verbindung_kreieren():
    button_frame = tk.Frame(root)
    if create_button_for_shape_var:
        explanation_text_for_shape = "Verbinden Sie die Punkte mit Linien"

        current_text_for_shapes = explanation_label.cget("text")
        if current_text_for_shapes == explanation_text_for_shape:
            explanation_label.config(text="")
        else:
            explanation_label.config(text=explanation_text_for_shape)

            # Verbindung erstellen und speichern
            line_connections = []
            line_length = None
            for i, shape in enumerate(shapes):
                shape_type, _ = shape
                if shape_type == "circle":
                    button_text = f"Kreis {i + 1}"
                    button = create_button(shape_type, i, button_text)
                    button_frame.columnconfigure(i, weight=1)
                    button.pack(fill=tk.BOTH, padx=5, pady=5)
                    button.config(command=lambda i=i: save_connection(i))
                    line_length = calculate_length_of_line(i)

            def save_connection(circle_id):
                line_id = int(render_fild.get())
                line_connections.append((circle_id + 1, line_id, line_length))
                print(f"Verbindung zwischen Kreis {circle_id + 1} und Linie {line_id} mit Länge {line_length}")

            # Liste in CSV-Datei speichern (Quelle, Ziel, Gewicht)/ (source, target, weight)
            if line_connections:
                with open("verbindungen.csv", "w", newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(["source", "target", "weight"])
                    for circle_id, line_id, line_length in line_connections:
                        csv_writer.writerow([circle_id, line_id, line_length])
                print("Verbindungen wurden in 'Dijkstra_data.csv' gespeichert")
            else:
                print("Keine Verbindungen zum Speichern vorhanden")
'''

'''
Problem da Schleife in Schleife ist wird die Schleife immer wieder ausgeführt
def verbindung_kreieren():
    total_laength = 0
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
        elif button_pressed_vk == "circle":
            button_id = button_pressed
            vk_list.append(button_id)
            lines_adding = True
            while lines_adding:
                if button_quit_vk == "quit":
                    lines_adding = False
                    set_running = False
                if button_pressed_vk == "line":
                    pass
#                   get laength and add to total_laength
#                   get ID save to first button create new List in list(all way points)
                elif button_pressed_vk == "circle":
                    pass
#                   print( total_laength)
#                   with open(".csv", a) as file:
#                       file.write(ID from first button, ID vom End button,total_laenght)
#                   Lines_adding = False
#                   break
    pass
'''

'''
# Erstelle einen Ordner für die CSV-Dateien
csv_folder = 'csv_files'
log_folder = 'log_files'
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
'''

'''
# Funktion zum Speichern der Koordinaten in einer CSV-Datei
def save_coordinates_to_csv(coordinates, filename):
    with open(os.path.join(csv_folder, filename), mode='w', newline='') as csv_file:
        fieldnames = ['Graph', 'Vertex', 'X Coordinate', 'Y Coordinate']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for graph_id, graph_coordinates in enumerate(coordinates):
            for vertex, x, y in graph_coordinates:
                writer.writerow({
                    'Graph': graph_id,
                    'Vertex': vertex,
                    'X Coordinate': x,
                    'Y Coordinate': y
                })
'''
'''
import easyocr

# Ein OCR-Modell initialisieren
reader = easyocr.Reader(['en'])

# Das Bild öffnen
image = "FLL_2022_Map.png"

# Text aus dem Bild extrahieren
result = reader.readtext(image)

# Den extrahierten Text ausgeben
for detection in result:
    print(detection[1])
'''


# in eine Funktion eiunbauen und dann in die anderen Files Deployen Für Arch Linux
import os
from PIL import Image

# Den aktuellen Pfad abrufen
current_directory = os.getcwd()

# Die Verzeichnisse in ihre einzelnen Teile aufteilen
directories = current_directory.split(os.path.sep)

# Den Inhalt des aktuellen Verzeichnisses anzeigen
print(f"Inhalt des aktuellen Verzeichnisses ({directories[-2]}/{directories[-1]}):")
for filename in os.listdir(current_directory):
    if os.path.isfile(filename):
        print(f"- {filename}")

# Den Bildpfad vom Benutzer abfragen
bildpfad = input("Gib den Bildnamen ein (einschließlich der Dateierweiterung): ")

# Das Bild öffnen
image = Image.open(bildpfad)

# Die ASCII-Zeichen, die für verschiedene Helligkeitswerte verwendet werden sollen
ASCII_CHARS = "@%#*+=-:. "

# Die maximale Breite und Höhe für das ASCII-Bild festlegen
MAX_WIDTH = 255
MAX_HEIGHT = 255

# Die Breite und Höhe des Bildes abrufen und auf die maximale Größe begrenzen
width, height = image.size
if width > MAX_WIDTH:
    new_width = MAX_WIDTH
    ratio = width / MAX_WIDTH
    new_height = int(height / ratio)
else:
    new_width = width
    new_height = height

# Das Bild auf die neue Größe verkleinern
image = image.resize((new_width, new_height))

# Eine Funktion zum Konvertieren eines Pixels in ein ASCII-Zeichen
def pixel_to_ascii(pixel_value):
    # Da ASCII-Zeichen von dunkel nach hell sortiert sind,
    # teilen wir den Pixelwert durch die Anzahl der ASCII-Zeichen und runden auf
    ascii_index = int((pixel_value / 255) * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[ascii_index]

# Eine Schleife durch die Pixel des Bildes, um ASCII-Zeichen zu generieren
ascii_image = ""
for y in range(new_height):
    for x in range(new_width):
        pixel_color = image.getpixel((x, y))
        gray_value = int(0.299 * pixel_color[0] + 0.587 * pixel_color[1] + 0.114 * pixel_color[2])
        ascii_image += pixel_to_ascii(gray_value)
    ascii_image += "\n"  # Eine Zeilenumbruch am Ende jeder Zeile hinzufügen

# Das ASCII-Bild ausgeben oder speichern
print(ascii_image)

# Den Dateinamen für die Ausgabedatei festlegen
ausgabedatei = input("Speichere als (Dateiname ohne Erweiterung): ") + ".txt"

# Das ASCII-Bild in eine Textdatei speichern
with open(ausgabedatei, "w") as file:
    file.write(ascii_image)

print(f"Das ASCII-Bild wurde als {ausgabedatei} gespeichert.")
