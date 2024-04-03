from Mazzo import *
from Player import *
from Enemy import *

###################################################
#todo: add più carte giocabili (asso,combinazioni)#
#toto: add conquista dei nemici se portati a 0 hp #
###################################################

def effetti(att):
    # effetti cuori
    if att[1] == "cuori":
        scarti.shuffle()
        for _ in range(att[0]): #ripeti n volte la pesca
            if len(scarti.seeDeck()) > 0: #non puoi prendere carte da un mazzo vuoto
                carta_pescata= scarti.pickCard()[0].split("_")
                taverna.addCard(carta_pescata[1],carta_pescata[0])
            else:
                break
    
    # effetti quadri
    elif att[1] == "quadri":
        pesca= True
        count= 0
        while count < att[0] and pesca:
            pesca=False
            for i in giocatori: # ogni giocatore pesca
                if len(i.seeHand()) < numMaxCarte: # a meno che non sia già full
                    i.draw(taverna.pickCard())
                    pesca=True
                    count+=1


#creo gli scarti
scarti=Mazzo()

#creo il mazzo nemico
castello=Mazzo()
for seme in ["picche","fiori","quadri","cuori"]:
    castello.addCard("K", seme)
    castello.addCard("J", seme)
    castello.addCard("Q", seme)
castello.shuffle()

#creo il mazzo da cui pescare
taverna=Mazzo()
for seme in ["picche","fiori","quadri","cuori"]:
    taverna.addCard("A", seme)
    for numero in range(2,11):
        taverna.addCard(str(numero), seme)

#creo giocatori
ferpetti=Player() 
# zucchetto= Player()
# Pagliaccio= Player()
giocatori= [ferpetti]#, zucchetto, Pagliaccio]

numGiocatori= len(giocatori)
# idCount del server
# impostare il limite giocatori da 1 a 4

#imposto i jolly e il num massimo di carte per giocatore in base al num giocatori
numMaxCarte= 8
while numGiocatori > 1:
    numGiocatori-= 1
    numMaxCarte-= 1
    if numGiocatori > 2: 
        taverna.addCard("Jolly")

#lo shuffle va fatto dopo l'aggiunta di eventuali Jolly
taverna.shuffle() 

#imposto maxcarte ai giocatori
for giocatore in giocatori:
    giocatore.setMaxCarte(numMaxCarte)

#ogni giocatore pesca
for _ in range(numMaxCarte):
    for i in giocatori:
        i.draw(taverna.pickCard())

#creo e pesco nemico
nemico= Enemy()
nemico.addStats(castello.pickCard())

#condizioni di gioco
re= 4
continua=True
#ciclo ci gioco
while re > 0 and continua:
    for giocatore in giocatori:
        sconfittoNelTurno= False
        print("\n---NUOVO TURNO---")
        print(nemico.getEnemyCard()[0],nemico.getStats())
        print(giocatore.seeHand())

        #chiedi per rinuncia
        rinuncia= input("vuoi rinunciare? (s/n): ")
        if rinuncia == "" or rinuncia[0].lower() != "s":

            #scegli la carta e attacca
            card= giocatore.selectCard(input("scegli una carta: "))
            if card[0]=="A":
                #chiedi per giocare un altra carta
                seconda_carta= input("vuoi giocare un altra carta? (s/n): ")
                print(giocatore.seeHand())
                if seconda_carta == "" or seconda_carta[0].lower() == "s":
                    second_card= giocatore.selectCard(input("scegli una altra carta: "))
                    second_attack=giocatore.calcolo(second_card, nemico)
                    effetti(second_attack)
                    
            # TODO: mettere le più carte giocabili qui
            elif card[0]:
                pass

            # attacco
            attacco= giocatore.calcolo(card, nemico)
            effetti(attacco)

            risultatoAttacco = nemico.subisciDanno(attacco[0])
            # se il nemico viene sconfitto nemico sconfitto
            if  risultatoAttacco[0] == True: 
                sconfittoNelTurno = True
                print("nemico sconfitto")
                # conquistato (?)  
                if risultatoAttacco[1] == True: 
                    print("nemico conquistato")
                    taverna.addCard(nemico.getEnemyCard())
                # se è un re, abbasso il counter
                if nemico.getStats()["attack"]==20: 
                    re-= 1
                nemico.addStats(castello.pickCard())
                # azzero la difesa una volta finito lo scontro
                for i in giocatori: 
                    i.defenceReset()
    
        if sconfittoNelTurno == False:
            continua= giocatore.subisciDanno(nemico.getStats()["attack"])
        if continua == False: #morte
            print("sei morto skill issue")
            break