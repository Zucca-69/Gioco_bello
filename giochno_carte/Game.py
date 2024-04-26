from Mazzo import *
from Player import *
from Enemy import *

from FrameGioco import *

class Game: 
    def __init__(self, nGiocatori):
        self.__nGiocatori = nGiocatori
        self.root = tk.Tk()
        self.gui = gui.GUI(self.root, self.process_choices)
        self.root.mainloop()

        self.__scarti = Mazzo()
        self.__castello = Mazzo()
        self.__taverna = Mazzo()
        self.__nemico = Enemy()
        self.__re = 4
        self.__continua = True
        self.creaGiocatori()

    def creaGiocatori(self):
        ferpetti = Player() 
        zucchetto = Player()
        pagliaccio = Player()
        moketto = Player()
        giocatori = [ferpetti, zucchetto, pagliaccio, moketto]
        giocatori = giocatori[:self.__nGiocatori]
        
        self.__giocatori = giocatori
        numGiocatori = len(giocatori)
        self.__numMaxCarte = 8
        i = 0
        while numGiocatori > 1:
            if numGiocatori > 2: 
                self.__taverna.addCard(f"Jolly{i}")
                i += 1
            numGiocatori -= 1
            self.__numMaxCarte -= 1
        self.__taverna.shuffle()
        
        for giocatore in giocatori:
            giocatore.setMaxCarte(self.__numMaxCarte)
        
        self.__taverna.shuffle() 

        for _ in range(self.__numMaxCarte):
            for i in giocatori:
                i.draw(self.__taverna.pickCard())
        
    def effetti(self, att):
        for effetto in att[1]:
            if effetto == "cuori":
                self.__scarti.shuffle()
                for _ in range(att[0]):
                    if len(self.__scarti.seeDeck()) > 0:
                        carta_pescata = self.__scarti.pickCard()[0].split("_")
                        self.__taverna.addCard(carta_pescata[1], carta_pescata[0])
                    else:
                        break
            elif effetto == "quadri":
                pesca = True
                count = 0
                while count < att[0] and pesca:
                    pesca = False
                    for i in self.__giocatori:
                        if len(i.seeHand()) < self.__numMaxCarte:
                            i.draw(self.__taverna.pickCard())
                            pesca = True
                            count += 1
    
    def add_carte_giocate(self, lista_giocate):
        for carta in lista_giocate:
            print(carta)

    def process_choices(self, choices):
        # Implementa qui la logica per elaborare le scelte dell'interfaccia grafica
        pass

    def run_game(self):
        nemico = Enemy()
        nemico.addStats(castello.pickCard())

        re = 4
        continua = True

        while re > 0 and continua:
            for giocatore in giocatori:
                # Aggiungi qui l'interfaccia grafica per visualizzare il turno e interagire con le carte
                pass