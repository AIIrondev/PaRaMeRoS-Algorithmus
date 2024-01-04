# import modules
import customtkinter as tk
import tkinter as tk2
import os

# var definition
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "..", "Bilder", "LOGO.ico")

class main:
    def __init__(self):
        self.root = tk.CTk()
        self.root.title("Algorithm Path finder")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg="white")
        self.root.iconbitmap(icon_path)
        self.root.mainloop()
        
if __name__ == "__main__":
    main()