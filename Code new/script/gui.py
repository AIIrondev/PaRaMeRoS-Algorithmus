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
        tk.CTkOptionMenu(self.window, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12", "13", "14", "15"], command=self.option_calback_menu).place(x=205, y=150)
        tk.CTkButton(self.window, text="Back", command=self.main_menu, corner_radius=32, font=("Arial", 19)).place(x=205, y=200)
        
    def option_calback_menu(self, event):
        if event == "Normal":
            self.normal()
        elif event == "Custom":
            self.custom()

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