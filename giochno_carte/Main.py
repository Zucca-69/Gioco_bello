from Mazzo import *
from Player import *
from Enemy import *

########################################################################
#todo: add rinuncia (fase 1)
#todo: add effetti cuori e quadri
#todo: add nemico colpisce (fase 4)
#todo: add più carte giocabili (asso)

########################################################################
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


numGiocatori= len(giocatori) #int(input("num giocatori: ")) # idCount del server
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

re= 4
while re > 0:
    for giocatore in giocatori:
        print("\n---NUOVO TURNO---")
        print(nemico.getEnemy()[0],nemico.getStats())
        print(giocatore.seeHand())
        card= giocatore.selectCard(input("scegli una carta: "))
        
        #ogni volta che un re cade, il contatore scala di 1
        if nemico.subisciDanno(giocatore.calcolo(card, nemico)):
            if nemico.getStats()["attack"]==20:
                re-= 1
            nemico.addStats(castello.pickCard())