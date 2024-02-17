
class Player:
    def __init__(self, numMaxCarte=0):
        self.__hand= []
        self.__defence= 0
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
    
    def selectCard(self,card):
        for i in self.__hand:
            if card in i[0]:
                self.__hand.remove(i)
                return card

    def setMaxCarte(self,maxCarte):
        self.__numMaxCarte= maxCarte

    #card : list of played card(dictionary)
    def calcolo(self,card,enemy):
        #calcolo -> danno + effetti (se attivi)
        card_values= card.split("_")
        if card_values[0] == "A":
            damage= 1 
        elif card_values[0] == "Jolly":
            damage= 0
        else:
            damage= int(card_values[0])
        stato=None

        if card_values[1] != enemy.getStats()["seme"]:
            if card_values[1] == "cuori":
                stato="cuori"
            elif card_values[1] == "quadri":
                stato="quadri"
            elif card_values[1] == "picche":
                self.__defence += damage
            elif card_values[1] == "fiori":
                damage= damage * 2
            #effetto del Jolly
            elif card_values[1] == None:
                enemy.modSeme(None)
        return damage,stato