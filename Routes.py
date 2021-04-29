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
        
        elif url == '/createContact':
            status, page = contactController.showCreatePage()
        else: # This triggers if the route doesn't exists
            status, page = contactController.error()


    elif method == 'POST':
        if url == '/contacts':
            body = body.split('&') # Fetch the body data, contains both key and values
            bodyValues = [] # Empty list used to store the values
            for param in body: # filter the values
                param = param.split('=')
                bodyValues.append(param[1])

            # bodyValues[0] = name, bodyValues[1] = phone, bodyValues[2] = address
            status, page = contactController.create(bodyValues[0], bodyValues[1], bodyValues[2])
        else:
            status, page = contactController.index()

    elif method == 'PUT':
        if url == '/contacts':
            status, page = contactController.update(body)
    

    elif method == 'DELETE':
        if len(params) == 1 and url == '/contacts':
            status, page = contactController.error()
 
        elif len(params) > 1 and url == '/contacts':
            param = params[1].split('=')
            if len(param) > 1:
                if param[0] == 'phone' and param[1] != '':
                    status, page = contactController.delete(param[1])


    else:
        status, page = contactController.error()


    try:
        #fin = open('src/views' + filename)
        #content = fin.read()
        #fin.close()
        #response = status + '\n\n' + content
 
        
        response = status + '\n\n' + page
    except IOError:
        #fin = open('src/views/error.html')
        #content = fin.read()
        #fin.close()
        
        response = status + page

    return response