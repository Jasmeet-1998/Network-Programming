# the approach is to basically try to make the connection with specific IP,Network or system via a port and then if the connection establish then that port is open else not.

import socket
import threading

from queue import Queue
# a sequence of collection/list all kind of elements every time we get a element from list it is no longer in the original list.

# use the IP ,network,server you own
# if you dont know which IP address to choose u can just use localhost 127.0.0.1

target='127.0.0.1'
queue=Queue()
open_ports=[]

def portscan(port):
    try:
        sock=socket.socket( socket.AF_INET , socket.SOCK_STREAM)#AF_INET spefies that this is a internet socket not unix socket, and SOCK_STREAM specifies we are using TCP instead of UDP
        sock.connect(( target , port))
        return True
    except:
        return False

#====================== Naive Way ===========================================
#for port in range(1,1024):# these range of ports are stadard ports for HTTP communication , ssh , Telnet and so on.
#    result=portscan(port)
#    if result:
#        print('port:{} is open'.format(port))
#    else:
#        print('port:{} is closed'.format(port))


# print(portscan())

#===============the optimized way ======================
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)# FIFO rule

def worker():
    while not queue.empty():
        port=queue.get()
        if portscan(port):
            print('port:{} is open'.format(port))
            open_ports.append(port)

port_list =range(100,10000)
fill_queue(port_list)

thread_list=[]

for t in range(1000):
    thread=threading.Thread(target=worker)#note here we are not calling the worker function we are only reffering it i.e worker not worker()
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

# wait until all threads have done execution
for thread in thread_list:
    thread.join()# this method waits until the thread is done

print("Open ports are: " , open_ports)
