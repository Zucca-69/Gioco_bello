import tkinter as tk
import socket

from network import Network
from MainWindow import *

from Mazzo import *
from Player import *
from Enemy import *

#condizioni di gioco
re= 4
continua=True
n = Network()

player = int(n.getP())
print("You are player", player)

server = "192.168.1.127"
port = 5555

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server, port))

try:
    client_sock.bind((server, port))
except socket.error as e:
    str(e)



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
for seme in ["picche","cuori"]: #,"fiori","quadri"]:
    taverna.addCard("A", seme)
    for numero in range(2,11):
        taverna.addCard(str(numero), seme)

#creo giocatori
ferpetti=Player() 
zucchetto= Player()
pagliaccio= Player()
moketto = Player()
giocatori= [ferpetti, zucchetto, pagliaccio, moketto]

numGiocatori= len(giocatori)
# idCount del server
# impostare il limite giocatori da 1 a 4
#imposto i jolly e il num massimo di carte per giocatore in base al num giocatori
numMaxCarte= 8
while numGiocatori > 1:
    if numGiocatori > 2: 
        i = 0
        taverna.addCard(f"Jolly{i}")
        i += 1
    numGiocatori-= 1
    numMaxCarte-= 1


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
'''
#schermata
root = MainWindow(giocatori)
for giocatore in giocatori:
    root.schermata_player(giocatore)
'''
#condizioni di gioco
re= 4
continua=True

#ciclo ci gioco
while re > 0 and continua:
    for giocatore in giocatori:
        print("\n---NUOVO TURNO---")
        print(nemico.getEnemyCard()[0],nemico.getStats())
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
            attacco = giocatore.calcolo(lista_giocate, nemico)
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

        # il nemico attacca e si verifica se il gioco continua (giocatore ancora vivo)
        continua= giocatore.subisciDanno(nemico.getStats()["attack"])
        if continua == False: #morte
            print("sei morto skill issue")
            break
        
# root.mainloop()