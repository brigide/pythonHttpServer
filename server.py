from socket import *

serverPort = 8081
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)

print("Servidor iniciado")

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()

    headers = request.split('\n')
    filename = headers[0].split()[1]
    method = headers[0].split()[0]
    print(method)
    print("")
    print(request)

  
    if filename == '/':
        filename = '/index.html'
    elif filename == '/teste':
        filename = '/teste.html'

    try:
        fin = open('pages' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK\n\n' + content
    except IOError:
        response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found'

    connectionSocket.sendall(response.encode())

    connectionSocket.close()

serverSocket.close()

