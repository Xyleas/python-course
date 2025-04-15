import socket
import threading
import sys

def handle_client(conn, addr):
    try:
        print(f"New connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Recieved message from {addr}: {message}")

            if message.upper() == "QUIT":
                print(f"Quit command recieved. Client on port {addr} lost connection.")
                conn.send("Shutting down.".encode())
                conn.close()
                sys.exit(0)
            response = "Your message was recieved"
            conn.send(response.encode())

    except Exception as e:
        print(f" An error occured with client {addr}: {e}")
    finally:
        conn.close()

def start_server():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s_socket.bind(('localhost', 6789))
        s_socket.listen(5)
        print("Server is waiting for a connection...")
        while True:
            connection, address = s_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection, address))
            client_thread.start()

    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        s_socket.close()

if __name__ == "__main__":
    start_server()