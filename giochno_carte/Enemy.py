class Enemy():
    def __init__(self):
        self.__card = None # tuple(segno_seme, seme) es("J_cuori", "cuori")
        self.__health = 0
        self.__attack = 0
        self.__seme = None
        self.__carta = None 
        self.__semeOriginale = None

    def addStats(self, card):
        # legge la carta e assegna al nemico vita, attacco e seme
        #returns: None
        self.__card= card
        if self.__card[0][0] == "K":
            self.__health=40
            self.__attack=20
        elif self.__card[0][0] == "Q":
            self.__health=30
            self.__attack=15
        elif self.__card[0][0] == "J":
            self.__health=20
            self.__attack=10

        self.__seme= card[1]
        self.__semeOriginale = card[1]

    def subisciDanno(self, danno):
        # returns: list[sconfitto(bool), conquistato(bool)]
        self.__health -= int(danno)
        ret = [False, False]

        if self.__health <= 0: 
            ret[0] = True # ucciso
            # nel caso abbia usato un jolly, ripristino il seme
            self.__seme = self.__semeOriginale 
        if self.__health == 0:
            ret[1] = True # conquistato
        return ret

    # imposta nuovo seme quando viene giocato il jolly
    def modSeme(self, nuovo_seme):
        self.__seme = nuovo_seme

    def getStats(self): 
        # get a dict of the enemy's stats
        # returns: dict
        return {"health" : self.__health, "attack" : self.__attack, "seme" : self.__seme}

    def getEnemyCard(self):
        # returns: tuple (segno_seme, seme)
        return self.__card