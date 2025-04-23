import socket

HOST = '' # Listen on all available interfaces
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_ipv4:
    # Enable IPv4 and bind to the address and port
    s_upv4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_ipv4.bind((HOST, PORT))
    s_ipv4.listen()

    print(f"IPV4 server listening on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s_ipv6:
        s_ipv6.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_ipv6.bind((HOST, PORT))
        s_ipv6.listen()

    print(f"IPV6 server listening on {HOST}:{PORT}")

    while True:
        # Accept IPv4 connections
        conn_ipv4, addr_ipv4 = s_ipv4.accept()
        with conn_ipv4:
            print(f"Connected by IPv4 {addr_ipv4}")
            # Handle IPv4 connection

        # Accept IPv6 connections
        conn_ipv6, addr_ipv6 = s_ipv6.accept()
        with conn_ipv6:
            print(f"Connected by IPv6 {addr_ipv6}")