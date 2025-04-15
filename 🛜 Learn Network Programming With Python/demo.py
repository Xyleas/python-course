import socket
# Create a socket objects
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

# Establishing a connection
server_address = ('www.example.com', 80) # Server IP and port number
s.connect(server_address)

# Sending data
message = 'Get / HTTP/1.0\r\n\r\n'
s.send(message.encode())

# Recieving data
data = s.recv(1024)
print('Received data: ', repr(data))