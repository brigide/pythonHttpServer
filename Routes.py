from src.controllers.ContactController import ContactController
def routes(url, params, method, body):
    contactController = ContactController()


    if method == 'GET':

        # Check if a query parameter exists and if the route is /contacts, if it exists, it must be a specific user search
        if len(params) == 1 and url == '/contacts': 
            contacts, status, page = contactController.index() # Returns the status and the html page with all users
        elif len(params) > 1 and url == '/contacts': # If there's no query parameters and the route is /contacts
            param = params[1].split('=') # Split the parameter (e.g. ?phone=123 -> param[0] is the key (phone), param[1] is the value (123))
            if len(param) > 1: # Verify if the paremeter value is empty
                if param[0] == 'phone' and param[1] != '':
                    contact, status, page  = contactController.show(param[1]) # Returns the status and the html page with the specific user
                else: # This triggers if the key isn't phone or if the value is empty
                    status, page = contactController.error()
            else: # This triggers if there's no query parameter even though there's a '?' in the URL
                status, page = contactController.error()
        else: # This triggers if the route is not '/contacts'
            status, page = contactController.error()


    elif method == 'POST':
        if url == '/contacts':
            print(body)
            status, page = contactController.create(body)

    elif method == 'PUT':
        if url == '/contacts':
            status, page = contactController.update(body)
    

    elif method == 'DELETE':
        if len(params) == 1 and url == '/contacts':
            status = 'HTTP/1.1 400 NOT FOUND'
            page = '/error.html'
 
        elif len(params) > 1 and url == '/contacts':
            param = params[1].split('=')
            if len(param) > 1:
                if param[0] == 'phone' and param[1] != '':
                    status, page = contactController.delete(param[1])


    else:
        status = 'HTTP/1.1 404 NOT FOUND'
        page = '/error.html'


    try:
        #fin = open('src/views' + filename)
        #content = fin.read()
        #fin.close()
        #response = status + '\n\n' + content

        content = '<html>\n<head>\n    <title>Contatos</title>\n</head>\n<body>\n  <h1>File Not Found</h1>\n</body>\n</html>'
 

        response = status + '\n\n' + page
    except IOError:
        fin = open('src/views/error.html')
        content = fin.read()
        fin.close()
        print(content)
        response = 'HTTP/1.1 404 NOT FOUND\n\n' + content

    return response