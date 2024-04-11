import tkinter as tk

from network import Network

#condizioni di gioco
re= 4
continua=True
n = Network()
player = int(n.getP())
print("You are player", player)

#ciclo ci gioco
while re > 0 and continua:
    try:
        game = n.send("get")
    except:
        run = False
        print("Couldn't get game")
        break

    if game.bothWent():
        #redrawWindow(win, game, player)
        try:
            game = n.send("reset")
        except:
            run = False
            print("Couldn't get game")
            break




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
                    
                                        
            # TODO: mettere le più carte giocabili qui
            elif card[0]:
                pass


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

        continua= giocatore.subisciDanno(nemico.getStats()["attack"])
        if continua == False: #morte
            print("sei morto skill issue")
            break