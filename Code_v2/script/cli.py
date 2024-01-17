'''
Path finding algorithm License Agreement

This License Agreement (the "Agreement") is entered into by and between Maximilian Gründinger ("Licensor") and the First Lego League Team known as PaRaMeRoS ("Licensee").

1. License Grant.
Licensor hereby grants Licensee a non-exclusive, non-transferable license to use and modify the software program known as [Your Program Name] (the "Program") solely for educational and non-commercial purposes. This license is granted exclusively to the members of the First Lego League Team identified as [First Lego League Team Name].

2. Restrictions.
Licensee shall not, and shall not permit others to:
a. Use the Program for any purpose other than educational and non-commercial activities within the First Lego League Team.
b. Allow non-members of the First Lego League Team to use or access the Program.
c. Commercialize or distribute the Program for financial gain.
d. Remove or alter any copyright, trademark, or other proprietary notices contained in the Program.

3. Security.
Licensor makes no warranties regarding the security of the Program. Licensee acknowledges and agrees that any use of the Program is at their own risk. Licensor shall not be responsible for any security bugs or issues that may arise in connection with the Program.

4. Term and Termination.
This Agreement shall remain in effect until terminated by either party. Licensor reserves the right to terminate this Agreement immediately if Licensee breaches any of its terms. Upon termination, Licensee shall cease all use of the Program and destroy all copies in their possession.

5. Disclaimer of Warranty.
THE PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. LICENSOR DISCLAIMS ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

6. Limitation of Liability.
IN NO EVENT SHALL LICENSOR BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM, EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

7. Governing Law.
This Agreement shall be governed by and construed in accordance with the laws of [Your Jurisdiction].

8. Entire Agreement.
This Agreement constitutes the entire agreement between the parties and supersedes all prior agreements, whether oral or written, with respect to the Program.

IN WITNESS WHEREOF, the parties hereto have executed this License Agreement as of the effective date.

Licensor:
Maximilian Gründinger

Licensee:
PaRaMeRoS

Date: 1.1.2024
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
run0 = "/home/web/website/PaRaMeRoS-Python/run.fll"
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
        
    def main_menu(self, combination, file, index, User, variable_input=None, mode=None):
        file_writer(dir0, "main_menu")
        # main menu -> main menu : commands -> 
        running_main_menu = True
        match mode:
            case None:
                match user_input:
                    case "exit":
                        running_main_menu = False
                        file_writer(file, "exit")
                        exit(Code=0)
                    case "help":
                        help("main")
                    case "load":
                        file_writer(file, "load")
                        self.main_load()
                    case "create":
                        file_writer(file, "create")
                        self.main_programm()
                    case "info":
                        self.info()
            case "main_menu":
                match user_input:
                    case "exit":
                        running_main_menu = False
                        file_writer(file, "exit")
                        exit(Code=0)
                    case "help":
                        help("main")
                    case "load":
                        file_writer(file, "load")
                        self.main_load()
                    case "create":
                        file_writer(file, "create")
                        self.main_programm()
                    case "info":
                        self.info()
            case "main_programm":
                self.main_programm()
            case "main_load":
                self.main_load()
                
    
    def main_programm(self):
        file_writer(dir0, "main_programm")
        match user_input:
            case int:
                # Hier muss noch die logik eingebaut werden da die distnacen hier so 1,2,34 aufgebaut
                pass
            case "back":
                file_writer(out0, "back")
                self.main_menu()
            case "help":
                help("create")
                    
    def main_load(self):
        file_writer(dir0, "main_load")
        pass
            
    def render(self, distance_render, count):
        file_writer(dir0, "main_render")
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
        file_writer(dir0, "main_save_gui")
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