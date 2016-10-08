import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
#print(sys.stderr, 'starting up on %s port %s', server_address)
sock.bind(server_address)

sock.listen(1)
conn, c_add = sock.accept()
print("conexión de: ",c_add)
while True:
    data = conn.recv(16)
    print("Se recibe: ",repr(data))
    rep = input("Responder: ")
    reply=str.encode(rep)
    conn.sendall(reply)
conn.close()
