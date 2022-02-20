from engine import Engine

import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename

class Menu1:
    def __init__(self,master):
        self.master = master
        self.master.title = "Improved Advisor"
        self.master.geometry('800x500')
        self.frame = tk.Frame(self.master)
        # self.engine = Engine
        self.file_upload = tk.Button(
            self.frame, 
            padx=20, 
            pady=30,
            text ="Upload .pdf from myWSU",
            command = lambda:self.openFile()
        )

        # # Display
        self.file_upload.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.frame.pack()

    def openFile(self):
        file_name = askopenfilename()
        if file_name is not None:
            print(f"looking for {file_name}")
            engine = Engine(file_name)
            self.transform_window(engine)

    def transform_window(self,engine):
        self.file_upload.grid_forget()

        name = tk.Label(self.frame, text=f"Name : {engine.get_user_name()}")
        id = tk.Label(self.frame, text=f"ID# : {engine.get_user_id()}")
        
        total_credits = tk.Label(self.frame, text="Total Credits : ")
        total_credits_calc = tk.Label(self.frame, text = f"{engine.get_user_tcredits()} / 140")

        upper_div_credits = tk.Label(self.frame, text="Upper-Div Credits : ")
        upper_div_credits_calc = tk.Label(self.frame, text=f"{engine.get_user_dcredits()} / 40")
        
        gpa = tk.Label(self.frame, text="GPA : ")
        gpa_calc = tk.Label(self.frame, text=f"{engine.get_user_gpa()}")
        
        ucore_classes = tk.Label(self.frame, text="UCORE Classes")
        major_classes = tk.Label(self.frame, text="Major-Specific Classes")
        
        name.grid(row = 0, column = 0, padx = 10, pady = 10)
        id.grid(row = 0, column = 1, padx = 10, pady = 10)

        total_credits.grid(row = 1, column = 0, padx = 10, pady = 10)
        total_credits_calc.grid(row = 1, column = 1, padx = 10, pady = 10)
        upper_div_credits.grid(row = 2, column = 0, padx = 10, pady = 10)
        upper_div_credits_calc.grid(row = 2, column = 1, padx = 10, pady = 10)
        gpa.grid(row = 3, column = 0, padx = 10, pady = 10)
        gpa_calc.grid(row = 3, column = 1, padx = 10, pady = 10)

        ucore_classes.grid(row = 4, column = 0, padx = 10, pady = 10)
        major_classes.grid(row = 5, column = 0, padx = 10, pady = 10)
        
        # self.frame.pack()
        


"""
    Need to display:
    Name || Id number
    Total Credits
    Upper-Div Credits
    GPA
    UCORE Classes
    Then Major Specific Classes
"""

"""
    If we can get that done then
    - Add button for ranked classes 
    - Add option to click on a class and view the live discussion

"""


def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == "__main__":
    main()