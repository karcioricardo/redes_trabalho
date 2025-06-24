import socket

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port)) #  Associa o socket ao endereço IP e porta
        s.listen() # Habilita o servidor para aceitar conexões
        print(f'Server listening on {host}:{port}')
        # Aceita uma nova conexão
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                 # Recebe dados do cliente (máximo 1024 bytes)
                data = conn.recv(1024)
                if not data:# Se não receber dados, encerra
                    break
                print(f'Received from client: {data.decode()}')
                conn.sendall(data)# Envia os dados de volta (eco)

if __name__ == "__main__":
    start_server()
