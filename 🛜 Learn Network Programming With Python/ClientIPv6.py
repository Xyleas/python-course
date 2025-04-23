import socket

HOST = '::1' # IPv6 loopback address | 127.0.0.1 in IPv4
PORT = 65432

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as c_s:
    c_s.connect((HOST, PORT))
    c_s.sendall(b'Hello, IPv6 Server!') # b changes the type to 'bytes'
    data = c_s.recv(1024)

print('Recieved', repr(data))