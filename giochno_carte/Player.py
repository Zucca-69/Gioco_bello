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
            if card == i[0]:
                self.__hand.remove(i)
                return card
        return False

    def setMaxCarte(self, maxCarte):
        self.__numMaxCarte= maxCarte

    def __traduci_simbolo(self, simbolo):
        #taduzione dei simboli in valori interi
        if simbolo.isalpha():
            if simbolo == "A":
                valore = 1
            elif simbolo == "J":
                valore = 10
            elif simbolo == "Q":
                valore = 15
            elif simbolo == "K":
                valore = 20 
            elif simbolo == "Jolly":
                valore = 0
        else: 
            valore = int(valore)
        return valore

    #card : list of played card(dictionary)
    def calcolo(self, lista_carte, enemy):
        #calcolo -> danno + effetti (se attivi)
        
        danno = 0
        effetti = []

        for pos_carta in range(len(lista_carte)):
            carta = lista_carte[pos_carta].split("_")
            # calcolo totale
            danno += self.__traduci_simbolo(carta[0])


            # effetti
            if len(carta) == 1: # jolly
                enemy.modSeme(None)
            elif len(carta) == 2: # carta normale
                if carta[1] not in effetti:
                    effetti.append(carta[1])

        return danno, effetti
    
    def subisciDanno(self,danno): # attacco del nemico
        danno=danno-self.__defence

        while danno > 0 and len(self.__hand) > 0: # ciclo per la difesa
            print(f"\ndanno da difendere: {danno}")
            print(self.seeHand())
            difesa = input("scegli una carta per difenderti: ")
            validità_difesa = self.selectCard(difesa)
            if validità_difesa != False:
                difesa = self.__traduci_simbolo()
                danno -= difesa #calcolo effettivo
            else: 
                print("input non vaolido\n")
    
        if danno > 0: #verifica se è riuscito a difendere
            return False #morto
        return True #si continua
    
    def defenceReset(self):
        self.__defence= 0