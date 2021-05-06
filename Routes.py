from src.controllers.ContactController import ContactController

def routes(url, params, method, body):
    contactController = ContactController()
    requestData = '' # RequestData is used if the response is not a .html
    filename = '' # filename is used if the response is a .html
    if method == 'GET':
        # Check if a query parameter exists and if the route is /contacts
        if len(params) == 1 and url == '/contacts' or url == '/': 
            status, filename = contactController.index() # Returns the status and the html page with all users
        elif len(params) > 1 and url == '/contacts': # If there's query parameters and the route is /contacts it must be a specific search
            param = params[1].split('=') # Split the parameter (e.g. ?phone=123 -> param[0] is the key (phone), param[1] is the value (123))
            if len(param) > 1: # Verify if the paremeter value is empty
                if param[0] == 'phone' and param[1] != '':
                    status, filename  = contactController.index() # Returns the status and the html page with the specific user
                else: # This triggers if the key isn't phone or if the value is empty
                    status, filename = contactController.error()
            else: # This triggers if there's no query parameter even though there's a '?' in the URL
                status, filename = contactController.error()

        elif url == '/getContacts':  # This route doesn't return a html page, instead, it's used to fetch data. 
            if len(params) == 1:
                status, requestData = contactController.getContacts('')
            elif len(params) > 1:
                param = params[1].split('=')
                print(param)
                if len(param) > 1 and param[0] == 'phone' and param[1] != '':
                    status, requestData = contactController.getContacts(param[1])
                else:
                    status, filename = contactController.error()

        elif url == '/update': 
            status, filename = contactController.getAllContacts()

        elif url == '/createContact':
            status, filename = contactController.showCreatePage()

        elif '/updateContact' in url:
            status, filename = contactController.showUpdatePage()

        else: # This triggers if the route doesn't exists
            status, filename = contactController.error()


    elif method == 'POST':
        if url == '/contacts': # The form from the creation page redirects to the /contacts route
            body = body.split('&') # Fetch the body data, contains both key and values
            bodyValues = [] # Empty list used to store the values
            for param in body: # filter the values
                param = param.split('=')
                bodyValues.append(param[1])

            # bodyValues[0] = name, bodyValues[1] = phone, bodyValues[2] = address
            status, filename = contactController.create(bodyValues[0], bodyValues[1], bodyValues[2])
        else:
            status, filename = contactController.index()

    elif method == 'PUT':
        if url == '/contacts':
            #body = body.split('&') # Fetch the body data, contains both key and values
           # bodyValues = [] # Empty list used to store the values
           # for param in body: # filter the values
                #param = param.split('=')
                #bodyValues.append(param[1])

            #query = url.split('=')
           # pastPhone = query[1]

            # bodyValues[0] = name, bodyValues[1] = phone, bodyValues[2] = address
            print(body)
            status, filename = contactController.update(bodyValues[0], bodyValues[1], bodyValues[2], pastPhone)
        else:
            status, filename = contactController.index()

    

    elif method == 'DELETE':
        if len(params) == 1 and url == '/contacts':
            status, filename = contactController.error()
 
        elif len(params) > 1 and url == '/contacts':
            param = params[1].split('=')
            if len(param) > 1:
                if param[0] == 'phone' and param[1] != '':
                    status, filename = contactController.delete(param[1])


    else:
        status, filename = contactController.error()


    try:
        if requestData != '':
            response = status + '\n\n' + requestData
        else:
            fin = open('src/views' + filename)
            content = fin.read()
            fin.close()
            response = status + '\n\n' + content
            print(response)
 
        
        #response = status + '\n\n' + page
    except IOError:
        #fin = open('src/views/error.html')
        #content = fin.read()
        #fin.close()
        
        response = status + filename
        
    return response