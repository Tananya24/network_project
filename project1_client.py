from socket import *
serverName = '127.0.0.1'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print('Hello! This is Rock-Paper-Scissors Game')
rps = input('Please choose R(Rock) or P(Paper) or S(Scissors): ')
clientSocket.send(rps.encode())
if(rps=='R'):
    clientInput="Rock"
elif(rps=='P'):
    clientInput="Paper"
elif(rps=='S'):
    clientInput="Scissors"
else:
    clientInput="Unknow"
print('Input of you: ',rps,"(",clientInput,")")
modifiedSentence = clientSocket.recv(1024)
result=modifiedSentence.decode()
print('\nResult From Server: ',result)
# count=0
# for chara in result:
#     if(count==0):
#         resultVS=chara
#     elif(count==1):
#         rpsServer=chara
#     count+=1
# if(rpsServer=='R'):
#     serverSend="Rock"
#     if(resultVS=='W'):
#         print('Wow, Win!')
#         print('(',clientInput,'Win',serverSend,')')
#     elif(resultVS=='E'):
#         print('Even!')
#         print('(',clientInput,'Even',serverSend,')')
#     elif(resultVS=='L'):
#         print('Sorry, Lose!',)
#         print('(',clientInput,'Lose',serverSend,')')
# elif(rpsServer=='P'):
#     serverSend="Paper"
#     if(resultVS=='W'):
#         print('Wow, Win!')
#         print('(',clientInput,'Win',serverSend,')')
#     elif(resultVS=='E'):
#         print('Even!')
#         print('(',clientInput,'Even',serverSend,')')
#     elif(resultVS=='L'):
#         print('Sorry, Lose!')
#         print('(',clientInput,'Lose',serverSend,')')
# elif(rpsServer=='S'):
#     serverSend="Scissors"
#     if(resultVS=='W'):
#         print('Wow, Win!')
#         print('(',clientInput,'Win',serverSend,')')
#     elif(resultVS=='E'):
#         print('Even!')
#         print('(',clientInput,'Even',serverSend,')')
#     elif(resultVS=='L'):
#         print('Sorry, Lose!')
#         print('(',clientInput,'Lose',serverSend,')')

print('\nThanks You for playing Rock-Paper-Scissors Game')
clientSocket.close()