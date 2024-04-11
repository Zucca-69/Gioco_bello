import tkinter as tk

class MainWindow():
    def __init__(self):
        super().__init__()
        
        self.geometry("800x500")
        self.title("Regicide Online")
        self.resizable(False, False)
        self.configure(background= "white")
        
root = MainWindow()
root.mainloop()