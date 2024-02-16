class Enemy:
    def __init__(self):
        self.__card= None
        self.__health=0
        self.__attack=0
        self.__seme= None

    def stats(self, card):
        self.__card= card
        if self.__card[0][0]=="K":
            self.__health=40
            self.__attack=20
        elif self.__card[0][0]=="Q":
            self.__health=30
            self.__attack=15
        elif self.__card[0][0]=="J":
            self.__health=20
            self.__attack=10
        self.__seme= card[1]

    #return tuple (sconfitto(bool) , conquistato(bool))
    def subisciDanno(self, danno):
        self.__health -= danno
        if self.__health <= 0:
            if self.__health == 0:
                return True, True
            return True, False
        return False, False

    #imposta nuovo seme quando viene giocato il jolly
    def modSeme(self, nuovo_seme):
        self.__seme= nuovo_seme

    def values(self): #ritorna le stat del nemico
        return {"health" : self.__health, "attack" : self.__attack, "seme" : self.__seme}

    def getEnemy(self):
        return card #ho un dubbio su cosa far ritornare