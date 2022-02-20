from user import User
from engine import Engine

import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename

file_path = ""

class Menu1:
    def __init__(self,master):
        self.master = master
        self.master.title = "Improved Advisor"
        self.master.geometry('800x500')
        self.frame = tk.Frame(self.master)

        self.file_upload = tk.Button(
            self.frame, 
            padx=20, 
            text ="Upload .pdf from myWSU",
            command = lambda:self.openFile()
        )

        # Display
        self.file_upload.grid(row=1, column=0)
        self.frame.pack()

    def openFile(self):
        file_name = askopenfilename()
        if file_name is not None:
            global file_path
            file_path = file_name
        print(f"looking for {file_path}")
        engine = Engine(file_path)
        







def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == "__main__":
    main()