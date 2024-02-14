
class Player:
    def __init__(self):
        self.__hand=[]
        self.__defence=[]

    def draw(self,card):
        self.__hand.append(card)

    def seeHand(self):
        return self.__hand
    
    def selectCard(self,card):
        if card in self.__hand:
            self.__hand.pop(card)
            return card

    #cards : list of played cards(dictionary)
    def calcolo(self,cards,enemy):
        if cards.values()== "cuori" and enemy.values()!="cuori":
            pass