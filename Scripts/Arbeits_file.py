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