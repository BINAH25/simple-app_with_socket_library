import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the host and port number 
HOST = "127.0.0.1"
PORT = 12345

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(5)

print(f"Serving listening on {HOST}:{PORT}")
client_socket, client_address = server_socket.accept()
print(f"connection established with {client_address}")

# Receive a message from the client
data = client_socket.recv(1024).decode('utf-8')
print(f"data received:{data}")

# send back the message receive
client_socket.send(data.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
