class Player:
    def __init__(self, numMaxCarte=0):
        self.__hand= []
        self.__defence= 0
        self.__numMaxCarte= numMaxCarte

    def draw(self, card):
        if len(self.__hand) < self.__numMaxCarte:
           self.__hand.append(card)
           return True
        return False

    def seeHand(self):
        output=[]
        for i in self.__hand:
            output.append(i[0])
        return output
    
    def selectCard(self, card):
        for i in self.__hand:
            if card in i[0]:
                self.__hand.remove(i)
                return card

    def setMaxCarte(self, maxCarte):
        self.__numMaxCarte= maxCarte

    #card : list of played card(dictionary)
    def calcolo(self, card, enemy):
        #calcolo -> danno + effetti (se attivi)
        #conteggio danno
        card_values= card.split("_")
        if card_values[0] == "A":
            damage= 1 
        elif card_values[0] == "Jolly":
            damage= 0
        else:
            damage= int(card_values[0])
        stato= None

        #attivazione effetti
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
    
    def subisciDanno(self,danno): # attacco del nemico
        danno=danno-self.__defence

        while danno > 0 and len(self.__hand) > 0: # ciclo per la difesa
            print(f"\ndanno da difendere: {danno}")
            print(self.seeHand())
            difesa = self.selectCard(input("scegli una carta per difenderti: ")[0])

            #taduzione dei simboli in valori per la difesa
            if difesa.isalpha():
                if difesa == "A":
                    difesa = 1
                elif difesa == "J":
                    difesa = 10
                elif difesa == "Q":
                    difesa = 15
                elif difesa == "K":
                    difesa = 20 
            if difesa == "1":
                difesa = 10
            danno -= int(difesa) #calcolo effettivo
        if danno > 0: #verifica se è riuscito a difendere
            return False #morto
        return True #si continua
    
    def defenceReset(self):
        self.__defence= 0