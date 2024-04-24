'''import tkinter as tk
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
        self.frame_gioco = FrameGioco(self.__gioco)

class  FrameGioco(ttk.Frame):
    def __init__(self, master, gioco):
        super().__init__(master)
        self.__gioco = gioco
        
        self.lbl_titolo = ttk.Label(self, text="Schermata Gioco", font=("Arial", 24))
        self.lbl_titolo.pack(padx=10, pady=10)
        
    def on_closing(self):
        if tk.messagebox.askokcancel("Chiusura", "Vuoi davvero chiudere l'applicazione?"):
            self.__gioco.terminaPartita()
            self.destroy()

# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

App("menu", 4, 5)'''


import tkinter as tk
from tkinter import ttk, messagebox

from Main import *

class App(tk.Tk):
    def __init__(self, titolo, rows, columns):
        super().__init__()

        # Main setup
        self.geometry("800x600")
        self.minsize(600, 400)
        self.title(titolo)
        self.configure(bg="green")

        # Set grid
        for i in range(rows):
            self.rowconfigure(i, weight=1)
            for j in range(columns):
                self.columnconfigure(j, weight=1)

        # Create the Menu Frame
        self.frame_menu = FrameMenu(self)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")

        # Show the Menu Frame
        self.show_frame(self.frame_menu)

    def show_frame(self, frame):
        frame.tkraise()

class FrameMenu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Empty Space to Left
        self.empty_space = tk.Label(self, text="", width=20)
        self.empty_space.grid(row=0, column=0)

        # Title
        self.lbl_titolo = ttk.Label(self, text="MENU", font=("Arial", 35))
        self.lbl_titolo.grid(row=0, column=1, columnspan=2, pady=50)

        # Name Entry
        self.lbl_nome = ttk.Label(self, text="Nome:", font=("Arial", 18))
        self.lbl_nome.grid(row=1, column=1, padx=10)

        self.entry_nome = ttk.Entry(self)
        self.entry_nome.grid(row=1, column=2, padx=10)

        # Buttons
        self.btn_nome = ttk.Button(self, text="Leggi Nome", command=self.mostra_valore)
        self.btn_nome.grid(row=2, column=1, padx=10, pady=30)

        self.btn_ricerca = ttk.Button(self, text="Gioca Partita Locale", command=self.gioca)
        self.btn_ricerca.grid(row=2, column=2, padx=10, pady=30)

    def mostra_valore(self):
        valore_inserito = self.entry_nome.get()
        print("Valore inserito:", valore_inserito)

        '''
        def make_a_suicidal_class():
        my_suicidal_class = SelfDestruct()
        for i in range(5):
            my_suicidal_class.do_stuff()
        return None'''

    def torna_al_menu(self):
        # Ask for Confirmation
        if messagebox.askokcancel("Chiusura", "Vuoi davvero tornare al Menu?"):
            # Destroy Game Frame and Show Menu Frame
            self.destroy()
            self.master.show_frame(self.master.frame_menu)
'''
class FrameGioco(ttk.Frame):
    def __init__(self, master, gioco):
        super().__init__(master)
        self.__gioco = gioco
        
        # Empty Space to Left
        self.empty_space = tk.Label(self, text="", width=20)
        self.empty_space.pack()

        # Title
        self.lbl_titolo = ttk.Label(self, text="Schermata Gioco", font=("Arial", 24))
        self.lbl_titolo.pack(padx=10, pady=10)

        # Button to Quit Game and Go Back to Menu
        self.btn_menu = ttk.Button(self, text="Torna al Menu", command=self.torna_al_menu)
        self.btn_menu.pack(padx=10, pady=10)

    def torna_al_menu(self):
        # Ask for Confirmation
        if messagebox.askokcancel("Chiusura", "Vuoi davvero tornare al Menu?"):
            # Destroy Game Frame and Show Menu Frame
            self.destroy()
            self.master.show_frame(self.master.frame_menu) 
            '''

def main():
    app = App("Menu", 4, 5)
    app.mainloop()

if __name__ == "__main__":
    main()

# https://stackoverflow.com/questions/70739246/opening-a-new-window-using-a-link-in-tkinter#:~:text=You%20can%20open%20new%20windows,Toplevel()%20command.