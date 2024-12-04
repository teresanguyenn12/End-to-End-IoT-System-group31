import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the server.")
        
        while True:
            data = client_socket.recv(1024).decode()
            print(data)
            if "Goodbye!" in data:
                break
            
            user_input = input("Your choice: ").strip()
            client_socket.sendall(user_input.encode())
            if user_input.lower() == "exit":
                break

if __name__ == "__main__":
    host = str(input("Enter the host IP address: "))
    port = int(input("Enter the port number: "))
    start_client(host, port)
