
class Player:
    def __init__(self, numMaxCarte):
        self.__hand=[]
        self.__defence=[]
        self.__numMaxCarte= numMaxCarte

    def draw(self,card):
        if len(self.__hand) < self.__numMaxCarte:
           self.__hand.append(card)
           return True
        return False

    def seeHand(self):
        return self.__hand
    
    def selectCard(self,card):
        if card in self.__hand:
            self.__hand.pop(card)
            return card

    #cards : list of played cards(dictionary)
    def calcolo(self,cards,enemy):
        danno= 0
        if cards.values() != enemy.values():
            if cards.values() == "cuori":
                pass
            elif cards.values() == "quadri":
                pass
            elif cards.values() == "picche":
                self.__defence += danno
            elif cards.values() == "fiori":
                danno= danno * 2
        return danno
    