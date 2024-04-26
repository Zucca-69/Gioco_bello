import tkinter as tk
from PIL import ImageTk, Image
import os

from Main import *

# Load the original image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")

global original_img
try:
    original_img = Image.open(image_path)
except Exception as e:
    print("Errore durante il caricamento dell'immagine:", e)

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Regicide - partita in corso")
        self.master.geometry("1000x600")
        self.master.configure(bg="#106040")
        self.master.minsize(1100, 600)
        
        # Frame per le carte del giocatore
        self.player_frame = tk.Frame(self.master)
        self.player_frame.pack(side=tk.BOTTOM, pady = 20)
        
        # definisco il gioco a cui mi riferisco
        self.gioco = Game(1)

        # carte da mostrare
        self.card_castello = self.gioco.getEnemy().getEnemyCard()
        self.player_cards = []

        frame_castello = tk.Frame(self.master, width=450, height=300, bg="#106040")
        frame_castello.pack()
        frame_castello.place(anchor='center', relx=0.5, rely=0.35)
        self.show_card(frame_castello, self.card_castello)
        
        # Mostra le carte del giocatore
        self.show_player_cards()

        # Bottone per la rinuncia del turno
        self.button_rinuncia = tk.Button(self.master, text="Rinuncia", command=self.rinuncia_turno)
        self.button_rinuncia.place(relx=0.97, rely=0.97, anchor='se')

    def rinuncia_turno(self):
        self.gioco.rinuncia(True)
    
    def card_clicked(self, event, card):
        self.gioco.action_done(card)

    def show_player_cards(self):
        for card in self.player_cards:
            frame = tk.Frame(self.player_frame)
            frame.pack(side=tk.LEFT)
            self.show_card(frame, card)

    def update_player_showed_cards(self, new_cards):
        # Rimuove le vecchie carte
        for widget in self.player_frame.winfo_children():
            widget.destroy()

        # Aggiunge le nuove carte
        self.player_cards = new_cards
        self.show_player_cards()

    def update_mano_player(mano):
        self.player_cards = mano
        self.update_player_showed_cards()

    def show_card(self, frame, card):
        card_coordinates = coordinate_carte[card.split("_")[1]][card]
        # Define the region you want to display (left, top, right, bottom)
        # Adjust these values as needed to show the desired part of the image
        left, top = card_coordinates[0], card_coordinates[1]
        carta = (left, top, left + 410, top + 570)
        crop_region = carta 

        try:
            # Crop the image
            cropped_img = original_img.crop(crop_region)

            # Resize the cropped image to fit the frame
            cropped_img = cropped_img.resize((142, 200), Image.BICUBIC)

            # Create an object of tkinter ImageTk from the cropped image
            img = ImageTk.PhotoImage(cropped_img)

            # Create a Label Widget to display the cropped image
            label = tk.Label(frame, image=img, bd=0)
            label.image = img  # Save a reference to the image to prevent garbage collection
            label.pack()
        
            # Bind the card click event to a function
            label.bind("<Button-1>", lambda event: self.card_clicked(event, card))

        except Exception as e:
            print("Errore durante la visualizzazione dell'immagine:", e)    

    def get_card_image(self, card):
        # Ottieni le coordinate della carta
        card_coordinates = coordinate_carte[card.split("_")[1]][card]
        # Definisci la regione da ritagliare
        left, top = card_coordinates[0], card_coordinates[1]
        carta = (left, top, left + 410, top + 570)
        # Ritaglia l'immagine originale
        cropped_img = original_img.crop(carta)
        # Ridimensiona l'immagine
        cropped_img = cropped_img.resize((142, 200), Image.BICUBIC)
        # Crea un oggetto ImageTk da mostrare sul pulsante
        card_img = ImageTk.PhotoImage(cropped_img)
        return card_img

coordinate_carte = {
    'quadri': {'K_quadri': (90, 545), 'Q_quadri': (90, 1205), 'J_quadri': (90, 1865), '10_quadri': (90, 2525), '9_quadri': (90, 3185), '8_quadri': (90, 3845), '7_quadri': (2520, 545), '6_quadri': (2520, 1205), '5_quadri': (2520, 1865), '4_quadri': (2520, 2525), '3_quadri': (2520, 3185), '2_quadri': (2520, 3845), 'A_quadri': (2043, 2525)}, 
    'picche': {'K_picche': (582, 545), 'Q_picche': (582, 1205), 'J_picche': (582, 1865), '10_picche': (582, 2525), '9_picche': (582, 3185), '8_picche': (582, 3845), '7_picche': (3012, 545), '6_picche': (3012, 1205), '5_picche': (3012, 1865), '4_picche': (3012, 2525), '3_picche': (3012, 3185), '2_picche': (3012, 3845), 'A_picche': (2043, 1865)}, 
    'cuori': {'K_cuori': (1074, 545), 'Q_cuori': (1074, 1205), 'J_cuori': (1074, 1865), '10_cuori': (1074, 2525), '9_cuori': (1074, 3185), '8_cuori': (1074, 3845), '7_cuori': (3504, 545), '6_cuori': (3504, 1205), '5_cuori': (3504, 1865), '4_cuori': (3504, 2525), '3_cuori': (3504, 3185), '2_cuori': (3504, 3845), 'A_cuori': (2043, 1205)}, 
    'fiori': {'K_fiori': (1566, 545), 'Q_fiori': (1566, 1205), 'J_fiori': (1566, 1865), '10_fiori': (1566, 2525), '9_fiori': (1566, 3185), '8_fiori': (1566, 3845), '7_fiori': (3996, 545), '6_fiori': (3996, 1205), '5_fiori': (3996, 1865), '4_fiori': (3996, 2525), '3_fiori': (3996, 3185), '2_fiori': (3996, 3845), 'A_fiori': (2043, 545)}, 
    'None': {'Jolly@_None': (2043, 3185), 'Back_None': (2043, 3845)}
}

def main():
    root = tk.Tk()
    game_ui = GameUI(root)
    # game_ui.update_player_showed_cards(["K_quadri"])
    root.mainloop()
'''
if __name__ == "__main__":
    main()
'''
root = tk.Tk()
Schermata = GameUI(root)

giocata = Game(1)