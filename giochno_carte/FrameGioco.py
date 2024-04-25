import tkinter as tk
from PIL import ImageTk, Image
import os

class FrameGioco():
    def __init__(self, coordinate_carte):
        self.__coordinate_carte = coordinate_carte
        self.__mano = []

        # Load the original image
        self.__current_dir = os.path.dirname(__file__)
        self.__image_path = os.path.join(self.__current_dir, "imm", "OIUGSZ0.jpg")

        try:
            self.__original_img = Image.open(self.__image_path)
        except Exception as e:
            print("Errore durante il caricamento dell'immagine:", e)

        self.__root = tk.Tk()

        self.__frame_castello = self.create_frame(anchor = 'center', relx=0.5, rely=0.5)
        self.show_card(self.__frame_castello, "Q_cuori") # nemico.getEnemyCard()[0]

        self.__player_hand = []


        self.__root.mainloop()

    def richiediMano(self, mano):
        self.__mano = mano 
        self.__frame_mano = self.create_frame(anchor= tk.S, relx=0.5, rely=0.8)
        self.show_hand(self.__player_hand)

    def create_frame(self, anchor, relx, rely):
        frame = tk.Frame(self.__root, width = 450, height = 300, bg = "#106040")
        frame.pack()
        frame.place(anchor = anchor, relx = relx, rely = rely)
        return frame

    def show_card(self, frame, card):
        card_coordinates = coordinate_carte[card.split("_")[1]][card]

        left, top = card_coordinates[0], card_coordinates[1]
        crop_region = (left, top, left + 410, top + 570) # (left, top, right, bottom)

        try:
            # crop dell'immagine
            cropped_img = original_img.crop(crop_region)

            # resizing dell'immagine croppata
            cropped_img = cropped_img.resize((142, 200), Image.BICUBIC)
            img = ImageTk.PhotoImage(cropped_img)

            # mostro l'immagine tramite una label
            label = tk.Label(frame, image=img, bd=0)
            label.image = img 
            label.pack()
        
            # bind tra click sulla carta e azione
            label.bind("<Button-1>", lambda event: card_clicked(event, card))

        except Exception as e:
            print("Errore durante la visualizzazione dell'immagine:", e)    

    def show_hand(self):
        nCarte = len(self.__player_hand)
        inizio = [0, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15][nCarte]
        
        # tolgo le carte già presenti
        for widget in self.__frame_mano.winfo_children():
            widget.destroy()
        
        # carico le nuove carte 
        for carta in self.__mano:
            self.show_card(self.__frame_mano, carta)

coordinate_carte = {
'quadri': {'K_quadri': (90, 545, 486, 1101), 'Q_quadri': (90, 1205, 486, 1761), 'J_quadri': (90, 1865, 486, 2421), '10_quadri': (90, 2525, 486, 3081), '9_quadri': (90, 3185, 486, 3741), '8_quadri': (90, 3845, 486, 4401), '7_quadri': (2520, 545, 2916, 1101), '6_quadri': (2520, 1205, 2916, 1761), '5_quadri': (2520, 1865, 2916, 2421), '4_quadri': (2520, 2525, 2916, 3081), '3_quadri': (2520, 3185, 2916, 3741), '2_quadri': (2520, 3845, 2916, 4401), 'A_quadri': (2043, 2525, 2439, 3081)}, 
'picche': {'K_picche': (582, 545, 978, 1101), 'Q_picche': (582, 1205, 978, 1761), 'J_picche': (582, 1865, 978, 2421), '10_picche': (582, 2525, 978, 3081), '9_picche': (582, 3185, 978, 3741), '8_picche': (582, 3845, 978, 4401), '7_picche': (3012, 545, 3408, 1101), '6_picche': (3012, 1205, 3408, 1761), '5_picche': (3012, 1865, 3408, 2421), '4_picche': (3012, 2525, 3408, 3081), '3_picche': (3012, 3185, 3408, 3741), '2_picche': (3012, 3845, 3408, 4401), 'A_picche': (2043, 1865, 2439, 2421)}, 
'cuori': {'K_cuori': (1074, 545, 1470, 1101), 'Q_cuori': (1074, 1205, 1470, 1761), 'J_cuori': (1074, 1865, 1470, 2421), '10_cuori': (1074, 2525, 1470, 3081), '9_cuori': (1074, 3185, 1470, 3741), '8_cuori': (1074, 3845, 1470, 4401), '7_cuori': (3504, 545, 3900, 1101), '6_cuori': (3504, 1205, 3900, 1761), '5_cuori': (3504, 1865, 3900, 2421), '4_cuori': (3504, 2525, 3900, 3081), '3_cuori': (3504, 3185, 3900, 3741), '2_cuori': (3504, 3845, 3900, 4401), 'A_cuori': (2043, 1205, 2439, 1761)}, 
'fiori': {'K_fiori': (1566, 545, 1962, 1101), 'Q_fiori': (1566, 1205, 1962, 1761), 'J_fiori': (1566, 1865, 1962, 2421), '10_fiori': (1566, 2525, 1962, 3081), '9_fiori': (1566, 3185, 1962, 3741), '8_fiori': (1566, 3845, 1962, 4401), '7_fiori': (3996, 545, 4392, 1101), '6_fiori': (3996, 1205, 4392, 1761), '5_fiori': (3996, 1865, 4392, 2421), '4_fiori': (3996, 2525, 4392, 3081), '3_fiori': (3996, 3185, 4392, 3741), '2_fiori': (3996, 3845, 4392, 4401), 'A_fiori': (2043, 545, 2439, 1101)}, 
'None': {'Jolly@_None': (2043, 3185, 2439, 3741), 'Back_None': (2043, 3845, 2439, 4401)}}

mano = ['10_quadri', '9_quadri', '8_quadri', '7_quadri', '6_quadri', '5_quadri', '4_quadri', '3_quadri']

gioco = FrameGioco(coordinate_carte)
gioco.richiediMano(mano)