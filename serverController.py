def routes(url):
    subUrl = url.split('?') 
    if url == '/':
        filename = '/index.html'

    elif subUrl[0] == '/test':
        filename = '/teste.html'

    else:
        filename = '/error.html'


    try:
        fin = open('pages' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 OK\n\n' + content
    except IOError:
        response = 'HTTP/1.1 404 NOT FOUND\n\n' + content

    return response


def requestHandler(request):
    headers = request.split('\n') 
    url = headers[0].split()[1] 
    subUrl = url.split('?') 
    print("sub: ", subUrl)
    method = headers[0].split()[0]
    body = headers[-1].split('&')
    for i in range(0, len(body)):
        body[i] = str(body[i])

    return headers, url, method, body


def methodHandler(method, body):
    if method == 'GET':
        return

    elif method == 'POST':
        name = []
        return 