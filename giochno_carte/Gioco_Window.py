'''import tkinter as tk
from PIL import ImageTk, Image
import os

# Load the original image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")
global original_img
original_img = Image.open(image_path)

def create_frames(castello, taverna, scarto):
    # Create an instance of tkinter window
    global win
    win = tk.Tk()

    # Define the geometry of the window
    win.geometry("700x600")
    win.configure(bg="#106040")

    frame_castello = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_castello.pack()
    frame_castello.place(anchor='center', relx=0.3, rely=0.5)
    show_card(frame_castello, coordinate_carte[castello.split("_")[1]][castello])

    frame_taverna = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_taverna.pack()
    frame_taverna.place(anchor='center', relx=0.5, rely=0.5)
    show_card(frame_taverna, coordinate_carte[taverna.split("_")[1]][taverna])

    frame_scarti = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_scarti.pack()
    frame_scarti.place(anchor='center', relx=0.7, rely=0.5)
    show_card(frame_scarti, coordinate_carte[scarto.split("_")[1]][scarto])

    win.mainloop()

def show_card(frame, card_coordinates):
    # Define the region you want to display (left, top, right, bottom)
    # Adjust these values as needed to show the desired part of the image
    left, top = card_coordinates[0], card_coordinates[1]
    carta = (left, top, left + 410, top + 570)
    crop_region = carta 

    # Crop the image
    cropped_img = original_img.crop(crop_region)

    # Resize the cropped image to fit the frame
    cropped_img = cropped_img.resize((200, 300), Image.BICUBIC)

    # Create an object of tkinter ImageTk from the cropped image
    img = ImageTk.PhotoImage(cropped_img)

    # Create a Label Widget to display the cropped image
    label = tk.Label(frame, image=img, bd = 0)
    label.pack()
'''




import tkinter as tk
from PIL import ImageTk, Image
import os

# Load the original image
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "imm", "OIUGSZ0.jpg")

try:
    original_img = Image.open(image_path)
except Exception as e:
    print("Errore durante il caricamento dell'immagine:", e)

def create_frames(castello, taverna, scarto):
    # Create an instance of tkinter window
    win = tk.Tk()

    # Define the geometry of the window
    win.geometry("1000x600")
    win.configure(bg="#106040")
    win.minsize(1000, 600)

    frame_taverna = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_taverna.pack()
    frame_taverna.place(anchor='center', relx=0.2, rely=0.5)
    show_card(frame_taverna, taverna)

    frame_castello = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_castello.pack()
    frame_castello.place(anchor='center', relx=0.5, rely=0.5)
    show_card(frame_castello, castello)

    frame_scarti = tk.Frame(win, width=600, height=400, bg = "#106040")
    frame_scarti.pack()
    frame_scarti.place(anchor='center', relx=0.8, rely=0.5)
    show_card(frame_scarti, scarto)

    win.mainloop()

def show_card(frame, card):
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
        cropped_img = cropped_img.resize((200, 300), Image.BICUBIC)

        # Create an object of tkinter ImageTk from the cropped image
        img = ImageTk.PhotoImage(cropped_img)

        # Create a Label Widget to display the cropped image
        label = tk.Label(frame, image=img, bd=0)
        label.image = img  # Save a reference to the image to prevent garbage collection
        label.pack()
    
        # Bind the card click event to a function
        label.bind("<Button-1>", lambda event: card_clicked(event, card))

    except Exception as e:
        print("Errore durante la visualizzazione dell'immagine:", e)

def card_clicked(event, card):
    print("Carta cliccata:", card)





# -------
global coordinate_carte
coordinate_carte = {
'quadri': {'K_quadri': (90, 545, 486, 1101), 'Q_quadri': (90, 1205, 486, 1761), 'J_quadri': (90, 1865, 486, 2421), '10_quadri': (90, 2525, 486, 3081), '9_quadri': (90, 3185, 486, 3741), '8_quadri': (90, 3845, 486, 4401), '7_quadri': (2520, 545, 2916, 1101), '6_quadri': (2520, 1205, 2916, 1761), '5_quadri': (2520, 1865, 2916, 2421), '4_quadri': (2520, 2525, 2916, 3081), '3_quadri': (2520, 3185, 2916, 3741), '2_quadri': (2520, 3845, 2916, 4401), 'A_quadri': (2043, 2525, 2439, 3081)}, 
'picche': {'K_picche': (582, 545, 978, 1101), 'Q_picche': (582, 1205, 978, 1761), 'J_picche': (582, 1865, 978, 2421), '10_picche': (582, 2525, 978, 3081), '9_picche': (582, 3185, 978, 3741), '8_picche': (582, 3845, 978, 4401), '7_picche': (3012, 545, 3408, 1101), '6_picche': (3012, 1205, 3408, 1761), '5_picche': (3012, 1865, 3408, 2421), '4_picche': (3012, 2525, 3408, 3081), '3_picche': (3012, 3185, 3408, 3741), '2_picche': (3012, 3845, 3408, 4401), 'A_picche': (2043, 1865, 2439, 2421)}, 
'cuori': {'K_cuori': (1074, 545, 1470, 1101), 'Q_cuori': (1074, 1205, 1470, 1761), 'J_cuori': (1074, 1865, 1470, 2421), '10_cuori': (1074, 2525, 1470, 3081), '9_cuori': (1074, 3185, 1470, 3741), '8_cuori': (1074, 3845, 1470, 4401), '7_cuori': (3504, 545, 3900, 1101), '6_cuori': (3504, 1205, 3900, 1761), '5_cuori': (3504, 1865, 3900, 2421), '4_cuori': (3504, 2525, 3900, 3081), '3_cuori': (3504, 3185, 3900, 3741), '2_cuori': (3504, 3845, 3900, 4401), 'A_cuori': (2043, 1205, 2439, 1761)}, 
'fiori': {'K_fiori': (1566, 545, 1962, 1101), 'Q_fiori': (1566, 1205, 1962, 1761), 'J_fiori': (1566, 1865, 1962, 2421), '10_fiori': (1566, 2525, 1962, 3081), '9_fiori': (1566, 3185, 1962, 3741), '8_fiori': (1566, 3845, 1962, 4401), '7_fiori': (3996, 545, 4392, 1101), '6_fiori': (3996, 1205, 4392, 1761), '5_fiori': (3996, 1865, 4392, 2421), '4_fiori': (3996, 2525, 4392, 3081), '3_fiori': (3996, 3185, 4392, 3741), '2_fiori': (3996, 3845, 4392, 4401), 'A_fiori': (2043, 545, 2439, 1101)}, 
'None': {'Jolly@_None': (2043, 3185, 2439, 3741), 'Back_None': (2043, 3845, 2439, 4401)}}

create_frames("Q_cuori", "Back_None", "4_fiori")