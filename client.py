import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 12345

client_socket.connect((HOST,PORT))

message = "Hello Server"
client_socket.send(message.encode('utf-8'))
data = client_socket.recv(1024).decode('utf-8')
print(f"data received back from server:{data}")

client_socket.close()
