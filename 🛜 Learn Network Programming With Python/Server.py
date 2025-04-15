import socket

# Server setup
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(('localhost', 6789))
s_socket.listen(5) # listen for incoming connections (max 5)

print("Waiting for a connection...")
connection, adderess = s_socket.accept()

# Recieve data from clience
data = connection.recv(1024)
print(f"Recievied message: {data.decode()} from {address}")

# Send a response to client
repsonse = "Hello, clinece. Your message was recieved."
connection.send(response.encode())

conneciton.close()