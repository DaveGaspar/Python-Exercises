import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is address family (IPv4, else IPv6)
# SOCK_STREAM is socket type (TCP, else UDP)

HOST = '127.0.0.1'
PORT = 12345

server_socket.bind((HOST, PORT))

server_socket.listen(1)
# 1 is the max number of pending connections

print("Server is listening for connections...")

client_socket, client_address = server_socket.accept()

print(f"Connection established with {client_address}")

while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Client: {data}")
    response = input("You: ")
    client_socket.send(response.encode('utf-8'))

client_socket.close()
server_socket.close()
