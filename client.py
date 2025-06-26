import socket

# Server settings
while True:
    HOST = '127.0.0.1'
    PORT = 15224

# Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

# Send a message
    message = input("Enter your message: ")
    client_socket.send(message.encode('utf-8'))

# Receive server response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {response}")

# clLient_socket.close()
