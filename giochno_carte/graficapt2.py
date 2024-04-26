import tkinter as tk
import random

class RegicideGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Regicide")

        self.player_frame = tk.Frame(self.master)
        self.player_frame.pack()

        self.enemy_frame = tk.Frame(self.master)
        self.enemy_frame.pack()

        self.create_widgets()

        # Inizializzazione del gioco
        self.init_game()

    def create_widgets(self):
        # Frame per le carte del giocatore
        self.player_label = tk.Label(self.player_frame, text="Carte del Giocatore")
        self.player_label.pack()

        self.player_cards = tk.Listbox(self.player_frame, selectmode=tk.SINGLE)
        self.player_cards.pack()

        # Frame per le statistiche del nemico
        self.enemy_label = tk.Label(self.enemy_frame, text="Statistiche del Nemico")
        self.enemy_label.pack()

        self.enemy_stats = tk.Label(self.enemy_frame, text="Salute: ?  Attacco: ?  Seme: ?")
        self.enemy_stats.pack()

        # Pulsante per giocare una carta
        self.play_button = tk.Button(self.master, text="Gioca Carta", command=self.play_card)
        self.play_button.pack()

    def init_game(self):
        # Inizializzazione delle carte del giocatore
        self.player_hand = []
        for _ in range(5):  # Ad esempio, peschiamo 5 carte iniziali
            card = self.pick_random_card()
            self.player_hand.append(card)
            self.player_cards.insert(tk.END, card)

        # Inizializzazione delle statistiche del nemico
        self.enemy_stats_data = {"health": 30, "attack": 15, "seme": "????"}
        self.update_enemy_stats()

    def update_enemy_stats(self):
        self.enemy_stats.config(text=f"Salute: {self.enemy_stats_data['health']}  Attacco: {self.enemy_stats_data['attack']}  Seme: {self.enemy_stats_data['seme']}")

    def pick_random_card(self):
        numeri = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        semi = ["picche", "fiori", "quadri", "cuori"]
        return f"{random.choice(numeri)}_{random.choice(semi)}"

    def play_card(self):
        selected_index = self.player_cards.curselection()
        if selected_index:  # Verifica se è stata selezionata una carta
            selected_card = self.player_hand.pop(selected_index[0])
            self.player_cards.delete(selected_index)
            # Logica per giocare la carta selezionata
            carta_giocata = selected_card.split("_")
            # Aggiornamento delle statistiche del nemico in base alla carta giocata
            if carta_giocata[1] != self.enemy_stats_data["seme"]:
                self.enemy_stats_data["seme"] = carta_giocata[1]
            # Da implementare: Logica per calcolare il danno e aggiornare le statistiche del nemico
            # Aggiornamento dell'interfaccia
            self.update_enemy_stats()
            print("Hai giocato la carta:", selected_card)

def main():
    root = tk.Tk()
    app = RegicideGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
