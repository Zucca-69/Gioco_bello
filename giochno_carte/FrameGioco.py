import tkinter as tk
from PIL import ImageTk, Image
import os
from game_logic import Game

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")

global original_img
try:
    original_img = Image.open(image_path)
except Exception as e:
    print("Errore durante il caricamento dell'immagine:", e)

class GameUI:
    def __init__(self, master, game_instance):
        self.master = master
        self.__game = game_instance
        self.master.title("Regicide - partita in corso")
        self.master.geometry("1000x600")
        self.master.configure(bg="#106040")
        self.master.minsize(1100, 600)
        
        self.__player_frame = tk.Frame(self.master)
        self.__player_frame.pack(side=tk.BOTTOM, pady=20)

        self.__init_widgets()

    def __init_widgets(self):        
        self.__frame_castello = tk.Frame(self.master, width=450, height=300, bg="#106040")
        self.__frame_castello.pack()
        self.__frame_castello.place(anchor='center', relx=0.5, rely=0.35)
        self.__show_card(self.__frame_castello, self.__game.get_enemy_card())

        self.__show_player_cards()

        self.__button_rinuncia = tk.Button(self.master, text="Rinuncia", command=self.__rinuncia_turno)
        self.__button_rinuncia.place(relx=0.97, rely=0.97, anchor='se')

    def __show_player_cards(self):
        for card in self.__game.get_player_cards():
            frame = tk.Frame(self.__player_frame)
            frame.pack(side=tk.LEFT)
            self.__show_card(frame, card)

    def __card_clicked(self, card):
        self.__game.process_card(card)

    def __update_player_showed_cards(self, new_cards):
        for widget in self.__player_frame.winfo_children():
            widget.destroy()

        self.__show_player_cards()

    def __update_mano_player(self, mano):
        self.__update_player_showed_cards(mano)

    def __show_card(self, frame, card):
        card_coordinates = coordinate_carte[card.split("_")[1]][card]

        left, top = card_coordinates[0], card_coordinates[1]
        crop_region = (left, top, left + 410, top + 570)

        try:
            cropped_img = original_img.crop(crop_region)
            cropped_img = cropped_img.resize((142, 200), Image.BICUBIC)

            img = ImageTk.PhotoImage(cropped_img)

            button = tk.Button(frame, image=img, bd=0, command=lambda: self.__card_clicked(card))
            button.image = img
            button.pack()

        except Exception as e:
            print("Errore durante la visualizzazione dell'immagine:", e)    

    def __rinuncia_turno(self):
        self.__game.rinuncia_turno()

coordinate_carte = {
    'quadri': {'K_quadri': (90, 545), 'Q_quadri': (90, 1205), 'J_quadri': (90, 1865), '10_quadri': (90, 2525), '9_quadri': (90, 3185), '8_quadri': (90, 3845), '7_quadri': (2520, 545), '6_quadri': (2520, 1205), '5_quadri': (2520, 1865), '4_quadri': (2520, 2525), '3_quadri': (2520, 3185), '2_quadri': (2520, 3845), 'A_quadri': (2043, 2525)}, 
    'picche': {'K_picche': (582, 545), 'Q_picche': (582, 1205), 'J_picche': (582, 1865), '10_picche': (582, 2525), '9_picche': (582, 3185), '8_picche': (582, 3845), '7_picche': (3012, 545), '6_picche': (3012, 1205), '5_picche': (3012, 1865), '4_picche': (3012, 2525), '3_picche': (3012, 3185), '2_picche': (3012, 3845), 'A_picche': (2043, 1865)}, 
    'cuori': {'K_cuori': (1074, 545), 'Q_cuori': (1074, 1205), 'J_cuori': (1074, 1865), '10_cuori': (1074, 2525), '9_cuori': (1074, 3185), '8_cuori': (1074, 3845), '7_cuori': (3504, 545), '6_cuori': (3504, 1205), '5_cuori': (3504, 1865), '4_cuori': (3504, 2525), '3_cuori': (3504, 3185), '2_cuori': (3504, 3845), 'A_cuori': (2043, 1205)}, 
    'fiori': {'K_fiori': (1566, 545), 'Q_fiori': (1566, 1205), 'J_fiori': (1566, 1865), '10_fiori': (1566, 2525), '9_fiori': (1566, 3185), '8_fiori': (1566, 3845), '7_fiori': (3996, 545), '6_fiori': (3996, 1205), '5_fiori': (3996, 1865), '4_fiori': (3996, 2525), '3_fiori': (3996, 3185), '2_fiori': (3996, 3845), 'A_fiori': (2043, 545)}, 
    'None': {'Jolly@_None': (2043, 3185), 'Back_None': (2043, 3845)}
}
