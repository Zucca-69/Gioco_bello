from Mazzo import *
from Player import *
from Enemy import *

###################################################
#todo: add più carte giocabili (asso,combinazioni)#
###################################################

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
        print("\n---NUOVO TURNO---")
        print(nemico.getEnemy()[0],nemico.getStats())
        print(giocatore.seeHand())

        #chiedi per rinuncia
        rinuncia= input("vuoi rinunciare? (s/n): ")
        if rinuncia[0] == "n":

            #scegli la carta e attacca
            card= giocatore.selectCard(input("scegli una carta: "))
            attacco= giocatore.calcolo(card, nemico)

            # effetti cuori
            if attacco[1] == "cuori":
                scarti.shuffle()
                for _ in range(attacco[0]): #ripeti n volte la pesca
                    if len(scarti.seeDeck()) > 0: #non puoi prendere carte da un mazzo vuoto
                        carta_pescata= scarti.pickCard()[0].split("_")
                        taverna.addCard(carta_pescata[1],carta_pescata[0])
                    else:
                        break
            
            # effetti quadri
            elif attacco[1] == "quadri":
                pesca= True
                count= 0
                while count < attacco[0] and pesca:
                    pesca=False
                    for i in giocatori: # ogni giocatore pesca
                        if len(i.seeHand()) < numMaxCarte: # a meno che non sia già full
                            i.draw(taverna.pickCard())
                            pesca=True
                            count+=1

        #ogni volta che un re cade, il contatore scala di 1
        if nemico.subisciDanno(attacco[0]): #verifica morte
            if nemico.getStats()["attack"]==20:
                re-= 1
            nemico.addStats(castello.pickCard())
            for i in giocatori:
                i.defenceReset()

        else: #se è ancora vivo attacca
            continua= giocatore.subisciDanno(nemico.getStats()["attack"])
            if continua == False: #morte
                print("sei morto skill issue")
                break