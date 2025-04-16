import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as c_socket:
        try:
            c_socket.connect(('localhost', 6789))
            
            while True:
                message = input("Enter your emssage (type 'QUIT' to exit): ")
                if message.upper() == "QUIT":
                    c_socket.send(message.encode()) # Inform the server of disconnection
                    break
                c_socket.send(message.encode())
                response = c_socket.recv(1024)
                print(f"Recieved from server: {response.decode()}")

        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            print("Connection is closed.")

if __name__ == "__main__":
    start_client()