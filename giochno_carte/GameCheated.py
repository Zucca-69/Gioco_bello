from Mazzo import *
from Player import *
from Enemy import *

from FrameGioco import *

class Game:
    def __init__(self, n_giocatori):
        self.__n_giocatori = n_giocatori
        self.__giocatori = []
        self.__current_player_index = 0
        self.__player_cards = []
        self.__enemy_card = None

        self.__setup_game()

        self.__gui = GameUI(self.__nemico.getEnemyCard()[0])
        self.__gui.add_game_instance(self)

    def cambio_turno(self):
        if self.__current_player_index + 1 == self.__n_giocatori:
            self.__current_player_index = 0
        self.__animale = True
        self.__lista_giocate = []
        self.__tot = 0

    def get_player_cards(self):
        return self.__player_cards

    def get_enemy_card(self):
        return self.__enemy_card

    def got_card(self, card):
        if card[0]=="A" and self.__animale: # se la prima carta è un animale
            self.__gui.update_player_showed_cards()

    def rinuncia_turno(self):
        # se rinuncio il turno
        if len(self.__lista_giocate) == 0: # e non ho giocato carte
            self.cambio_turno() # tocca al prossimo
        else: 
            attacca_nemico()

    def attacca_nemico(self):
        pass 

    def __setup_game(self):
        #creo gli scarti
        self.__scarti=Mazzo()

        #creo il mazzo nemico
        self.__castello=Mazzo()
        for seme in ["picche","fiori","quadri","cuori"]:
            self.__castello.addCard("K", seme)
            self.__castello.addCard("J", seme)
            self.__castello.addCard("Q", seme)
        self.__castello.shuffle()

        # pesco nemico 
        self.__nemico= Enemy()
        self.__nemico.addStats(self.__castello.pickCard())

        #creo il mazzo da cui pescare
        self.__taverna=Mazzo()
        for seme in ["picche","cuori","fiori","quadri"]:
            self.__taverna.addCard("A", seme)
            for numero in range(2,11):
                self.__taverna.addCard(str(numero), seme)

        #condizioni di gioco
        self.__re= 4
        self.__continua=True
        
    
    def creaGiocatori(self):
        # istanzio i giocatori e creo la lista giocatori 
        player_0 = Player() 
        player_1 = Player()
        player_2 = Player()
        player_3 = Player()

        giocatori = [player_0, player_1, player_2, player_3]
        self.__giocatori = giocatori[:self.__n_giocatori]
        
        # calcolo num max delle carte in mano e aggiungo eventuali jolly 
        numGiocatori = len(self.__giocatori)
        self.__numMaxCarte = 8
        i = 0
        while numGiocatori > 1:
            if numGiocatori > 2: 
                self.__taverna.addCard(f"Jolly{i}")
                i += 1
            numGiocatori -= 1
            self.__numMaxCarte -= 1

        # mescolo il mazzo
        self.__taverna.shuffle()
        
        # imposto val num max carte e faccio pescare i vari giocatori
        for giocatore in giocatori:
            giocatore.setMaxCarte(self.__numMaxCarte)

        for _ in range(self.__numMaxCarte):
            for i in giocatori:
                i.draw(self.__taverna.pickCard())

giocata = Game(2)