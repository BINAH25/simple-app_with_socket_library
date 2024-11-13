import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 12345
server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f"Serving listening on {HOST}:{PORT}")
client_socket, client_address = server_socket.accept()
print(f"connection established with {client_address}")

data = client_socket.recv(1024).decode('utf-8')
print(f"data received:{data}")

client_socket.send(data.encode('utf-8'))
client_socket.close()
server_socket.close()
