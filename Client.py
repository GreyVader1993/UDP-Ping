import time
from socket import *

#Client Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Set Timeout
clientSocket.settimeout(1)
#String to send
#message = "Ping"

for i in range(10):
    try:
        # Store the start time.
        start = time.time()
        #Sending message to the server
        message = "Ping" + str(i+1)
        clientSocket.sendto(message.encode(),("127.0.0.1",12000))
        #Wait for Response from server
        data,server = clientSocket.recvfrom(1024)
        print(message, i+1)
        #Calculate RTT and Print
        end = time.time()
        diff = end - start
        print("RTT - ", diff, " ", data)
    except:
        print ('Request Time Out')

clientSocket.close()