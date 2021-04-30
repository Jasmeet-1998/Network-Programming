import threading
import socket

host = '127.0.0.1' #localhost if running on a server pick the IP address of the server.
port = 55555 # make sure not to choose ports from range 1 to 10000 as their are some reserve ports their.

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port)) # tuple specifies that server is bind to localhost at port 55555
server.listen() # puts server into listening mode i.e listening for incoming connection

clients = []
nicknames = []

# sending a broadcast messages to all the connections/client
def broadcast(message):
    for client in clients:
        client.send(message)


# handling client connection
def handle(client):
    while True:
        try:
            message=client.recv(1024) # get message from the client
            broadcast(message) # then broadcast to all clients
        except:
            index=clients.index(client)
            clients.remove(client) # remove this client
            client.close() # close the connection
            nickname=nicknames[index] #and store the client nickname to the nickname var
            broadcast(f'nickname:{nickname} left the chat...'.encode('ascii'))
            nicknames.remove(nickname) # remove that client nickname from nicknames array
            break # come out of loop

# main method
def receive():
    while True:
        client , address=server.accept()# the client and address of the new joining client will be stored in variable via .accept method
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nicknames)
        clients.append(client)

        print('nickname of the client is:{}'.format(nickname))
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # to handle multiple flow of messages from different client
        thread = threading.Thread(target=handle,args=(client,))
        thread.start()# in python we use .start() instead of run()

print('TCP Chat Room Server Started!')
receive()

