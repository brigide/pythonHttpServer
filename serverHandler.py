
def requestHandler(request):

    headers = request.split('\n') 

    url = headers[0].split()[1] 

    params = url.split('?')

    url = params[0]

    method = headers[0].split()[0]


    body = headers[-1]#.split('&')
    print(body)
    #for i in range(0, len(body)):
        #body[i] = str(body[i])

    return headers, url, params, method, body
