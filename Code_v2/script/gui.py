'''
MIT LICENSE

© 2023 Maximilian Gründinger

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including, but not limited to, the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

NOTICE: You are not a member of another FIRST LEGO LEAGUE TEAM or intend to use it for First Lego League in Germany, Austria, Swiss!

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

# class main -> main funkltion GUI class
class main:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Algorithmus")
        self.window.geometry("600x420")
        self.window.resizable(True, True)
        self.window._set_appearance_mode("light")
        self.window.iconbitmap(icon_path)
        self.logic_instance = logik()
        self.main_menu()
        
    def main_menu(self):
        self.reset_screen()
        tk.CTkLabel(self.window, text="Welcome to the Algorithm Path finder", font=("Arial", 25), text_color="black").place(x=75, y=25)
        tk.CTkButton(self.window, text="Create new simulation", command=self.main_programm, corner_radius=32, font=("Arial", 19)).place(x=180, y=100)
        tk.CTkButton(self.window, text="Load simulation", command=self.main_load, corner_radius=32, font=("Arial", 19)).place(x=205, y=150)
        tk.CTkButton(self.window, text="Exit", command=self.window.destroy, corner_radius=32, font=("Arial", 19), fg_color="red", hover_color="darkred").place(x=217, y=200)
        tk.CTkLabel(self.window, text="Made by: @AIIronDev", font=("Arial", 10), text_color="black").place(x=240, y=340)
        tk.CTkLabel(self.window, text="(c) Maximilian Gründinger v.2", font=("Arial", 10), text_color="black").place(x=220, y=360)
        tk.CTkLabel(self.window, text="Github: https://github.com/PaRaMeRoS/Algorithmus", font=("Arial", 10), text_color="blue").place(x=200, y=380)
        tk.CTkComboBox(self.window, values=["Light", "Dark"], command=self.window._set_appearance_mode).place(x=215, y=240)

    
    def main_programm(self):
        self.reset_screen()
        self.combobox_var = tk2.StringVar()
        tk.CTkLabel(self.window, text="Configuration", font=("Arial", 25), text_color="black").place(x=75, y=25)
        tk.CTkLabel(self.window, text="Choose the Point count", font=("Arial", 25), text_color="black").place(x=75, y=75)
        self.Option = tk.CTkComboBox(self.window, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "18", "19", "20"], variable=self.combobox_var).place(x=205, y=150) # vieleicht auch gegen Slider austauschen
        tk.CTkLabel(self.window, text="", font=("Arial", 25), text_color="black").place(x=75, y=200)
        tk.CTkButton(self.window, text="Start", command=self.running, corner_radius=32, font=("Arial", 19)).place(x=205, y=250)
        tk.CTkButton(self.window, text="Back", command=self.main_menu, corner_radius=32, font=("Arial", 19)).place(x=205, y=300)
        
    def main_load(self):
        self.reset_screen()
        tk.CTkLabel(self.window, text="Load", font=("Arial", 25), text_color="black").place(x=75, y=25)
        tk.CTkButton(self.window, text="Select Path", font=("Arial", 16), text_color="black", command=self.get_path).place(x=75, y=75)
        tk.CTkButton(self.window, text="Back", command=self.main_menu, corner_radius=32, font=("Arial", 19)).place(x=205, y=300)
        tk.CTkButton(self.window, text="Load", command=self.logic_instance.load_simulation, corner_radius=32, font=("Arial", 19)).place(x=205, y=250)
        tk.CTkLabel(self.window, text="this is work in Progress", font=("Arial", 16), text_color="red").place(x=250, y=200)
        def get_path(self):
            self.path_load = tk2.filedialog.askdirectory(initialdir="/", title="Select Path")
            tk.CTkLabel(self.window, text=self.path_load, font=("Arial", 16)).place(x=75, y=50)
        
    def reset_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
            
    def render(self):
        # self.save_gui() # Speicherfunktion muss noch eingebaut werden
        self.active_task = "saving"  # file ausgelesern werden
        self.running_done = 50  # Set the initial value (you can change this)
        self.window2 = tk.CTk()
        self.window2.title("Algorithmus _Render")
        self.window2.geometry("600x420")
        self.window2.resizable(True, True)
        self.window2._set_appearance_mode("light")
        self.window2.iconbitmap(icon_path)
        logik.render()
        tk.CTkLabel(self.window2, text="Render", font=("Arial", 25)).place(x=75, y=25)

        match self.active_task:
            case "saving":
                tk.CTkLabel(self.window2, text="saving", font=("Arial", 25)).place(x=125, y=75)
                self.scrollbar = ttk.Progressbar(self.window2, orient='horizontal', mode='determinate', length=280, maximum=100, value=self.running_done).place(x=150, y=150)
            case "dijkstra":
                tk.CTkLabel(self.window2, text="dijkstra", font=("Arial", 25)).place(x=75, y=75)
            case "A*":
                tk.CTkLabel(self.window2, text="A*", font=("Arial", 25)).place(x=75, y=75)

        self.window2.mainloop()

    def help(self):
        tk2.messagebox.showinfo("Help", "Please enter the distances between the points in the order that they are displayed. \n\nExample: \nFrom: 1 \nTo: 2 \nDistance: 5 \n\nFrom: 1 \nTo: 3 \nDistance: 4 \n\n If you have any more questions, please contact me on Github: @PaRaMeRoS/Algorithmus or via E-Mail: PaRaMeRoS@mein.gmx \n\n Have fun!")

    def running(self): # Scrollscreen ausbessern
        self.reset_screen()
        self.combobox = int(self.combobox_var.get())
        fenster_liste = self.logic_instance.get_combinations(self.combobox)

        tk.CTkLabel(self.window, text="Further creating", font=("Arial", 25), text_color="grey").place(x=75, y=25)
        tk.CTkLabel(self.window, text="Please enter the according Distances between the Points", font=("Arial", 16), text_color="black").place(x=75, y=75)
        tk.CTkButton(self.window, text="Help", font=("Arial", 16), fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.help).place(x=75, y=100)
        tk.CTkButton(self.window, text="Save", font=("Arial", 16), corner_radius=32, command=self.save_gui).place(x=225, y=100)
        tk.CTkButton(self.window, text="Render", font=("Arial", 16), corner_radius=32, command=self.render).place(x=375, y=100)	
        tk.CTkButton(self.window, text="Back", command=self.main_programm, corner_radius=32, font=("Arial", 19)).place(x=280, y=25)

        scrollable_frame = tk.CTkCanvas(self.window)
        scrollable_frame.place(x=0, y=150, relwidth=3, relheight=1)

        frame = tk.CTkFrame(scrollable_frame)
        frame_id = scrollable_frame.create_window((0, 0), window=frame, anchor="nw")

        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=scrollable_frame.yview)
        scrollbar.place(x=self.window.winfo_width() - scrollbar.winfo_reqwidth(), y=150, height=scrollable_frame.winfo_reqheight())

        def update_scrollregion(event):
            scrollable_frame.config(scrollregion=scrollable_frame.bbox("all"))
    
        frame.bind("<Configure>", update_scrollregion)
        scrollable_frame.config(yscrollcommand=scrollbar.set)

        self.distance = []
        for element1, element2 in fenster_liste:
            # Erstelle ein neues Frame für jede Iteration
            inner_frame = tk.CTkFrame(frame)
            inner_frame.pack()

            tk.CTkLabel(inner_frame, text="From ", font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text=str(element1), font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text="To ", font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text=str(element2), font=("Arial", 16), text_color="black").pack(side="left")
            distance_entry = tk.CTkEntry(inner_frame, placeholder_text="Distance")
            distance_entry.pack(side="left")
            self.distance.append(distance_entry.get())

        frame.update_idletasks()

    def save_gui(self):
        # Hier muss noch die Speicherfunktion rein -> logik.save_simulation()
        count = self.combobox
        Distance_list = self.distance
        self.path = ""
        self.window3 = tk.CTk()
        self.window3.title("Algorithmus _Save")
        self.window3.geometry("600x420")
        self.window3.resizable(True, True)
        self.window3._set_appearance_mode("light")
        self.window3.iconbitmap(icon_path)
        tk.CTkLabel(self.window3, text="Save", font=("Arial", 25)).place(x=75, y=25)
        tk.CTkButton(self.window3, text="Select Path", font=("Arial", 16), command=self.get_path).place(x=75, y=75)
        tk.CTkLabel(self.window3, text=self.path, font=("Arial", 16)).place(x=75, y=50)
        tk.CTkLabel(self.window3, text="Enter Author: ", font=("Arial", 16)).place(x=75, y=200)
        tk.CTkEntry(self.window3, placeholder_text="Author").place(x=125, y=200)
        tk.CTkLabel(self.window3, text="Enter Simulation Name: ", font=("Arial", 16)).place(x=75, y=150)
        tk.CTkEntry(self.window3, placeholder_text="Simulation Name").place(x=125, y=150)
        #tk.CTkButton(self.window3, text="Save", font=("Arial", 16), command=lambda: self.logic_instance.save_simulation().place(x=75, y=100)# Add right command
        tk.CTkButton(self.window3, text="Break", command=self.window3.destroy, corner_radius=32, font=("Arial", 19)).place(x=280, y=25)
        self.window3.mainloop()

    def error_window(self):
        tk2.messagebox.showerror("Error", "Please enter a number between 1 and 20")

    def get_path(self):
        self.path = tk2.filedialog.askdirectory(initialdir="/", title="Select Path")


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