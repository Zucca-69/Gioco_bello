from Mazzo import *
from Player import *
from Enemy import *

class Game: 
    def __init__(self, nGiocatori):     # preparazione del gioco
        self.__nGiocatori = nGiocatori
        
        #creo gli self.__scarti
        self.__scarti=Mazzo()

        #creo il mazzo nemico
        self.__castello=Mazzo()
        for seme in ["picche","fiori","quadri","cuori"]:
            self.__castello.addCard("K", seme)
            self.__castello.addCard("J", seme)
            self.__castello.addCard("Q", seme)
        self.__castello.shuffle()

        #creo il mazzo da cui pescare
        self.__taverna=Mazzo()
        for seme in ["picche","cuori","fiori","quadri"]:
            self.__taverna.addCard("A", seme)
            for numero in range(2,11):
                self.__taverna.addCard(str(numero), seme)

        #creo e pesco nemico
        self.__nemico= Enemy()
        self.__nemico.addStats(self.__castello.pickCard())

        #condizioni di gioco
        self.__re= 4
        self.__continua=True
        
        # chiama funzioni 
        self.creaGiocatori()
        self.gioco()

    def creaGiocatori(self):
        #creo giocatori
        ferpetti=Player() 
        zucchetto= Player()
        pagliaccio= Player()
        moketto = Player()
        giocatori= [ferpetti, zucchetto, pagliaccio, moketto]
        giocatori = giocatori[:self.__nGiocatori]
        
        self.__giocatori = []
        for giocatore in giocatori:
            self.__giocatori.append(giocatore)
            
        numGiocatori= len(giocatori)
        # idCount del server
        # impostare il limite giocatori da 1 a 4
        #imposto i jolly e il num massimo di carte per giocatore in base al num giocatori
        self.__numMaxCarte= 8
        i = 0
        while numGiocatori > 1:
            if numGiocatori > 2: 
                self.__taverna.addCard(f"Jolly{i}")
                i += 1
            numGiocatori-= 1
            self.__numMaxCarte-= 1
        self.__taverna.shuffle()
            
        #imposto maxcarte ai giocatori
        for giocatore in giocatori:
            giocatore.setMaxCarte(self.__numMaxCarte)

        #ogni giocatore pesca
        for _ in range(self.__numMaxCarte):
            for i in giocatori:
                i.draw(self.__taverna.pickCard())
        
        #lo shuffle va fatto dopo l'aggiunta di eventuali Jolly
        self.__taverna.shuffle() 

    def effetti(self, att):
        for effetto in att[1]:
            # effetti cuori
            if effetto == "cuori":
                self.__scarti.shuffle()
                for _ in range(att[0]): #ripeti n volte la pesca
                    if len(self.__scarti.seeDeck()) > 0: #non puoi prendere carte da un mazzo vuoto
                        carta_pescata= self.__scarti.pickCard()[0].split("_")
                        self.__taverna.addCard(carta_pescata[1],carta_pescata[0])
                    else:
                        break
            
            # effetti quadri
            elif effetto == "quadri":
                pesca= True
                count= 0
                while count < att[0] and pesca:
                    pesca=False
                    for i in self.__giocatori: # ogni giocatore pesca
                        if len(i.seeHand()) < self.__numMaxCarte: # a meno che non sia già full
                            i.draw(self.__taverna.pickCard())
                            pesca=True
                            count+=1
                        
    def gioco(self):
        #ciclo ci gioco
        while self.__re > 0 and self.__continua:
            for pos_giocatore in range(len(self.__giocatori)):
                giocatore = self.__giocatori[pos_giocatore]
                print(f"\n--- NUOVO TURNO ({pos_giocatore}) ---")
                print(self.__nemico.getEnemyCard()[0],self.__nemico.getStats())
                print(giocatore.seeHand())
                animale = True
                sconfittoNelTurno = False

                #chiedi per rinuncia
                rinuncia= input("vuoi rinunciare? (s/n): ")
                if rinuncia == "" or rinuncia[0].lower() != "s":
                    lista_giocate = []
                    tot = 0

                    #scegli la carta
                    card= giocatore.selectCard(input("scegli una carta: "))
                    lista_giocate.append(card)
                    
                    if card[0]=="A" and animale: # se la prima carta è un animale
                        #chiedi per rinuncia
                        card = input("vuoi giocare un altra carta? (s/n): ")
                        print(giocatore.seeHand())
                        if card == "" or card[0].lower() == "s":
                            animale = False
                            card= giocatore.selectCard(input("scegli una altra carta: "))
                            lista_giocate.append(card)                    

                    elif str(card[0]).isdigit() == True: # se la prima carta è normale
                        #gioca carte con lo stesso simbolo
                        if int(card[0]) >= 2 and int(card[0]) <= 5:
                            giocabili = []
                            for carta in giocatore.seeHand():
                                if carta[0] == str(card[0]):
                                    giocabili.append(carta)
                                    
                            vuoleGiocare = True
                            while tot + int(card[0]) <= 10 and len(giocabili) > 0 and vuoleGiocare:
                                print(giocabili)
                                #chiedi per rinuncia
                                rinuncia= input("vuoi rinunciare? (s/n): ")
                                if rinuncia == "" or rinuncia[0].lower() != "s":
                                    vuoleGiocare = True
                                    card= giocatore.selectCard(input("scegli una carta: "))
                                    lista_giocate.append(card)
                                    giocabili.remove(card)
                                    tot += int(card[0])
                                else:
                                    vuoleGiocare = False

                    # attacco al nemico
                    attacco = giocatore.calcolo(lista_giocate, self.__nemico)
                    self.effetti(attacco)
                    risultatoAttacco = self.__nemico.subisciDanno(attacco[0])

                    # se il nemico viene sconfitto nemico sconfitto
                    if  risultatoAttacco[0] == True: 

                        sconfittoNelTurno = True
                        print("nemico sconfitto")
                        # conquistato (?)  
                        if risultatoAttacco[1] == True: 
                            print("nemico conquistato")
                            self.__taverna.addCard(self.__nemico.getEnemyCard())
                        else: 
                            self.__scarti.addCard(self.__nemico.getEnemyCard())
                            
                        # se è un re, abbasso il counter
                        if self.__nemico.getStats()["attack"]==20: 
                            re-= 1
                        self.__nemico.addStats(self.__castello.pickCard())
                        
                        # azzero la difesa una volta finito lo scontro
                        for i in self.__giocatori: 
                            i.defenceReset()
                            
                if sconfittoNelTurno == False:    
                    # il nemico attacca e si verifica se il gioco continua (giocatore ancora vivo)
                    continua= giocatore.subisciDanno(self.__nemico.getStats()["attack"])
                    if continua == False: #morte
                        print("sei morto skill issue")
                        break

partita = Game(2)