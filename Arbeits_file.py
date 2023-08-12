'''
Ablauf:
def Verbindung_creiren():
    1. Schritt: if create_button_for_shape wurde gepressed:
    2. Schritt: wenn 1.Schritt == True dann Displayen das wir Punkt über Linien zu punkt verbindungen erstellen kann ausßerdem wird ein Button erstzellt der gedrückt wird wenn eine Strecke erstellt wurde
    3. Schritt: auflisten wenn ein Button gedrückt der Valid ist (Punkt, Linien, Punkt)
    4. Schritt: wenn Verbindung erstellt wurde dann wird die Verbindung in eine Liste gespeichert
    5. Schritt: wenn der Button für die komplette Abschließung gedrückt wird dann wird die Liste in eine Datei gespeichert
'''

'''
Code:
def verbindung_creiren():
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