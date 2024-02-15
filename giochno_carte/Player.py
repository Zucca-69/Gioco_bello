
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
        output=[]
        for i in self.__hand:
            output.append(i[0])
        return output
    
    #todo fai in modo che non chieda una tupla
    def selectCard(self,card):
        for i in self.__hand:
            if card in i[0]:
                self.__hand.remove(i)
                return card
        return "nuh uh"

    #cards : list of played cards(dictionary)
    def calcolo(self,cards,enemy):
        damage= 0
        if cards.values() != enemy.values():
            if cards.values() == "cuori":
                pass
            elif cards.values() == "quadri":
                pass
            elif cards.values() == "picche":
                self.__defence += damage
            elif cards.values() == "fiori":
                damage= damage * 2
        return damage
    