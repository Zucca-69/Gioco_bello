from Mazzo import*
from Player import*
from Campo import*

#creo il mazzo nemico
castello=Mazzo()
castello.addCard("k")
castello.addCard("J")
castello.addCard("Q")

#creo il mazzo da cui pescare
taverna=Mazzo()
taverna.addCard("A")
for i in range(2,11):
    taverna.addCard(str(i))

#print(f"CASTELLO:{castello.seeDeck()}")
#print(f"TAVERNA{taverna.seeDeck()}")

taverna.shuffle()

print("\nMazzo dopo la mischiatura:")
print(taverna.seeDeck())

# print(taverna.pickCard())
# print("\nMazzo dopo la rimozione:")
# print(taverna.seeDeck())

#creo gli scarti
scarti=Mazzo()


#creo un giocatore
ferpetti=Player()
#pesco
ferpetti.draw(taverna.pickCard())
# print(ferpetti.seeHand())

