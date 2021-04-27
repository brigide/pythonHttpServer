from socket import *
from serverHandler import requestHandler
from Routes import routes

serverPort = 8081
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(1)

print("Server listening on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()

    request = connectionSocket.recv(1024).decode()

    headers, url, params, method, body = requestHandler(request)

    print(headers)
    print("")
    print(url)
    print("")
    print(method)
    print("")
    print(body)

  
    response = routes(url, params, method, body)
    connectionSocket.sendall(response.encode())

    connectionSocket.close()

serverSocket.close()

