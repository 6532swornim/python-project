import socket

# Server settings
HOST = '127.0.0.1'
PORT = 15224

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started. Listening on {HOST}:{PORT}")

clients = []

# Accept connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected with {client_address}")
    clients.append(client_socket)

    # Receive message
    message = client_socket.recv(1024)
    print(f"{client_address}: {message}")
    client_socket.send("Message received!".encode('utf-8'))
