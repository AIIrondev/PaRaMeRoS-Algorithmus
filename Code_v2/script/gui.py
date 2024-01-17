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

# class main -> main funkltion GUI class
class main:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Algorithmus")
        self.window.geometry("600x420")
        self.window.resizable(False, False)
        self.window._set_appearance_mode("light")
        self.window.iconbitmap(icon_path)
        self.logic_instance = logik()
        self.main_menu()
        
    def main_menu(self):
        self.reset_screen()
        tk.CTkLabel(self.window, text="Welcome to the Algorithm Path finder ", font=("Arial", 25), text_color="black").place(x=80, y=25)
        tk.CTkLabel(self.window, text="from the PaRaMeRoS FLL Team", font=("Arial", 25), text_color="black").place(x=110, y=54)
        tk.CTkButton(self.window, text="Create new simulation", command=self.main_programm, corner_radius=32, font=("Arial", 19)).place(x=180, y=100)
        tk.CTkButton(self.window, text="Load simulation", command=self.main_load, corner_radius=32, font=("Arial", 19)).place(x=205, y=150)
        tk.CTkButton(self.window, text="Licence", command=self.licence, corner_radius=32, font=("Arial", 19)).place(x=225, y=300)
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
            
    def render(self, distance_render, count):
        # self.save_gui() # Speicherfunktion muss noch eingebaut werden
        self.active_task = "saving"  # file ausgelesern werden
        self.running_done = 50  # Set the initial value (you can change this)
        self.window2 = tk.CTk()
        self.window2.title("Algorithmus _Render")
        self.window2.geometry("600x420")
        self.window2.resizable(True, True)
        self.window2._set_appearance_mode("light")
        self.window2.iconbitmap(icon_path)
        logik.render(self, distance_render, count)
        tk.CTkLabel(self.window2, text="Render", font=("Arial", 25)).place(x=75, y=25) 
        tk.CTkLabel(self.window2, text="The simulation is being rendered", font=("Arial", 16)).place(x=75, y=75)
        self.window2.mainloop()

    def help(self):
        tk2.messagebox.showinfo("Help", "Please enter the distances between the points in the order that they are displayed. \n\nExample: \nFrom: 1 \nTo: 2 \nDistance: 5 \n\nFrom: 1 \nTo: 3 \nDistance: 4 \n\n If you have any more questions, please contact me on Github: @PaRaMeRoS/Algorithmus or via E-Mail: PaRaMeRoS@mein.gmx \n\n Have fun!")

    def running(self): # Scrollscreen ausbessern
        global distance_list
        distance_list = []
        self.reset_screen()
        self.combobox = int(self.combobox_var.get())
        render_sd = self.combobox
        fenster_liste = self.logic_instance.get_combinations(self.combobox)

        tk.CTkLabel(self.window, text="Further creating", font=("Arial", 25), text_color="grey").place(x=75, y=25)
        tk.CTkLabel(self.window, text="Please enter the according Distances between the Points", font=("Arial", 16), text_color="black").place(x=75, y=75)
        tk.CTkButton(self.window, text="Help", font=("Arial", 16), fg_color="green", hover_color="darkgreen", corner_radius=32, command=self.help).place(x=75, y=100)
        tk.CTkButton(self.window, text="Save", font=("Arial", 16), corner_radius=32, command=lambda: self.save_gui(distance_list, render_sd)).place(x=225, y=100)
        tk.CTkButton(self.window, text="Render", font=("Arial", 16), corner_radius=32, command=lambda: self.render(distance_list, render_sd)).place(x=375, y=100)	
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
        
        for element1, element2 in fenster_liste:
            # Erstelle ein neues Frame für jede Iteration
            inner_frame = tk.CTkFrame(frame)
            inner_frame.pack()

            tk.CTkLabel(inner_frame, text="From ", font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text=str(element1), font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text="To ", font=("Arial", 16), text_color="black").pack(side="left")
            tk.CTkLabel(inner_frame, text=str(element2), font=("Arial", 16), text_color="black").pack(side="left")

            # Erstellen Sie eine StringVar, um den Wert des Entry-Widgets zu verfolgen
            distance_var = tk.StringVar()
            distance_entry = tk.CTkEntry(inner_frame, textvariable=distance_var, placeholder_text="Distance")
            distance_entry.pack(side="left")

            # Fügen Sie die StringVar (nicht den Entry-Widget) zur Liste hinzu
            distance_list.append(distance_var)

        frame.update_idletasks()

    def licence(self):
        tk2.messagebox.showinfo("Licence", f"Path finding algorithm License Agreement\nThis License Agreement (the 'Agreement') is entered into by and between Maximilian Gründinger ('Licensor') and the First Lego League Team known as PaRaMeRoS ('Licensee').\n1. License Grant.\nLicensor hereby grants Licensee a non-exclusive, non-transferable license to use and modify the software program known as [Your Program Name] (the 'Program') solely for educational and non-commercial purposes. This license is granted exclusively to the members of the First Lego League Team identified as [First Lego League Team Name].\n2. Restrictions.\nLicensee shall not, and shall not permit others to:\na. Use the Program for any purpose other than educational and non-commercial activities within the First Lego League Team.\nb. Allow non-members of the First Lego League Team to use or access the Program.\nc. Commercialize or distribute the Program for financial gain.\nd. Remove or alter any copyright, trademark, or other proprietary notices contained in the Program.\n3. Security.\nLicensor makes no warranties regarding the security of the Program. Licensee acknowledges and agrees that any use of the Program is at their own risk. Licensor shall not be responsible for any security bugs or issues that may arise in connection with the Program.\n4. Term and Termination.\nThis Agreement shall remain in effect until terminated by either party. Licensor reserves the right to terminate this Agreement immediately if Licensee breaches any of its terms. Upon termination, Licensee shall cease all use of the Program and destroy all copies in their possession.\n5. Disclaimer of Warranty.\nTHE PROGRAM IS PROVIDED 'AS IS' WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. LICENSOR DISCLAIMS ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.\n6. Limitation of Liability.\nIN NO EVENT SHALL LICENSOR BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM, EVEN IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.\n7. Governing Law.\nThis Agreement shall be governed by and construed in accordance with the laws of [Your Jurisdiction].\n8. Entire Agreement.\nThis Agreement constitutes the entire agreement between the parties and supersedes all prior agreements, whether oral or written, with respect to the Program.\nIN WITNESS WHEREOF, the parties hereto have executed this License Agreement as of the effective date.\nLicensor:\nMaximilian Gründinger\nLicensee:\nPaRaMeRoS\nDate: 1.1.2024")

    def save_gui(self, distance_list, count):
        try:
            Distance_list = distance_list
            self.author_save = tk2.StringVar()
            self.simulation_name_save = tk2.StringVar()
            self.path = ""
            self.window3 = tk.CTk()
            self.window3.title("Algorithmus _Save")
            self.window3.geometry("600x420")
            self.window3.resizable(True, True)
            self.window3._set_appearance_mode("light")
            self.window3.iconbitmap(icon_path)
            self.author_save.set("DefaultAuthor")
            self.simulation_name_save.set("DefaultSimulationName")
            tk.CTkLabel(self.window3, text="Save", font=("Arial", 25)).place(x=75, y=25)
            tk.CTkButton(self.window3, corner_radius=32, text="Select Path", font=("Arial", 16), command=self.get_path).place(x=75, y=75)
            tk.CTkLabel(self.window3, text=self.path, font=("Arial", 16)).place(x=75, y=50)
            tk.CTkLabel(self.window3, text="Enter Author: ", font=("Arial", 16)).place(x=75, y=200)
            tk.CTkEntry(self.window3, placeholder_text="Author", textvariable=self.author_save).place(x=225, y=200)
            tk.CTkLabel(self.window3, text="Enter Simulation Name: ", font=("Arial", 16)).place(x=75, y=150)
            tk.CTkEntry(self.window3, placeholder_text="Simulation Name", textvariable=self.simulation_name_save).place(x=250, y=150)
            tk.CTkButton(self.window3, corner_radius=32, text="Save", font=("Arial", 16), command=lambda: self.logic_instance.save_simulation(self.path, self.simulation_name_save.get(), count, distance_list, self.author_save.get())).place(x=200, y=300)
            tk.CTkButton(self.window3, text="Break", command=self.window3.destroy, corner_radius=32, font=("Arial", 19)).place(x=280, y=25)
            self.window3.mainloop()
        except Exception as e:
            ttk.messagebox.showerror("Error", f"An error occurred: {e}")

    def error_window(self):
        tk2.messagebox.showerror("Error", "Please enter a number between 1 and 20")

    def get_path(self):
        self.path = tk2.filedialog.askdirectory(initialdir="/", title="Select Path")

    def display_rendert_path(self, result, file):
        self.window4 = tk.CTk()
        self.window4.title("Algorithmus _Render_result")
        self.window4.geometry("600x420")
        self.window4.resizable(True, True)
        self.window4._set_appearance_mode("light")
        self.window4.iconbitmap(icon_path)
        tk.CTkLabel(self.window4, text="Render", font=("Arial", 25)).place(x=75, y=25)
        tk.CTkLabel(self.window4, text="The shortest Path is: ", font=("Arial", 16)).place(x=75, y=75)
        tk.CTkLabel(self.window4, text=result, font=("Arial", 16)).place(x=75, y=100)
        tk2.PhotoImage(file=file, width=200, height=100).place(x=75, y=125)
        tk.CTkButton(self.window4, text="Break", command=self.window4.destroy, corner_radius=32, font=("Arial", 19)).place(x=280, y=25)
        self.window4.mainloop()

class logik:
    def __init__(self):
        pass

    def save_simulation(self, file_path, file_name, count, Distance_list, author_save):
        POINTS = count  # POINTS -> Anzahl der Punkte
        ERDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        BEDATE = datetime.datetime.now()  # ERDATE -> erstellungsdatum
        AUTOR = author_save # AUTOR -> wer hat es erstellt
        EDIT = 1 # EDIT -> wie oft bearbeitet
        print(file_name)
        print(author_save)
        Distance_list_values = [distance.get() for distance in Distance_list]
        self.save_path = os.path.join(file_path, f"{file_name}.fll") # Projekt files -> weiter machen
        with open(self.save_path, "w") as file:
            file.write(str(POINTS) + "\n")
            file.write(str(ERDATE) + "\n")
            file.write(str(BEDATE) + "\n")
            file.write(str(Distance_list_values) + "\n")
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
        points = logik.get_combinations(self, count)
        processed_values = [(*point, distance) for point, distance in zip(points, distance_render_logik)]
        with open(os.path.join(base_dir, "..", "config","count.fll"), "w") as file:
            file.write(str(count))
        with open(os.path.join(base_dir, "..", "config", "points.csv"), "w") as file:
            file.truncate(0)
            for point1, point2, distance in processed_values:
                file.write(str(point1) + ", " + str(point2) + ", " + str(distance.get()) + "\n")
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
    window = main()
    window.window.mainloop()