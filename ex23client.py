import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

client_socket.connect((HOST, PORT))

print("Connected to the server.")

while True:
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        break

    print(f"Server: {data}")

client_socket.close()
