import socket
from _thread import *
import pickle
from Game import *

server = socket.gethostbyname(socket.gethostname())
port = 5555

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_sock.bind((server, port))
except socket.error as e:
    str(e)

server_sock.listen(4)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


# Codice sul server per gestire i turni dei giocatori
def main_game_loop():
    current_player_index = 0
    while not game_over:
        current_player = players[current_player_index]
        # Invia un messaggio al client corrente per indicare il suo turno
        send_message_to_client(current_player.socket, "È il tuo turno!")
        # Attendi l'input del giocatore corrente
        player_input = receive_player_input(current_player.socket)
        # Esegui l'azione del giocatore e aggiorna lo stato del gioco
        update_game_state(player_input)
        # Passa al turno del prossimo giocatore
        current_player_index = (current_player_index + 1) % len(players)



# # Ciclo di gioco sul server
# while game_in_progress:
#     for client_socket in connected_clients:
#         message = receive_message(client_socket)
#         process_message(message)
#     update_game_state()
#     send_game_state_to_clients()



def threaded_client(conn, gameId):
    global idCount
    #conn.send(str.encode(str(game_state)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = server_sock.accept()
    print("Connected to:", addr)
    idCount += 1
    
    gameId = (idCount - 1)//2

    games[gameId] = Game(gameId)
    newPlayer=Player()
    games[gameId].add_player(newPlayer)
    if idCount == 4:
        
        games[gameId].update_game_state(1)
        print("Creating a new game...")
        games[gameId].start_game()
    else:
        games[gameId].update_game_state(0)
        


    start_new_thread(threaded_client, (conn, gameId))