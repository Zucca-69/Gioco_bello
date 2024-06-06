import random

class Mazzo:
    def __init__(self):
        self.__deck = {}
        self.__semi = ("picche", "fiori", "quadri", "cuori", None)

    def addCard(self, numero, seme=None):
        if type(numero) == str:
            if seme in self.__semi:
                chiave_carta = f"{numero}_{seme}"
                self.__deck[chiave_carta] = seme
            return True
        return False

    def shuffle(self):
        carte = list(self.__deck.keys())
        random.shuffle(carte)
        self.__deck = {carta: self.__deck[carta] for carta in carte}

    def seeDeck(self):
        return self.__deck

    def pickCard(self, first=False):
        if first:
            # Estrai la prima carta se richiesto
            if self.__deck:
                carta, seme = next(iter(self.__deck.items()))
                del self.__deck[carta]
                return carta, seme
            else:
                return None, None
        else:
            # Estrai l'ultima carta come fatto precedentemente
            if self.__deck:
                carta, seme = self.__deck.popitem()
                return carta, seme
            else:
                return None, None
