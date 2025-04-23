import socket

HOST = '::1' # IPv6 loopback address | 127.0.0.1 in IPv4
PORT = 65432

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.sendall(data)
            print(f"Received: {data.decode()}")