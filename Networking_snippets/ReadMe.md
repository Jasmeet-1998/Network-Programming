# Networking_scripts (Snippets)


#### NOTE-> DDOS & Port Scanning is I'llegal if you are executing these scripts make sure these are your own server,networks or computers i.e that you own them and Using  Scripts in this repo and their implications & results its total responsibility is yours , These snippets are purely for EDUCATION PURPOSES.
 
***
## Scripts 
***

### - DDOS Script
### - Port Scanner
### - TCP Chat Room

***

## Script - 1
***
 
****DDOS**** : stands for distributed denial of service and it attacks the resources of a server by flooding it with requests.

****Method - Usually via botnets****

#### To make It work

- Go to snippet_ddos.py and u need to provide values for target(IP address you are targeting),port,fake_ip

****Python is not ideal for these kind of attacks performance wise  as it only simulates multithreading by faster switching between the tasks though gets the job done.****

#### botnets 

- Normal machines of ordinary people that the hacker gets control of and these machines act as zombies and the hacker use these
slave machines for collective attack on the target server.

- Instead of 1 DDOS script their are 1000 of DDOS script that are executing at the same time from different sources i.e distributed.


****Result - Server get overwhelms with the amount of requests and then justs shuts down entirely.****


### PREVENTION: Blocking IP's , Rate Limitations (No. of time a specific IP can make the request to the server is fixed) applied in the Server side code.



***
## Script -2
***
### PORT Scanner

****manually u can use netstat -an |find /i "listening" in the cmd to see which ports are open in Windows.****
****Usage- Open port that are of no use can be a security flaws also port scanning is Illegal so only scan your own network or your Own computer to find the Spots where u can just close the ports and make your system more secure.****
  
***
## Script -3
***
### TCP Chat Room
