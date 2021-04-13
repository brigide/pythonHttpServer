from socket import *
from serverController import routes, methodHandler, requestHandler

serverPort = 8081
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)

print("Servidor iniciado")

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()

    headers, url, method, body = requestHandler(request)

    result = methodHandler(method, body)
    print(headers)
    print("")
    print(url)
    print("")
    print(method)
    print("")
    print(body)

  
    response = routes(url)

    connectionSocket.sendall(response.encode())

    connectionSocket.close()

serverSocket.close()

