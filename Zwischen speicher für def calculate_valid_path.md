def calculate_paths_thread():
    # Algorithmus für das Path Finding System
    path_order = [i for i in range(len(line_coordinates_list))]  # Erstellt eine Reihenfolge für die Strecken
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
            # Überprüfe, ob die Strecke möglich ist (hier kann dein eigener Überprüfungsalgorithmus verwendet werden)
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