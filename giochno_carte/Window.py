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
        self.menu = FrameMenu(self)

        # run
        self.mainloop()

class FrameMenu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # placing the frame itself
        self.pack()

        # titolo centrale
        self.lbl_titolo = ttk.Label(self, text="MENU", font=("Arial", 35))
        self.lbl_titolo.pack(pady = 50)

        # nome giocatore
        self.lbl_nome = ttk.Label(self, text="Nome:", font=("Arial", 18))
        self.lbl_nome.pack(side=tk.LEFT, padx=10, pady= 10)

        self.entry_nome = ttk.Entry(self)
        self.entry_nome.pack(side=tk.LEFT, padx= 10, pady= 10)

        # bottoni per giocare
        self.btn_nome = ttk.Button(text = "leggi nome", command= self.mostra_valore)
        self.btn_nome.pack(side = tk.BOTTOM, expand = True)
        
        self.btn_ricerca = ttk.Button(text="gioca partita locale", command= self.gioca)
        self.btn_ricerca.pack(side = tk.BOTTOM, expand = True)

    def mostra_valore(self):
        valore_inserito = self.entry_nome.get()
        print("Valore inserito:", valore_inserito)

    def gioca(self):
        # inizia il gioco
        self.__gioco = Game(2) # inserisci num giocatori
        
        # Nasconde il frame del menu e mostra il frame del gioco
        self.pack_forget()
        print("dio belletti")
        self.frame_gioco = FrameGioco()

class  FrameGioco(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        print("PORCA MADONNA SI")
        self.lbl_titolo = ttk.Label(self, text="Schermata Gioco", font=("Arial", 24))
        self.lbl_titolo.pack(padx=10, pady=10)

# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

App("menu", 4, 5)