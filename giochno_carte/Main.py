from Mazzo import *
from Player import *
from Enemy import *

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

numGiocatori= 2 #int(input("num giocatori: ")) # idCount del server
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

#creo giocatori
ferpetti=Player(numMaxCarte) 
zucchetto= Player(numMaxCarte)
giocatori= [ferpetti, zucchetto]

#ogni giocatore pesca
for _ in range(numMaxCarte): 
    ferpetti.draw(taverna.pickCard())
    zucchetto.draw(taverna.pickCard())

#creo e pesco nemico
nemico= Enemy()
nemico.addStats(castello.pickCard())

re= 4
while re > 0:
    for giocatore in giocatori:
        print("\n---NUOVO TURNO---")
        print(nemico.values())
        print(giocatore.seeHand())
        card= giocatore.selectCard(input("scegli una carta: "))
        
        #ogni volta che un re cade, il contatore scala di 1
        if nemico.subisciDanno(giocatore.calcolo(card, nemico)):
            re-= 4
            break