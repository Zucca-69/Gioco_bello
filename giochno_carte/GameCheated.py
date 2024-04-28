from Mazzo import *
from Player import *
from Enemy import *

from FrameGioco import *

class Game:
    def __init__(self, n_giocatori):
        self.__n_giocatori = n_giocatori
        self.__giocatori = []
        self.__current_player_index = n_giocatori - 1
        self.__player_cards = []
        self.__lista_giocate = []
        self.__enemy_card = None
        self.__nemico= Enemy()

        self.__setup_game()

        self.__gui = GameUI(self.__nemico.getEnemyCard()[0])
        self.__gui.add_game_instance(self)

        self.cambio_turno() # faccio partire il primo giocatore

        self.__gui.add_player_hand(self.__player_cards)

    def cambio_turno(self):
        if self.__current_player_index + 1 == self.__n_giocatori:
            self.__current_player_index = 0
        self.__player_cards = self.__giocatori[self.__current_player_index].seeHand()
        self.__gui.add_player_hand(self.__player_cards)

        # da togliere (per verificare carte)
        print(self.__player_cards)
        
        self.__animale = True
        self.__lista_giocate = []
        self.__tot = 0

        self.__gui.master.mainloop()
        exit() # una volta chiusa la schermata termino l'esecuzione di tutto

    def get_player_cards(self):
        return self.__player_cards

    def get_enemy_card(self):
        return self.__enemy_card

    def got_card(self, card):
        if card in self.__player_cards:
            self.__player_cards.remove(card)
            self.__giocatori[self.__current_player_index].selectCard(card)
            self.__lista_giocate.append(card)

            self.__gui.update_player_showed_cards(self.__giocatori[self.__current_player_index].seeHand())


        if card[0]=="A" and self.__animale: # se la prima carta è un animale
            pass

    def rinuncia_turno(self):
        # se rinuncio il turno
        if len(self.__lista_giocate) != 0: # e non ho giocato carte
            self.attacca_nemico()
        self.cambio_turno() # tocca al prossimo

    def attacca_nemico(self):
        self.__gui.update_card(self.__gui.get_enemy_frame(), self.draw_new_enemy_card()[0])
    
    def draw_new_enemy_card(self):
        # pesco nemico 
        self.__nemico.addStats(self.__castello.pickCard())
        return self.__nemico.getEnemyCard()

    def __setup_game(self):
        #creo gli scarti
        self.__scarti=Mazzo()

        #creo il mazzo nemico
        self.__castello=Mazzo()
        for seme in ["picche","fiori","quadri","cuori"]:
            self.__castello.addCard("K", seme)
            self.__castello.addCard("Q", seme)
            self.__castello.addCard("J", seme)
        self.__castello.shuffle()

        self.draw_new_enemy_card()

        #creo il mazzo da cui pescare
        self.__taverna=Mazzo()
        for seme in ["picche","cuori","fiori","quadri"]:
            self.__taverna.addCard("A", seme)
            for numero in range(2,11):
                self.__taverna.addCard(str(numero), seme)
            
        self.creaGiocatori()

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

giocata = Game(1)
