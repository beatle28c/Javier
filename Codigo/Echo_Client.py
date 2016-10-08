import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
#print(sys.stderr, 'connecting to %s port %s',server_address)
sock.connect(server_address)

try:
        mes = "Hola";
        message=str.encode(mes)
        print(message)
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
            
        while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print(data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()
