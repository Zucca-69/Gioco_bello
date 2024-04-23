import tkinter as tk
import socket

from network import Network
from MainWindow import *

from Mazzo import *
from Player import *
from Enemy import *



# Ciclo di gioco sul client
while game_in_progress:
    game_state = receive_game_state_from_server()
    #update_ui(game_state)
    player_input = get_player_input()
    send_message_to_server(player_input)




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


'''
#schermata
root = MainWindow(giocatori)
for giocatore in giocatori:
    root.schermata_player(giocatore)
'''

        
# root.mainloop()