import socket

server=socket.socket()                              

host ="127.0.0.1"

port =5001

server.bind((host,port))

server.listen()

conn,addr=server.accept()
print(conn)
print(addr)

print("Connection From :",str(addr))

while True:
    data = conn.recv(1024).decode()
    
    if not data:
        break
    
    data = str(data).upper()
    
    print(f"from Clinet :{str(data)}")
    
    data = input("Type Message :")
    
    conn.send(data.encode())
    
conn.close()