'''
MIT LICENSE

© 2023 Maximilian Gründinger

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including, but not limited to, the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

NOTICE: IF you are not a member of the FIRST LEGO LEAGUE TEAM PaRaMeRoS or intend to use it for FIRST LEGO LEAGUE you are not allowed to use, copy, resell or take parts of the Software/Code!!!
There is an exception if I (Maximilian Gründinger) give you a written permission to do so. If you want to use the Software/Code for FIRST LEGO LEAGUE, please contact me via email (maximiliangruendinger@gmail.com).

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

DISCLAIMER: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This license is valid only for the year 2023. After 2023, the aforementioned terms and conditions will be considered invalid. 
Users are not authorized to copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
excluding older or custom versions from third parties.

For older versions, the above legal terms and conditions will remain valid from the year 2023 onwards.
'''

# import modules
import customtkinter as tk
import os
import tkinter as tk2
from tkinter import ttk
import datetime
import shutil

# var definition
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "..", "Bilder", "LOGO.ico")
dir0 = "/home/web/website/PaRaMeRoS-Python/directory.fll"
in0 = "/home/web/website/PaRaMeRoS-Python/output.fll"
out0 = "/home/web/website/PaRaMeRoS-Python/input.fll" 
start0 = "/home/web/website/PaRaMeRoS-Python/start.fll"
user0 = "/home/web/website/PaRaMeRoS-Python/user.fll"
version = "2.2.1"

# class main -> main funkltion GUI class
class main:
    def __init__(self):
        # alle Dateien werden gelesen und aufbereitet für die Verarbeitung durch die Funktion command
        with open(user0, "r") as file:
            User = file.read().strip()

        with open(dir0, "r") as file:
            dir1 = file.read().strip()

        if not any(element in dir1 for element in DIR_LIST):
            with open(out0, "w") as f:
                input1 = f.read().strip()

        with open(in0, "r") as file:
            input234 = file.read().strip()
            input1 = input234
            user_input = None
        
        try: 
            input234 = input234.split(", ")
            user_input = input234[1]
            imput1 = input234[0]
            input1 = input1.replace(", ", "")

        except IndexError:
            imput1 = input234
            user_input = None
        
        if not any(element in input1 for element in ALL_LIST):
            null = None 

        index = None

        for j, element in enumerate(DIR_LIST):
            if element == dir1:
                index = j

        index1 = None

        for i, element in enumerate(ALL_LIST):
            if element == input1:
                index1 = i
            
        together = (index, index1)
        print(together)

        self.main_menu(together, out0, index, User, user_input)
        
    def main_menu(self, combination, file, index, User, variable_input=None):
        file_writer(dir0, "main_menu")
        # main menu -> main menu : commands -> 
        running_main_menu = True
        while running_main_menu:
            match user_input:
                case "exit":
                    running_main_menu = False
                    file_writer(file, "exit")
                    exit(Code=0)
                case "help":
                    help()
                case "load":
                    file_writer(file, "load")
                    self.main_load()
                case "create":
                    file_writer(file, "create")
                    self.main_programm()
                case "info":
                    self.info()
    
    def main_programm(self):
        pass
    
    def main_load(self):
        pass
            
    def render(self, distance_render, count):
        pass

    def help(self, mode):
        match mode:
            case "main":
                file_writer(out0, "load -> load a project\ncreate -> create a new project\nexit -> exit the programm\nhelp -> show this help\ninfo -> show info about the programm")
            case "load":
                file_writer(out0, "set_name -> sets the Directory that will be loadet\nback -> goes back to the main Menu\nload -> loads the file ?is work in progress?\nhelp -> show this help")
            case "create":
                file_writer(out0, "set_name -> sets the name of the project\nset_count -> sets the count of the points\nset_distance -> sets the distance between the points\nback -> goes back to the main Menu\ncreate -> creates the project\nhelp -> show this help")
            case "save_gui":
                file_writer(out0, "set_author -> sets the Author for the saving\nset_name -> sets name for the projekt\nsave -> saves the project\nback -> goes back to the main programm\nhelp -> show this help")
            case "render":
                file_writer(out0, "set_name -> sets the name of the project\nset_count -> sets the count of the points\nset_distance -> sets the distance between the points\nback -> goes back to the main Menu\ncreate -> creates the project\nhelp -> show this help")
            case None:
                file_writer(out0, "Error")

    def save_gui(self, distance_list, count):
        pass

    def info(self):
        file_writer(file, f"Version: {version}\n Author: Maximilian Gründinger\n Date: 2021-08-15\n License: Custom MIT\n")


class file_writer:
    def __init__(self, file, text):
        self.file = file
        self.text = text
        text.replace("\n", "<br>")
        text.replace(" ", "&nbsp;")
        with open(file, "w") as f:
            f.write(text)
        with open(start0, "w") as f:
            f.write("Done!")
    

 
class logik:
    def __init__(self):
        pass

    def save_simulation(self, file_path, file_name, count, Distance_list):
        POINTS = count  # POINTS -> Anzahl der Punkte
        ERDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        BEDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        EDIT = 1 # EDIT -> wie oft bearbeitet
        self.save_path = os.path.join(file_path, f"/{file_name}.txt") # Projekt files -> weiter machen
        with open(self.save_path, "w") as file:
            file.write(str(POINTS) + "\n")
            file.write(str(ERDATE) + "\n")
            file.write(str(BEDATE) + "\n")
            file.write(str(Distance_list) + "\n")
            file.write(str(AUTOR) + "\n")
            file.write(str(EDIT) + "\n")
        
    
    def load_simulation(self):
        pass

    def get_combinations(self, count):
        combinations = []
        for i in range(count):
            for j in range(count):
                if i != j:
                    com = [i, j]
                    if com not in combinations and com[::-1] not in combinations:
                        combinations.append(com)
        return combinations
    
    def render(self, distance_render_logik, count):
        # 1. Schritt: Alle Punkte in einer Liste speichern und in ein File speichern
        # 2. Schritt: Dijkstra Algorithmus starten -> danach A* Algorithmus starten
        # 3. Schritt: Finisched PAth displayen und in ein File speichern
        ## 1.Schritt
        points = self.get_combinations(count)
        list_combinations = points.append(distance_render_logik)
        with open(os.path.join(base_dir, "..", "config","count.fll"), "w") as file:
            file.write(str(count))
        with open("points.csv", "w") as file:
            file.truncate(0)
            for point1, point2, distance in distance_list:
                file.append(str(point1) + ", " + str(point2) + ", " + str(distance) + "\n")
        ## 2.Schritt
        os.system("python3 " + os.path.join(base_dir, "..", "script", "Dijkstra.py"))
        ## 3.Schritt
        waiting = True
        while waiting:
            if os.path.exists(os.path.join(base_dir, "..", "export_folder", "shortest_path_a_star.png")):
                waiting = False
                with open(os.path.join(base_dir, "..", "config", "shortest_path.fll"), "r") as file:
                    result = file.read()
                gui.display_rendert_path()
                shutil.move(os.path.join(base_dir, "..", "export_folder", "shortest_path_a_star.png"), os.path.join(base_dir, "..", "export_folder", "shortest_path.png"))
            else:
                pass
                

# main running area -> main function
if __name__ == "__main__":
    main()