from src.controllers.ContactController import ContactController

def routes(url, params, method, body):
    contactController = ContactController()


    if method == 'GET':

        if len(params) == 1 and url == '/contacts':
            contacts, status, filename = contactController.index()
            print(contacts)
        elif len(params) > 1 and url == '/contacts':
            param = params[1].split('=')
            if len(param) > 1:
                if param[0] == 'phone' and param[1] != '':
                    contact, status, filename = contactController.show(param[1])
                    print(contact)
                else:
                    status = 'HTTP/1.1 404 NOT FOUND'
                    filename = '/error.html'
            else: 
                status = 'HTTP/1.1 404 NOT FOUND'
                filename = '/error.html'
        else:
            status = 'HTTP/1.1 404 NOT FOUND'
            filename = '/error.html'


    elif method == 'POST':
        if url == '/contacts':
            print(body)
            status, filename = contactController.create(body)

    elif method == 'PUT':
        if url == '/contacts':
            status, filename = contactController.update(body)
    

    elif method == 'DELETE':
        if len(params) == 1 and url == '/contacts':
            status = 'HTTP/1.1 400 NOT FOUND'
            filename = '/error.html'
 
        elif len(params) > 1 and url == '/contacts':
            param = params[1].split('=')
            if len(param) > 1:
                if param[0] == 'phone' and param[1] != '':
                    status, filename = contactController.delete(param[1])


    else:
        status = 'HTTP/1.1 404 NOT FOUND'
        filename = '/error.html'


    try:
        fin = open('src/views' + filename)
        content = fin.read()
        fin.close()
        response = status + '\n\n' + content
    except IOError:
        fin = open('src/views/error.html')
        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 404 NOT FOUND\n\n' + content

    return response