import tkinter as tk
from PIL import ImageTk, Image
import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")

global original_img
try:
    original_img = Image.open(image_path)
except Exception as e:
    print("Errore durante il caricamento dell'immagine:", e)

class GameUI:
    def __init__(self, enemy_card):
        self.master = tk.Tk()
        self.__game = None
        self.master.title("Regicide - partita in corso")
        self.master.geometry("1200x600")
        self.master.configure(bg="#106040")
        self.master.minsize(1200, 600)
        self.__scarto = None
        self.__difesa = 0

        self.__enemy_card = enemy_card
        self.__player_cards = []

    def update_enemy_card(self, card):
        self.__enemy_card = card
        self.__show_card(self.__frame_castello, self.__enemy_card)

    def add_game_instance(self, instance):
        self.__game = instance
        self.__init_widgets()

    def mod_difesa(self, new_value):
        self.__difesa = new_value
        
        #cancello e riscrivo la label
        self.__label_difesa.place_forget()
        self.__label_difesa = tk.Label(self.master, text = f"Difesa: {self.__difesa}", font = ("Arial", 18))
        self.__label_difesa.place(anchor="sw", relx= 0.02, rely= 0.98)

    def __init_widgets(self):
        # label per la difesa passiva
        self.__label_difesa = tk.Label(self.master, text = f"Difesa: {self.__difesa}", font = ("Arial", 18))
        self.__label_difesa.place

        # imposto il frame del castello (e mostro il nemico)
        self.__frame_castello = tk.Frame(self.master, width=142, height=200, bg="#106040")
        self.__frame_castello.place(anchor='center', relx=0.5, rely=0.35)
        self.__show_card(self.__frame_castello, self.__enemy_card)

        # imposto frame scarti
        self.__frame_scarti = tk.Frame(self.master, width=142, height=200, bg="#106040")
        self.__frame_scarti.place(anchor='center', relx=0.3, rely=0.35)

        # imposto frame del giocatore 
        self.__player_frame = tk.Frame(self.master, bg = "#106040")
        self.__player_frame.pack(side=tk.BOTTOM, pady=20)

        # mostro le carte del giocatore
        self.__show_player_cards()

        # metto il tasto per terminare il turno 
        self.__button_finisci = tk.Button(self.master, text="Termina", command=self.__finisci_turno)
        self.__button_finisci.place(relx=0.98, rely=0.98, anchor='se')

    def add_player_hand(self, players_hand):
        self.__player_cards= players_hand
        self.update_player_showed_cards(players_hand)
    
    def __show_player_cards(self):
        for card in self.__player_cards:
            frame = tk.Frame(self.__player_frame, bg = "#106040")
            frame.pack(side=tk.LEFT)
            self.__show_card(frame, card)

    def update_card(self, frame, new_card):
        # Rimuovi tutti i widget all'interno del frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Aggiungi la nuova carta
        if frame == self.__frame_castello:
            self.__enemy_card = new_card
        elif frame == self.__frame_scarti:
            self.__scarto = new_card

        self.__show_card(frame, new_card)

    def __card_clicked(self, card):
        puoi_giocare_ancora = self.__game.got_card(card)
        
        # Se il frame della carta è il castello, non aggiornare il mazzo degli scarti
        if card != self.__enemy_card:
            self.__scarto = card
            self.update_card(self.__frame_scarti, card)

        self.update_player_showed_cards(self.__game.get_player_cards())

        if puoi_giocare_ancora == False:
            self.__finisci_turno()

    def update_player_showed_cards(self, new_cards):
        for widget in self.__player_frame.winfo_children():
            widget.destroy()

        self.__show_player_cards()

    def __show_card(self, frame, card):
        if card != None:
            card_coordinates = coordinate_carte[card.split("_")[1]][card]

            left, top = card_coordinates[0], card_coordinates[1]
            crop_region = (left, top, left + 410, top + 570)

            try:
                cropped_img = original_img.crop(crop_region)
                cropped_img = cropped_img.resize((142, 200), Image.BICUBIC)

                img = ImageTk.PhotoImage(cropped_img)

                # uso una label per non avere i bordi del bottone
                label = tk.Label(frame, image=img, bd=0, highlightthickness=0)
                label.image = img
                label.pack()

                # collego alla label un bottone
                label.bind("<Button-1>", lambda event, card=card: self.__card_clicked(card))


            except Exception as e:
                print("Errore durante la visualizzazione dell'immagine:", e)    

    def __finisci_turno(self):
        self.__game.finisci_turno()

    def get_enemy_frame(self):
        return self.__frame_castello

global coordinate_carte
coordinate_carte = {
    'quadri': {'K_quadri': (90, 545), 'Q_quadri': (90, 1205), 'J_quadri': (90, 1865), '10_quadri': (90, 2525), '9_quadri': (90, 3185), '8_quadri': (90, 3845), '7_quadri': (2520, 545), '6_quadri': (2520, 1205), '5_quadri': (2520, 1865), '4_quadri': (2520, 2525), '3_quadri': (2520, 3185), '2_quadri': (2520, 3845), 'A_quadri': (2043, 2525)},
    'picche': {'K_picche': (582, 545), 'Q_picche': (582, 1205), 'J_picche': (582, 1865), '10_picche': (582, 2525), '9_picche': (582, 3185), '8_picche': (582, 3845), '7_picche': (3012, 545), '6_picche': (3012, 1205), '5_picche': (3012, 1865), '4_picche': (3012, 2525), '3_picche': (3012, 3185), '2_picche': (3012, 3845), 'A_picche': (2043, 1865)},
    'cuori': {'K_cuori': (1074, 545), 'Q_cuori': (1074, 1205), 'J_cuori': (1074, 1865), '10_cuori': (1074, 2525), '9_cuori': (1074, 3185), '8_cuori': (1074, 3845), '7_cuori': (3504, 545), '6_cuori': (3504, 1205), '5_cuori': (3504, 1865), '4_cuori': (3504, 2525), '3_cuori': (3504, 3185), '2_cuori': (3504, 3845), 'A_cuori': (2043, 1205)},
    'fiori': {'K_fiori': (1566, 545), 'Q_fiori': (1566, 1205), 'J_fiori': (1566, 1865), '10_fiori': (1566, 2525), '9_fiori': (1566, 3185), '8_fiori': (1566, 3845), '7_fiori': (3996, 545), '6_fiori': (3996, 1205), '5_fiori': (3996, 1865), '4_fiori': (3996, 2525), '3_fiori': (3996, 3185), '2_fiori': (3996, 3845), 'A_fiori': (2043, 545)},
    'None': {'Jolly@_None': (2043, 3185), 'Back_None': (2043, 3845)}
}

