import random
from socket import *
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
rps=['R','P','S']
while True:
     connectionSocket, addr = serverSocket.accept()
     clientPaly = connectionSocket.recv(1024).decode()
     print('Get input!')
     if(clientPaly=='R'):
          clientInput="Rock"
     elif(clientPaly=='P'):
          clientInput="Paper"
     elif(clientPaly=='S'):
          clientInput="Scissors"
     else:
          clientInput="Non"
     print('Wait a result')
     serverPlay=random.choice('RPS')
     if(serverPlay=='R'):
          serverRandom="Rock"
     elif(serverPlay=='P'):
          serverRandom="Paper"
     elif(serverPlay=='S'):
          serverRandom="Scissors"
     else:
          serverRandom="Non"
     if((serverPlay=='R' and clientPaly=='P') or (serverPlay=='P' and clientPaly=='S') or (serverPlay=='S' and clientPaly=='R')):
          capitalizedSentence='Wow, Client win Server. ( Client: '+clientInput+', Server: '+serverRandom+' )'
          print('Finish!')
     elif(serverPlay==clientPaly):
          capitalizedSentence='Cilent Even Server. ( Client: '+clientInput+', Server: '+serverRandom+' )'
          print('Finish!')
     elif((serverPlay=='P' and clientPaly=='R') or (serverPlay=='S' and clientPaly=='P') or (serverPlay=='R' and clientPaly=='S')):
          capitalizedSentence='Sorry, Client lose Server. ( Client: '+clientInput+', Server: '+serverRandom+' )'
          print('Finish!')
     else:
          if(clientInput=="Non"):
               capitalizedSentence='Sorry, Input error.'
               print('Failed!')
          else:
               capitalizedSentence='No result.'
               print('Failed!')
     connectionSocket.send(capitalizedSentence.encode())
     # connectionSocket.send(serverUse.encode())
     
     connectionSocket.close()