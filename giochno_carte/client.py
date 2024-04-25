# Client.py

import socket
from network import Network
from Mazzo import *
from Player import *
from Enemy import *

class Client:
    def __init__(self):
        self.__server = socket.gethostbyname(socket.gethostname())
        self.__port = 5555
        self.__client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__network = Network()

    def connect_to_server(self):
        # Connessione al server
        try:
            self.__client_sock.connect((self.__server, self.__port))
        except socket.error as e:
            print(str(e))

    def play_game(self):
        # Ciclo di gioco sul client
        game_in_progress=True
        while game_in_progress:
            # Ricevi lo stato di gioco dal server
            game_state = self.receive_game_state_from_server()
            if game_state == -1:
                print("unlucky")
                break
            elif game_state ==0:
                pass #menù
            elif game_state==1:

                player_input = self.get_player_input()
            # Invia l'input al server
            self.send_message_to_server(player_input)
        return "game ended (message from client)"

    def receive_game_state_from_server(self):
        # Ricevi lo stato di gioco dal server
        game_state = None
        try:
            game_state = self.__client_sock.recv(4096).decode()
        except socket.error as e:
            print(str(e))
        return game_state

    def get_player_input(self):
        # Ottieni l'input del giocatore (potrebbe essere tramite interfaccia grafica)
        player_input = input("Inserisci il tuo input: ")
        return player_input

    def send_message_to_server(self, message):
        # Invia un messaggio al server
        try:
            self.__client_sock.send(str.encode(message+ "form"+self.__network.getP()))
        except socket.error as e:
            print(str(e))



signorino=Client()

signorino.connect_to_server()
signorino.play_game()
'''
#schermata
root = MainWindow(giocatori)
for giocatore in giocatori:
    root.schermata_player(giocatore)
'''

        
# root.mainloop()