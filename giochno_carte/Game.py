from Mazzo import *
from Player import *
from Enemy import *


class Game:
    def __init__(self, id):
        #self.__ready = False
        self.__id = id
        # Inizializza le variabili di gioco
        self.__players = []  # Lista dei giocatori
        self.__game_state = None  # Stato del gioco
        #creo gli scarti
        self.__scarti=Mazzo()
        #creo il mazzo nemico
        self.__castello=Mazzo()
        #creo il mazzo da cui pescare
        self.__taverna=Mazzo()
        #creo nemico
        self.__nemico= Enemy()

        self.__numMaxCarte= 8

    
    # def getReady(self):
    #     return self.__ready
    # def setReady(self, ready):
    #     self.__ready = ready
    def getId(self):
        return self.__id
    def getPlayers(self):
        return self.__players
    def getGameState(self):
        return self.__game_state
    

        

    def connected(self):
        return self.ready
    
        
    def add_player(self, player):
        # Aggiungi un giocatore al gioco
        self.__players.append(player)


    #     # Nel metodo start_game() della classe Game
    # def start_game(self):
    #     while re > 0 and continua:
    #         for player in players:
    #             print("\n---NUOVO TURNO---")
    #             print(nemico.getEnemyCard()[0], nemico.getStats())
    #             print(player.seeHand())

    #             if not player_wants_to_skip_turn():
    #                 player_turn(player)

    #                 # Attacco del nemico
    #                 enemy_attack()

    #                 # Verifica se il gioco continua
    #                 continua = check_game_continuation()
    #                 if not continua:
    #                     break

    # Metodo per gestire il turno di un giocatore
    def player_turn(self, player):
        # Logica del turno del giocatore
        actions = player.take_turn()
        process_actions(actions)

    # Metodo per gestire l'attacco del nemico
    def enemy_attack(self):
        # Logica dell'attacco del nemico
        enemy.make_attack(players)

    # Metodo per verificare se il gioco continua
    def check_game_continuation(self):
        # Logica per verificare se il gioco può continuare
        return True  # o False a seconda delle condizioni di fine del gioco

    
    def start_game(self):
        # Inizia il gioco
        # Distribuisci carte ai giocatori, inizia il primo turno, ecc.
        
        for seme in ["picche","fiori","quadri","cuori"]:
            self.__castello.addCard("K", seme)
            self.__castello.addCard("J", seme)
            self.__castello.addCard("Q", seme)
        self.__castello.shuffle()

        
        for seme in ["picche","cuori","fiori","quadri"]:
            self.__taverna.addCard("A", seme)
            for numero in range(2,11):
                self.__taverna.addCard(str(numero), seme)

        

        numGiocatori= len(self.__players)
        # idCount del server
        # impostare il limite giocatori da 1 a 4
        #imposto i jolly e il num massimo di carte per giocatore in base al num giocatori
        
        while numGiocatori > 1:
            if numGiocatori > 2: 
                i = 0
                self.__taverna.addCard(f"Jolly{i}")
                i += 1
            numGiocatori-= 1
            self.__numMaxCarte-= 1


        #lo shuffle va fatto dopo l'aggiunta di eventuali Jolly
        self.__taverna.shuffle() 

        #imposto maxcarte ai giocatori
        for giocatore in self.__players:
            giocatore.setMaxCarte(self.__numMaxCarte)

        #ogni giocatore pesca
        for _ in range(self.__numMaxCarte):
            for i in self.__players:
                i.draw(self.__taverna.pickCard())

        #creo e pesco nemico
        
        self.__nemico.addStats(self.__castello.pickCard())


        #condizioni di gioco
        re= 4
        continua=True

        #ciclo ci gioco
        while re > 0 and continua:
            for giocatore in self.__players:
                print("\n---NUOVO TURNO---")
                print(self.__nemico.getEnemyCard()[0],self.__nemico.getStats())
                print(giocatore.seeHand())
                animale = True

                #chiedi per rinuncia
                rinuncia= input("vuoi rinunciare? (s/n): ")
                if rinuncia == "" or rinuncia[0].lower() != "s":
                    lista_giocate = []
                    tot = 0

                    #scegli la carta
                    card= giocatore.selectCard(input("scegli una carta: "))
                    lista_giocate.append(card)
                    
                    if card[0]=="A" and animale:
                        #chiedi per rinuncia
                        card = input("vuoi giocare un altra carta? (s/n): ")
                        print(giocatore.seeHand())
                        if card == "" or card[0].lower() == "s":
                            animale = False
                            card= giocatore.selectCard(input("scegli una altra carta: "))
                            lista_giocate.append(card)                    

                    if str(card[0]).isdigit() == True: # se una carta normale
                        #gioca carte con lo stesso simbolo
                        if int(card[0]) >= 2 and int(card[0]) <= 5:
                            giocabili = []
                            for carta in giocatore.seeHand():
                                if carta[0] == str(card[0]):
                                    giocabili.append(carta)
                            
                            while tot + int(card[0]) <= 10 and len(giocabili) > 0:
                                print(giocabili)
                                #chiedi per rinuncia
                                rinuncia= input("vuoi rinunciare? (s/n): ")
                                if rinuncia == "" or rinuncia[0].lower() != "s":
                                    card= giocatore.selectCard(input("scegli una carta: "))
                                    lista_giocate.append(card)
                                    giocabili.remove(card)
                                    tot += int(card[0])

                    # attacco al nemico
                    attacco = giocatore.calcolo(lista_giocate, self.__nemico)
                    risultatoAttacco = self.__nemico.subisciDanno(attacco[0])

                    # se il nemico viene sconfitto nemico sconfitto
                    if  risultatoAttacco[0] == True: 

                        sconfittoNelTurno = True
                        print("nemico sconfitto")
                        # conquistato (?)  
                        if risultatoAttacco[1] == True: 
                            print("nemico conquistato")
                            self.__taverna.addCard(self.__nemico.getEnemyCard())
                        # se è un re, abbasso il counter
                        if self.__nemico.getStats()["attack"]==20: 
                            re-= 1
                        self.__nemico.addStats(self.__castello.pickCard())
                        # azzero la difesa una volta finito lo scontro
                        for i in self.__players: 
                            i.defenceReset()

                # il nemico attacca e si verifica se il gioco continua (giocatore ancora vivo)
                continua= giocatore.subisciDanno(self.__nemico.getStats()["attack"])
                if continua == False: #morte
                    print("sei morto skill issue")
                    break


    def effetti(self,att):
        # effetti cuori
        if att[1] == "cuori":
            self.__scarti.shuffle()
            for _ in range(att[0]): #ripeti n volte la pesca
                if len(self.__scarti.seeDeck()) > 0: #non puoi prendere carte da un mazzo vuoto
                    carta_pescata= self.__scarti.pickCard()[0].split("_")
                    self.__taverna.addCard(carta_pescata[1],carta_pescata[0])
                else:
                    break
        
        # effetti quadri
        elif att[1] == "quadri":
            pesca= True
            count= 0
            while count < att[0] and pesca:
                pesca=False
                for i in self.__players: # ogni giocatore pesca
                    if len(i.seeHand()) < self.__numMaxCarte: # a meno che non sia già full
                        i.draw(self.__taverna.pickCard())
                        pesca=True
                        count+=1
    
    def process_player_action(self, player, action):
        # Processa l'azione di un giocatore durante il suo turno
        # Eseguire la logica del gioco in base all'azione del giocatore
        if self.__game_state==-1:
            pass #todo gioco finito idk
        elif self.__game_state==0:
            pass #todo gioco menù
        elif self.__game_state==1:
            pass #todo fase 1
        elif self.__game_state==2:
            pass #todo fase 2
        elif self.__game_state==3:
            pass #todo fase 3
        elif self.__game_state==4:
            pass #todo fase 4

    def update_game_state(self,new_state):
        # Aggiorna lo stato del gioco (ad esempio, punteggio, stato dei giocatori, ecc.)
        self.__game_state=new_state
        

    def send_game_state_to_clients(self):
        # Invia lo stato del gioco ai client connessi
        pass
