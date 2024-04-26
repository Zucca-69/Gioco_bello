from Mazzo import *
from Player import *
from Enemy import *

class Game:
    def __init__(self, n_giocatori):
        self.__n_giocatori = n_giocatori
        self.__giocatori = []
        self.__current_player_index = 0
        self.__player_cards = []
        self.__enemy_card = None

        self.__setup_game()

    def __setup_game(self):
        # Inizializza il gioco, crea i giocatori, distribuisce le carte, etc.
        pass

    def get_player_cards(self):
        return self.__player_cards

    def get_enemy_card(self):
        return self.__enemy_card

    def process_card(self, card):
        # Elabora la carta selezionata dal giocatore
        pass

    def rinuncia_turno(self):
        # Elabora la rinuncia al turno
        pass
