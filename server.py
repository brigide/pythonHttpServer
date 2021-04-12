from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)

print("Servidor iniciado")

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()
    print(request)

    headers = request.split('\n')
    filename = headers[0].split()[1]

    if filename == '/':
        filename = '/index.html'
    elif filename == '/teste':
        filename = '/teste.html'

    try:
        fin = open('pages' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    connectionSocket.sendall(response.encode())

    connectionSocket.close()

serverSocket.close()

