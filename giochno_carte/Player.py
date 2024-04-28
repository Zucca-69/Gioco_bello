class Player:
    def __init__(self, numMaxCarte=0):
        self.__hand= []
        self.__defence= 0
        self.__immunità = False
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
            if card == i[0]:
                self.__hand.remove(i)
                return card
        return False

    def setMaxCarte(self, maxCarte):
        self.__numMaxCarte= maxCarte

    def __traduci_simbolo(self, simbolo):
        #taduzione dei simboli in valori interi
        if simbolo.isalnum():
            if simbolo == "A":
                simbolo = 1
            elif simbolo == "J":
                simbolo = 10
            elif simbolo == "Q":
                simbolo = 15
            elif simbolo == "K":
                simbolo = 20 
            elif simbolo[:5] == "Jolly":
                simbolo = 0
        return int(simbolo)

    #card : list of played card(dictionary)
    def calcolo(self, lista_carte, enemy):
        #calcolo -> danno + effetti (se attivi)
        
        danno = 0
        effetti = []

        for pos_carta in range(len(lista_carte)):
            carta = lista_carte[pos_carta].split("_")
            # calcolo totale
            danno += self.__traduci_simbolo(str(carta[0]))

            # effetti
            if carta[1] != enemy.getStats()["seme"] and carta[1] not in effetti:
                effetti.append(carta[1])

        # applico effetti personali
        if "fiori" in effetti:
            danno = danno * 2
        if "picche" in effetti:
            self.__defence += danno
        if "None" in effetti:
            enemy.modSeme(None)
            self.__immunità = True

        return danno, effetti
    
    def subisciDanno(self,danno): # attacco del nemico
        danno = danno - self.__defence

        # a seguito di un jolly        
        if self.__immunità == True:
            danno = 0

        # ciclo per la difesa 
        while danno > 0 and len(self.__hand) > 0: # ciclo per la difesa
            print(f"\ndanno da difendere: {danno}")
            print(self.seeHand())
            difesa = input("scegli una carta per difenderti: ")
            validità_difesa = self.selectCard(difesa)
            
            if validità_difesa != False:
                difesa = difesa.split("_")
                difesa = self.__traduci_simbolo(str(difesa[0]))
                danno -= difesa #calcolo effettivo
            else: 
                print("input non vaolido\n")
    
        if danno > 0: #verifica se è riuscito a difendere
            return False #morto
        return True #si continua
        
    def defenceReset(self):
        self.__defence= 0

    def getDifesa(self):
        return self.__defence