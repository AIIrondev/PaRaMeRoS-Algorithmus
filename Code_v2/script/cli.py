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
import os
import datetime
import shutil
import click as cli

# var definition
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "..", "Bilder", "LOGO.ico")

# class main -> main funkltion GUI class
class main:
    def __init__(self):
        @cli.command()
        @cli.argument("--load", "-l", default="my_programm.fll", help="This will load a simulation that you have created before")
        @cli.argument("--create", "-c", default="10", help="This will create a new simulation")
        @cli.argument("--save", "-s", default="my_programm.fll", help="This will save your simulation")
        @cli.argument("--info", "-i", help="This will show you some information about the programm like version, config etc.")
        @cli.argument("--render", "-r", help="This will render your simulation")


class logik:
    def __init__(self):
        pass

    def save_simulation(self, file_path, file_name, count, Distance_list, ERDATE, AUTOR):
        POINTS = count  # POINTS -> Anzahl der Punkte
        ERDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        BEDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        EDIT = 1 # EDIT -> wie oft bearbeitet
        self.save_path = file_path + file_name + "/simulation.txt"
        with open(file_path, "w") as file:
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
    
    def render(self, distance_list):
        # 1. Schritt: Alle Punkte in einer Liste speichern und in ein File speichern
        # 2. Schritt: Dijkstra Algorithmus starten -> danach A* Algorithmus starten
        # 3. Schritt: Finisched PAth displayen und in ein File speichern
        ## 1.Schritt
        points = get_combinations(self.combobox)
        list_combinations = points.append(distance_list)
        with open("points.txt", "w") as file:
            file.truncate(0)
            for point1, point2, distance in distance_list:
                file.append(str(point1) + ", " + str(point2) + ", " + str(distance) + "\n")
        ## 2.Schritt
        os.system("python3 " + os.path.join(base_dir, "..", "script", "dijkstra.py"))
        ## 3.Schritt
        waiting = True
        while waiting:
            if os.path.exists(os.path.join(base_dir, "..", "export_folder", "shortest_path_a_star.png")):
                waiting = False
                with open("shortest_path.txt", "r") as file:
                    result = file.read()
                gui.display_rendert_path()
                shutil.move(os.path.join(base_dir, "..", "export_folder", "shortest_path_a_star.png"), os.path.join(base_dir, "..", "export_folder", "shortest_path.png"))
            else:
                pass
                
            
                    
                    
class config:
    def __init__(self):
        pass

    def save_config(self, file):
        self.config_path = os.path.join(base_dir, "..", "config", file)
    
    
    def load_config(self):
        pass

# main running area -> main function
if __name__ == "__main__":
    window = main()
    window.window.mainloop()