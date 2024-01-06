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
import tkinter as tk2
import os

# var definition
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "..", "Bilder", "LOGO.ico")

# class main -> main funkltion GUI class
class main:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Algorithmus")
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        self.window._set_appearance_mode("light")
        self.window.iconbitmap(icon_path)

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
        self.Option = tk.CTkComboBox(self.window, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15", "16", "17", "18", "19", "20"], variable=self.combobox_var).place(x=205, y=150)
        tk.CTkLabel(self.window, text="", font=("Arial", 25), text_color="black").place(x=75, y=200)
        self.Entry = tk.CTkEntry(self.window, placeholder_text="Count of Connections betwen Points").place(x=205, y=200)
        tk.CTkButton(self.window, text="Start", command=self.running, corner_radius=32, font=("Arial", 19)).place(x=205, y=250)
        tk.CTkButton(self.window, text="Back", command=self.main_menu, corner_radius=32, font=("Arial", 19)).place(x=205, y=300)

    def main_load(self):
        self.reset_screen()
        pass
        
    def reset_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

#    def new_window_render(self): 
#        self.window1 = tk.CTk()
#        self.window1.titel("Render") # AttributeError: '_tkinter.tkapp' object has no attribute 'titel'
#        self.window1.geometry("600x400")
#        self.window1.resizable(False, False)
#        self.window1._set_appearance_mode("light")
#        self.window1.iconbitmap(icon_path)
#        # Hier noch die Elemente hinzufügen
#        self.window1.mainloop()

    def running(self):
        self.reset_screen()
        print(self.combobox_var.get()) # geht jetzt nicht wie self.Entry.get() -> AttributeError: 'main' object has no attribute 'Entry'
        tk.CTkLabel(self.window, text="Further creating", font=("Arial", 25), text_color="black").place(x=75, y=25) # change Titel
        tk.CTkLabel(self.window, text="Please enter the according Distances between the Points", font=("Arial", 16), text_color="black").place(x=75, y=75)
        tk.CTkButton(self.window, text="Back", command=self.main_programm, corner_radius=32, font=("Arial", 19)).place(x=205, y=300)
        self.new_window_render()

# main running area -> main function
if __name__ == "__main__":
    window = main()
    window.window.mainloop()