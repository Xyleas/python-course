import socket

HOST = 'localhost'
PORT = 65432

try: 
    with socket.create_connection((HOST, PORT)) as s_ipv4:
        print("Connected via IPv4")
except ConnectionRefusedError:
    print("IPv4 Connection Failed")

# Try to connect through IPv6
try:
    ipv6_info = socket.getaddrinfo(HOST, PORT, socket.AF_INET6)[0]
    # Extract the IPv6 address
    address = ipv6_info[4][0]
    # Create a connection
    with socket.create_connection((address, PORT)) as s_ipv6:
        print("Connected via IPv6")
except ConnectionRefusedError:
    print("IPv6 Connection Failed.")
