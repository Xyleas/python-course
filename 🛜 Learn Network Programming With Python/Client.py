import socket

# Server setup
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect(('localhost', 6789))

# sending a message to server
message = "Hello, server!"
c_socket.send(message.encode())

# Recieving response from sserver
response = c_socket.recv(1024)
print(f"Recievied from server: {response.decode()}")

c_socket.close()