import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # Conecta ao servidor
        print(f'Connected to server at {host}:{port}')
        while True:
            message = input('Enter message to send: ')
            if message.lower() == 'exit':  # Comando para sair
                print('Closing connection.')
                break
            # Envia a mensagem para o servidor
            s.sendall(message.encode())
             # Recebe a resposta do servidor
            data = s.recv(1024)
            print(f'Receivexied from server: {data.decode()}')

if __name__ == "__main__":
    start_client()
