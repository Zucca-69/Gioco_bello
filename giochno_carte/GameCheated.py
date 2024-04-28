from Mazzo import *
from Player import *
from Enemy import *

from FrameGioco import *

class Game:
    def __init__(self, n_giocatori):
        self.__n_giocatori = n_giocatori
        self.__giocatori = []
        self.__current_player_index = n_giocatori - 1
        self.__player_cards = []
        self.__lista_giocate = []
        self.__enemy_card = None
        self.__nemico= Enemy()
        self.__sconfittoNelTurno = False

        self.__setup_game()

        self.__gui = GameUI(self.__nemico.getEnemyCard()[0])
        self.__gui.add_game_instance(self)

        self.cambio_turno() # faccio partire il primo giocatore

        self.__gui.add_player_hand(self.__player_cards)

    def cambio_turno(self):
        if self.__current_player_index + 1 == self.__n_giocatori:
            self.__current_player_index = 0
        self.__player_cards = self.__giocatori[self.__current_player_index].seeHand()
        self.__gui.add_player_hand(self.__player_cards)
        
        self.__animale = True
        self.__lista_giocate = []
        self.__tot = 0

        self.__gui.master.mainloop()
        exit() # una volta chiusa la schermata termino l'esecuzione di tutto

    def get_player_cards(self):
        return self.__player_cards

    def get_enemy_card(self):
        return self.__enemy_card

    def got_card(self, card):
        if card in self.__player_cards:
            self.__giocatori[self.__current_player_index].selectCard(card)
            self.__player_cards.remove(card)
            self.__lista_giocate.append(card)

            if len(self.__lista_giocate) == 2 and self.__lista_giocate[0][0] == "A":
                self.finisci_turno()

            self.__gui.update_player_showed_cards(self.__giocatori[self.__current_player_index].seeHand())

        '''
        if card[0] != "A" or self.__animale == False: # se la prima carta è un animale
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
        '''

    def finisci_turno(self):
        # se rinuncio il turno
        if len(self.__lista_giocate) != 0: # e non ho giocato carte
            self.attacca_nemico()
        self.attacca_giocatore()
        self.cambio_turno() # tocca al prossimo

    def attacca_giocatore(self):
        if self.__sconfittoNelTurno == False:    
            # il nemico attacca e si verifica se il gioco continua (giocatore ancora vivo)
            self.__continua= self.__giocatori[self.__current_player_index].subisciDanno(self.__nemico.getStats()["attack"])
            if self.__continua == False: #morte
                print("sei morto skill issue")
                return False
    
    def effetti_globali(self, att):
        # effetti cuori
        if "cuori" in att[1]:
            self.__scarti.shuffle()
            for _ in range(att[0]): #ripeti n volte la pesca
                if len(self.__scarti.seeDeck()) > 0: #non puoi prendere carte da un mazzo vuoto
                    carta_pescata= self.__scarti.pickCard()[0].split("_")
                    self.__taverna.addCard(carta_pescata[1],carta_pescata[0])
                else:
                    break

        # effetti quadri
        if "quadri" in att[1]:
            pesca= True
            count= 0
            while count < att[0] and pesca:
                pesca=False
                for i in self.__giocatori: # ogni giocatore pesca
                    if len(i.seeHand()) < self.__numMaxCarte: # a meno che non sia già full
                        i.draw(self.__taverna.pickCard())
                        pesca=True
                        count+=1

    def attacca_nemico(self):
        # attacco al nemico
        attacco = self.__giocatori[self.__current_player_index].calcolo(self.__lista_giocate, self.__nemico)
        self.effetti_globali(attacco)
        risultatoAttacco = self.__nemico.subisciDanno(attacco[0])

        # se il nemico viene sconfitto
        if  risultatoAttacco[0] == True:
            # preparo il nuovo nemico                
            self.__gui.update_card(self.__gui.get_enemy_frame(), self.draw_new_enemy_card()[0])

            self.__sconfittoNelTurno = True

            # conquistato (?)  
            if risultatoAttacco[1] == True: 
                self.__taverna.addCard(self.__nemico.getEnemyCard())
                print("sesso")
            else: 
                self.__scarti.addCard(self.__nemico.getEnemyCard())
                
            # se è un re, abbasso il counter
            if self.__nemico.getStats()["attack"]==20: 
                self.__re -= 1
    
            if self.check_vittoria() == True:
                print("HAI VINTO")
                exit()
            else:
                self.__nemico.addStats(self.__castello.pickCard())
            
            # azzero la difesa una volta finito lo scontro
            for i in self.__giocatori: 
                i.defenceReset()
    
    def check_vittoria(self):
        if self.__re == 0:
            return True
        return False

    def draw_new_enemy_card(self):
        # pesco nemico 
        self.__nemico.addStats(self.__castello.pickCard())
        return self.__nemico.getEnemyCard()

    def __setup_game(self):
        #creo gli scarti
        self.__scarti=Mazzo()

        #creo il mazzo nemico
        self.__castello=Mazzo()
        for seme in ["picche","fiori","quadri","cuori"]:
            self.__castello.addCard("K", seme)
            self.__castello.addCard("Q", seme)
            self.__castello.addCard("J", seme)
        self.__castello.shuffle()

        self.draw_new_enemy_card()

        #creo il mazzo da cui pescare
        self.__taverna=Mazzo()
        for seme in ["picche","cuori","fiori","quadri"]:
            self.__taverna.addCard("A", seme)
            for numero in range(2,11):
                self.__taverna.addCard(str(numero), seme)
            
        self.creaGiocatori()

        #condizioni di gioco
        self.__re= 4
        self.__continua=True
        
    
    def creaGiocatori(self):
        # istanzio i giocatori e creo la lista giocatori 
        player_0 = Player() 
        player_1 = Player()
        player_2 = Player()
        player_3 = Player()

        giocatori = [player_0, player_1, player_2, player_3]
        self.__giocatori = giocatori[:self.__n_giocatori]
        
        # calcolo num max delle carte in mano e aggiungo eventuali jolly 
        numGiocatori = len(self.__giocatori)
        self.__numMaxCarte = 8
        i = 0
        while numGiocatori > 1:
            if numGiocatori > 2: 
                self.__taverna.addCard(f"Jolly{i}")
                i += 1
            numGiocatori -= 1
            self.__numMaxCarte -= 1

        # mescolo il mazzo
        self.__taverna.shuffle()

        # imposto val num max carte e faccio pescare i vari giocatori
        for giocatore in giocatori:
            giocatore.setMaxCarte(self.__numMaxCarte)

        for _ in range(self.__numMaxCarte):
            for i in giocatori:
                i.draw(self.__taverna.pickCard())

giocata = Game(1)
