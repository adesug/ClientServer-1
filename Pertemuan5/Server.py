import socket

def server_program():
    host = socket.gethostname()
    port = 5000 #initiate port no above 1024

    server_socket = socket.socket() #get instance
    #look closely, the bind() function takes tuple as argumet
    server_socket.bind((host, port))

    #configure how many client the server can listen sumultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: "+ str(address))
    while True:
        #receive data stream, it won't accept data packet greater that
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: "+str(data))
        data = input(" -> ")
        conn.send(data.encosde())

    conn.close()


server_program()
# if _name_ == '_main_':
#    server_program