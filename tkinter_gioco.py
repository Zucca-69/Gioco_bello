import tkinter as tk

def display_text():
    input_text = entry.get()
    label.config(text="Hai scritto: " + input_text)

# Creazione della finestra
root = tk.Tk()
root.config(bg= "darkgreen")
root.title("Input di testo Tkinter")

# Aggiunta di un input di testo
entry = tk.Entry(root)
entry.pack()

# Aggiunta di un pulsante per visualizzare il testo
button = tk.Button(root, text="Mostra testo", command=display_text)
button.pack()

# Aggiunta di una label per mostrare il risultato
label = tk.Label(root, text="")
label.pack()

# Esecuzione del loop principale della finestra
root.mainloop()
