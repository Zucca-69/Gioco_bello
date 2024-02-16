class Enemy:
    def __init__(self,card):
        self.__healt=0
        self.__attack=0
        self.__card=card

    def stats(self):
        if self.__card[0][0]=="K":
            self.__healt=40
            self.__attack=20
        elif self.__card[0][0]=="Q":
            self.__healt=30
            self.__attack=15
        elif self.__card[0][0]=="J":
            self.__healt=20
            self.__attack=10
        return self.__healt, self.__attack