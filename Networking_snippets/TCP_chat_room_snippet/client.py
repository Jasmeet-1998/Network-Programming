import socket
import threading

nickname=input('Please Provide a Nickname: ')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555)) ## this trigers the accept method in the top_chat_room snippet

def receive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('Something Went Wrong..')
            client.close()
            break

# get input infinitely unless the client exits
def write():
    while True:
        message=f'{nickname}:{input("")}'
        client.send(message.encode('ascii'))

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()