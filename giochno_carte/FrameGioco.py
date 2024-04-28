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
        self.master.geometry("1000x600")
        self.master.configure(bg="#106040")
        self.master.minsize(1100, 600)
        self.__scarto = None

        self.__enemy_card = enemy_card
        self.__player_cards = []

    def update_enemy_card(self, card):
        self.__enemy_card = card
        self.__show_card(self.__frame_castello, self.__enemy_card)

    def add_game_instance(self, instance):
        self.__game = instance
        self.__init_widgets()

    def __init_widgets(self):
        # imposto il frame del castello (e mostro il nemico)
        self.__frame_castello = tk.Frame(self.master, width=142, height=200, bg="#106040")
        self.__frame_castello.place(anchor='center', relx=0.5, rely=0.35)
        self.__show_card(self.__frame_castello, self.__enemy_card)

        # imposto frame scarti
        self.__frame_scarti = tk.Frame(self.master, width=142, height=200, bg="#106040")
        self.__frame_scarti.place(anchor='center', relx=0.3, rely=0.35)

        # imposto frame del giocatore 
        self.__player_frame = tk.Frame(self.master)
        self.__player_frame.pack(side=tk.BOTTOM, pady=20)

        # mostro le carte del giocatore
        self.__show_player_cards()

        # metto il tasto per la rinuncia 
        self.__button_rinuncia = tk.Button(self.master, text="Rinuncia", command=self.__rinuncia_turno)
        self.__button_rinuncia.place(relx=0.97, rely=0.97, anchor='se')

    def add_player_hand(self, players_hand):
        self.__player_cards= players_hand
        self.__show_player_cards()
    
    def __show_player_cards(self):
        for card in self.__player_cards:
            frame = tk.Frame(self.__player_frame)
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
        self.__game.got_card(card)
        
        # Se il frame della carta è il castello, non aggiornare il mazzo degli scarti
        if card != self.__enemy_card:
            self.__scarto = card
            self.update_card(self.__frame_scarti, card)

        self.update_player_showed_cards(self.__game.get_player_cards())


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

    def __rinuncia_turno(self):
        self.__game.rinuncia_turno()

    def get_enemy_frame(self):
        return self.__frame_castello

global coordinate_carte
coordinate_carte = {
'quadri': {'K_quadri': (90, 545, 486, 1101), 'Q_quadri': (90, 1205, 486, 1761), 'J_quadri': (90, 1865, 486, 2421), '10_quadri': (90, 2525, 486, 3081), '9_quadri': (90, 3185, 486, 3741), '8_quadri': (90, 3845, 486, 4401), '7_quadri': (2520, 545, 2916, 1101), '6_quadri': (2520, 1205, 2916, 1761), '5_quadri': (2520, 1865, 2916, 2421), '4_quadri': (2520, 2525, 2916, 3081), '3_quadri': (2520, 3185, 2916, 3741), '2_quadri': (2520, 3845, 2916, 4401), 'A_quadri': (2043, 2525, 2439, 3081)}, 
'picche': {'K_picche': (582, 545, 978, 1101), 'Q_picche': (582, 1205, 978, 1761), 'J_picche': (582, 1865, 978, 2421), '10_picche': (582, 2525, 978, 3081), '9_picche': (582, 3185, 978, 3741), '8_picche': (582, 3845, 978, 4401), '7_picche': (3012, 545, 3408, 1101), '6_picche': (3012, 1205, 3408, 1761), '5_picche': (3012, 1865, 3408, 2421), '4_picche': (3012, 2525, 3408, 3081), '3_picche': (3012, 3185, 3408, 3741), '2_picche': (3012, 3845, 3408, 4401), 'A_picche': (2043, 1865, 2439, 2421)}, 
'cuori': {'K_cuori': (1074, 545, 1470, 1101), 'Q_cuori': (1074, 1205, 1470, 1761), 'J_cuori': (1074, 1865, 1470, 2421), '10_cuori': (1074, 2525, 1470, 3081), '9_cuori': (1074, 3185, 1470, 3741), '8_cuori': (1074, 3845, 1470, 4401), '7_cuori': (3504, 545, 3900, 1101), '6_cuori': (3504, 1205, 3900, 1761), '5_cuori': (3504, 1865, 3900, 2421), '4_cuori': (3504, 2525, 3900, 3081), '3_cuori': (3504, 3185, 3900, 3741), '2_cuori': (3504, 3845, 3900, 4401), 'A_cuori': (2043, 1205, 2439, 1761)}, 
'fiori': {'K_fiori': (1566, 545, 1962, 1101), 'Q_fiori': (1566, 1205, 1962, 1761), 'J_fiori': (1566, 1865, 1962, 2421), '10_fiori': (1566, 2525, 1962, 3081), '9_fiori': (1566, 3185, 1962, 3741), '8_fiori': (1566, 3845, 1962, 4401), '7_fiori': (3996, 545, 4392, 1101), '6_fiori': (3996, 1205, 4392, 1761), '5_fiori': (3996, 1865, 4392, 2421), '4_fiori': (3996, 2525, 4392, 3081), '3_fiori': (3996, 3185, 4392, 3741), '2_fiori': (3996, 3845, 4392, 4401), 'A_fiori': (2043, 545, 2439, 1101)}, 
'None': {'Jolly@_None': (2043, 3185, 2439, 3741), 'Back_None': (2043, 3845, 2439, 4401)}
}
