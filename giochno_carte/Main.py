from Mazzo import*
from Player import*
from Enemy import*

#creo il mazzo nemico
castello=Mazzo()
castello.addCard("K")
castello.addCard("J")
castello.addCard("Q")

castello.shuffle()

#creo il mazzo da cui pescare
taverna=Mazzo()
taverna.addCard("A")
for i in range(2,11):
    taverna.addCard(str(i))

#print(f"CASTELLO:{castello.seeDeck()}")
#print(f"TAVERNA{taverna.seeDeck()}")

taverna.shuffle()

#print("\nMazzo dopo la mischiatura:")
#print(taverna.seeDeck())
a= "troia"
# print(taverna.pickCard())
# print("\nMazzo dopo la rimozione:")
# print(taverna.seeDeck())

#creo gli scarti
scarti=Mazzo()

numGiocatori= int(input("num giocatori: ")) # idCount del server
if numGiocatori > 2:
    #add jolly
    if numGiocatori == 4:
        #add jolly
        pass

#creo un giocatore
ferpetti=Player()
#pesco
ferpetti.draw(taverna.pickCard())
print(ferpetti.seeHand())

#creo e pesco nemico
nemico=Enemy(castello.pickCard())
nemico.stats()

re= 4
while re > 0:
    re= 0
    #pass
#ogni volta che un re cade, il contatore scala di 1