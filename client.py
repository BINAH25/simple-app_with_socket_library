import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the host and port number 
HOST = '127.0.0.1'
PORT = 12345

# coonect the to host and port number
client_socket.connect((HOST,PORT))

message = "Hello Server"

# Send a message to the server
client_socket.send(message.encode('utf-8'))
data = client_socket.recv(1024).decode('utf-8')
print(f"data received back from server:{data}")

# Close the connection
client_socket.close()
