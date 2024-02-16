import random

class Mazzo:
    def __init__(self):
        self.__deck={}
        self.__semi=("picche","fiori","quadri","cuori", None)

    def addCard(self,numero, seme = None):
        if type(numero) == str:
            if seme in self.__semi:
                chiave_carta = f"{numero}_{seme}"
                self.__deck[chiave_carta] = seme
            return True
        return False
        
    def shuffle(self):
        # Estrai tutte le chiavi (carte) dal mazzo
        carte = list(self.__deck.keys())
        # Mischia le carte
        random.shuffle(carte)
        # Ricostruisci il mazzo con le carte mescolate
        self.__deck = {carta: self.__deck[carta] for carta in carte}

    def seeDeck(self):
        return self.__deck
    
    def pickCard(self):
        #è l'ultima carta ma dettagli, forse meglio così
        #card=tupla -> (chiave_carta, seme)
        card=self.__deck.popitem()
        return card