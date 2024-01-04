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
        self.window.title("Folder sorter")
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
        tk.CTkLabel(self.window, text="Made by: @AIIronDev", font=("Arial", 10), text_color="black").place(x=240, y=360)
        tk.CTkLabel(self.window, text="Github: https://github.com/Iron-witch/Folder-sorter", font=("Arial", 10), text_color="blue").place(x=200, y=380)

    
    def main_programm(self):
        self.reset_screen()
        tk.CTkLabel(self.window, text="You ", font=("Arial", 25), text_color="black").place(x=75, y=25)
        tk.CTkCheckbutton(self.window, text="Create new simulation", command=self.main_programm, corner_radius=32, font=("Arial", 19)).place(x=180, y=100)
        

    def main_load(self):
        self.reset_screen()
        pass
        
    def reset_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()


# main running area -> main function
if __name__ == "__main__":
    window = main()
    window.window.mainloop()