import tkinter as tk
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = tk.Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = tk.Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Load the original image
original_img = Image.open("C:\\Users\\Classe 4BI\\Desktop\\benini\\giochino\\Gioco_bello\\giochno_carte\\imm\\OIUGSZ0.jpg")

# Define the region you want to display (left, top, right, bottom)
# Adjust these values as needed to show the desired part of the image
crop_region = (500, 500, 1000, 1000)  # Example values

# Crop the image
cropped_img = original_img.crop(crop_region)

# Create an object of tkinter ImageTk from the cropped image
img = ImageTk.PhotoImage(cropped_img)

# Create a Label Widget to display the cropped image
label = tk.Label(frame, image=img)
label.pack()

win.mainloop()
