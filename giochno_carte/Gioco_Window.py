import tkinter as tk
from PIL import ImageTk, Image
import os

# Load the original image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")
global original_img
original_img = Image.open(image_path)

def show_card(card_coordinates):
    # Create an instance of tkinter window
    win = tk.Tk()

    # Define the geometry of the window
    win.geometry("700x600")
    win.configure(bg="#106040")

    frame = tk.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Define the region you want to display (left, top, right, bottom)
    # Adjust these values as needed to show the desired part of the image
    left, top = card_coordinates[0], card_coordinates[1]
    carta = (left, top, left + 410, top + 570)
    crop_region = carta 

    # Crop the image
    cropped_img = original_img.crop(crop_region)

    # Create an object of tkinter ImageTk from the cropped image
    img = ImageTk.PhotoImage(cropped_img)

    # Create a Label Widget to display the cropped image
    label = tk.Label(frame, image=img, bd = 0)
    label.pack()

    win.mainloop()

# -------
cards = {}

top = 545
for simbolo in ["K_", "Q_", "J_", "10_", "9_", "8_"]:
    left = 90
    for seme in ["quadri", "picche", "cuori", "fiori"]:
        cards[simbolo + seme] = (left, top, left + 396, top + 556)
        left += 492
    top += 660

top = 545
left -= 15
for carta in ["A_fiori", "A_cuori", "A_picche", "A_quadri", "Jolly@_None", "Back_None"]:
    cards[carta] = (left, top, left + 396, top + 556)
    top += 660

test = []
top = 545
for simbolo in ["7_", "6_", "5_", "4_", "3_", "2_"]:
    left = 2520
    for seme in ["quadri", "picche", "cuori", "fiori"]:
        cards[simbolo + seme] = (left, top, left + 396, top + 556)
        test.append(simbolo + seme)
        left += 492
    top += 660

# ------
print(cards)

for carta in test:
    print(carta)
    show_card(cards[carta])