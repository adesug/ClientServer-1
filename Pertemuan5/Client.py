import socket

def client_program():
    host = socket.gethostname()
    port = 5000 #initiate port no above 1024

    client_socket = socket.socket() #get instance
    #look closely, the bind() function takes tuple as argumet
    client_socket.connect((host, port))

    messsage = input(" -> ") #take input

    while messsage.lower().strip() !='byte':
        client_socket.send(messsage.encode()) # send message
        data = client_socket.recv(1024).decode()

        print('Received from server: '+data) # show in terminal

        messsage = input(" -> ") #again take input

    client_socket.close() #close the connection

client_program()
# if _name_ == '_main_':
#    server_program