import socket

host ="127.0.0.1"
port =5001

obj=socket.socket()            

obj.connect((host,port))

message =input("type message :")

while message != 'q':
    obj.send(message.encode())
    
    data=obj.recv(1024).decode()
    
    data =str(data).upper()
    
    print(f"Recived frome server :{data}")
    
    message=input("type messsage :")
    
obj.close()
    
                      


