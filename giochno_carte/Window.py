import tkinter as tk
from tkinter import ttk
import subprocess

from Main import *

class App(tk.Tk):
    def __init__(self, titolo, rows, columns):
        super().__init__()

        # main setup
        self.geometry("800x600")
        self.minsize(600, 400)
        self.title(titolo)
        self.configure(bg= "green")

        # set grid
        for i in range(rows):
            self.rowconfigure(i, weight=1)  # Imposta il peso della riga
            for j in range(columns):
                self.columnconfigure(j, weight=1)  # Imposta il peso della colonn

        # widgets
        self.menu = Menu(self)

        # run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # placing the frame itself
        self.pack()

        # titolo centrale
        self.lbl_titolo = ttk.Label(self, text="MENU", font=("Arial", 35))
        self.lbl_titolo.pack(padx = 0, pady = 50)

        # nome giocatore
        self.lbl_nome = ttk.Label(self, text="Nome:", font=("Arial", 18))
        self.lbl_nome.pack(side=tk.LEFT, padx=10)

        self.entry_nome = ttk.Entry(self)
        self.entry_nome.pack(side=tk.LEFT, padx= 10)

        # bottoni per giocare
        self.btn_ricerca = ttk.Button(text="gioca partita locale", command= self.gioca)
        self.btn_ricerca.pack(padx= 10, pady= 30)

    def gioca(self):
        try:
            subprocess.run(["python", "Main.py"])
        except FileNotFoundError:
            print("File non trovato")

print("dio can")
App("menu", 4, 5)